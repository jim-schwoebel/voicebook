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
##            GENERATE_FILTERED.PY            ##    
================================================ 

Quickly manipulate the audio file to create machine-generated audio with
filters.

Librosa has some handy filters for this that makes it quite easy for mono
audio.
'''
import librosa, os 
import soundfile as sf
import numpy as np 

os.chdir(os.getcwd()+'/data/')
curdir=os.getcwd()
wavfile=input('what is the name of the wav file (in ./data/ dir) you would like to manipulate?\n')

# load noise file and make 10 seconds 
y1, sr1 = librosa.load('beep.wav')
y1=np.append(y1,y1)
y1=np.append(y1,y1)
y1=np.append(y1,y1)
y1=np.append(y1,y1)
y1=np.append(y1,y1)

# load file 
y, sr = librosa.load(wavfile)
  
# time stretch (1/4 speed)
y_slow = librosa.effects.time_stretch(y, 0.50)

# pitch down very deep
y_low = librosa.effects.pitch_shift(y, sr, n_steps=-6)

# add noise to first 10 seconds
for i in range(len(y1)):
    y[i]=y[i]+y1[i]

y_noise=y

librosa.output.write_wav(curdir+'/'+wavfile[0:-4]+'_slow.wav',y_slow, sr)
librosa.output.write_wav(curdir+'/'+wavfile[0:-4]+'_lowpitch.wav',y_low, sr)
librosa.output.write_wav(curdir+'/'+wavfile[0:-4]+'_noise.wav',y_noise, sr)
