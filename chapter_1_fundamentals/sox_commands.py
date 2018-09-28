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
##               SOX_COMMANDS.PY              ##    
================================================ 

Useful sox commands.
'''

import os
# take in one.wav and two.wav to make three.wav 
os.system('sox one.wav two.wav three.wav')
# take first second of one.wav and output to output.wav  
os.system('sox one.wav output.wav trim 0 1')
# make volume 2x in one.wav and output to volup.wav 
os.system('sox -v 2.0 one.wav volup.wav')
# make volume ½ in one.wav and output to voldown.wav 
os.system('sox -v -0.5 one.wav volup.wav')
# reverse one.wav and output to reverse.wav 
os.system('sox one.wav reverse.wav reverse')
# change sample rate of one.wav to 16000 Hz
os.system('sox one.wav -r 16000 sr.wav')
# change audio file to 16 bit quality
os.system('sox -b 16 one.wav 16bit.wav')
# convert mono file to stereo by cloning channels
os.system('sox one.wav -c 2 stereo.wav')
# make stereo file mono by averaging out the channels
os.system('sox stereo.wav -c 1 mono.wav')
# double speed of file 
os.system('sox one.wav 2x.wav speed 2.0')
