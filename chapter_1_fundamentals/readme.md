*This section documents all the scripts in the Chapter_1_fundamentals folder.*

## Voice computing definitions
**Voice computing** aims to develop hardware or software to process voice inputs. Here are some common terms you will encounter in this discipline:

| Term | Definition | 
| ------- | ------- |
| voice computer | any computerized system (assembled hardware and software) that can process voice inputs.| 
| voice computing software | can read/write, record, clean, encrypt/decrypt, playback, transcode, transcribe, compress, publish, featurize, model, and visualize voice files. | 
| voice computing hardware | can include a motherboard, microphones, sound cards (with D/A and A/D converters), central processing units (CPUs), graphics cards, storage devices (e.g. hard disks), computer monitors, WiFi chips, bluetooth chips, radio transmitters, speakers, and a power supply. | 
| microphone  |  a transducer that converts sound (e.g. pressure waves in air) into an electrical signal (e.g. amps - C/s).  |
| sound cards  | convert audio from PCM data to various audio formats (e.g. .WAV) through audio codecs.  |
| codec |  software program used to encode and decode digital audio data to and from a digital audio coding format. | 
| audio coding format | the output file type of a digital signal that has been manipulated by an audio codec program. | 
| transcoding | the process of converting one audio coding format to another. | 
| audio channels | the number of audio inputs or outputs of a recorded audio signal. | 
| speaker |  Speakers operate in the reverse way as a microphone, where analog sound is transduced from an electrical signal (e.g. current - amps). | 

## Installing dependencies 
See [getting started](https://github.com/jim-schwoebel/voicebook/wiki/0.0.-Getting-started).
## How to read and write audio files
using various libraries: pydub, wave, librosa, and soundfile. 
```Python3
from pydub import AudioSegment
data = AudioSegment.from_wav("test.wav")
data.export("new_test.wav")

import wave
data=wave.open('test.wav', mode='rb')
params=data.getparams()
# _wave_params(nchannels=1, sampwidth=2, framerate=16000, nframes=47104, comptype='NONE', compname='not compressed')

import librosa
y, sr = librosa.load('test.wav')
librosa.output.write_wav('new_test.wav', y, sr)

from scipy.io import wavfile
fs, data = wavfile.read('test.wav')
wavfile.write('new_test.wav',fs, data)

import soundfile as sf
data, fs = sf.read('test.wav')
sf.write('new_test.ogg', data, fs)
```
## Manipulating audio files 
Assumes [SoX](http://sox.sourceforge.net/) is installed on the host system.
```Python3
import os
# take in one.wav and two.wav to make three.wav 
os.system('sox one.wav two.wav three.wav')
# take first second of one.wav and output to output.wav  
os.system('sox one.wav output.wav trim 0 1')
# make volume 2x in one.wav and output to volup.wav 
os.system('sox -v 2.0 one.wav volup.wav')
# make volume ½ in one.wav and output to voldown.wav 
os.system('sox -v -0.5 one.wav volup.wav')
# reverse one.wav and output to reverse.wav 
os.system('sox one.wav reverse.wav reverse')
# change sample rate of one.wav to 16000 Hz
os.system('sox one.wav -r 16000 sr.wav')
# change audio file to 16 bit quality
os.system('sox -b 16 one.wav 16bit.wav')
# convert mono file to stereo by cloning channels
os.system('sox one.wav -c 2 stereo.wav')
# make stereo file mono by averaging out the channels
os.system('sox stereo.wav -c 1 mono.wav')
# double speed of file 
os.system('sox one.wav 2x.wav speed 2.0')
```
## Playing audio files 
### synchronous playback
play_sync.py
```Python3
'''
play_sync.py
Play back an audio file synchronously.
'''

import pygame

def sync_playback(filename):
    # takes in a file and plays it back 
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

sync_playback('one.wav')
```
### asynchronous playback
play_async.py
```Python3
import sounddevice as sd
import soundfile as sf
import time 

def async_playback(filename):
    data, fs = sf.read(filename)
    sd.play(data, fs)
    return data, fs 

# playback file 
data, fs = async_playback('play.wav')

# can execute commands 
print('able to execute this before finishing')
print('hi, this is cool!')

# can stop after 1 second playing back
time.sleep(1)
sd.stop()
print('stopped')
```
## Recording streaming audio
### check microphone / set default mic
mic_check.py
```Python3
import sounddevice as sd

mics=sd.query_devices()
default_devices=sd.default.device
default_input=default_devices[0]
default_output=default_devices[1]

# prints all available devices 
for i in range(len(mics)):
    print(mics[i])

# can set default device easily with 
sounddevice.default.device = 0
```

### synchronous recording 
sync_record.py
```Python3
import sounddevice as sd
import soundfile as sf
import time 

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

# playback file 
sync_record('sync_record.wav', 10, 16000, 1)
```
### asynchronous recording
async_record.py
```Python3
import sounddevice as sd
import soundfile as sf
import time 

def printstuff(number):
    for i in range(number):
         print(i)

def async_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    # can execute commands 
    print('able to execute this before finishing')
    printstuff(30)
    # now wait until done before writing to file 
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

# playback file 
async_record('async_record.wav', 10, 16000, 1)
```
## Converting audio formats 
### using [ffmpy module](https://ffmpy.readthedocs.io/en/latest/)
convert_wav.py
```Python3
import ffmpy

def convert_wav(filename):
    #take in an audio file and convert with ffmpeg file type
    #types of input files: .mp3 
    #output file type: .wav
   
    if filename[-4:] in ['.mp3','.m4a','.ogg']:
        ff = ffmpy.FFmpeg(
            inputs={filename:None},
            outputs={filename[0:-4]+'.wav': None}
            )
        ff.run()

convert_wav('test.mp3')
```
## Transcribing audio 
### using [PocketSphinx](https://github.com/cmusphinx/pocketsphinx-python)
sphinx_transcribe.py
```Python3
import speech_recognition as sr_audio
import sounddevice as sd
import soundfile as sf
import os, json, datetime

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

def transcribe_audio_sphinx(filename):
    # transcribe the audio (note this is only done if a voice sample)
    r=sr_audio.Recognizer()
    with sr_audio.AudioFile(filename) as source:
        audio = r.record(source) 
    text=r.recognize_sphinx(audio)
    print('transcript: '+text)
    
    return text

def store_transcript(filename, transcript):
    jsonfilename=filename[0:-4]+'.json'
    print('saving %s to current directory'%(jsonfilename))
    data = {
        'date': str(datetime.datetime.now()),
        'filename':filename,
        'transcript':transcript,
        }
    print(data)
    jsonfile=open(jsonfilename,'w')
    json.dump(data,jsonfile)
    jsonfile.close()

# record file and print transcript
filename='sync_record.wav'
sync_record(filename, 10, 16000, 1)
transcript=transcribe_audio_sphinx(filename)

# now write the transcript into a .json file
# e.g. sync_record.wav transcript will be stored in sync_record.json
store_transcript(filename, transcript)
```
### using [Google Speech-to-Text API](https://cloud.google.com/speech-to-text/)
google_transcribe.py
```Python3
# assumes environment variables are set properly following the Google Speech API documentation
import speech_recognition as sr_audio
import sounddevice as sd
import soundfile as sf
import os, json, datetime

def transcribe_audio_google(filename):
    # transcribe the audio (note this is only done if a voice sample)
    r=sr_audio.Recognizer()
    with sr_audio.AudioFile(filename) as source:
        audio = r.record(source) 
    text=r.recognize_google_cloud(audio)

    return text    

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

def store_transcript(filename, transcript):
    jsonfilename=filename[0:-4]+'.json'
    print('saving %s to current directory'%(jsonfilename))
    data = {
        'date': str(datetime.datetime.now()),
        'filename':filename,
        'transcript':transcript,
        }
    print(data)
    jsonfile=open(jsonfilename,'w')
    json.dump(data,jsonfile)
    jsonfile.close()

# record file and print transcript
filename='google_record.wav'
sync_record(filename, 10, 16000, 1)
transcript=transcribe_audio_google(filename)

# now write the transcript into a .json file
# e.g. sync_record.wav transcript will be stored in sync_record.json
store_transcript(filename, transcript)
```
## Text-to-speech systems 
### using [Pyttsx3](https://github.com/nateshmbhat/pyttsx3)
Abridged from speak_custom.py
```Python3
import pyttsx3
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak_text('this is a test')
```
### using [Google TTS API](https://cloud.google.com/text-to-speech/)
speak_google.py
```Python3
def speak_google(text, filename, model):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE,
        name=model)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open(filename, 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file %s'%(filename))

# experiment with various voices
base='output'
models=['en-US-Wavenet-A','en-US-Wavenet-B','en-US-Wavenet-C','en-US-Wavenet-D',
        'en-US-Wavenet-E','en-US-Wavenet-F']
text='hey I am testing out google TTS'

# loop through various voices
# now all these files will be in the current directory 
for i in range(len(models)):
    speak_google(text, base+'_'+models[i]+'.mp3', models[i])
```
## References
If you are interested to read more on any of these topics, check out the documentation below.

**Reading/writing voice files**
* [Soundfile](https://github.com/bastibe/SoundFile)

**Manipulating voice files** 
* [SoX](http://sox.sourceforge.net/)
* [Pydub](https://github.com/jiaaro/pydub)
 
**Audio file playback**
* [Pygame](https://www.pygame.org/docs/ref/mixer.html)
* [Sounddevice](https://python-sounddevice.readthedocs.io/en/0.3.11/)

**Recording audio files**
* [Sounddevice](https://python-sounddevice.readthedocs.io/en/0.3.11/) 

**Audio file conversion**
* [FFmpeg](https://www.ffmpeg.org/) 
* [ffmpy module](http://ffmpy.readthedocs.io/en/latest/) 

**Transcription**
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* [Pocketsphinx](https://github.com/cmusphinx/pocketsphinx-python) 
* [Google Speech API](https://cloud.google.com/speech-to-text/)

**Text-to-speech systems (TTS)**
* [Pyttsx3](https://github.com/nateshmbhat/pyttsx3)
* [Google TTS](https://cloud.google.com/text-to-speech/)
