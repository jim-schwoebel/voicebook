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
##               LABEL_MEMUPPS.PY             ##    
================================================ 

Label a voice file with metadata:
1) Microphone
2) Environment
3) Mode
4) User (distance)
5) Processing
6) Storage 
'''
import os, taglib, json
import sounddevice as sd
import soundfile as sf 

def get_defaults():
    if 'label.json' in os.listdir():
        data=json.load('label.json')
    else:
        mic=input('what is the microphone?')
        env=input('what is the environment?')
        mode=input('what is the mode?')
        sampletype=input('sample type? (e.g. voice)')
        distance=input('what is the distance from mic?')
        process=input('do you use any processing (e.g. SoX noisefloor, .wav--> .opus --> .wav)? if so what?')
        storage=input('where are you storing files?')
        data={
            'microphone':mic,
            'environment':env,
            'mode':mode,
            'sample type': sampletype,
            'distance':distance,
            'processing':process,
            'storage':storage,
        }
            
        jsonfile=open('label.json','w')
        json.dump(data,jsonfile)
        jsonfile.close()
    return data 

def label_sample(file):
    data=get_defaults()    
    audio=taglib.File(os.getcwd()+'/'+file)
    print(audio)
    audio.tags['microphone']=data['microphone']
    audio.tags['environment']=data['environment']
    audio.tags['mode']=data['mode']
    audio.tags['sample type']=data['sample type']
    audio.tags['distance']=data['distance']
    audio.tags['processing']=data['processing']
    audio.tags['storage']=data['storage']
    audio.save()

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')
    label_sample(filename)

file='test.wav'
sync_record(file,10,18000,1)
