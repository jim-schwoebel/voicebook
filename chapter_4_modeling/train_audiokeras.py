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
##             TRAIN_AUDIOKERAS.PY            ##    
================================================ 

This script takes in two folders filled with .wav files, folder A and folder B, 
and classifies them with nlx-audioclassify features.

It upgrades nlx-audiomodel from simple classification techniques 
to deep learning approaches.
'''
import speech_recognition as sr
from pydub import AudioSegment
import librosa, getpass, random, os, json, nltk 
import numpy as np
from nltk import word_tokenize 
from nltk.classify import apply_features, SklearnClassifier, maxent
import keras.models
from keras import layers 
from keras.optimizers import SGD
from keras.models import Sequential,model_from_json
from keras.layers import Dense, Dropout
from textblob import TextBlob
from operator import itemgetter
import getpass
import numpy as np
import pickle
import datetime 
import time 

#####################################################################
#                      HELPER FUNCTIONS                            ##                     
#####################################################################
def featurize(wavfile):
    #initialize features 
    hop_length = 512
    n_fft=2048
    #load file 
    y, sr = librosa.load(wavfile)
    #extract mfcc coefficients 
    mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=13)
    mfcc_delta = librosa.feature.delta(mfcc) 
    #extract mean, standard deviation, min, and max value in mfcc frame, do this across all mfccs
    mfcc_features=np.array([np.mean(mfcc[0]),np.std(mfcc[0]),np.amin(mfcc[0]),np.amax(mfcc[0]),
                            np.mean(mfcc[1]),np.std(mfcc[1]),np.amin(mfcc[1]),np.amax(mfcc[1]),
                            np.mean(mfcc[2]),np.std(mfcc[2]),np.amin(mfcc[2]),np.amax(mfcc[2]),
                            np.mean(mfcc[3]),np.std(mfcc[3]),np.amin(mfcc[3]),np.amax(mfcc[3]),
                            np.mean(mfcc[4]),np.std(mfcc[4]),np.amin(mfcc[4]),np.amax(mfcc[4]),
                            np.mean(mfcc[5]),np.std(mfcc[5]),np.amin(mfcc[5]),np.amax(mfcc[5]),
                            np.mean(mfcc[6]),np.std(mfcc[6]),np.amin(mfcc[6]),np.amax(mfcc[6]),
                            np.mean(mfcc[7]),np.std(mfcc[7]),np.amin(mfcc[7]),np.amax(mfcc[7]),
                            np.mean(mfcc[8]),np.std(mfcc[8]),np.amin(mfcc[8]),np.amax(mfcc[8]),
                            np.mean(mfcc[9]),np.std(mfcc[9]),np.amin(mfcc[9]),np.amax(mfcc[9]),
                            np.mean(mfcc[10]),np.std(mfcc[10]),np.amin(mfcc[10]),np.amax(mfcc[10]),
                            np.mean(mfcc[11]),np.std(mfcc[11]),np.amin(mfcc[11]),np.amax(mfcc[11]),
                            np.mean(mfcc[12]),np.std(mfcc[12]),np.amin(mfcc[12]),np.amax(mfcc[12]),
                            np.mean(mfcc_delta[0]),np.std(mfcc_delta[0]),np.amin(mfcc_delta[0]),np.amax(mfcc_delta[0]),
                            np.mean(mfcc_delta[1]),np.std(mfcc_delta[1]),np.amin(mfcc_delta[1]),np.amax(mfcc_delta[1]),
                            np.mean(mfcc_delta[2]),np.std(mfcc_delta[2]),np.amin(mfcc_delta[2]),np.amax(mfcc_delta[2]),
                            np.mean(mfcc_delta[3]),np.std(mfcc_delta[3]),np.amin(mfcc_delta[3]),np.amax(mfcc_delta[3]),
                            np.mean(mfcc_delta[4]),np.std(mfcc_delta[4]),np.amin(mfcc_delta[4]),np.amax(mfcc_delta[4]),
                            np.mean(mfcc_delta[5]),np.std(mfcc_delta[5]),np.amin(mfcc_delta[5]),np.amax(mfcc_delta[5]),
                            np.mean(mfcc_delta[6]),np.std(mfcc_delta[6]),np.amin(mfcc_delta[6]),np.amax(mfcc_delta[6]),
                            np.mean(mfcc_delta[7]),np.std(mfcc_delta[7]),np.amin(mfcc_delta[7]),np.amax(mfcc_delta[7]),
                            np.mean(mfcc_delta[8]),np.std(mfcc_delta[8]),np.amin(mfcc_delta[8]),np.amax(mfcc_delta[8]),
                            np.mean(mfcc_delta[9]),np.std(mfcc_delta[9]),np.amin(mfcc_delta[9]),np.amax(mfcc_delta[9]),
                            np.mean(mfcc_delta[10]),np.std(mfcc_delta[10]),np.amin(mfcc_delta[10]),np.amax(mfcc_delta[10]),
                            np.mean(mfcc_delta[11]),np.std(mfcc_delta[11]),np.amin(mfcc_delta[11]),np.amax(mfcc_delta[11]),
                            np.mean(mfcc_delta[12]),np.std(mfcc_delta[12]),np.amin(mfcc_delta[12]),np.amax(mfcc_delta[12])])
    
    return mfcc_features

def exportfile(newAudio,time1,time2,filename,i):
    #Exports to a wav file in the current path.
    newAudio2 = newAudio[time1:time2]
    g=os.listdir()
    if filename[0:-4]+'_'+str(i)+'.wav' in g:
        filename2=str(i)+'_segment'+'.wav'
        print('making %s'%(filename2))
        newAudio2.export(filename2,format="wav")
    else:
        filename2=str(i)+'.wav'
        print('making %s'%(filename2))
        newAudio2.export(filename2, format="wav")

    return filename2 

def audio_time_features(filename):
    #recommend >0.50 seconds for timesplit 
    timesplit=0.50
    hop_length = 512
    n_fft=2048
    
    y, sr = librosa.load(filename)
    duration=float(librosa.core.get_duration(y))
    
    #Now splice an audio signal into individual elements of 100 ms and extract
    #all these features per 100 ms
    segnum=round(duration/timesplit)
    deltat=duration/segnum
    timesegment=list()
    time=0

    for i in range(segnum):
        #milliseconds
        timesegment.append(time)
        time=time+deltat*1000

    newAudio = AudioSegment.from_wav(filename)
    filelist=list()
    
    for i in range(len(timesegment)-1):
        filename=exportfile(newAudio,timesegment[i],timesegment[i+1],filename,i)
        filelist.append(filename)

        featureslist=np.array([0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0,
                               0,0,0,0])
    
    #save 100 ms segments in current folder (delete them after)
    for j in range(len(filelist)):
        try:
            features=featurize(filelist[i])
            featureslist=featureslist+features 
            os.remove(filelist[j])
        except:
            print('error splicing')
            featureslist.append('silence')
            os.remove(filelist[j])

    #now scale the featureslist array by the length to get mean in each category
    featureslist=featureslist/segnum
    
    return featureslist

#####################################################################
##                 INITIALIZE VARIABLES                            ## 
#####################################################################
start=time.time()
name1=input('folder name 1 \n')
name2=input('folder name 2 \n')
modelname=name1+'_'+name2+'_dl_audio'

jsonfilename=name1+'_'+name2+'.json'
dir3=os.getcwd()+'/data'
model_dir=os.getcwd()+'/models'

#####################################################################
##                  INITIALIZE FUNCTIONS                           ## 
#####################################################################
#FEATURIZE .WAV FILES WITH AUDIO FEATURES --> MAKE JSON (if needed)
#############################################################

try:
    os.chdir(dir3)
except:
    os.mkdir(dir3)
    os.chdir(dir3)

if jsonfilename not in os.listdir():

    try:
        os.chdir(dir3)
        g=json.load(jsonfile)
        
    except:
       #define some helper functions to featurize audio into proper form
        print('cannot load previous file')
        print('feauturizing')
        

        #104 features obtained by 
        #np.append(featurize(filename),audio_time_series(filename),textfeatures(filename))

        #load a folder, transcribe the data, make all the data into .txt files
        #load all the files into .json database (one,two)
        dir1='/Users/'+getpass.getuser()+'/nlx-model/nlx-audiomodelkeras/'+name1

        g='error'
        while g == 'error':
            try:
                g='noterror'
                os.chdir(dir1)
            except:
                g='error'
                print('directory not recognized')
                dir1=input('input first directory path')

        dir2='/Users/'+getpass.getuser()+'/nlx-model/nlx-audiomodelkeras/'+name2

        g='error'
        while g == 'error':
            try:
                g='noterror'
                os.chdir(dir2)
            except:
                g='error'
                print('directory not recognized')
                dir2=input('input second directory path')

        #now go through each directory and featurize the samples and save them as .json files
        os.chdir(dir1)
            
        dirlist1=os.listdir()

        #if broken session, load all previous transcripts
        #this reduces costs if tied to GCP
        one=list()
        for i in range(len(dirlist1)):
            try:
                if dirlist1[i][-5:]=='.json':
                    #this assumes all .json in the folder are transcript (safe assumption if only .wav files)
                    jsonfile=dirlist1[i]
                    features=json.load(open(jsonfile))['features']
                    one.append(features)
            except:
                pass 
                
        for i in range(len(dirlist1)):
            if dirlist1[i][-4:]=='.wav' and dirlist1[i][0:-4]+'.json'not in dirlist1 and os.path.getsize(dirlist1[i])>500:
                #loop through files and get features
                #try:
                wavfile=dirlist1[i]
                print('%s - featurizing %s'%(name1.upper(),wavfile))
                #ontain features 
                #try:
                features=np.append(featurize(wavfile),audio_time_features(wavfile))
                print(features)
                #append to list 
                one.append(features.tolist())
                #save intermediate .json just in case
                data={
                    'features':features.tolist(),
                    }
                jsonfile=open(dirlist1[i][0:-4]+'.json','w')
                json.dump(data,jsonfile)
                jsonfile.close()
##                except:
##                    pass
            else:
                pass 

        #repeat same process in other directory
        os.chdir(dir2)
            
        dirlist2=os.listdir()

        two=list()
        
        for i in range(len(dirlist2)):
            try:
                if dirlist2[i][-5:]=='.json':
                    #this assumes all .json in the folder are transcript (safe assumption if only .wav files)
                    jsonfile=dirlist2[i]
                    features=json.load(open(jsonfile))['features']
                    two.append(features)                
            except:
                pass
                
        for i in range(len(dirlist2)):
            if dirlist2[i][-4:]=='.wav' and dirlist2[i][0:-4]+'.json' not in dirlist2 and os.path.getsize(dirlist2[i])>500:
                #loop through files and get features 
                try:
                    wavfile=dirlist2[i]
                    print('%s - featurizing %s'%(name2.upper(),wavfile))
                    #obtain features 
                    features=np.append(featurize(wavfile),audio_time_features(wavfile))
                    print(features)
                    #append to list 
                    two.append(features.tolist())
                    #save intermediate .json just in case
                    data={
                        'features':features.tolist(),
                        }
                    jsonfile=open(dirlist2[i][0:-4]+'.json','w')
                    json.dump(data,jsonfile)
                    jsonfile.close()
                except:
                    pass
            else:
                pass

        #randomly shuffle one and two
        random.shuffle(one)
        random.shuffle(two)
        
        #make sure they are the same length (For later) - this avoid errors
        while len(one)>len(two):
            print('%s is %s more than %s, balancing...'%(name1.upper(),str(len(one)-len(two)),name2.upper()))
            one.pop()
        while len(two)>len(one):
            print('%s is %s more than %s, balancing...'%(name2.upper(),str(len(two)-len(one)),name1.upper()))
            two.pop()
            
        #now write to json
        data={
            name1:one,
            name2:two,
            }

        os.chdir(dir3)
        jsonfile=open(name1+'_'+name2+'.json','w')
        json.dump(data,jsonfile)
        jsonfile.close()


#LOAD AND BALANCE DATASETS
#####################################################################
#get output vector of 1 (similarity)
#load this using some form of .json
#note this assumes a binary classification problem A/B
try:
    g=json.load(open(name1+'_'+name2+'.json'))
except:
    print('error loading .json')
 
s1_temp =g[name1]
s2_temp= g[name2]

s1list=list()
s2list=list()

#make into well-formatted numpy arrays 
for i in range(len(s1_temp)):
    s1list.append(np.array(g[name1][i]))
                  
for i in range(len(s2_temp)):
    s2list.append(np.array(g[name2][i]))

s1=s1list
s2=s2list

#TEST AND TRAIN SET GENERATION 
#################################################################
#Now generate train and test sets (1/2 left out for testing)
#randomize message labels
labels=list()

for i in range(len(s1)):
    labels.append([s1[i],0])
    
for i in range(len(s2)):
    labels.append([s2[i],1])

random.shuffle(labels)
half=int(len(labels)/2)

#make sure we featurize all these train_set2s 
train_set2=list()
labels_train_set2=list()
test_set2=list()
labels_test_set2=list()

for i in range(half):
    embedding=labels[half][0]
    train_set2.append(embedding)
    labels_train_set2.append(labels[half][1])

for i in range(half):
    #repeat same process for embeddings
    embedding=labels[half+i][0]
    test_set2.append(embedding)
    labels_test_set2.append(labels[half+i][1])

#MODEL OPTIMIZATION 
#################################################################
#make classifier/test classifier (these are all easy methods)

# DATA PRE-PROCESSING 
############################################################################
x_train = np.array(train_set2)
y_train = np.array(labels_train_set2)
x_test = np.array(test_set2)
y_test = np.array(labels_test_set2)

# MAKE MODEL
############################################################################
model = Sequential()
model.add(Dense(64, input_dim=len(x_train[0]), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(16, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=100,
          batch_size=30)

# EVALUATE MODEL / PREDICT OUTPUT 
score = model.evaluate(x_test, y_test, batch_size=128)

print("\n final %s: %.2f%% \n" % (model.metrics_names[1], score[1]*100))
print(model.predict(x_train[0][np.newaxis,:]))

# now retrain model with all the data 
############################################################################
model = Sequential()
model.add(Dense(64, input_dim=len(x_train[0]), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(16, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train+x_test, y_train+y_test,
          epochs=20,
          batch_size=128)

#SAVE TO DISK
############################################################################
try:
    os.chdir(model_dir)
except:
    os.mkdir(model_dir)
    os.chdir(model_dir)

# serialize model to JSON
model_json = model.to_json()
with open(modelname+".json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights(modelname+".h5")
print("\n Saved %s.json model to disk"%(modelname))

# SUMMARIZE RESULTS
############################################################################
execution=time.time()-start
print('summarizing data...')
g=open(modelname+'.txt','w')
g.write('SUMMARY OF MODEL')
g.write('\n\n')
g.write('Keras-based implementation of a neural network, 208 audio input features (mfccs and their deltas), 1 output feature; binary classification, 2 layers (relu | sigmoid activation functions), loss=binary_crossentropy, optimizer=rmsprop')
g.write('\n\n')
g.write('MODEL FILE NAME: \n\n %s.json | %s.h5'%(modelname,modelname))
g.write('\n\n')
g.write('DATE CREATED: \n\n %s'%(datetime.datetime.now()))
g.write('\n\n')
g.write('EXECUTION TIME: \n\n %s\n\n'%(str(execution)))
g.write('GROUPS: \n\n')
g.write('Group 1: %s (%s training, %s testing)'%(name1,str(int(len(train_set2)/2)),str(int(len(test_set2)/2))))
g.write('\n')
g.write('Group 2: %s (%s training, %s testing)'%(name2,str(int(len(labels_train_set2)/2)),str(int(len(labels_test_set2)/2))))
g.write('\n\n')
g.write('FEATURES: \n\n Audio features - mfcc coefficients and deltas (208 features)')
g.write('\n\n')
g.write('MODEL ACCURACY: \n\n')
g.write('%s: %s \n\n'%(str('accuracy'),str(score[1]*100)))
g.write('(C) 2018, NeuroLex Laboratories')
g.close()


##APPLY CLASSIFIER TO PREDICT DATA
############################################################################
#This is an automated unit test to save and load the model to disk
#ensures you can call the model later 
print('testing loaded model\n')
# load json and create model
json_file = open(modelname+'.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights(modelname+".h5")
print("Loaded model from disk \n")
print(loaded_model.predict(x_train[0][np.newaxis,:]))

### evaluate loaded model on test data
##loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
##score = loaded_model.evaluate(X, Y, verbose=0)

#OUTPUT CLASS
#print(model.predict_classes(x_train[0][np.newaxis,:]))
