'''
audio_cluster.py

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
