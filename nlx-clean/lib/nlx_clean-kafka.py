'''
All the helper functions for nlx-clean (kafka version)
'''
# STEP 1: INITIALIZE FUNCTIONS (FROM NLX-CLEAN.PY)
#########################################################
def dict_to_binary(the_dict):
    str = json.dumps(the_dict)
    binary = ' '.join(format(ord(letter), 'b') for letter in str)
    return binary

def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)  
    return d

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

# MAIN METHOD - VAD using webrtcvad (google)
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
    silencecom="sox %s %s "%(filename2,filename3)
    silenceremove=silencecom+"silence -l 1 0.1 1% -1 2.0 1%"
    command=noisereduction
    #run command 
    os.system(command)
    print(command)
    #reduce silence again
    os.system(silenceremove)
    print(silenceremove)
    #rename and remove files 
    os.remove(filename)
    os.rename(filename3,filename)
    os.remove(filename2)
    os.remove(noisefile)
    os.remove('noise.prof')
    
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
