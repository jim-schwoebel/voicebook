'''
================================================ 
##            VOICEBOOK REPOSITORY            ##      
================================================ 

repository name: voicebook 
repository version: 1.0 
repository link: https://github.com/jim-schwoebel/voicebook 
author: Jim Schwoebel 
author contact: js@neurolex.co 
description: a book and repo to get you started programming voice applications in Python - 10 chapters and 200+ scripts. 
license category: opensource 
license: Apache 2.0 license 
organization name: NeuroLex Laboratories, Inc. 
location: Seattle, WA 
website: https://neurolex.ai 
release date: 2018-09-28 

This code (voicebook) is hereby released under a Apache 2.0 license license. 

For more information, check out the license terms below. 

================================================ 
##               LICENSE TERMS                ##      
================================================ 

Copyright 2018 NeuroLex Laboratories, Inc. 

Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 

     http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License. 

================================================ 
##               SERVICE STATEMENT            ##        
================================================ 

If you are using the code written for a larger project, we are 
happy to consult with you and help you with deployment. Our team 
has >10 world experts in Kafka distributed architectures, microservices 
built on top of Node.js / Python / Docker, and applying machine learning to 
model speech and text data. 

We have helped a wide variety of enterprises - small businesses, 
researchers, enterprises, and/or independent developers. 

If you would like to work with us let us know @ js@neurolex.co. 

================================================ 
##              AUDIO_PLOTMANY.PY             ##    
================================================ 

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
