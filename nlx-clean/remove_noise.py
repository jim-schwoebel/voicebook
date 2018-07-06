from __future__ import print_function, division, unicode_literals
import wave
from scipy import signal
import soundfile as sf 
import scipy.io.wavfile as wav
from scipy.fftpack import fftfreq
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np


##HELPER FUNCTIONS (from pyRMT library) - MIT License
#https://rsmith.home.xs4all.nl/miscellaneous/filtering-a-sound-recording.html
##########################################################################
#LOAD DATA
filename='test235.wav'
data,samplerate=sf.read(filename)

wr = wave.open(filename, 'r')
par = list(wr.getparams()) # Get the parameters from the input.
# This file is stereo, 2 bytes/sample, 44.1 kHz.
par[3] = 0 # The number of samples will be set by writeframes.

# Open the output file
ww = wave.open('filtered_'+filename, 'w')
ww.setparams(tuple(par)) # Use the same parameters as the input file.

lowpass = 21 # Remove lower frequencies.
highpass = 9000 # Remove higher frequencies.

sz = wr.getframerate() # Read and process 1 second at a time.
c = int(wr.getnframes()/sz) # whole file
for num in range(c):
    print('Processing {}/{} s'.format(num+1, c))
    da = np.fromstring(wr.readframes(sz), dtype=np.int16)
    left, right = da[0::2], da[1::2] # left and right channel
    lf, rf = np.fft.rfft(left), np.fft.rfft(right)
    lf[:lowpass], rf[:lowpass] = 0, 0 # low pass filter
    lf[55:66], rf[55:66] = 0, 0 # line noise
    lf[highpass:], rf[highpass:] = 0,0 # high pass filter
    nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
    ns = np.column_stack((nl,nr)).ravel().astype(np.int16)
    ww.writeframes(ns.tostring())
# Close the files.
wr.close()
ww.close()


