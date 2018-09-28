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
##                  TEXT_STREAM.PY            ##    
================================================ 

Transcribe an audio file every 1 second and then propagate it on the screen.

Do this in an asynchronous manner, as transcription can take some time.
'''
####################################################
##              IMPORT STATEMENTS                 ## 
####################################################
import os, json, shutil
import speech_recognition as sr_audio
import sounddevice as sd
import soundfile as sf 

####################################################
#           HELPER FUNCTIONS                      ##
####################################################
def transcribe_pocket(filename):
    # transcribe the audio (note this is only done if a voice sample)
    r=sr_audio.Recognizer()
    with sr_audio.AudioFile(filename) as source:
        audio = r.record(source) 
    text=r.recognize_sphinx(audio)
    
    return text

def sync_record(filename, duration, fs, channels):
    #print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    #print('done recording')

####################################################
##              MAIN SCRIPT                       ## 
####################################################

# set recording params 
duration=1
fs=44100
channels=1

try:
    os.mkdir('recordings')
    os.chdir(os.getcwd()+'/recordings')
except:
    shutil.rmtree('recordings')
    os.mkdir('recordings')
    os.chdir(os.getcwd()+'/recordings')

filenames=list()
transcripts=list()
for i in range(30):
    filename='%s.wav'%(str(i))
    sync_record(filename, duration, fs, channels)
    transcript=transcribe_pocket(filename)
    # print transcript on screen 
    print(transcript)
    filenames.append(filename)
    transcripts.append(transcript)

data={
    'filenames':filenames,
    'transcripts':transcripts
    }

jsonfile=open('recordings.json','w')
json.dump(data,jsonfile)
jsonfile.close()
    
