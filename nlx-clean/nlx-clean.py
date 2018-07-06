'''
NLX-clean microservice
@Author: Jim Schwoebel

This microservice takes in a speech sample and cleans it to be processed further along the pipeline.

Specifically, there are a few checks:

    -check if speech sample is provided with a speech sample classifier (speech vs. other)
    -if not .wav format, convert to .wav using ffmpeg (can be a video or any sample) 
    -if not mono signal, convert to mono signal using stereo2mono()

Note that this microservice does not cover speaker diarization. It is assumed all samples coming in are
single-speaker samples. If you are looking to separate out multiple speakers, use the NLX-diarize microservice instead.

Happy cleaning! 

(C) NeuroLex Laboratories, 2018

'''
from __future__ import print_function, division, unicode_literals
import os, json, shutil, time, sys, datetime, pickle
import importlib, scipy, ffmpy, getpass, wave, pydub, collections, contextlib, sys, webrtcvad 
import soundfile as sf
import librosa 
from scipy import signal
import scipy.io.wavfile as wav
from scipy.fftpack import fftfreq
import matplotlib.pyplot as plt
import numpy as np
#import pymongo
from pydub import AudioSegment

hostdir=os.getcwd()
os.chdir(hostdir+'/nlx-audiomodel/models/')
sys.path.append(os.getcwd())

from load_audioclassify import featurize2, exportfile, audio_time_features, featurize

#load ML model
modelname='voicelex.pickle'
loadmodel=open(modelname,'rb')
model = pickle.load(loadmodel)
loadmodel.close()

## IF WE ARE LOADING PYAUDIOANALYSIS 3 FOR SILENCE REMOVAL NEED THIS IMPORT

##os.chdir(hostdir+'/nlx-pyaudioanalysis3/')
##sys.path.append(os.getcwd())
##
##import audioBasicIO as aIO
##import audioSegmentation as aS

os.chdir(hostdir)

##SOME THINGS TO DO (to set up environment)
####################################################################################
#brew uninstall ffmpeg (if needed)
#brew install ffmpeg --with-theora --with-libvorbis
#brew install sox 

##INITIALIZE FUNCTIONS FOR CLEANING
####################################################################################
def read_wave(path):
    """Reads a .wav file.

    Takes the path, and returns (PCM audio data, sample rate).
    """
    with contextlib.closing(wave.open(path, 'rb')) as wf:
        num_channels = wf.getnchannels()
        assert num_channels == 1
        sample_width = wf.getsampwidth()
        assert sample_width == 2
        sample_rate = wf.getframerate()
        assert sample_rate in (8000, 16000, 32000)
        pcm_data = wf.readframes(wf.getnframes())
        return pcm_data, sample_rate


def write_wave(path, audio, sample_rate):
    """Writes a .wav file.

    Takes path, PCM audio data, and sample rate.
    """
    with contextlib.closing(wave.open(path, 'wb')) as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio)


class Frame(object):
    """Represents a "frame" of audio data."""
    def __init__(self, bytes, timestamp, duration):
        self.bytes = bytes
        self.timestamp = timestamp
        self.duration = duration


def frame_generator(frame_duration_ms, audio, sample_rate):
    """Generates audio frames from PCM audio data.

    Takes the desired frame duration in milliseconds, the PCM data, and
    the sample rate.

    Yields Frames of the requested duration.
    """
    n = int(sample_rate * (frame_duration_ms / 1000.0) * 2)
    offset = 0
    timestamp = 0.0
    duration = (float(n) / sample_rate) / 2.0
    while offset + n < len(audio):
        yield Frame(audio[offset:offset + n], timestamp, duration)
        timestamp += duration
        offset += n


def vad_collector(sample_rate, frame_duration_ms,
                  padding_duration_ms, vad, frames):
    """Filters out non-voiced audio frames.

    Given a webrtcvad.Vad and a source of audio frames, yields only
    the voiced audio.

    Uses a padded, sliding window algorithm over the audio frames.
    When more than 90% of the frames in the window are voiced (as
    reported by the VAD), the collector triggers and begins yielding
    audio frames. Then the collector waits until 90% of the frames in
    the window are unvoiced to detrigger.

    The window is padded at the front and back to provide a small
    amount of silence or the beginnings/endings of speech around the
    voiced frames.

    Arguments:

    sample_rate - The audio sample rate, in Hz.
    frame_duration_ms - The frame duration in milliseconds.
    padding_duration_ms - The amount to pad the window, in milliseconds.
    vad - An instance of webrtcvad.Vad.
    frames - a source of audio frames (sequence or generator).

    Returns: A generator that yields PCM audio data.
    """
    num_padding_frames = int(padding_duration_ms / frame_duration_ms)
    # We use a deque for our sliding window/ring buffer.
    ring_buffer = collections.deque(maxlen=num_padding_frames)
    # We have two states: TRIGGERED and NOTTRIGGERED. We start in the
    # NOTTRIGGERED state.
    triggered = False

    voiced_frames = []
    for frame in frames:
        is_speech = vad.is_speech(frame.bytes, sample_rate)

        sys.stdout.write('1' if is_speech else '0')
        if not triggered:
            ring_buffer.append((frame, is_speech))
            num_voiced = len([f for f, speech in ring_buffer if speech])
            # If we're NOTTRIGGERED and more than 90% of the frames in
            # the ring buffer are voiced frames, then enter the
            # TRIGGERED state.
            if num_voiced > 0.9 * ring_buffer.maxlen:
                triggered = True
                sys.stdout.write('+(%s)' % (ring_buffer[0][0].timestamp,))
                # We want to yield all the audio we see from now until
                # we are NOTTRIGGERED, but we have to start with the
                # audio that's already in the ring buffer.
                for f, s in ring_buffer:
                    voiced_frames.append(f)
                ring_buffer.clear()
        else:
            # We're in the TRIGGERED state, so collect the audio data
            # and add it to the ring buffer.
            voiced_frames.append(frame)
            ring_buffer.append((frame, is_speech))
            num_unvoiced = len([f for f, speech in ring_buffer if not speech])
            # If more than 90% of the frames in the ring buffer are
            # unvoiced, then enter NOTTRIGGERED and yield whatever
            # audio we've collected.
            if num_unvoiced > 0.9 * ring_buffer.maxlen:
                sys.stdout.write('-(%s)' % (frame.timestamp + frame.duration))
                triggered = False
                yield b''.join([f.bytes for f in voiced_frames])
                ring_buffer.clear()
                voiced_frames = []
    if triggered:
        sys.stdout.write('-(%s)' % (frame.timestamp + frame.duration))
    sys.stdout.write('\n')
    # If we have any leftover voiced audio when we run out of input,
    # yield it.
    if voiced_frames:
        yield b''.join([f.bytes for f in voiced_frames])

def checkfilesize(filename):
    if os.path.getsize(filename) < 1000:
        return False
    else:
        return True
    
def is_stereo(filename,y):
    if librosa.util.valid_audio(y)==True:
        return False
    else:
        return True  
    
def remove_silence(filename,sr):

#MAIN METHOD - VAD using webrtcvad (google)
###################################################################
    directory=os.getcwd()
    #convert data to proper format for processing by VAD (downsample to 32000
    data, sample_rate = sf.read(filename) 
    os.remove(filename)
    sf.write(filename,data,32000)
    
    #now frame generate using VAD 
    audio, sample_rate = read_wave(filename)
    vad = webrtcvad.Vad(1)
    frames = frame_generator(30, audio, sample_rate)
    frames = list(frames)
    segments=vad_collector(sample_rate, 30, 300, vad, frames)

    #remove file, create voiced segments, and stitch together 
    os.mkdir(filename[0:-4])
    os.chdir(filename[0:-4])
             
    for i, segment in enumerate(segments):
        path = '%d.wav' % (i,)
        print(' Writing %s' % (path,))
        write_wave(path, segment, sample_rate)

    listdir=os.listdir()
    print(listdir)
    if len(listdir)==0:
        print('silence file')
        silencefile='yes'
    else:
        silencefile='no'
        sound=AudioSegment.from_wav('0.wav') 
        for i in range(1,len(listdir),1):
            file=str(i)+'.wav'
            sound = sound+AudioSegment.from_wav(file)       

    #now go back to host directory and delete directory
    os.chdir(directory)
    shutil.rmtree(filename[0:-4])

    #make new file
    os.remove(filename)
    #should take in existing sample rate 
    sf.write(filename,data,sr)
    
    print(silencefile)

    return [filename, silencefile]

#ALT METHOD 1 - SOUNDFILE
###################################################################   
###   remove_silence script in this directory (uses soundfile to clip under power thresholds)
###   note this is custom code that I wrote to do this...
##        
##    #threshold determined from experimental testing
##    threshold=0.0001
##    data, samplerate = sf.read(filename)
##    
##    datalist=list()
##
##    #REMOVE SILENCE AT THRESHOLD 
##    #########################################################    
##    #rewrite to mono file if it is not already a mono file
##    #more info here: https://stackoverflow.com/questions/30401042/stereo-to-mono-wav-in-python
##    if len(data[0])==1:
##        for i in range(len(data)):
##            framemean=np.mean(data[i])
##            if framemean>=threshold:
##                datalist.append(np.array(data[i][0]))
##            else:
##                pass
##
##    elif len(data[0])==2:
##        for i in range(len(data)):
##            framemean=np.mean(data[i])
##            if framemean>=threshold:
##                datalist.append(np.array(data[i][0],data[i][1]))
##            else:
##                pass
##    elif len(data[1])==3:
##        for i in range(len(data)):
##            framemean=np.mean(data[i])
##            if framemean>=threshold:
##                datalist.append(np.array(data[i][0],data[i][1],data[i][2]))
##            else:
##                pass
##    elif len(data[0])==4:
##        for i in range(len(data)):
##            framemean=np.mean(data[i])
##            if framemean>=threshold:
##                datalist.append(np.array(data[i][0],data[i][1],data[i][2],data[i][3]))
##            else:
##                pass
##            
##    elif len(data[0])==5:
##        for i in range(len(data)):
##            framemean=np.mean(data[i])
##            if framemean>=threshold:
##                datalist.append(np.array(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4]))
##            else:
##                pass
##            
##    elif len(data[0])==6:
##        for i in range(len(data)):
##            framemean=np.mean(data[i])
##            if framemean>=threshold:
##                datalist.append(np.array(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5]))
##            else:
##                pass
##            
##    #TESTING
##    #########################################################
##    #this if for testing what should be cut, etc. 
####    for i in range(0,len(data),samplerate):
####        print(np.mean(data[i]))
####        time.sleep(0.5)
##    #########################################################
##
##    #seconds cleaned
##    datalist=np.array(datalist)
##
##    duration1=len(data)/samplerate
##    duration2=len(datalist)/samplerate
##    silence=duration1-duration2 
##    print('cut off %s seconds'%(str(silence)))
##
##    try:
##        print('writing %s with removed silence'%(filename))
##        #os.remove(filename)
##        sf.write(filename, datalist, samplerate)
##        #can remove original file too...
##    except:
##        print('error writing file')
    
#ALT METHOD 2 - USE PYAUDIOANALYSIS
        
#note there are errors here with python 3 for some reason...
#(we could debug them in future for more robust silence removal - method 1 --> method 2 ---> method 3 --> output silence removal) 
        
##    [Fs, x] = aIO.readAudioFile(filename)
##    segments = aS.silenceRemoval(x, Fs, 0.020, 0.020, smoothWindow = 1.0, Weight = 0.3, plot = False)
    
#ALT METHOD 3 - LIBROSA       
#(we could debug them in future for more robust silence removal - method 1 --> method 2 ---> method 3 --> method 4 --> output silence removal)
###################################################################       
##    print('removing silence...')
##    yt, index=librosa.effects.trim(y)
##    os.remove(filename)
##    
##    #get new duration
##    librosa.output.write_wav(filename, yt, sr)
##    
##    duration2=librosa.core.get_duration(y=yt,sr=sr)
##    silence=duration-duration2
##
##    ff = ffmpy.FFmpeg(
##        inputs={filename:None},
##        outputs={filename[0:-4]+'.wav': None}
##        )
##    
##    print('removed %s seconds of silence...'%(str(silence)))

#ALT METHOD 4 - USE SOX
###################################################################
## THIS IS FROM AN EXTERNAL SHELL COMMAND
##  CAN INTEGRATE THIS INTO FUTURE FOR FILTER PIPELINE METHOD 1 >> METHOD 2 >> METHOD 3 >> METHOD 4 ... --> output removed silence

##    #clip silence and rename file
##    os.chdir(path)
##    os.system("sox %s %s"%(filename,filename)+' silence -l 1 0.1 1% -1 2.0 1%')
##    #os.system("sox %s %s"%(filename, filename2)+" noisered noise.prof 0.21 silence -l 1 0.3 5% -1 2.0 5%")
##    print('removed silence')

from pydub import AudioSegment

def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=10):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms

def remove_leading_trailing(filename, y, sr, duration_uncleaned):
    sound = AudioSegment.from_file(os.getcwd()+'/'+filename, format="wav")
    os.remove(filename)
    start_trim = detect_leading_silence(sound)
    end_trim = detect_leading_silence(sound.reverse())

    duration = len(sound)    
    trimmed_sound = sound[start_trim:duration-end_trim]
    sound.export(filename, format="wav")

    #get new duration
    yt,sr2=librosa.core.load(filename)
    duration_cleaned=librosa.core.get_duration(y=yt,sr=sr)
    silence=duration_uncleaned-duration_cleaned
    
    print('removed %s seconds of silence...'%(str(silence)))

    return [filename, silence, duration_cleaned]

def remove_noise_silence(filename):
#now use sox to denoise using the noise profile and remove silence
#assumes sox is installed on the machine 
    data, samplerate =sf.read(filename)
    duration=data/samplerate
    first_data=samplerate*1
    filter_data=list()
    for i in range(int(first_data)):
        filter_data.append(data[i])
    noisefile='noiseprof.wav'
    sf.write(noisefile, filter_data, samplerate)
    os.system('sox %s -n noiseprof noise.prof'%(noisefile))
    filename2='tempfile.wav'
    filename3='tempfile2.wav'
    noisereduction="sox %s %s noisered noise.prof 0.21 "%(filename,filename2)
    #silencecom="sox %s %s "%(filename2,filename3)
    #silenceremove=silencecom+"silence -l 1 0.1 1% -1 2.0 1%"
    command=noisereduction
    #run command 
    os.system(command)
    print(command)
    #reduce silence again
    #os.system(silenceremove)
    #print(silenceremove)
    #rename and remove files 
    os.remove(filename)
    os.rename(filename2,filename)
    #os.remove(filename2)
    os.remove(noisefile)
    os.remove('noise.prof')

#now use librosa to filter out sound from background mask
##y, sr = librosa.load(filename)
##S_full, phase = librosa.magphase(librosa.stft(y))
##idx = slice(*librosa.time_to_frames([30, 35], sr=sr))
##S_filter = librosa.decompose.nn_filter(S_full,
##                               aggregate=np.median,
##                               metric='cosine',
##                               width=int(librosa.time_to_frames(2, sr=sr)))
##S_filter = np.minimum(S_full, S_filter)
##margin_i, margin_v = 2, 10
##power = 2
##mask_i = librosa.util.softmask(S_filter,
##                       margin_i * (S_full - S_filter),
##                       power=power)
##mask_v = librosa.util.softmask(S_full - S_filter,
##                       margin_v * S_filter,
##                       power=power)
##S_foreground = mask_v * S_full
##S_background = mask_i * S_full
##y_out = librosa.istft(S_full-S_background, length=len(y))
##librosa.output.write_wav(os.getcwd()+'/'+filename, y_out, sr)

####METHOD 2 - USE SCIPY NOISE HIGH/LOW PASS FILTER
##################################################################################    
    #need .wav format
##    wr = wave.open(filename, 'r')
##    par = list(wr.getparams()) # Get the parameters from the input.
##    # This file is stereo, 2 bytes/sample, 44.1 kHz.
##    par[3] = 0 # The number of samples will be set by writeframes.
##    # Open the output file
##    newfile='filtered_'+filename
##    ww = wave.open(newfile, 'w')
##    ww.setparams(tuple(par)) # Use the same parameters as the input file.
##    lowpass = 21 # Remove lower frequencies.
##    highpass = 9000 # Remove higher frequencies.
##    sz = wr.getframerate() # Read and process 1 second at a time.
##    c = int(wr.getnframes()/sz) # whole file
##    for num in range(c):
##        print('Processing {}/{} s'.format(num+1, c))
##        da = np.fromstring(wr.readframes(sz), dtype=np.int16)
##        left, right = da[0::2], da[1::2] # left and right channel
##        lf, rf = np.fft.rfft(left), np.fft.rfft(right)
##        lf[:lowpass], rf[:lowpass] = 0, 0 # low pass filter
##        lf[55:66], rf[55:66] = 0, 0 # line noise
##        lf[highpass:], rf[highpass:] = 0,0 # high pass filter
##        nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
##        ns = np.column_stack((nl,nr)).ravel().astype(np.int16)
##        ww.writeframes(ns.tostring())
##    # Close the files.
##    wr.close()
##    ww.close()
##    #remove old file and write new file with noise reduced
##    os.remove(filename)
##    os.rename(newfile,filename)
##    
##    #now get new file and write with filter first 200 ms (post filter noise)
##    data, samplerate =sf.read(filename)
##    duration=data/samplerate
##    first_data=samplerate*1
##    filter_data=data[0]
##    for i in range(int(first_data)):
##        filter_data=filter_data+data[i]
##    filtermean=filter_data/(first_data+1)
##    new_data=list()
##    for i in range(len(data)):
##        new_data.append(data[i]-filtermean)
##    sf.write(filename, new_data, samplerate)
    
####METHOD 1 - USE FFMPEG-NORMALIZE TO NORMALIZE AUDIO AROUND NORMAL AUDIO
    #remove noise with first 200 ms of audio as a noise average
    
##METHOD 2 - USE ADDITIONAL SOX COMMANDS 
##  CAN INTEGRATE THIS INTO FUTURE FOR FILTER PIPELINE METHOD 1 >> METHOD 2 >> ... --> output noise reduction
    
##    filename2=filename[0:-4]+'_noise.wav'
##    os.system("sox %s %s"%(filename,filename2)+" trim 0 0.900")
##    os.system("sox %s"%(filename2)+" -n noiseprof noise.prof")
##    os.system("sox %s %s"%(filename,filename)+" noisered noise.prof 0.21")
##    print('removed noise')
    
    return filename
              
def stereo2mono(filename):
    #read wav
    y, sr = librosa.load(filename,sr=None)
    mono=librosa.to_mono(y)
    #remove file currently
    os.remove(filename)
    #overwrite file to one channel 
    librosa.output.write_wav(filename,mono,sr)

def getclass(inputlist):
    #for pyaudioanalysis models (loading)
    array=inputlist[1].tolist()
    maxval=np.max(array)
    index=array.index(maxval)
    choices=inputlist[2]
    #output choice
    classtype=choices[index]
    print('the sample is %s'%(classtype))
    
    return classtype

def checkvoice(wavfile,hostdir,incoming_dir):
##    #Hard voting classifier (97-100% accurate at classifying input sample as voice)
##    sample=featurize(wavfile)
##
##    #reshape if one sample
##    sample=sample.reshape(1,-1)
##
##    classtype=model.predict(sample)

    classtype=0
    
    if classtype == 0:
        print('voice sample...')
        return True
        #voice sample 
    else:
        print('other sample...')
        return False

def wavconvert(filename):
    
    #take in an audio file and convert with ffpeg file type
    #types of input files: .ogg 
    #output file type: .wav

    size=os.path.getsize(filename)

    if filename[-4:] != '.wav':
        ff = ffmpy.FFmpeg(
            inputs={filename:None},
            outputs={filename[0:-4]+'.wav': None}
            )
        ff.run()
        stereo2mono(filename[0:-4]+'.wav')
        size2=os.path.getsize(filename[0:-4]+'.wav')
        os.remove(filename)
        #this logs previous file format and size (archived in future for server)
        return [[filename,size], [filename[0:-4]+'.wav',size2]]
    
    else:
        return [[filename,size], [filename,size]]

def oggconvert(filename):

    ##GET RIGHT FILENAME 
    #####################################################################
    if filename[-4:] in ['.wav','.mp3','.mp4','.ogg','.m4a']:
        filename2=filename[0:-4]+'.ogg'
    elif filename[-5:] in ['.webm','.mogg','.flac','aiff']:
        filename2=filename[0:-5]+'.ogg'

    ##CONVERT FILE / REMOVE INTERMEDIATE FILE 
    #####################################################################
    if filename[-4:] != '.ogg':
        if filename[-4:]=='.mp4':
            #VIDEO CONVERSION (EXTRACT ONLY AUDIO)
            print('ffmpeg -i %s -ac 2 -ar 44100 -vn %s'%(os.getcwd()+'/'+filename, os.getcwd()+'/'+filename2))
            print(os.listdir())
            os.system('ffmpeg -i %s -ac 2 -ar 44100 -vn %s'%(os.getcwd()+'/'+filename, os.getcwd()+'/'+filename2))
            print(os.listdir())
            os.remove(filename)
        else:
            #AUDIO CONVERSION
            print('ffmpeg -i %s %s'%(os.getcwd()+'/'+filename,os.getcwd()+'/'+filename2))
            print(os.listdir())
            ff = ffmpy.FFmpeg(
                inputs={filename:None},
                outputs={filename2: None}
                )
            ff.run()
            print(os.listdir())
            os.remove(filename)
    else:
        filename2=filename
    
    return filename2

##GO TO HOST DIRECTORY AND BEGIN BULK PROCESSING 
####################################################################################

#host directory in app is likely /usr/app/...
hostdir=os.getcwd()

#now create some folders if they have not already been created 
incoming_dir=hostdir+'/nlx-clean-incoming/'
processed_dir=hostdir+'/nlx-clean-processed/'

#incoming folder = samples on server that need to be cleaned 
#processed_folder = samples on server that have been cleaned 

try:
    os.chdir(incoming_dir)
except:
    os.mkdir(incoming_dir)

try:
    os.chdir(processed_dir)
except:
    os.mkdir(processed_dir)

#change to incoming directory to look for samples
os.chdir(incoming_dir)

#initialize sleep time for worker (default is 1 second)
sleeptime=1

# now initialize process list with files already in the directory
processlist=list()
convertformat_list=list()

#error counts will help us debug later
errorcount=0
processcount=0

#initialize t for infinite loop
t=1

#infinite loop for worker now begins with while loop...

while t>0:
    #go to incoming directory
    os.chdir(incoming_dir)
    listdir=os.listdir()
    print(listdir)
    
    try:
        if listdir==['DS_Store'] or listdir==[]:
            print("no files found")
            
        else:
        
            #look for any files that have not been previously in the directory
            for i in range(len(listdir)):
                #make sure in incoming directory
                os.chdir(incoming_dir)
                
                if listdir[i] == 'DS_Store':
                    pass
                
                elif listdir[i][-4:] in ['.wav','.mp3','.mp4','.ogg','.m4a'] or listdir[i][-5:] in ['.webm','.mogg','.flac','aiff']:
                    #log start time for later 
                    start_time=time.time()
                                
                    if listdir[i] not in processlist:
                        #get file name 
                        filename=listdir[i]
                        
                        #rename file to have no spaces for ffmpeg later...
                        filename_new=listdir[i].replace(' ','_')
                        os.rename(filename,filename.replace(' ','_'))
                        filename=filename_new
                                  
                        #create a .ogg file for librosa to analyze 
                        #for some reason we need ogg files to do all this processing in librosa or it errors!! Create temp one...
                        oggfile=oggconvert(filename)
                        
                        #get duration and inital numpy array of file for analysis using librosa library
                        y, sr = librosa.load(oggfile,sr=None, mono=True)
                        duration=librosa.core.get_duration(y=y,sr=sr)
                        
                        #make mono if stereo format (remove previous file and overwrite it)
                        if is_stereo(oggfile, y) == True:
                            print('converting stereo file to mono...')
                            newaudiodata=stereo2mono(oggfile)
                            
                        #convert back to .wav
                        output=wavconvert(oggfile)
                        filename=output[1][0]

                        #remove silence from the file
                        print('detecting voice activity...')
                        [filename, silencefile]=remove_silence(filename, sr)

                        if silencefile == 'no':
                            #remove noise and silence from file
                            print('removing noise and silence from file...')
                            filename=remove_noise_silence(filename)
                            
                            #check if file size
                            if checkfilesize(filename)==True:
                                print('file size OK')
                            if sr != 44100:
                                print(sr)
                                
                            if checkfilesize(filename) == True and checkvoice(filename,hostdir,incoming_dir) == True:

                                #get size for .json
                                size=os.path.getsize(filename)

                                #now move the sample to the processed folder 
                                shutil.move(os.getcwd()+'/'+filename,processed_dir+filename)
                                    
                                #log processing time 
                                end_time=time.time()
                                processtime=end_time-start_time

                                #change to processed dir to dump .json
                                os.chdir(processed_dir)

                                #get and store new duration
                                y2, sr2 = librosa.load(filename,sr=None, mono=True)
                                duration2=librosa.core.get_duration(y=y2,sr=sr2)
                                #now get stitched file size
                                size2=os.path.getsize(filename)

                                #silence removed
                                silence=duration-duration2

                                data={
                                    'filename':filename,
                                    'file incoming location':incoming_dir,
                                    'file process location':processed_dir,
                                    'file size':size,
                                    #this is useful for billing purposes...
                                    'file duration':duration,
                                    'cleaned dfile duration':duration2,
                                    'silence removed':silence,
                                    'processed datetime':str(datetime.datetime.now()),
                                    'processing time':processtime,
                                    'cleaned file size':size2,
                                    'process worker count':processcount,
                                    'error count':errorcount,
                                    #'removed segments':removedfilelist,
                                    #keep all for now and A/B test this 
                                    }

                                #write to .json
                                with open(filename[0:-4]+'.json', 'w') as f:
                                    json.dump(data, f)
                                f.close()

                                processcount=processcount+1
                                #sleep before looking for new samples
                                print('running session has processed %s samples'%(str(processcount)))

                            else:
                                #remove the file from pipeline if it is too small                  
                                print('removing file because not a voice file or too small...')
                                
                                try:
                                    os.remove(filename)
                                except:
                                    pass
                        else:
                            print('silence file detected, removing file...')
                            os.remove(filename)
                        
        print('sleeping...')                        
        time.sleep(sleeptime)
               
    except:
        print('worker error on file %s'%(listdir[i]))
        try:
            os.remove(filename)
        except:
            pass
        try:
            os.remove(oggfile)
        except:
            pass
        errorcount=errorcount+1
        time.sleep(sleeptime)
