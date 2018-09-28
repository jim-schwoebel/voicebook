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
##               AUDIO_CLUSTER.PY             ##    
================================================ 

Plot audio files in terms of their pitches.

Abridged from tutorial:
https://blog.galvanize.com/data-science-projects-classifying-and-visualizing-musical-pitch/
'''
########################################################################
## 							IMPORT STATEMENTS  						  ##
########################################################################
import os, librosa 
import scipy.io.wavfile as wav
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np 

########################################################################
##     MAIN CODE BASE    					       ##
########################################################################

os.chdir('data/samples')
listdir=os.listdir()
wavfiles=list()
for i in range(len(listdir)):
    if listdir[i][-4:]=='.wav':
        wavfiles.append(listdir[i])

wavfiles=sorted(wavfiles)
samples=list()
for i in range(len(wavfiles)):
    y, sr = librosa.core.load(wavfiles[i])
    rmse=np.mean(librosa.feature.rmse(y)[0])
    mfcc=np.mean(librosa.feature.mfcc(y)[0])
    samples.append(np.array([rmse, mfcc]))
        
kmeans = KMeans(3, max_iter = 1000, n_init = 100)
kmeans.fit_transform(samples)
predictions = kmeans.predict(samples)

x=list()
y=list()
for i in range(len(predictions)):
    x.append(i)
    y.append(predictions[i])


x0=list()
x1=list()
x2=list()

y0=list()
y1=list()
y2=list()

for i in range(len(y)):
    if y[i] == 0:
        x0.append(x[i])
        y0.append(y[i])
    elif y[i] == 1:
        x1.append(x[i])
        y1.append(y[i])
    elif y[i] == 2:
        x2.append(x[i])
        y2.append(y[i])

plt.scatter(x0, y0, marker='o', c='black')
plt.scatter(x1, y1, marker='o', c='blue')
plt.scatter(x2, y2, marker='o', c='red')
plt.xlabel('sample number')
plt.ylabel('k means class')
plt.savefig('kmeans.png')
