'''
audio_plotspd.py

Takes in a folder of .wav files and plots them in terms of their
spectral power densities (PSDs).

Note it's best to limit the visualization to around 15-30 samples;
otherwise, it can get pretty cluttered.

Following tutorial here:
https://www.kaggle.com/vinayshanbhag/visualizing-audio-data
'''

import numpy as np # linear algebra
from subprocess import check_output

# Any results you write to the current directory are saved as output.
import scipy.io.wavfile as wav
import scipy.signal as signal
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

os.chdir('data/samples')
files = sorted(os.listdir())
columns=5

fig, ax = plt.subplots(int(np.ceil(len(files)/columns)),columns,figsize=(10,10))
fig.suptitle("Spectral Power Density", x=0.5, y=1.05, fontsize=16)
for idx, file in enumerate(files):
    if file[-4:]=='.wav':
        r,c = idx//columns, idx%columns
        rate, data = wav.read(file)
        f, Pxx = signal.welch(data, fs=rate)
        ax[r,c].semilogy(f,Pxx)
        ax[r,c].set_title(file);
        if not c and not r:
            ax[r,c].set_xlabel("frequency")
            ax[r,c].set_ylabel("power");
    
plt.tight_layout()
plt.subplots_adjust(wspace=0.05, hspace=0.1)
plt.savefig('plotspd.png')
os.system('open plotspd.png')
