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
##           LOAD_AUDIOTEXTCLASSIFY.PY        ##    
================================================ 

Fingerprint mkxed models in a streaming folder. 
'''

import speech_recognition as sr  
import librosa
from pydub import AudioSegment
import os, nltk, random, json 
from nltk import word_tokenize 
from nltk.classify import apply_features, SklearnClassifier, maxent
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
from sklearn import svm
from sklearn import metrics
from textblob import TextBlob
from operator import itemgetter
import getpass
import numpy as np
import pickle
import datetime 
import time

cur_dir=os.getcwd()+'/load_dir'
model_dir=os.getcwd()+'/models'
load_dir=os.getcwd()+'/load_dir'

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

def textfeatures(transcript):
    #alphabetical features 
    a=transcript.count('a')
    b=transcript.count('b')
    c=transcript.count('c')
    d=transcript.count('d')
    e=transcript.count('e')
    f=transcript.count('f')
    g_=transcript.count('g')
    h=transcript.count('h')
    i=transcript.count('i')
    j=transcript.count('j')
    k=transcript.count('k')
    l=transcript.count('l')
    m=transcript.count('m')
    n=transcript.count('n')
    o=transcript.count('o')
    p=transcript.count('p')
    q=transcript.count('q')
    r=transcript.count('r')
    s=transcript.count('s')
    t=transcript.count('t')
    u=transcript.count('u')
    v=transcript.count('v')
    w=transcript.count('w')
    x=transcript.count('x')
    y=transcript.count('y')
    z=transcript.count('z')
    space=transcript.count(' ')

    #numerical features and capital letters 
    num1=transcript.count('0')+transcript.count('1')+transcript.count('2')+transcript.count('3')+transcript.count('4')+transcript.count('5')+transcript.count('6')+transcript.count('7')+transcript.count('8')+transcript.count('9')
    num2=transcript.count('zero')+transcript.count('one')+transcript.count('two')+transcript.count('three')+transcript.count('four')+transcript.count('five')+transcript.count('six')+transcript.count('seven')+transcript.count('eight')+transcript.count('nine')+transcript.count('ten')
    number=num1+num2
    capletter=sum(1 for c in transcript if c.isupper())

    #part of speech 
    text=word_tokenize(transcript)
    g=nltk.pos_tag(transcript)
    cc=0
    cd=0
    dt=0
    ex=0
    in_=0
    jj=0
    jjr=0
    jjs=0
    ls=0
    md=0
    nn=0
    nnp=0
    nns=0
    pdt=0
    pos=0
    prp=0
    prp2=0
    rb=0
    rbr=0
    rbs=0
    rp=0
    to=0
    uh=0
    vb=0
    vbd=0
    vbg=0
    vbn=0
    vbp=0
    vbp=0
    vbz=0
    wdt=0
    wp=0
    wrb=0
    
    for i in range(len(g)):
        if g[i][1] == 'CC':
            cc=cc+1
        elif g[i][1] == 'CD':
            cd=cd+1
        elif g[i][1] == 'DT':
            dt=dt+1
        elif g[i][1] == 'EX':
            ex=ex+1
        elif g[i][1] == 'IN':
            in_=in_+1
        elif g[i][1] == 'JJ':
            jj=jj+1
        elif g[i][1] == 'JJR':
            jjr=jjr+1                   
        elif g[i][1] == 'JJS':
            jjs=jjs+1
        elif g[i][1] == 'LS':
            ls=ls+1
        elif g[i][1] == 'MD':
            md=md+1
        elif g[i][1] == 'NN':
            nn=nn+1
        elif g[i][1] == 'NNP':
            nnp=nnp+1
        elif g[i][1] == 'NNS':
            nns=nns+1
        elif g[i][1] == 'PDT':
            pdt=pdt+1
        elif g[i][1] == 'POS':
            pos=pos+1
        elif g[i][1] == 'PRP':
            prp=prp+1
        elif g[i][1] == 'PRP$':
            prp2=prp2+1
        elif g[i][1] == 'RB':
            rb=rb+1
        elif g[i][1] == 'RBR':
            rbr=rbr+1
        elif g[i][1] == 'RBS':
            rbs=rbs+1
        elif g[i][1] == 'RP':
            rp=rp+1
        elif g[i][1] == 'TO':
            to=to+1
        elif g[i][1] == 'UH':
            uh=uh+1
        elif g[i][1] == 'VB':
            vb=vb+1
        elif g[i][1] == 'VBD':
            vbd=vbd+1
        elif g[i][1] == 'VBG':
            vbg=vbg+1
        elif g[i][1] == 'VBN':
            vbn=vbn+1
        elif g[i][1] == 'VBP':
            vbp=vbp+1
        elif g[i][1] == 'VBZ':
            vbz=vbz+1
        elif g[i][1] == 'WDT':
            wdt=wdt+1
        elif g[i][1] == 'WP':
            wp=wp+1
        elif g[i][1] == 'WRB':
            wrb=wrb+1

    #sentiment
    tblob=TextBlob(transcript)
    polarity=float(tblob.sentiment[0])
    subjectivity=float(tblob.sentiment[1])

    #word repeats
    words=transcript.split()
    newlist=transcript.split()
    repeat=0
    for i in range(len(words)):
        newlist.remove(words[i])
        if words[i] in newlist:
            repeat=repeat+1 
    
    featureslist=np.array([a,b,c,d,
                           e,f,g_,h,
                           i,j,k,l,
                           m,n,o,p,
                           q,r,s,t,
                           u,v,w,x,
                           y,z,space,number,
                           capletter,cc,cd,dt,
                           ex,in_,jj,jjr,
                           jjs,ls,md,nn,
                           nnp,nns,pdt,pos,
                           prp,prp2,rbr,rbs,
                           rp,to,uh,vb,
                           vbd,vbg,vbn,vbp,
                           vbz,wdt,wp,
                           wrb,polarity,subjectivity,repeat])
    
    return featureslist 
                           
def transcribe(wavfile):
    r = sr.Recognizer()
    # use wavfile as the audio source (must be .wav file)
    with sr.AudioFile(wavfile) as source:
        #extract audio data from the file
        audio = r.record(source)                    

    transcript=r.recognize_sphinx(audio)
    print(transcript)
    return transcript

def convert(file):
    
    if file[-4:] != '.wav':
        filename=file[0:-4]+'.wav'
        os.system('ffmpeg -i %s -an %s'%(file,filename))
        os.remove(file)
    elif file[-4:] == '.wav':
        filename=file
    else:
        filename=file 
        os.remove(file)

    return filename

model_list=list()
os.chdir(model_dir)
listdir=os.listdir()

for i in range(len(listdir)):
    if listdir[i][-16:]=='audiotext.pickle' and listdir[i]:
        model_list.append(listdir[i])

count=0
errorcount=0

try:
    os.chdir(load_dir)
except:
    os.mkdir(load_dir)
    os.chdir(load_dir)
    
listdir=os.listdir()
print(os.getcwd())
for i in range(len(listdir)):
    try:
        if listdir[i][-5:] not in ['Store','.json']:
            if listdir[i][-4:] != '.wav':
                if listdir[i][-5:] != '.json':
                    filename=convert(listdir[i])
            else:
                filename=listdir[i]

            print(filename)

            if filename[0:-4]+'_audiotext.json' not in listdir:

                transcript=transcribe(filename)
                features=np.append(featurize(filename),audio_time_features(filename))
                features=np.append(features,textfeatures(transcript))
                
                features=features.reshape(1,-1)

                os.chdir(model_dir)

                class_list=list()
                model_acc=list()
                deviations=list()
                modeltypes=list()
                
                for j in range(len(model_list)):
                    modelname=model_list[j]
                    i1=modelname.find('_')
                    name1=modelname[0:i1]
                    i2=modelname[i1:]
                    i3=i2.find('_')
                    name2=i2[0:i3]

                    loadmodel=open(modelname, 'rb')
                    model = pickle.load(loadmodel)
                    loadmodel.close()
                    
                    output=str(model.predict(features)[0])
                    print(output)
                    classname=output
                    class_list.append(classname)

                    g=json.load(open(modelname[0:-7]+'.json'))
                    model_acc.append(g['accuracy'])
                    deviations.append(g['deviation'])
                    modeltypes.append(g['modeltype'])

                os.chdir(load_dir)

                jsonfilename=filename[0:-4]+'_audiotext.json'
                jsonfile=open(jsonfilename,'w')
                data={
                    'filename':filename,
                    'filetype':'mixed file',
                    'class':class_list,
                    'model':model_list,
                    'model accuracies':model_acc,
                    'model deviations':deviations,
                    'model types':modeltypes,
                    'transcript':transcript,
                    'features':features.tolist(),
                    'count':count,
                    'errorcount':errorcount,
                    }
                json.dump(data,jsonfile)
                jsonfile.close()
                
            count=count+1
    except:
        errorcount=errorcount+1
        count=count+1 

