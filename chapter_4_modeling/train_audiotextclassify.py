'''
train_audiotextclassify.py

Jim Schwoebel
(C) 2018, NeuroLex Laboratories 

This function takes in two folders with wav files (20 secs),
transcribes them through PocketSphinx,
fingerprints them with audio and text features (.json),
and then builds an optimized machine learning model from these features.

This model-building scripts assumes the input audio files are of the same length.

This also includes textclassify and audioclassify together. 

Total features include:
labels = ['mfcc1_mean_(0.02 second window)', 'mfcc1_std_(0.02 second window)', 'mfcc1_max_(0.02 second window)', 'mfcc1_min_(0.02 second window)', 
        'mfcc2_mean_(0.02 second window)', 'mfcc2_std_(0.02 second window)', 'mfcc2_max_(0.02 second window)', 'mfcc2_min_(0.02 second window)', 
        'mfcc3_mean_(0.02 second window)', 'mfcc3_std_(0.02 second window)', 'mfcc3_max_(0.02 second window)', 'mfcc3_min_(0.02 second window)', 
        'mfcc4_mean_(0.02 second window)', 'mfcc4_std_(0.02 second window)', 'mfcc4_max_(0.02 second window)', 'mfcc4_min_(0.02 second window)', 
        'mfcc5_mean_(0.02 second window)', 'mfcc5_std_(0.02 second window)', 'mfcc5_max_(0.02 second window)', 'mfcc5_min_(0.02 second window)', 
        'mfcc6_mean_(0.02 second window)', 'mfcc6_std_(0.02 second window)', 'mfcc6_max_(0.02 second window)', 'mfcc6_min_(0.02 second window)', 
        'mfcc7_mean_(0.02 second window)', 'mfcc7_std_(0.02 second window)', 'mfcc7_max_(0.02 second window)', 'mfcc7_min_(0.02 second window)', 
        'mfcc8_mean_(0.02 second window)', 'mfcc8_std_(0.02 second window)', 'mfcc8_max_(0.02 second window)', 'mfcc8_min_(0.02 second window)', 
        'mfcc9_mean_(0.02 second window)', 'mfcc9_std_(0.02 second window)', 'mfcc9_max_(0.02 second window)', 'mfcc9_min_(0.02 second window)', 
        'mfcc10_mean_(0.02 second window)', 'mfcc10_std_(0.02 second window)', 'mfcc10_max_(0.02 second window)', 'mfcc10_min_(0.02 second window)', 
        'mfcc11_mean_(0.02 second window)', 'mfcc11_std_(0.02 second window)', 'mfcc11_max_(0.02 second window)', 'mfcc11_min_(0.02 second window)', 
        'mfcc12_mean_(0.02 second window)', 'mfcc12_std_(0.02 second window)', 'mfcc12_max_(0.02 second window)', 'mfcc12_min_(0.02 second window)', 
        'mfcc13_mean_(0.02 second window)', 'mfcc13_std_(0.02 second window)', 'mfcc13_max_(0.02 second window)', 'mfcc13_min_(0.02 second window)', 
        'mfccdelta1_mean_(0.02 second window)', 'mfccdelta1_std_(0.02 second window)', 'mfccdelta1_max_(0.02 second window)', 'mfccdelta1_min_(0.02 second window)', 
        'mfccdelta2_mean_(0.02 second window)', 'mfccdelta2_std_(0.02 second window)', 'mfccdelta2_max_(0.02 second window)', 'mfccdelta2_min_(0.02 second window)', 
        'mfccdelta3_mean_(0.02 second window)', 'mfccdelta3_std_(0.02 second window)', 'mfccdelta3_max_(0.02 second window)', 'mfccdelta3_min_(0.02 second window)', 
        'mfccdelta4_mean_(0.02 second window)', 'mfccdelta4_std_(0.02 second window)', 'mfccdelta4_max_(0.02 second window)', 'mfccdelta4_min_(0.02 second window)', 
        'mfccdelta5_mean_(0.02 second window)', 'mfccdelta5_std_(0.02 second window)', 'mfccdelta5_max_(0.02 second window)', 'mfccdelta5_min_(0.02 second window)', 
        'mfccdelta6_mean_(0.02 second window)', 'mfccdelta6_std_(0.02 second window)', 'mfccdelta6_max_(0.02 second window)', 'mfccdelta6_min_(0.02 second window)', 
        'mfccdelta7_mean_(0.02 second window)', 'mfccdelta7_std_(0.02 second window)', 'mfccdelta7_max_(0.02 second window)', 'mfccdelta7_min_(0.02 second window)', 
        'mfccdelta8_mean_(0.02 second window)', 'mfccdelta8_std_(0.02 second window)', 'mfccdelta8_max_(0.02 second window)', 'mfccdelta8_min_(0.02 second window)', 
        'mfccdelta9_mean_(0.02 second window)', 'mfccdelta9_std_(0.02 second window)', 'mfccdelta9_max_(0.02 second window)', 'mfccdelta9_min_(0.02 second window)', 
        'mfccdelta10_mean_(0.02 second window)', 'mfccdelta10_std_(0.02 second window)', 'mfccdelta10_max_(0.02 second window)', 'mfccdelta10_min_(0.02 second window)', 
        'mfccdelta11_mean_(0.02 second window)', 'mfccdelta11_std_(0.02 second window)', 'mfccdelta11_max_(0.02 second window)', 'mfccdelta11_min_(0.02 second window)', 
        'mfccdelta12_mean_(0.02 second window)', 'mfccdelta12_std_(0.02 second window)', 'mfccdelta12_max_(0.02 second window)', 'mfccdelta12_min_(0.02 second window)', 
        'mfccdelta13_mean_(0.02 second window)', 'mfccdelta13_std_(0.02 second window)', 'mfccdelta13_max_(0.02 second window)', 'mfccdelta13_min_(0.02 second window)', 
        'mfcc1_mean_(0.50 second window)', 'mfcc1_std_(0.50 second window)', 'mfcc1_max_(0.50 second window)', 'mfcc1_min_(0.50 second window)', 
        'mfcc2_mean_(0.50 second window)', 'mfcc2_std_(0.50 second window)', 'mfcc2_max_(0.50 second window)', 'mfcc2_min_(0.50 second window)', 
        'mfcc3_mean_(0.50 second window)', 'mfcc3_std_(0.50 second window)', 'mfcc3_max_(0.50 second window)', 'mfcc3_min_(0.50 second window)', 
        'mfcc4_mean_(0.50 second window)', 'mfcc4_std_(0.50 second window)', 'mfcc4_max_(0.50 second window)', 'mfcc4_min_(0.50 second window)', 
        'mfcc5_mean_(0.50 second window)', 'mfcc5_std_(0.50 second window)', 'mfcc5_max_(0.50 second window)', 'mfcc5_min_(0.50 second window)', 
        'mfcc6_mean_(0.50 second window)', 'mfcc6_std_(0.50 second window)', 'mfcc6_max_(0.50 second window)', 'mfcc6_min_(0.50 second window)', 
        'mfcc7_mean_(0.50 second window)', 'mfcc7_std_(0.50 second window)', 'mfcc7_max_(0.50 second window)', 'mfcc7_min_(0.50 second window)', 
        'mfcc8_mean_(0.50 second window)', 'mfcc8_std_(0.50 second window)', 'mfcc8_max_(0.50 second window)', 'mfcc8_min_(0.50 second window)', 
        'mfcc9_mean_(0.50 second window)', 'mfcc9_std_(0.50 second window)', 'mfcc9_max_(0.50 second window)', 'mfcc9_min_(0.50 second window)', 
        'mfcc10_mean_(0.50 second window)', 'mfcc10_std_(0.50 second window)', 'mfcc10_max_(0.50 second window)', 'mfcc10_min_(0.50 second window)', 
        'mfcc11_mean_(0.50 second window)', 'mfcc11_std_(0.50 second window)', 'mfcc11_max_(0.50 second window)', 'mfcc11_min_(0.50 second window)', 
        'mfcc12_mean_(0.50 second window)', 'mfcc12_std_(0.50 second window)', 'mfcc12_max_(0.50 second window)', 'mfcc12_min_(0.50 second window)', 
        'mfcc13_mean_(0.50 second window)', 'mfcc13_std_(0.50 second window)', 'mfcc13_max_(0.50 second window)', 'mfcc13_min_(0.50 second window)', 
        'mfccdelta1_mean_(0.50 second window)', 'mfccdelta1_std_(0.50 second window)', 'mfccdelta1_max_(0.50 second window)', 'mfccdelta1_min_(0.50 second window)', 
        'mfccdelta2_mean_(0.50 second window)', 'mfccdelta2_std_(0.50 second window)', 'mfccdelta2_max_(0.50 second window)', 'mfccdelta2_min_(0.50 second window)', 
        'mfccdelta3_mean_(0.50 second window)', 'mfccdelta3_std_(0.50 second window)', 'mfccdelta3_max_(0.50 second window)', 'mfccdelta3_min_(0.50 second window)', 
        'mfccdelta4_mean_(0.50 second window)', 'mfccdelta4_std_(0.50 second window)', 'mfccdelta4_max_(0.50 second window)', 'mfccdelta4_min_(0.50 second window)', 
        'mfccdelta5_mean_(0.50 second window)', 'mfccdelta5_std_(0.50 second window)', 'mfccdelta5_max_(0.50 second window)', 'mfccdelta5_min_(0.50 second window)', 
        'mfccdelta6_mean_(0.50 second window)', 'mfccdelta6_std_(0.50 second window)', 'mfccdelta6_max_(0.50 second window)', 'mfccdelta6_min_(0.50 second window)', 
        'mfccdelta7_mean_(0.50 second window)', 'mfccdelta7_std_(0.50 second window)', 'mfccdelta7_max_(0.50 second window)', 'mfccdelta7_min_(0.50 second window)', 
        'mfccdelta8_mean_(0.50 second window)', 'mfccdelta8_std_(0.50 second window)', 'mfccdelta8_max_(0.50 second window)', 'mfccdelta8_min_(0.50 second window)', 
        'mfccdelta9_mean_(0.50 second window)', 'mfccdelta9_std_(0.50 second window)', 'mfccdelta9_max_(0.50 second window)', 'mfccdelta9_min_(0.50 second window)', 
        'mfccdelta10_mean_(0.50 second window)', 'mfccdelta10_std_(0.50 second window)', 'mfccdelta10_max_(0.50 second window)', 'mfccdelta10_min_(0.50 second window)', 
        'mfccdelta11_mean_(0.50 second window)', 'mfccdelta11_std_(0.50 second window)', 'mfccdelta11_max_(0.50 second window)', 'mfccdelta11_min_(0.50 second window)', 
        'mfccdelta12_mean_(0.50 second window)', 'mfccdelta12_std_(0.50 second window)', 'mfccdelta12_max_(0.50 second window)', 'mfccdelta12_min_(0.50 second window)', 


    Text features - numpy array C (64)

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
    
    np.append(A,B,C) --> 271 features

#^ it is this approach that we take in the current representation [208 features]

The models tested here include:
    -Naive Bayes
    -Decision tree 
    -Support vector machines
    -Bernoulli
    -Maximum entropy
    -Adaboost
    -Gradient boost
    -Logistic regression
    -Hard voting
    -K nearest neighbors
    -Random forest 
    -SVM algorithm
    -... [future: Deep learning models, etc.]

The output is an optimized machine learning model to a feature as a
.pickle file, which can be easily imported into the future through code like:

    import pickle
    f = open(classifiername+'_%s'%(selectedfeature)+'.pickle', 'rb')
    classifier = pickle.load(function(f))
    ##where function is the feature 
    f.close()
    ##classify with proper function...
    classifier.classify(startword(text))

Happy modeling!!
'''

import speech_recognition as sr  
import librosa
from pydub import AudioSegment
import os, nltk, random, json 
from nltk import word_tokenize
from nltk.classify import apply_features, SklearnClassifier, maxent
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

# INITIALIZE FUNCTIONS 
#############################################################
def optimizemodel_sc(train_set2,labels_train_set2,test_set2,labels_test_set2,modelname,classes,testing_set,min_num,selectedfeature,training_data):
    filename=modelname
    start=time.time()
    jmsgs=train_set2+test_set2
    omsgs=labels_train_set2+labels_test_set2
    
    c1=0
    c5=0

    #try:
    #decision tree
    classifier2 = DecisionTreeClassifier(random_state=0)
    classifier2.fit(train_set2,labels_train_set2)
    scores = cross_val_score(classifier2, test_set2, labels_test_set2,cv=5)
    print('Decision tree accuracy (+/-) %s'%(str(scores.std())))
    c2=scores.mean()
    c2s=scores.std()
    print(c2)
##    except:
##        c2=0
##        c2s=0

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
    
#FEATURIZE .WAV FILES WITH AUDIO FEATURES --> MAKE JSON (if needed)
#############################################################

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
modelname=name+'_sc_audiotext'

jsonfilename=name+'_audiotext.json'
dir3=os.getcwd()+'/train-diseases/spreadsheets/'
model_dir=os.getcwd()+'/models'
cur_dir=dir3
testing_set=0.33

try:
    os.chdir(dir3)
except:
    os.mkdir(dir3)
    os.chdir(dir3)

if jsonfilename not in os.listdir():

    features_list=list()

    for i in range(len(folderlist)):

        name=folderlist[i]

        dir_=cur_dir+name

        g='error'
        
        while g == 'error':
            try:
                g='noterror'
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
        
        # remove any prior features 
        dirlist=os.listdir()
        for j in range(len(dirlist)):
            if dirlist[j][-5:]=='.json':
                os.remove(dirlist[j])
        dirlist=os.listdir()

        #if broken session, load all previous transcripts
        #this reduces costs if tied to GCP
        one=list()
        for j in range(len(dirlist)):
            try:
                if dirlist[j][-5:]=='.json':
                    #this assumes all .json in the folder are transcript (safe assumption if only .wav files)
                    jsonfile=dirlist[j]
                    features=json.load(open(jsonfile))['features']
                    if len(features) != 272:
                        os.remove(dirlist[j])
                    else:
                        one.append(features)
            except:
                pass 
            
        for j in range(len(dirlist)):
            try:
                if dirlist[j][-4:]=='.wav' and dirlist[j][0:-4]+'.json' not in dirlist and os.path.getsize(dirlist[j])>500:
                    #loop through files and get features
                    try:
                        wavfile=dirlist[j]
                        print('%s - featurizing %s'%(name.upper(),wavfile))
                        #obtain features
                        transcript=transcribe(wavfile)
                        text_features=textfeatures(transcript)
                        audio_features=np.append(featurize(wavfile),audio_time_features(wavfile))
                        features=np.append(audio_features,text_features)
                        print(features)
                        #append to list 
                        one.append(features.tolist())
                        #save intermediate .json just in case
                        data={
                            'features':features.tolist(),
                            'transcript':transcript,
                            }
                        jsonfile=open(dirlist[j][0:-4]+'.json','w')
                        json.dump(data,jsonfile)
                        jsonfile.close()
                    except:
                        pass
                else:
                    pass
            except:
                pass
            
        features_list.append(one)
        
    #randomly shuffle lists
    feature_list2=list()
    feature_lengths=list()
    for i in range(len(features_list)):
        one=features_list[i]
        random.shuffle(one)
        feature_list2.append(one)
        feature_lengths.append(len(one))
    
    # remember folderlist has all the labels
    
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
        
    #now write to json
    data={}
    for i in range(len(folderlist)):
        data.update({folderlist[i]:feature_list2[i]})
    
    os.chdir(dir3)
        
    jsonfile=open(jsonfilename,'w')
    json.dump(data,jsonfile)
    jsonfile.close()
    
else:
    pass

# DATA PREPROCESSING 
#############################################################
# note that this assumes a classification problem based on total number of classes 
os.chdir(cur_dir)

#load data - can do this through loading .txt or .json files
#json file must have 'message' field 
data=json.loads(open(jsonfilename).read())

classes=list(data)
features=list()
labels=list()
for i in range(len(classes)):
    for j in range(len(data[classes[i]])):
        feature=data[classes[i]][j]
        features.append(feature)
        labels.append(classes[i])

train_set, test_set, train_labels, test_labels = train_test_split(features,
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

#MODEL OPTIMIZATION / SAVE TO DISK 
#################################################################            
selectedfeature='mixed features (mfcc coefficients and text features).'
min_num=len(data[classes[0]])
[mixed_model, mixed_acc, mixed_summary, data]=optimizemodel_sc(train_set,train_labels,test_set,test_labels,modelname,classes,testing_set,min_num,selectedfeature,training_data)

g=open(modelname+'.txt','w')
g.write(mixed_summary)
g.close()

g2=open(modelname+'.json','w')
json.dump(data,g2)
g2.close()
              
print(mixed_model)
print(mixed_acc)
