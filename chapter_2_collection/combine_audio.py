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
##               COMBINE_AUDIO.PY             ##    
================================================ 

Combine audio in series or in parallel using SoX CLI.
'''
import os

def combine_series(one, two):
	three=one[0:-4]+'_'+two[0:-4]+'_series.wav'
	command='sox --combine concatenate %s %s %s'%(one, two, three)
	print(command)
	os.system(command)
	return three

def combine_channels(left, right):
	mixed=left[0:-4]+'_'+right[0:-4]+'_mixed.wav'
	command='sox --combine merge %s %s %s'%(left,right,mixed)
	print(command)
	os.system(command)
	return mixed

# combine two wav files in series => (1_2_series.wav)
combine_series('1.wav', '2.wav')

# combine two wav files together in same channel (1_2_mixed.wav)
combine_channels('1.wav', '2.wav')
