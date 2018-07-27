'''
audio_plotmany.py

Takes in a folder of .wav files and plots them.

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
fig, ax = plt.subplots(int(np.ceil(len(files)/columns))*2,columns,figsize=(15,30))
fig.suptitle("Frequency Spectrum & Oscillogram", x=0.5, y=0.91, fontsize=16)
for idx, file in enumerate(files):
    r,c = idx//columns*2, idx%columns
    rate, data = wav.read(file)
    f, t, Sxx = signal.spectrogram(data, fs=rate)
    d = 20*np.log10(Sxx+1e-10)
    ax[r,c].pcolormesh(t,f,d, vmin=-1e1,vmax=d.max())
    ax[r,c].set_title(file);
    if not c and not r:
        ax[r,c].set_xlabel("time")
        ax[r,c].set_ylabel("frequency");
        ax[r,c].set_xticks([])
        ax[r,c].set_frame_on(False)
        ax[r,c].set_yticks([])
    else: ax[r,c].axis("off")
    
    norm_data = (data -data.mean())/data.std()
    ax[r+1,c].plot(norm_data,lw=0.03)
    ax[r+1,c].axis("off") 

plt.subplots_adjust(wspace=0.05, hspace=0.1)
plt.savefig('plotmany.png')
os.system('open plotmany.png')
