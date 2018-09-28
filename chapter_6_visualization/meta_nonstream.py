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
##               META_NONSTREAM.PY            ##    
================================================ 

Stream in an audio file from the microphone and output
meta features - like gender and age detection.

More on matplotlib bar charts here:
https://pythonspot.com/matplotlib-bar-chart/
'''
#########################################################
##                   IMPORT STATEMENTS                 ##
#########################################################

import sounddevice as sd
import soundfile as sf
import random, time, librosa, os 
import numpy as np
import matplotlib.pyplot as plt
from drawnow import drawnow
import shutil, os, json
import librosa 

#########################################################
##.                  HELPER FUNCTIONS.                 ##
#########################################################

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
	features=g['features']['meta features']
	# remove file 
	os.remove(filename[0:-4]+'.json')
	
	# go back to current directory 
	os.chdir(curdir)

	return features

#########################################################
##.                  MAIN SCRIPT                       ##
#########################################################

# plot out meta features on the screen in streaming way
curdir=os.getcwd()
datadir=os.getcwd()+'/data/'
os.chdir(datadir)
metadir=curdir.replace('/chapter_6_visualization','/chapter_3_featurization')
# wavfile
print("what file in the ./data directory would you like to meta featurize?")
file=input("? \n")
folder=file[0:-4]

# every 20 seconds 
data, samplerate = sf.read(os.getcwd()+'/'+file)
duration=int(len(data)/samplerate)
intervals=int(duration/20)

try:
	os.mkdir(folder)
	os.chdir(folder)
except:
	shutil.rmtree(folder)
	os.mkdir(folder)
	os.chdir(folder)

# now break up 
for i in range(intervals):
	sf.write(str(i)+'.wav', data[i*20*samplerate:(i+1)*20*samplerate], samplerate)

wavfiles=list()
listdir=os.listdir()
for i in range(len(listdir)):
	if listdir[i][-4:] == '.wav':
		wavfiles.append(listdir[i])

wavfiles=sorted(wavfiles,key=lambda x: int(os.path.splitext(x)[0]))
print(wavfiles)
features=np.zeros(71)

for i in range(len(wavfiles)):    
    # read in file 
    features2=meta_featurize(wavfiles[i], datadir, metadir)
    features=features+features2

objects = ('addiction', 'adhd', 'africanamerican', 'als', 'alternative (music)', 
			'amharic', 'angry', 'anxiety', 'autism', 'awake', 'bipolar', 
			'cantonese', 'christian', 'cold', 'country', 'depression', 'disgust', 
			'dutch', 'dyslexia', 'edm', 'english', 'awake', 'fear', 
			'fifties', 'folk', 'fourties', 'french',
			'males', 'german', 'glioblastoma', 'graves disease', 'happy', 'holiday (music)', 
			'indie', 'italian', 'japanese', 'jazz', 'korean', 
			'latin', 'macedonian', 'mandarin', 'multiple sclerosis', 'natural (speech)',
			'neutral', 'newage', 'controls', 'polish', 'popcontrolbalanced', 
			'portuguese_controls', 'parkinsons', 'badquality', 'rap', 'reggae', 'rock', 
			'romanian', 'russian', 'sad', 'schizophrenia', 'seventies', 'sixties', 
			'sleep apnea', 'soundtrack', 'spanish', 'stressed', 'surprise', 
			'swedish', 'teens', 'thirties', 'turkish', 'twenties', 'vietnamese')

y_pos = np.arange(len(objects))
values=list(features)

fig, ax = plt.subplots()

ax.barh(y_pos, features, align='center',color='blue')
ax.set_yticks(y_pos)
ax.set_yticklabels(objects)
ax.invert_yaxis()  # labels read top-to-bottom

ax.set_xlabel('Frequency counts')
ax.set_ylabel('Model type')
ax.set_title('Meta feature frequencies')
plt.savefig('nonstream_bar.png')
plt.show()

plt.savefig('meta_nonstream.png')
os.system('open meta_nonstream.png')
#shutil.rmtree(datadir+'/'+folder)
