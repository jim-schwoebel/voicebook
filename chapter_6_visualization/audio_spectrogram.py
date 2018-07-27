'''
Audio_spectrogram.py

Librosa figures for a given piece of data.

Taken from librosa documentation 
https://librosa.github.io/librosa/generated/librosa.display.specshow.html 
'''
import librosa, os
import matplotlib.pyplot as plt
import numpy as np
import librosa.display
import audio_plot as ap 

# load file 
data_dir=os.getcwd()+'/data'
os.chdir(data_dir)
filename='Voice.wav'
imgfile=ap.plot_spectrogram(filename)