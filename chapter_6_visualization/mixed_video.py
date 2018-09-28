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
##                MIXED_VIDEO.PY              ##    
================================================ 

Make a video from a folder of images.

The idea here is to print out the waveform (as .png file)
underneath the text file in series.

This helps show time-series data!
'''
import cv2, os, shutil, librosa 
import soundfile as sf
import speech_recognition as sr_audio
import matplotlib.pyplot as plt
import numpy as np


def transcribe_pocket(filename):
    # transcribe the audio (note this is only done if a voice sample)
    try:
        r=sr_audio.Recognizer()
        with sr_audio.AudioFile(filename) as source:
            audio = r.record(source) 
        text=r.recognize_sphinx(audio)
    except:
        text=''
    print(text)

    # get audio features
    y, sr = librosa.load(filename)
    rmse=np.mean(librosa.feature.rmse(y)[0])*1000

    # write transcript to file (for archive)
    g=open(filename[0:-4]+'.txt','w')
    g.write(text)
    g.close()

    # remove wavfile 
    os.remove(filename)

    return text, rmse 

def make_fig(filename, transcriptions, x, y):
    plt.scatter(x, y, color='blue')
    for i, transcript in enumerate(transcriptions):
        plt.annotate(transcript, (x[i],y[i]))

    # write labels and save fig 
    plt.xlabel('time (seconds)')
    plt.ylabel('root mean square power (average)')

    plt.savefig(filename)

# change to data directory 
os.chdir('data')
curdir=os.getcwd()
wavfile=input('what .wav file in the ./data directory would you like to make a mixed feature video? \n')

# make a folder, delete the folder if it is there 
folder=wavfile[0:-4]

try:
	os.mkdir(folder)
	os.chdir(folder)
except:
	shutil.rmtree(folder)
	os.mkdir(folder)
	os.chdir(folder)

# now copy the file into the folder 
shutil.copy(curdir+'/'+wavfile, curdir+'/'+folder+'/'+wavfile)

# now break up the file into 1 second segments 
data, samplerate = sf.read(wavfile)
os.remove(wavfile)
duration=int(len(data)/samplerate)

for i in range(duration):
    try:
        sf.write(str(i)+'.wav', data[samplerate*(i):samplerate*(i+1)], samplerate)
    except:
        pass 

# now get wavfiles and sort them 
files=os.listdir()
wavfiles=list()
for i in range(len(files)):
	if files[i][-4:]=='.wav':
		wavfiles.append(files[i])
wavfiles=sorted(wavfiles)

# now transcribe each of these wav files and remove them 
# save as .txt files 
transcriptions=list()
x=list()
y=list()

for i in range(len(wavfiles)):
	# now make image from these transcripts 
	text, rmse=transcribe_pocket(wavfiles[i])

	# update lists 
	x.append(i)
	y.append(rmse)
	transcriptions.append(text)

	# make audio plot and save as filename 
	make_fig(str(i)+'.png',transcriptions,x,y)

# now get all the .png files in directory and sort by number 
listdir=os.listdir()
pngs=list()
for i in range(len(listdir)):
	if listdir[i][-4:]=='.png':
		pngs.append(listdir[i])

pngs=sorted(pngs,key=lambda x: int(os.path.splitext(x)[0]))
print(pngs)

# now make video from pngs 
video_name = 'mixed_video.avi'

img=cv2.imread(pngs[0])
height, width, layers = img.shape
video = cv2.VideoWriter(video_name,-1,1,(width,height))

for i in range(len(pngs)):
	video.write(cv2.imread(pngs[i]))

cv2.destroyAllWindows()
video.release()
