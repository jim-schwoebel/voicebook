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
##               GENERATE_REMIX.PY            ##    
================================================ 

Given a list of .wav files (20 seconds), remix them to 4 seconds of each
(20/5=4) and normalize the remixed file.

Useful for putting together audio playbacks to summarize audio recordings.
'''

from pydub import AudioSegment
import os, getpass, random

folder=input('what folder (in ./data directory) would you like to remix? \n')
os.chdir(os.getcwd()+'/data/'+folder)

listdir=os.listdir()
random.shuffle(listdir)
t=0
for i in range(len(listdir)):
    if listdir[i][-4:]=='.wav':
        if t==0:
            soundt=AudioSegment.from_wav(os.getcwd()+'/'+listdir[i])
            sound=soundt[0:(len(soundt))]
            t=t+1
        else:
            soundt=AudioSegment.from_wav(os.getcwd()+'/'+listdir[i])
            sound=sound+soundt[0:(len(soundt))]
        
sound.export('remix.wav', format="wav")
os.system('ffmpeg-normalize remix.wav -o remix-normalized.wav')
