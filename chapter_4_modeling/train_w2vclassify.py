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
##            TRAIN_W2VCLASSIFY.PY            ##    
================================================ 

This script takes in two lists of sentences, which are then broken down to their
respective words. Word2vec embedding models are then created for each of these
lists in numpy arrays.

Now, we have two word2vec models we can use for machine learning tasks. This is useful
for vocabulary-sensitive classificaion tasks.

For example,
--> we could apply model A on A and model B on A for a feature representation of A (200 features)
--> and a model A on B and model B on B for a feature representation of B (200 features)

#This would make it useful to train both typical classification models (SVM) as well as
#higher-order RNN/CNN models for deep learning.

#This embedding also suits itself to add other similar dimensional feature vectors for images and/or audio as well
#to increase model accuracy into the future. 

'''

import speech_recognition as sr
from gensim.models import Word2Vec
import numpy as np
import random, os, json, getpass
from sklearn.model_selection import train_test_split
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

#INITIALIZE FUNCTIONS
#####################################################################

#function to make a word2vec model from a series of sentences

def w2v(textlist,size,modelname):
    sentences=list()
    
    #split into individual word embeddings
    for i in range(len(textlist)):
        if len(textlist[i].split())==0:
            pass
        else:
            sentences.append(textlist[i].split())

    #test (for small samples)
    #print(sentences)
    model = Word2Vec(sentences, size=size, window=5, min_count=1, workers=4)
    
    if modelname in os.listdir():
        #do not save if already file in folder with same name 
        pass
    else:
        print('saving %s to disk...'%(modelname))
        model.save(modelname)
        
    return model

#function to get output embedding given a test set and a word2vec model 

def w2v_embedding(test_set,size,modelname):
    model=Word2Vec.load(modelname)

    sentences2=list()
    for i in range(len(test_set)):
        sentences2.append(test_set[i].split())

    w2v_embed=list()
    for i in range(len(sentences2)):
        for j in range(len(sentences2[i])):
            try:
                w2v_embed.append(model[sentences2[i][j]])
            except:
                #pass if there is an error to not distort averages
                pass
                #other option: w2v_embed.append(np.zeros(size))

    return w2v_embed

def sentence_embedding(sentence,size,modelname):
    model=Word2Vec.load(modelname)

    sentences2=sentence.split()

    w2v_embed=list()
    for i in range(len(sentences2)):
        try:
            #print(sentences2[i])
            w2v_embed.append(model[sentences2[i]])
            #print(model[sentences2[i]])
        except:
            #pass if there is an error to not distort averages... :)
            pass

    out_embed=np.zeros(size)
    for j in range(len(w2v_embed)):
        out_embed=out_embed+w2v_embed[j]

    out_embed=(1/size)*out_embed
##
##    try:
##        print(sentence)
##        print(out_embed)
##    except:
##        print('contains unknown character')
   
    return out_embed

def transcribe(wavfile):
    r = sr.Recognizer()
    # use wavfile as the audio source (must be .wav file)
    with sr.AudioFile(wavfile) as source:
        #extract audio data from the file
        audio = r.record(source)                    

    transcript=r.recognize_sphinx(audio)
    print(transcript)
    return transcript

def optimizemodel_sc(train_set2,labels_train_set2,test_set2,labels_test_set2,modelname,classes,testing_set,min_num,selectedfeature,training_data):
    filename=modelname
    start=time.time()
    jmsgs=train_set2+test_set2
    omsgs=labels_train_set2+labels_test_set2
    
    c1=0
    c5=0

    try:
        #decision tree
        classifier2 = DecisionTreeClassifier(random_state=0)
        classifier2.fit(train_set2,labels_train_set2)
        scores = cross_val_score(classifier2, test_set2, labels_test_set2,cv=5)
        print('Decision tree accuracy (+/-) %s'%(str(scores.std())))
        c2=scores.mean()
        c2s=scores.std()
        print(c2)
    except:
        c2=0
        c2s=0

    try:
        classifier3 = GaussianNB()
        classifier3.fit(train_set2, labels_train_set2)
        scores = cross_val_score(classifier3, test_set2, labels_test_set2,cv=5)
        print('Gaussian NB accuracy (+/-) %s'%(str(scores.std())))
        c3=scores.mean()
        c3s=scores.std()
        print(c3)
    except:
        c3=0
        c3s=0

    try:
        #svc 
        classifier4 = SVC()
        classifier4.fit(train_set2,labels_train_set2)
        scores=cross_val_score(classifier4, test_set2, labels_test_set2,cv=5)
        print('SKlearn classifier accuracy (+/-) %s'%(str(scores.std())))
        c4=scores.mean()
        c4s=scores.std()
        print(c4)
    except:
        c4=0
        c4s=0

    try:
        #adaboost
        classifier6 = AdaBoostClassifier(n_estimators=100)
        classifier6.fit(train_set2, labels_train_set2)
        scores = cross_val_score(classifier6, test_set2, labels_test_set2,cv=5)
        print('Adaboost classifier accuracy (+/-) %s'%(str(scores.std())))
        c6=scores.mean()
        c6s=scores.std()
        print(c6)
    except:
        c6=0
        c6s=0

    try:
        #gradient boosting 
        classifier7=GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
        classifier7.fit(train_set2, labels_train_set2)
        scores = cross_val_score(classifier7, test_set2, labels_test_set2,cv=5)
        print('Gradient boosting accuracy (+/-) %s'%(str(scores.std())))
        c7=scores.mean()
        c7s=scores.std()
        print(c7)
    except:
        c7=0
        c7s=0

    try:
        #logistic regression
        classifier8=LogisticRegression(random_state=1)
        classifier8.fit(train_set2, labels_train_set2)
        scores = cross_val_score(classifier8, test_set2, labels_test_set2,cv=5)
        print('Logistic regression accuracy (+/-) %s'%(str(scores.std())))
        c8=scores.mean()
        c8s=scores.std()
        print(c8)
    except:
        c8=0
        c8s=0

    try:
        #voting 
        classifier9=VotingClassifier(estimators=[('gradboost', classifier7), ('logit', classifier8), ('adaboost', classifier6)], voting='hard')
        classifier9.fit(train_set2, labels_train_set2)
        scores = cross_val_score(classifier9, test_set2, labels_test_set2,cv=5)
        print('Hard voting accuracy (+/-) %s'%(str(scores.std())))
        c9=scores.mean()
        c9s=scores.std()
        print(c9)
    except:
        c9=0
        c9s=0

    try:
        #knn
        classifier10=KNeighborsClassifier(n_neighbors=7)
        classifier10.fit(train_set2, labels_train_set2)
        scores = cross_val_score(classifier10, test_set2, labels_test_set2,cv=5)
        print('K Nearest Neighbors accuracy (+/-) %s'%(str(scores.std())))
        c10=scores.mean()
        c10s=scores.std()
        print(c10)
    except:
        c10=0
        c10s=0

    try:
        #randomforest
        classifier11=RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
        classifier11.fit(train_set2, labels_train_set2)
        scores = cross_val_score(classifier11, test_set2, labels_test_set2,cv=5)
        print('Random forest accuracy (+/-) %s'%(str(scores.std())))
        c11=scores.mean()
        c11s=scores.std()
        print(c11)
    except:
        c11=0
        c11s=0

    try:
##        #svm
        classifier12 = svm.SVC(kernel='linear', C = 1.0)
        classifier12.fit(train_set2, labels_train_set2)
        scores = cross_val_score(classifier12, test_set2, labels_test_set2,cv=5)
        print('svm accuracy (+/-) %s'%(str(scores.std())))
        c12=scores.mean()
        c12s=scores.std()
        print(c12)
    except:
        c12=0
        c12s=0

    #IF IMBALANCED, USE http://scikit-learn.org/dev/modules/generated/sklearn.naive_bayes.ComplementNB.html

    maxacc=max([c2,c3,c4,c6,c7,c8,c9,c10,c11,c12])

    if maxacc==c1:
        print('most accurate classifier is Naive Bayes'+'with %s'%(selectedfeature))
        classifiername='naive-bayes'
        classifier=classifier1
        #show most important features
        classifier1.show_most_informative_features(5)
    elif maxacc==c2:
        print('most accurate classifier is Decision Tree'+'with %s'%(selectedfeature))
        classifiername='decision-tree'
        classifier2 = DecisionTreeClassifier(random_state=0)
        classifier2.fit(train_set2+test_set2,labels_train_set2+labels_test_set2)
        classifier=classifier2
    elif maxacc==c3:
        print('most accurate classifier is Gaussian NB'+'with %s'%(selectedfeature))
        classifiername='gaussian-nb'
        classifier3 = GaussianNB()
        classifier3.fit(train_set2+test_set2, labels_train_set2+labels_test_set2)
        classifier=classifier3
    elif maxacc==c4:
        print('most accurate classifier is SK Learn'+'with %s'%(selectedfeature))
        classifiername='sk'
        classifier4 = SVC()
        classifier4.fit(train_set2+test_set2,labels_train_set2+labels_test_set2)
        classifier=classifier4
    elif maxacc==c5:
        print('most accurate classifier is Maximum Entropy Classifier'+'with %s'%(selectedfeature))
        classifiername='max-entropy'
        classifier=classifier5
    #can stop here (c6-c10)
    elif maxacc==c6:
        print('most accuracate classifier is Adaboost classifier'+'with %s'%(selectedfeature))
        classifiername='adaboost'
        classifier6 = AdaBoostClassifier(n_estimators=100)
        classifier6.fit(train_set2+test_set2, labels_train_set2+labels_test_set2)
        classifier=classifier6
    elif maxacc==c7:
        print('most accurate classifier is Gradient Boosting '+'with %s'%(selectedfeature))
        classifiername='graidentboost'
        classifier7=GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
        classifier7.fit(train_set2+test_set2, labels_train_set2+labels_test_set2)
        classifier=classifier7
    elif maxacc==c8:
        print('most accurate classifier is Logistic Regression '+'with %s'%(selectedfeature))
        classifiername='logistic_regression'
        classifier8=LogisticRegression(random_state=1)
        classifier8.fit(train_set2+test_set2, labels_train_set2+labels_test_set2)
        classifier=classifier8
    elif maxacc==c9:
        print('most accurate classifier is Hard Voting '+'with %s'%(selectedfeature))
        classifiername='hardvoting'
        classifier7=GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
        classifier7.fit(train_set2+test_set2, labels_train_set2+labels_test_set2)
        classifier8=LogisticRegression(random_state=1)
        classifier8.fit(train_set2+test_set2, labels_train_set2+labels_test_set2)
        classifier6 = AdaBoostClassifier(n_estimators=100)
        classifier6.fit(train_set2+test_set2, labels_train_set2+labels_test_set2)
        classifier9=VotingClassifier(estimators=[('gradboost', classifier7), ('logit', classifier8), ('adaboost', classifier6)], voting='hard')
        classifier9.fit(train_set2+test_set2, labels_train_set2+labels_test_set2)
        classifier=classifier9
    elif maxacc==c10:
        print('most accurate classifier is K nearest neighbors '+'with %s'%(selectedfeature))
        classifiername='knn'
        classifier10=KNeighborsClassifier(n_neighbors=7)
        classifier10.fit(train_set2+test_set2, labels_train_set2+labels_test_set2)
        classifier=classifier10
    elif maxacc==c11:
        print('most accurate classifier is Random forest '+'with %s'%(selectedfeature))
        classifiername='randomforest'
        classifier11=RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
        classifier11.fit(train_set2+test_set2, labels_train_set2+labels_test_set2)
        classifier=classifier11
    elif maxacc==c12:
        print('most accurate classifier is SVM '+' with %s'%(selectedfeature))
        classifiername='svm'
        classifier12 = svm.SVC(kernel='linear', C = 1.0)
        classifier12.fit(train_set2+test_set2, labels_train_set2+labels_test_set2)    
        classifier=classifier12

    modeltypes=['decision-tree','gaussian-nb','sk','adaboost','gradient boosting','logistic regression','hard voting','knn','random forest','svm']
    accuracym=[c2,c3,c4,c6,c7,c8,c9,c10,c11,c12]
    accuracys=[c2s,c3s,c4s,c6s,c7s,c8s,c9s,c10s,c11s,c12s]
    model_accuracy=list()
    for i in range(len(modeltypes)):
        model_accuracy.append([modeltypes[i],accuracym[i],accuracys[i]])

    model_accuracy.sort(key=itemgetter(1))
    endlen=len(model_accuracy)

    print('saving classifier to disk')
    f=open(modelname+'.pickle','wb')
    pickle.dump(classifier,f)
    f.close()

    end=time.time()

    execution=end-start
    
    print('summarizing session...')

    accstring=''
    
    for i in range(len(model_accuracy)):
        accstring=accstring+'%s: %s (+/- %s)\n'%(str(model_accuracy[i][0]),str(model_accuracy[i][1]),str(model_accuracy[i][2]))

    training=len(train_set2)
    testing=len(test_set2)
    
    summary='SUMMARY OF MODEL SELECTION \n\n'+'WINNING MODEL: \n\n'+'%s: %s (+/- %s) \n\n'%(str(model_accuracy[len(model_accuracy)-1][0]),str(model_accuracy[len(model_accuracy)-1][1]),str(model_accuracy[len(model_accuracy)-1][2]))+'MODEL FILE NAME: \n\n %s.pickle'%(filename)+'\n\n'+'DATE CREATED: \n\n %s'%(datetime.datetime.now())+'\n\n'+'EXECUTION TIME: \n\n %s\n\n'%(str(execution))+'GROUPS: \n\n'+str(classes)+'\n'+'('+str(min_num)+' in each class, '+str(int(testing_set*100))+'% used for testing)'+'\n\n'+'TRAINING SUMMARY:'+'\n\n'+training_data+'FEATURES: \n\n %s'%(selectedfeature)+'\n\n'+'MODELS, ACCURACIES, AND STANDARD DEVIATIONS: \n\n'+accstring+'\n\n'+'(C) 2018, NeuroLex Laboratories'

    data={
        'model':modelname,
        'modeltype':model_accuracy[len(model_accuracy)-1][0],
        'accuracy':model_accuracy[len(model_accuracy)-1][1],
        'deviation':model_accuracy[len(model_accuracy)-1][2]
        }
    
    return [classifier, model_accuracy[endlen-1], summary, data]

#LOAD AND BALANCE DATASETS
#####################################################################

#size of each embedding vector
#(100 is used as default to reduce dimensionality)
size=100
classnum=input('how many classes are you training?')

folderlist=list()
a=0
while a != int(classnum):
    folderlist.append(input('what is the folder name for class %s?'%(str(a+1))))
    a=a+1

name=''
for i in range(len(folderlist)):
    if i==0:
        name=name+folderlist[i]
    else:
        name=name+'_'+folderlist[i]
    
start=time.time()
#modelname=input('what is the name of your classifier?')
modelname=name+'_sc_w2v'
jsonfilename=name+'_w2v.json'
dir3=os.getcwd()+'/train-diseases/spreadsheets/'
model_dir=os.getcwd()+'/models/'

try:
    os.chdir(model_dir)
except:
    os.mkdir(model_dir)
    
cur_dir=dir3
testing_set=0.33

try:
    os.chdir(dir3)
except:
    os.mkdir(dir3)
    os.chdir(dir3)

if jsonfilename not in os.listdir():
    
    features_list=list()
    transcripts_list=list()
    filenames_list=list()

    for i in range(len(folderlist)):

        name=folderlist[i]

        dir_=cur_dir+name

        g='error'
        while g == 'error':
            try:
                g='noterror'
                print('changing directory: '.upper()+dir_)
                os.chdir(dir_)
            except:
                g='error'
                print('directory not recognized')
                dir_=input('input directory %s path'%(str(i+1)))

        #now go through each directory and featurize the samples and save them as .json files 
        try:
            os.chdir(dir_)
        except:
            os.mkdir(dir_)
            os.chdir(dir_)

        # remove any prior featurization
        dirlist=os.listdir()
        for j in range(len(dirlist)):
            if dirlist[j][-5:]=='.json':
                os.remove(dirlist[j])
        dirlist=os.listdir()
        transcripts=list()
        filenames=list()
        for j in range(len(dirlist)):

            try:
            
                filename=dirlist[j][0:-4]+'.json'
                
                if dirlist[j][-4:]=='.wav' and dirlist[j][0:-4]+'.json' not in dirlist:
                    #transcribe and save as .json data
                    print(name.upper()+' - transcribing %s'%(dirlist[j]))
                    transcript=transcribe(dirlist[j])
                    print(transcript)
                    transcripts.append(transcript)
                    data={
                        'filename':filename,
                        'transcript':transcript,
                        }
                    jsonfile=open(dirlist[j][0:-4]+'.json','w')
                    json.dump(data,jsonfile)
                    jsonfile.close()
                    filenames.append(filename)
                else:
                    #load file if already in directory
                    if dirlist[j][0:-4]+'.json' in dirlist:
                        transcripts.append(json.load(open(dirlist[j][0:-4]+'.json'))['transcript'])
                        filenames.append(filename)

            except:

                pass

        # now train word2vec model
        os.chdir(model_dir)
        print('training w2v models')
        w2v(transcripts,size,modelname+'_%s.pickle'%(str(i+1)))

        filenames_list.append(filenames)
        transcripts_list.append(transcripts)

    # for testing only 
    #   print(transcripts_list[0])
    #   print(transcripts_list[1])

    # randomly shuffle lists
    feature_lengths=list()
    feature_list2=list()
    for i in range(len(transcripts_list)):
        one=transcripts_list[i]
        random.shuffle(one)
        feature_list2.append(one)
        feature_lengths.append(len(one))

    min_num=np.amin(feature_lengths)
    #make sure they are the same length (For later) - this avoid errors
    while min_num*len(folderlist) != np.sum(feature_lengths):
        for i in range(len(folderlist)):
            while len(feature_list2[i])>min_num:
                print('%s is %s more than %s, balancing...'%(folderlist[i].upper(),str(len(feature_list2[i])-int(min_num)),'min value'))
                feature_list2[i].pop()
        feature_lengths=list()
        for i in range(len(feature_list2)):
            one=feature_list2[i]
            feature_lengths.append(len(one))

    #rename intermediate varibale back into list 
    transcript_list=feature_list2

    # FEATURIZE 
    # now that we have an equal number of transcripts in each feature array,
    # we can now build an actual feature set from each representative transcript
    labels=list()
    
    for i in range(len(folderlist)):

        name=folderlist[i]
        dir_=cur_dir+name
        transcripts=transcript_list[i]
        random.shuffle(transcripts)

        for j in range(len(transcripts)):

            try:
                #get numpy array features 
                sentence=transcripts[j]
                embedding=np.array([])
                os.chdir(model_dir)
                for k in range(len(folderlist)-1):
                    if k==0:
                        output=sentence_embedding(sentence,size,modelname+'_%s.pickle'%(str(k+1)))
                        output2=sentence_embedding(sentence,size,modelname+'_%s.pickle'%(str(k+2)))
                        embedding_temp=np.append(output,output2)
                        embedding=np.append(embedding,embedding_temp)
                    else:
                        embedding_temp=sentence_embedding(sentence,size,modelname+'_%s.pickle'%(str(k+2)))
                        embedding=np.append(embedding,embedding_temp)
                        
                    print(embedding)
                    
                os.chdir(dir_)
                features=embedding.tolist()
                features_list.append(features)
                labels.append(name)

            except:
                pass 

    os.chdir(cur_dir)
    
    data={
        'features':features_list,
        'labels':labels,
        }

    jsonfile=open(jsonfilename,'w')
    json.dump(data,jsonfile)
    jsonfile.close()

else:
    
    g=json.load(open(jsonfilename))
    features_list=g['features']
    labels=g['labels']
    
# TRAIN AND TEST SET GENERATION 
#################################################################
# note that this assumes a classification problem based on total number of classes 
os.chdir(cur_dir)

#load data - can do this through loading .txt or .json files
#json file must have 'message' field 
data=json.loads(open(jsonfilename).read())

classes=list()
for i in range(len(labels)):
    if labels[i] not in classes:
        classes.append(labels[i])

train_set, test_set, train_labels, test_labels = train_test_split(features_list,
                                                                  labels,
                                                                  test_size=testing_set,
                                                                  random_state=42)

try:
    os.chdir(model_dir)
except:
    os.mkdir(model_dir)
    os.chdir(model_dir)
    
g=open(modelname+'_training_data.txt','w')
g.write('train labels'+'\n\n'+str(train_labels)+'\n\n')
g.write('test labels'+'\n\n'+str(test_labels)+'\n\n')
g.close()

training_data=open(modelname+'_training_data.txt').read()

# MODEL OPTIMIZATION / SAVE TO DISK 
#################################################################            
selectedfeature='w2v features from all vocabulary of each class.'
min_num=int(len(features_list)/len(classes))

[w2v_model, w2v_acc, w2v_summary, data]=optimizemodel_sc(train_set,train_labels,test_set,test_labels,modelname,classes,testing_set,min_num,selectedfeature,training_data)

g=open(modelname+'.txt','w')
g.write(w2v_summary)
g.close()

g2=open(modelname+'.json','w')
json.dump(data,g2)
g2.close()
              
print(w2v_model)
print(w2v_acc)

