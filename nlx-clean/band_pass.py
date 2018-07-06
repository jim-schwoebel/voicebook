'''
Bandpass filter for human voice range.

Good for filtering signals on our server.

REFERENCES:

https://dsp.stackexchange.com/questions/2993/human-speech-noise-filter
https://rsmith.home.xs4all.nl/miscellaneous/filtering-a-sound-recording.html

'''
from scipy.signal import butter, lfilter, filtfilt
import os
import numpy as np
from scipy.io import wavfile
import soundfile as sf
import wave

os.chdir("/Users/jimschwoebel/desktop")
filename='test2.wav'
sr,wr=wavfile.read(filename)

def stereoToMono(audiodata):
    try:
        d = audiodata.sum(axis=1) / 2

        return np.array(d, dtype='int16')
    except:
        return audiodata

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a 

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = filtfilt(b, a, data)
    y=np.array(y,dtype='int16')
    return y

wr=stereoToMono(wr)
# 80 - 8000 HZ suggested by online forum 
output=butter_bandpass_filter(wr, 80,8000,sr,order=5)

# write to new file and remove previous file
sf.write('filtered-test.wav', output,sr)
