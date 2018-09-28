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
##                  META_MULTI.PY             ##    
================================================ 

Stream in an audio file from the microphone and output
meta features - like gender and age detection.

'''
#########################################################
##.                  IMPORT STATEMENTS                 ##
#########################################################

import sounddevice as sd
import soundfile as sf
import random, time, librosa, os 
import numpy as np
import matplotlib.pyplot as plt
from drawnow import drawnow
import shutil, os, json

#########################################################
##.                  HELPER FUNCTIONS.                 ##
#########################################################

def make_fig():
    plt.subplot(2, 1, 1)
    plt.scatter(x, y)
    plt.xlabel('time (s)')
    plt.ylabel('male (1) vs. female (0)')
    plt.subplot(2, 1, 2)
    plt.scatter(x2, y2)
    plt.xlabel('time (s)')
    plt.ylabel('twenties (1) vs. control (0)')
    plt.tight_layout()

def record_data(filename, duration, fs, channels):
    # synchronous recording 
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done')
    
    return filename 

def meta_featurize(filename, datadir, metadir):

	# from a wav file in the current directory featurize it with meta features
	# derived from machine learning models 
	# can be used in a streaming or non-streaming way 
	# note: models were trained on 20 second periods so this is probably the best windows for files 

	curdir=os.getcwd()
	os.chdir(metadir)
	if 'load_dir' not in os.listdir():
		# make load directory folder 
		os.system('python3 meta_features.py')
            
	shutil.move(curdir+'/'+filename, metadir+'/load_dir/'+filename)
	# now featurize the file 
	os.system('python3 meta_features.py')
	# now load the .json result
	os.chdir('load_dir')
	g=json.load(open(filename[0:-4]+'.json'))
	# get classes
	classes=g['class']
	# remove file 
	os.remove(filename[0:-4]+'.json')
	os.remove(filename)
	# go back to current directory 
	os.chdir(curdir)

	return classes

#########################################################
##.                  MAIN SCRIPT                       ##
#########################################################

# plot out meta features on the screen in streaming way
curdir=os.getcwd()
datadir=os.getcwd()+'/data/'
metadir=curdir.replace('/chapter_6_visualization','/chapter_3_featurization')

# wavfile
#file=input('what file in the ./data directory would you like to meta featurize? \n')
x=list()
y=list()
x2=list()
y2=list()

for i in range(30):    
    # record 20ms of data 
    filename=record_data('sample.wav', 1, 44100, 1)
    classes=meta_featurize(filename, datadir, metadir)
    sample=classes[27]

    # make a simple method for finding whether or not class is control
    if sample.find('male') > 0:
    	sample=1
    else:
        sample=0

    x.append(i)
    y.append(sample)

    sample2=classes[69]
    if sample2.find('control') > 0:
    	sample2=0
    else:
    	sample2=1

    x2.append(i)
    y2.append(sample2)

    drawnow(make_fig)

plt.savefig('meta_multi.png')
os.system('open meta_multi.png')
