'''
Audio_stream.py

Give some simple visual feedback when recording an audio stream.
'''
import sounddevice as sd
import soundfile as sf
import random, time, librosa, os 
import numpy as np
import matplotlib.pyplot as plt
from drawnow import drawnow

def make_fig():
    plt.scatter(x, y)  

def record_data(filename, duration, fs, channels):
    # synchronous recording 
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    y, sr = librosa.load(filename)
    rmse=np.mean(librosa.feature.rmse(y)[0])
    os.remove(filename)
    
    return rmse*1000

# initialize plot 
plt.ion()  # enable interactivity
fig = plt.figure()  # make a figure

x = list()
y = list()

for i in range(100):    
    # record 20ms of data 
    sample=record_data('sample.wav',0.02, 44100, 1)
    x.append(i)
    y.append(sample)
    drawnow(make_fig)

plt.savefig('stream.png')
os.system('open stream.png')