*This section documents all the scripts in the Chapter_2_collection folder.*

## Recording modes
There are 6 main recording modes when collecting voice samples from end users:

| Mode | Description | 
| ------- | ------- |
| Active-synchronous (AS) mode | record audio synchronously, prompting a user action. | 
| Active-asynchronous (AA) mode | record audio asynchronously, prompting a user action. |
| Passive-synchronous (PS) mode | record audio in the background synchronously, prompting no user action. | 
| Passive-asynchronous (PA) mode | record audio in the background asynchronously, prompting no user action | 
| Active-Passive synchronous (APS) mode | record audio actively - prompting a user action, followed by recording an audio sample passively - all in a synchronous manner. |
| Active-Passive asynchronous (APA) mode | record audio actively - prompting a user action, followed by recording an audio sample passively - all in an asynchronous manner. | 

### Active Asynchronous mode
as_record.py 
```python3 
import sounddevice as sd
import soundfile as sf 
from bs4 import BeautifulSoup
import speech_recognition as sr_audio
import os, pyttsx3, pygame, time

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')
    
def sync_playback(filename):
    # takes in a file and plays it back 
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def speak_text(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def transcribe_audio_sphinx(filename):
    # transcribe the audio (note this is only done if a voice sample)
    r=sr_audio.Recognizer()
    with sr_audio.AudioFile(filename) as source:
        audio = r.record(source) 
    text=r.recognize_sphinx(audio)
    print('transcript: '+text)
    return text
    
def fetch_weather():
    os.system('open https://www.yahoo.com/news/weather')

speak_text('would you like to get the weather?')
sync_playback('beep.mp3')
time.sleep(2)
sync_record('response.wav',2,16000,1)
transcript=transcribe_audio_sphinx('response.wav')
if transcript.lower().find('yes') >= 0 or transcript.lower().find('yeah') >= 0:
    fetch_weather()
```
### Active Asynchronous mode
aa_record.py 
```python3
import sounddevice as sd
import soundfile as sf 
from bs4 import BeautifulSoup
import speech_recognition as sr_audio
import os, pyttsx3, pdfkit, pygame

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    try:
        fetch_weather()
    except:
        pass
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')
    
def sync_playback(filename):
    # takes in a file and plays it back 
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def speak_text(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def transcribe_audio_sphinx(filename):
    # transcribe the audio (note this is only done if a voice sample)
    r=sr_audio.Recognizer()
    with sr_audio.AudioFile(filename) as source:
        audio = r.record(source) 
    text=r.recognize_sphinx(audio)
    print('transcript: '+text)
    return text
    
def fetch_weather():
    link='https://www.yahoo.com/news/weather'
    pdfkit.from_url(link, 'out.pdf')

speak_text('would you like to get the weather?')
sync_playback('beep.mp3')
time.sleep(1.2)
sync_record('response.wav',5,16000,1)
transcript=transcribe_audio_sphinx('response.wav')
if transcript.lower().find('yes') >= 0 or transcript.lower().find('yeah')>=0:
    speak_text('ok, great here it is.')
    os.system('open out.pdf')
```
### Passive-synchronous (PS) mode
ps_record.py
```python3
import sounddevice as sd
import soundfile as sf 
import time, os, shutil 


def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')


# make a folder to put recordings in 
try:
    os.mkdir('recordings')
    os.chdir(os.getcwd()+'/recordings')
except:
    shutil.rmtree('recordings')
    os.mkdir('recordings')
    os.chdir(os.getcwd()+'/recordings')
    
i=0

# loop through 10 times recording a 2 second sample 
# can change to infinite loop ==> while i > -1: 
while i<10:
    # record a mono file synchronously
    filename=str(i+1)+'.wav'
    print('recording %s'%(filename))
    sync_record(filename, 2, 16000, 1)
    time.sleep(10)
    i=i+1
```
### Passive-asynchronous (PA) mode 
pa_record.py
```python3
import sounddevice as sd
import soundfile as sf 
import time, os, shutil, psutil 
# define synchronous recording function (did this is Chapter 1)
def get_battery():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    return percent 

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    print('battery is currently at %s'%get_battery())
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')
# make a folder to put recordings in 
try:
    os.mkdir('recordings')
    os.chdir(os.getcwd()+'/recordings')
except:
    shutil.rmtree('recordings')
    os.mkdir('recordings')
    os.chdir(os.getcwd()+'/recordings')
    
i=0

# loop through 10 times recoridng a 2 second sample 
# can change to infinite loop ==> while i > -1: 
while i<10:
    # record a mono file synchronously
    filename=str(i+1)+'.wav'
    print('recording %s'%(filename))
    sync_record(filename, 2, 16000, 1)
    time.sleep(10)
    i=i+1
```
### Active-passive synchronous (APS) mode 
aps_record.py
```python3
import os

# ONLY 1 CONFIGURATION 
# active-synchronous (AS)
os.system('python3 as_record.py')
# passive-synchronous (PS)
os.system('python3 ps_record.py')
```
### Active-passive-asynchronous (APA) mode 
apa_record.py
```python3 
import os

# APA CONFIG 1 (AA → PA)
os.system('python3 aa_record.py')
os.system('python3 pa_record.py')

# APA CONFIG 2 (AS→ PA)
# os.system('python3 as_record.py')
# os.system('python3 pa_record.py')

# APA CONFIG 3 (AA→ PS)
# os.system('python3 aa_record.py')
# os.system('python3 ps_record.py')
```

## Cleaning audio files
### Removing noise
remove_noise.py
```python3 
import soundfile as sf
import os

def remove_noise(filename):
    #now use sox to denoise using the noise profile
    data, samplerate =sf.read(filename)
    duration=data/samplerate
    first_data=samplerate/10
    filter_data=list()
    for i in range(int(first_data)):
        filter_data.append(data[i])
    noisefile='noiseprof.wav'
    sf.write(noisefile, filter_data, samplerate)
    os.system('sox %s -n noiseprof noise.prof'%(noisefile))
    filename2='tempfile.wav'
    filename3='tempfile2.wav'
    noisereduction="sox %s %s noisered noise.prof 0.21 "%(filename,filename2)
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

    return filename

remove_noise('test.wav')
```
### changing volume
change_volume.py
```python3
import os

def change_volume(filename, vol):
    # rename file
    if vol > 1:
        new_file=filename[0:-4]+'_increase_'+str(vol)+'.wav'
    else:
        new_file=filename[0:-4]+'_decrease_'+str(vol)+'.wav'
    # changes volume, vol, by input 
    os.system('sox -v %s %s %s'%(str(vol),filename,new_file))

    return new_file 
# increase volume by 2x 
new_file=change_volume('5.wav', 2)
# decrease volume by 1/2 
new_file=change_volume('5.wav', 0.5)
```
### trim audio 
trim_audio.py
```python3 
import os
def trim_audio(filename, start, end):
	clip_duration=end-start 
	new_filename=filename[0:-4]+'_trimmed_'+str(start)+'_'+str(end)+'.wav'
	command='sox %s %s trim %s %s'%(filename,new_filename,str(start),str(clip_duration))
	os.system(command)
	return new_filename

# trim from second 30 to 40 => (test_trimmed_30_40.wav)
trim_audio('test.wav', 30, 40)
```
### combining audio files 
combine.py
```python3
import os

def combine_files(one,two):
    three=one[0:-4]+'_'+two[0:-4]+'.wav'
    os.system('sox %s %s %s'%(one,two,three))
    return three

combine_files('test1.wav','test2.wav')
```
### transcoding
transcode.py
```python3 
import os

def combine_files(one,two):
    three=one[0:-4]+'_'+two[0:-4]+'.wav'
    os.system('sox %s %s %s'%(one,two,three))
    return three

combine_files('test1.wav','test2.wav')
```

### changing sample rates 
change_samplerate.py
```python3 
import os

def change_samplerate(filename, samplerate):
    new_filename=filename[0:-4]+'_sr'+str(samplerate)+'.wav
    new_samplerate=str(int(samplerate/1000))
    os.system('sox %s -r %sk %s'%(filename, new_samplerate, new_filename))
    return new_filename

change_samplerate('test.wav',48000)
```
### changing number of channels 
change_channels.py
```python3
import os

def stereo2mono(filename):
    #Change stereo to mono 
    new_filename=filename[0:-4]+'_mono.wav'
    os.system('sox %s %s remix 1-2'%(filename,new_filename))
    return new_filename
def separate_channels(filename):
    #Change stereo to two mono files (mix-down)
    channel_1=filename[0:-4]+'_1.wav'
    channel_2=filename[0:-4]+'_2.wav'
    os.system('sox %s %s remix 1'%(filename, channel_1))
    os.system('sox %s %s remix 2'%(filename, channel_2))
    return channel_1, channel_2
def multiplex(channel_1, channel_2):
    #Convert two mono files into one stereo file (multiplexing)
    output=channel_1[0:-4]+'_'+channel_2[0:-4]+'.wav'
    os.system('sox -M %s %s %s'%(channel_1,channel_2,output))
    return output

stereo2mono('stereo.wav')
separate_channels('stereo.wav')
multiplex('stereo_1.wav','stereo_2.wav')
```
### removing silence
trim_silence.py
```python3
import os

def trim_silence(filename):
	new_filename=filename[0:-4]+'_trimmed.wav'
	command='sox %s %s silence -l 1 0.1 1'%(filename, new_filename)+"% -1 2.0 1%"
	os.system(command)
	return new_filename

# trim the leading and trailing silence => (test_trimmed.wav)
trim_silence('test.wav')
```
## Speaker diarization  
Run this in the terminal:
```python3
cd ~
cd voicebook/chapter_2_collection
python3 diarize.py
```
Now there will be 2 folders made in the current directory: diarize_incoming and diarize_processed. If you put in the file that needs to be diarized in the diarize_incoming folder the file will automatically be diarized into Speaker A and Speaker B. Then, each speaker is transcribed using Google Speech API (if applicable) or Pocketsphinx.

## Storing voice files 
### converting to .FLAC format 
convert_flac.py
```python3
import shutil, os, ffmpy 

def zipdir(folder, delete):
    # ziph is zipfile handle
    shutil.make_archive(folder, 'zip', folder)
    if delete == True:
        shutil.rmtree(folder)

def convert_flac():
    listdir=os.listdir()
    removedfiles=list()
    for i in range(len(listdir)):
        if listdir[i][-4:]!='flac':
            file=listdir[i]
            newfile=file[0:-4]+'.flac'
            os.system('ffmpeg -i %s %s'%(file,newfile))
            os.remove(file)
            removedfiles.append(file)
    return removedfiles 

# get 10 files recorded in 'recordings' folder in current directory
# record them if the folder doesn't exist 
hostdir=os.getcwd()
if 'recordings' not in os.listdir():
    os.system('python3 ps_record.py')

# change to directory of recordings to compress all files in directory 
os.chdir(hostdir+'/recordings')
convert_flac()

# change back to main directory and compress files, delete main folder 
os.chdir(hostdir)
zipdir('recordings', True)
```
### converting to .OPUS format 
```python3
import shutil, os, ffmpy 

def zipdir(folder, delete):
    # ziph is zipfile handle
    shutil.make_archive(folder, 'zip', folder)
    if delete == True:
        shutil.rmtree(folder)

def convert_opus(opusdir):
    curdir=os.getcwd()
    listdir=os.listdir()
    removedfiles=list()
    for i in range(len(listdir)):
        if listdir[i][-4:]!='opus':
            # get new file names 
            file=listdir[i]
            newfile=file[0:-4]+'.opus'
            # copy file to opus encoding folder 
            shutil.copy(curdir+'/'+file, opusdir+'/'+file)
            os.chdir(opusdir)
            # encode with opus codec 
            os.system('opusenc %s %s'%(file,newfile))
            shutil.copy(opusdir+'/'+newfile, curdir+'/'+newfile)
            # delete files in opus folder 
            os.remove(file)
            os.remove(newfile)
            # delete .wav file in original dir 
            os.chdir(curdir)
            os.remove(file)
            removedfiles.append(file)
    return removedfiles 

# get 10 files recorded in 'recordings' folder in current directory
# record them if the folder doesn't exist 
hostdir=os.getcwd()
opusdir=hostdir+'/opustools'
if 'recordings' not in os.listdir():
    os.system('python3 ps_record.py')

# change to directory of recordings to compress all files in directory 
os.chdir(hostdir+'/recordings')
convert_opus(opusdir)

# change back to main directory and compress files, delete main folder 
os.chdir(hostdir)
zipdir('recordings', True)
```
### unpacking compressed .FLAC or .OPUS files 
unpacking_files.py
```python3
import zipfile, os, shutil

def unzip(file):
    filepath=os.getcwd()+'/'+file
    folderpath=os.getcwd()+'/'+file[0:-4]
    zip = zipfile.ZipFile(filepath)
    zip.extractall(path=folderpath)
def convert_wav(opusdir):
    curdir=os.getcwd()
    listdir=os.listdir()
    removedfiles=list()

    for i in range(len(listdir)):
        file=listdir[i]
        newfile=file[0:-5]+'.wav'
        if file[-5:] in ['.opus','.flac']:
            if file[-5:]=='.flac':
                os.system('ffmpeg -i %s %s'%(file, newfile))
                os.remove(file)
            elif file[-5:]=='.opus':
                # copy file to opus encoding folder 
                print(file)
                shutil.copy(curdir+'/'+file, opusdir+'/'+file)
                os.chdir(opusdir)
                # encode with opus codec 
                os.system('opusdec %s %s'%(file,newfile))
                shutil.copy(opusdir+'/'+newfile, curdir+'/'+newfile)
                # delete files in opus folder 
                os.remove(file)
                os.remove(newfile)
                # delete .wav file in original dir 
                os.chdir(curdir)
                os.remove(file)

# extract zip file into 'recordings' folder
unzip('recordings.zip')
# now cd into this folder and convert files to wav format
opusdir=os.getcwd()+'/opustools'
os.chdir('recordings')
print(os.listdir())
convert_wav(opusdir)
```
### uploading files to a FTP server
store_ftp.py
```python3
import sounddevice as sd
import soundfile as sf 
import time, os, shutil 
from ftplib import FTP


def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')
    return filename 

def upload_file(file, session)
    uploadfile = open(file,'rb')
    session.storbinary('STOR %s'%(file),uploadfile,1024)
    uploadfile.close() 

# get environment variables 
domain=os.environ['DOMAIN_NAME']
username=os.environ['DOMAIN_USER']
password=os.environ['DOMAIN_PASSWORD']

# log into session
session = ftplib.FTP(domain,username,password)

# record sample (note, could loop through and record samples with while loop)
file = sync_record('test.wav',10,16000,1)

# upload to server / remove file 
upload_file(file, session)
os.remove(file)

# log off server 
session.quit()
```
### uploading files to Google cloud storage 
store_gcp.py
```python3
import sounddevice as sd
import soundfile as sf 
import time, os, shutil 
from google.cloud import storage

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')
    return filename 


def upload_gcp(bucket_name, source_file_name):
    destination_blob_name=source_file_name
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = 'test-bucket'

# Creates the new bucket
bucket = storage_client.create_bucket(bucket_name)
print('Bucket {} created.'.format(bucket.name))

# get a recording (can loop here too)
file=syn_record('test.wav', 10, 16000, 1)
# upload this recording to gcp
upload_gcp(bucket_name, file)
# delete file after the recording has been uploaded 
os.remove(file)
```
## MEMUPPS voice controls
Having a consistent **M**icrophone type, recording **E**nvironment, recording **M**ode, **U**ser operation, cleaning **P**rocess, **P**ublishing medium, and **S**torage method is important to collect and distribute high-quality data. These are known as **MEMUPPS controls.** 

label_memupps.py
```python3
import os, taglib, json
import sounddevice as sd
import soundfile as sf 

def get_defaults():
    if 'label.json' in os.listdir():
        data=json.load('label.json')
    else:
        mic=input('what is the microphone?')
        env=input('what is the environment?')
        mode=input('what is the mode?')
        sampletype=input('sample type? (e.g. voice)')
        distance=input('what is the distance from mic?')
        process=input('do you use any processing (e.g. SoX noisefloor, .wav--> .opus --> .wav)? if so what?')
        storage=input('where are you storing files?')
        data={
            'microphone':mic,
            'environment':env,
            'mode':mode,
            'sample type': sampletype,
            'distance':distance,
            'processing':process,
            'storage':storage,
        }
            
        jsonfile=open('label.json','w')
        json.dump(data,jsonfile)
        jsonfile.close()
    return data 

def label_sample(file):
    data=get_defaults()    
    audio=taglib.File(os.getcwd()+'/'+file)
    print(audio)
    audio.tags['microphone']=data['microphone']
    audio.tags['environment']=data['environment']
    audio.tags['mode']=data['mode']
    audio.tags['sample type']=data['sample type']
    audio.tags['distance']=data['distance']
    audio.tags['processing']=data['processing']
    audio.tags['storage']=data['storage']
    audio.save()

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')
    label_sample(filename)

file='test.wav'
sync_record(file,10,18000,1)
```
## References
If you are interested to read more on any of these topics, check out the documentation below.

**Data collection**
* [pysoundfile](https://pysoundfile.readthedocs.io/en/0.9.0/) 
* [sounddevice](https://python-sounddevice.readthedocs.io/en/0.3.11/) 
* [os](https://docs.python.org/3/library/os.html) 

**Cleaning audio** 
* [sox](http://sox.sourceforge.net/)

**Speaker diarization** 
* [pyaudioanalysis](https://github.com/tyiannak/pyAudioAnalysis/wiki/5.-Segmentation)

**Transcoding** 
* [ffmpeg](https://www.ffmpeg.org/)
* [.opus codec](http://opus-codec.org/)
* [.flac codec](https://xiph.org/flac/)
 
**Storage**
* [google cloud storage client library](https://cloud.google.com/storage/docs/reference/libraries)
* [ftplib](https://docs.python.org/3/library/ftplib.html) 
* [shutil](https://docs.python.org/3/library/shutil.html)
* [zipfile](https://docs.python.org/3/library/zipfile.html)

**MEMUPPS voice controls**
* [pytaglib](https://pypi.org/project/pytaglib/)
