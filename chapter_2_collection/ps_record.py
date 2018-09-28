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
##               PS_RECORD.PY                 ##    
================================================ 

Quick example illustrating passive-synchronous mode (PS mode).

Record a 2 second audio sample in background every 10 seconds. 

Do this for 10 iterations. 

It's a blocking example, meaning no other code can run when 
the code is recording a sample.
'''
import sounddevice as sd
import soundfile as sf 
import time, os, shutil 

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

# make a folder to put recordings in 
try:
    os.mkdir('recordings')
    os.chdir(os.getcwd()+'/recordings')
except:
    shutil.rmtree('recordings')
    os.mkdir('recordings')
    os.chdir(os.getcwd()+'/recordings')
    
i=0

# loop through 10 times recording a 2 second sample 
# can change to infinite loop ==> while i > -1: 
while i<10:
    # record a mono file synchronously
    filename=str(i+1)+'.wav'
    print('recording %s'%(filename))
    sync_record(filename, 2, 16000, 1)
    time.sleep(10)
    i=i+1

    
    
