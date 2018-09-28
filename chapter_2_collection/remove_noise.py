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
##               REMOVE_NOISE.PY              ##    
================================================ 

Given an audio file, remove the noise from the first 100 milliseconds of audio.

This is good at removing things such as air conditioning noise from
the raw audio.
'''
import soundfile as sf
import os

def remove_noise(filename):
    #now use sox to denoise using the noise profile
    data, samplerate =sf.read(filename)
    duration=data/samplerate
    first_data=samplerate/10
    filter_data=list()
    for i in range(int(first_data)):
        filter_data.append(data[i])
    noisefile='noiseprof.wav'
    sf.write(noisefile, filter_data, samplerate)
    os.system('sox %s -n noiseprof noise.prof'%(noisefile))
    filename2='tempfile.wav'
    filename3='tempfile2.wav'
    noisereduction="sox %s %s noisered noise.prof 0.21 "%(filename,filename2)
    command=noisereduction
    #run command 
    os.system(command)
    print(command)
    #reduce silence again
    #os.system(silenceremove)
    #print(silenceremove)
    #rename and remove files 
    os.remove(filename)
    os.rename(filename2,filename)
    #os.remove(filename2)
    os.remove(noisefile)
    os.remove('noise.prof')

    return filename

remove_noise('test.wav')
