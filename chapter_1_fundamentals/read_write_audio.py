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
has >10 world experts in kafka distributed architectures, microservices 
built on top of Node.JS / Python / Docker, and applying machine learning to 
model speech and text data. 

We have helped a wide variety of enterprises - small businesses, 
researchers, enterprises, and/or independent developers. 

If you would like to work with us let us know @ js@neurolex.co. 

================================================ 
##             READ_WRITE_AUDIO.PY            ##    
================================================ 

Read_write_audio.py

Read and write audio files with various libraries in Python.
'''

from pydub import AudioSegment
data = AudioSegment.from_wav("test.wav")
data.export("new_test.wav")

import wave
data=wave.open('test.wav', mode='rb')
params=data.getparams()
# _wave_params(nchannels=1, sampwidth=2, framerate=16000, nframes=47104, comptype='NONE', compname='not compressed')

import librosa
y, sr = librosa.load('test.wav')
librosa.output.write_wav('new_test.wav', y, sr)

from scipy.io import wavfile
fs, data = wavfile.read('test.wav')
wavfile.write('new_test.wav',fs, data)

import soundfile as sf
data, fs = sf.read('test.wav')
sf.write('new_test.ogg', data, fs)
