'''
Audio_stream.py

Give some simple visual feedback when recording an audio stream.
'''
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr_audio
import random, time, librosa, os 
import numpy as np
import matplotlib.pyplot as plt
from drawnow import drawnow

def transcribe_pocket(filename):
    # transcribe the audio (note this is only done if a voice sample)
    r=sr_audio.Recognizer()
    try:
        with sr_audio.AudioFile(filename) as source:
            audio = r.record(source) 
        text=r.recognize_sphinx(audio)    
    except:
        text=''
        
    return text

def make_fig():
    plt.scatter(x, y)  


def record_data(filename, duration, fs, channels):
    # synchronous recording 
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)

# initialize plot 
plt.ion()  # enable interactivity
fig = plt.figure()  # make a figure

x = list()
y = list()

transcriptions=list()
for i in range(30):    
    # record 20ms of data 
    sample=record_data('sample.wav',1, 44100, 1)
    transcription=transcribe_pocket('sample.wav')
    x.append(i)
    y.append(len(transcription.split()))
    transcriptions.append(transcription)
    drawnow(make_fig)
    # put words on top of the graph
    os.remove('sample.wav')

# label all the points with spoken words
for i, transcript in enumerate(transcriptions):
    plt.annotate(transcript, (x[i],y[i]))

plt.xlabel('time (seconds)')
plt.ylabel('number of words')
plt.savefig('wordstream.png')
os.system('open wordstream.png')