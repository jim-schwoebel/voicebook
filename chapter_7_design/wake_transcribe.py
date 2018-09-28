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
##            WAKE_TRANSCRIBE.PY              ##    
================================================ 

Use asynchronous transcription as a wakeword detector.
'''
import soundfile as sf
import sounddevice as sd
import speech_recognition as sr_audio
import pyttsx3 
import os, time

# transcribe with pocketsphinx (open-source)
def speak():
    engine = pyttsx3.init()
    engine.say("hello!!")
    engine.runAndWait() 

def find_wake(transcript, hotwords):
    for i in range(len(hotwords)):
##        print(transcript)
##        print(transcript.lower().find(hotwords[i]))
        if transcript.lower().find(hotwords[i])>=0:
            print('%s wakeword found!!'%(hotwords[i].upper()))
            speak()
            break 
        
def transcribe_sphinx(file):
    try:
        r=sr_audio.Recognizer()
        with sr_audio.AudioFile(file) as source:
            audio = r.record(source) 
        transcript=r.recognize_sphinx(audio)
        print('sphinx transcript: '+transcript)
    except:
        transcript=''
        print(transcript)
        
    return transcript 

def async_record(hotwords, filename, filename2, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    transcript=transcribe_sphinx(filename2)
    find_wake(transcript, hotwords)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

# initial parameters
hotwords=['test', 'testing']
i=0
t=1
filename2='n/a'
# create infinite loop
while t>0:
    # record a mono file asynchronous, transcribe, and fine wakeword 
    filename=str(i+1)+'.wav'
    async_record(hotwords, filename, filename2, 3, 16000, 1)
    filename2=filename 
    i=i+1
    try:
        os.remove(str(i-2)+'.wav')
    except:
        pass
