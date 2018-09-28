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
##             CHANGE_CHANNELS.PY             ##    
================================================ 
change_channels.py

Functions for some audio manipulation 
'''
import os

def stereo2mono(filename):
    #Change stereo to mono 
    new_filename=filename[0:-4]+'_mono.wav'
    os.system('sox %s %s remix 1-2'%(filename,new_filename))
    return new_filename

def separate_channels(filename):
    #Change stereo to two mono files (mix-down)
    channel_1=filename[0:-4]+'_1.wav'
    channel_2=filename[0:-4]+'_2.wav'
    os.system('sox %s %s remix 1'%(filename, channel_1))
    os.system('sox %s %s remix 2'%(filename, channel_2))
    return channel_1, channel_2
    
def multiplex(channel_1, channel_2):
    #Convert two mono files into one stereo file (multiplexing)
    output=channel_1[0:-4]+'_'+channel_2[0:-4]+'.wav'
    os.system('sox -M %s %s %s'%(channel_1,channel_2,output))
    return output

stereo2mono('stereo.wav')
separate_channels('stereo.wav')
multiplex('stereo_1.wav','stereo_2.wav')
