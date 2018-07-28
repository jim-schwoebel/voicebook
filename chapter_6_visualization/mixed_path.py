'''
Mixed path.py

Give some simple visual feedback when recording an audio stream with
text and rmse.

Mixes features intuitively to gauge how power relates to keywords.
'''
import sounddevice as sd
import soundfile as sf
import random, time, librosa, os 
import numpy as np
import matplotlib.pyplot as plt
import speech_recognition as sr_audio
from drawnow import drawnow

def make_fig():
    plt.scatter(x, y)
    for i, transcript in enumerate(transcriptions):
        plt.annotate(transcript, (x[i],y[i]))

def annotate(transcript, x,y):
    plt.annotate(transcript, (x,y))
    
def record_data(filename, duration, fs, channels):
    # synchronous recording 
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    y, sr = librosa.load(filename)
    rmse=np.mean(librosa.feature.rmse(y)[0])
    
    return rmse*1000

def transcribe_pocket(filename):
    # transcribe the audio (note this is only done if a voice sample)
    try:
        r=sr_audio.Recognizer()
        with sr_audio.AudioFile(filename) as source:
            audio = r.record(source) 
        text=r.recognize_sphinx(audio)
    except:
        text=''
    print(text)
    
    return text

# initialize plot 
plt.ion()  # enable interactivity
fig = plt.figure()  # make a figure

x = list()
y = list()
transcriptions=list()

for i in range(30):    
    # record 20ms of data 
    sample=record_data('sample.wav',1, 44100, 1)
    transcript = transcribe_pocket('sample.wav')
    transcriptions.append(transcript)
    os.remove('sample.wav')
    x.append(i)
    y.append(sample)
    drawnow(make_fig)

plt.xlabel('time (seconds)')
plt.ylabel('root mean square power (average)')
plt.savefig('mixedstream.png')
os.system('open mixedstream.png')
