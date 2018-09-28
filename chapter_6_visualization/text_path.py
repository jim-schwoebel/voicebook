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
##                 TEXT_PATH.PY               ##    
================================================ 

Give some simple visual feedback when recording an audio stream
in the form of a text stream.
'''
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr_audio
import random, time, librosa, os 
import numpy as np
import matplotlib.pyplot as plt
from drawnow import drawnow

def transcribe_pocket(filename):
    # transcribe the audio (note this is only done if a voice sample)
    r=sr_audio.Recognizer()
    try:
        with sr_audio.AudioFile(filename) as source:
            audio = r.record(source) 
        text=r.recognize_sphinx(audio)    
    except:
        text=''
        
    return text

def make_fig():
    plt.scatter(x, y)  


def record_data(filename, duration, fs, channels):
    # synchronous recording 
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)

# initialize plot 
plt.ion()  # enable interactivity
fig = plt.figure()  # make a figure

x = list()
y = list()

transcriptions=list()
for i in range(30):    
    # record 20ms of data 
    sample=record_data('sample.wav',1, 44100, 1)
    transcription=transcribe_pocket('sample.wav')
    x.append(i)
    y.append(len(transcription.split()))
    transcriptions.append(transcription)
    drawnow(make_fig)
    # put words on top of the graph
    os.remove('sample.wav')

# label all the points with spoken words
for i, transcript in enumerate(transcriptions):
    plt.annotate(transcript, (x[i],y[i]))

plt.xlabel('time (seconds)')
plt.ylabel('number of words')
plt.savefig('wordstream.png')
os.system('open wordstream.png')
