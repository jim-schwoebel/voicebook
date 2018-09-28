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
##               META_FEATURES.PY             ##    
================================================ 

Load in meta features by featurizing and applying loaded ML models.

71 total models are trained and provided here for you; feel free to add to this list.

Note these are models trained on the NeuroLex standard embedding - which
is usually just a combination of mfcc coefficients and mfcc deltas spread out
over time. 

====================================================================
MODEL ACCURACIES 

A list of accuracies, standard deviations, and modeltypes is provided below
(also in summary.xlsx in the meta_models folder).

====================================================================

addiction_controls  0.616666666666667 0.233333333333333 logistic regression
adhd_controls 0.62  0.0653197264742181  sk
africanamerican_controls  0.887894736842105 0.0528836071034967  hard voting
als_controls  0.833333333333333 0.210818510677892 hard voting
alternative_alternativecontrolbalanced  0.743333333333333 0.163842743032593 random forest
amharic_amharic_controls  0.666666666666667 0.182574185835055 knn
angry_angry_controls  0.598824786324786 0.0216278858906185  hard voting
anxiety_controls  0.8 0.244948974278318 knn
autism_controls 0.583333333333333 0.105409255338946 random forest
awake_fatigued  0.772527472527473 0.0845225693319974  gaussian-nb
bipolar_controls  0.706666666666667 0.149666295470958 gaussian-nb
caffeine_controls 0.933333333333333 0.133333333333333 hard voting
cantonese_cantonese_controls  0.783333333333333 0.296273147243853 adaboost
christian_christiancontrolbalanced  0.86  0.195959179422654 logistic regression
cold_controls 0.826666666666667 0.18306040290328  logistic regression
country_countrycontrolbalanced  0.9 0.122474487139159 svm
depression_controls 0.833333333333333 0.139443337755679 adaboost
disgust_disgust_controls  0.793333333333333 0.123648246606609 logistic regression
dutch_dutch_controls  0.705714285714286 0.16747829588289  random forest
dyslexia_controls 0.59  0.0916515138991168  knn
edm_edmcontrolbalanced  0.71  0.190787840283389 svm
english_english_controls  0.686274509803922 0.0733002966373284  logistic regression
fear_fear_controls  0.612705882352941 0.0359251646457615  gaussian-nb
fifties_fifties_controls  0.794545131389912 0.0151656184818545  knn
folk_folkcontrolbalanced  0.683333333333333 0.290593262902712 logistic regression
fourties_fourties_controls  0.774859823805254 0.0186105837039435  knn
french_french_controls  0.819047619047619 0.118187368057056 gaussian-nb
gender  0.886945812807882 0.0601933355302945  hard voting
german_german_controls  0.516666666666667 0.260341655863555 random forest
glioblastoma_controls 0.666666666666667 0.278886675511358 knn
graves_disease_controls 0.8 0.187082869338697 logistic regression
happy_happy_controls  0.544996147089866 0.0387385680145828  logistic regression
highquality_badquality  0.756666666666667 0.0827311576399391  logistic regression
holiday_holidaycontrolbalanced  0.633333333333333 0.250554939639549 svm
indie_indiecontrolbalanced  0.743333333333333 0.163842743032593 svm
italian_italian_controls  0.683333333333333 0.24381231397213  adaboost
japanese_japanese_controls  0.813333333333333 0.243675558433294 hard voting
jazz_jazzcontrolbalanced  0.793333333333333 0.111853078237084 gaussian-nb
korean_korean_controls  0.763333333333333 0.225191276720727 gaussian-nb
latin_latincontrolbalanced  0.87  0.166132477258361 gaussian-nb
macedonian_macedonian_controls  0.733333333333333 0.226077666104176 random forest
mandarin_mandarin_controls  0.633333333333333 0.250554939639549 gaussian-nb
multiple_sclerosis_controls 0.81  0.110352969048312 gradient boosting
natural_non-natural 0.796153846153846 0.0803100500685427  adaboost
neutral_neutral_controls  0.557614471387894 0.0346767702052588  gaussian-nb
newage_newagecontrolbalanced  0.843333333333333 0.134824989441045 adaboost
parkinsons_controls 0.65  0.3 random forest
polish_polish_controls  0.586666666666667 0.223706156474167 knn
pop_popcontrolbalanced  0.643333333333333 0.20127372185934  hard voting
portuguese_portuguese_controls  0.606666666666667 0.179381653960983 decision-tree
postpartum_depression_controls  0.893333333333333 0.137275068546493 knn
rap_rapcontrolbalanced  0.803333333333333 0.16746475582774  hard voting
reggae_reggaecontrolbalanced  0.703333333333333 0.0609188896083236  random forest
rock_rockcontrolbalanced  0.693333333333333 0.105725010181025 logistic regression
romanian_romanian_controls  0.766666666666667 0.2 logistic regression
russian_russian_controls  0.64  0.32  decision-tree
sad_sad_controls  0.57773240365648  0.0294270111310834  knn
schizophrenia_controls  0.73  0.198438347548496 svm
seventies_seventies_controls  0.795753660637382 0.0378425083662649  hard voting
sixties_sixties_controls  0.797694462400345 0.0346864094031604  knn
sleep_apnea_controls  0.713333333333333 0.0710242525088751  gaussian-nb
soundtrack_soundtrackcontrolbalanced  0.9 0.122474487139159 gradient boosting
spanish_spanish_controls  0.571111111111111 0.0896082006829153  adaboost
stressed_calm 0.788888888888889 0.0926962382871743  logistic regression
surprise_surprise_controls  0.59468085106383  0.0361563038199457  knn
swedish_swedish_controls  0.666666666666667 0.182574185835055 logistic regression
teens_teens_controls  0.762092175756338 0.0212424639835302  knn
thirties_thirties_controls  0.765463935070702 0.00626231620665817 knn
turkish_turkish_controls  0.733333333333333 0.152023390013218 adaboost
twenties_twenties_controls  0.747827586437699 0.00483503800126851 knn
vietnamese_vietnamese_controls  0.65  0.2 gaussian-nb

====================================================================

An example output from the script is below

====================================================================

META FEATURES 


[1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 
0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


 META CLASSES: 


['controls', 'adhd', 'africanamerican', 'controls', 'alternativecontrolbalanced', 
'amharic_controls', 'angry_controls', 'anxiety', 'controls', 'controls', 'controls', 
'cantonese', 'christian', 'controls', 'country', 'depression', 'disgust_controls', 
'dutch_controls', 'controls', 'edmcontrolbalanced', 'english', 'awake', 'fear_controls', 
'fifties_controls', 'folkcontrolbalanced', 'fourties_controls', 'french_controls', 
'male', 'german', 'controls', 'controls', 'happy_controls', 'holiday', 
'indiecontrolbalanced', 'italian', 'japanese', 'jazzcontrolbalanced', 'korean', 
'latin', 'macedonian_controls', 'mandarin_controls', 'multiple_sclerosis', 'natural', 
'neutral_controls', 'newagecontrolbalanced', 'controls', 'polish', 'popcontrolbalanced', 
'portuguese_controls', 'controls', 'badquality', 'rapcontrolbalanced', 'reggae', 'rock', 
'romanian', 'russian_controls', 'sad', 'controls', 'seventies_controls', 'sixties', 
'controls', 'soundtrackcontrolbalanced', 'spanish_controls', 'stressed', 'surprise_controls', 
'swedish', 'teens', 'thirties', 'turkish', 'twenties', 'vietnamese_controls']

=====================================================================================

Happy Meta-featurizing!  
'''

################################################################################
##                      IMPORT STATEMENTS                                     ##
################################################################################

import librosa, pickle, getpass, time, zipfile
from pydub import AudioSegment
import os, nltk, random, json 
from nltk import word_tokenize 
import numpy as np 


################################################################################
##                      HELPER FUNCTIONS                                     ##
################################################################################

def unzip(file):
    filepath=os.getcwd()+'/'+file
    folderpath=os.getcwd()+'/'+file[0:-4]
    zip = zipfile.ZipFile(filepath)
    zip.extractall(path=folderpath)

def featurize2(wavfile):
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
            features=featurize2(filelist[i])
            featureslist=featureslist+features 
            os.remove(filelist[j])
        except:
            print('error splicing')
            os.remove(filelist[j])

    #now scale the featureslist array by the length to get mean in each category
    featureslist=featureslist/segnum
    
    return featureslist

def featurize(wavfile):
    features=np.append(featurize2(wavfile),audio_time_features(wavfile))
    return features 

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

################################################################################
##                             MAIN SCRIPT                                    ##
################################################################################

# initialize directories and variables 
cur_dir=os.getcwd()+'/load_dir'
model_dir=os.getcwd()+'/meta_models/'
load_dir=cur_dir 
errorcount=0
count=0

labels = ['addiction_controls', 'adhd_controls', 'africanamerican_controls','als_controls','alternative_alternativecontrolbalanced',
           'amharic_amharic_controls','angry_angry_controls','anxiety_controls','autism_controls',
           'bipolar_controls','caffeine_controls','cantonese_cantonese_controls','christian_christiancontrolbalanced',
           'cold_controls','country_countrycontrolbalanced','depression_controls','disgust_disgust_controls',
           'dutch_dutch_controls', 'dyslexia_controls', 'edm_edmcontrolbalanced', 'english_english_controls',
           'awake_fatigued', 'fear_fear_controls', 'fifties_fifties_controls', 'folk_folkcontrolbalanced',
           'fourties_fourties_controls', 'french_french_controls','gender','german_german_controls',
           'glioblastoma_controls','graves_disease_controls','happy_happy_controls','holiday_holidaycontrolbalanced',
           'indie_indiecontrolbalanced','italian_italian_controls','japanese_japanese_controls','jazz_jazzcontrolbalanced',
           'korean_korean_controls','latin_latincontrolbalanced','macedonian_macedonian_controls','mandarin_mandarin_controls',
           'multiple_sclerosis_controls','natural_non-natural','neutral_neutral_controls','newage_newagecontrolbalanced',
           'parkinsons_controls','polish_polish_controls','pop_popcontrolbalanced','portuguese_portuguese_controls','postpartum_depression_controls',
           'highquality_badquality','rap_rapcontrolbalanced','reggae_reggaecontrolbalanced','rock_rockcontrolbalanced',
           'romanian_romanian_controls','russian_russian_controls','sad_sad_controls','schizophrenia_controls',
           'seventies_seventies_controls','sixties_sixties_controls','sleep_apnea_controls','soundtrack_soundtrackcontrolbalanced',
           'spanish_spanish_controls','stressed_calm','surprise_surprise_controls','swedish_swedish_controls','teens_teens_controls',
           'thirties_thirties_controls','turkish_turkish_controls','twenties_twenties_controls','vietnamese_vietnamese_controls']

try:
    os.chdir(model_dir)
except:
    print('ERROR! \n\n You need to download the meta models. \n\n Please clone the repo (git@github.com:jim-schwoebel/voicebook.git)',
      'and navigate to the chapter_3_featurization/meta_models folder, and add these models to the working directory then re-run script.')
    os.chdir(model_dir)

model_list=list()

for i in range(len(labels)):
    model_list.append(labels[i]+'.pickle')

# testing
# print(model_list)

# make a directory to load audio files in
try:
    os.chdir(load_dir)
except:
    os.mkdir(load_dir)
    os.chdir(load_dir)

listdir=os.listdir()

print('META FEAUTRIZING...')
for i in range(len(listdir)):
    try:
      if listdir[i][-5:] not in ['Store','.json']:
          if listdir[i][-4:] != '.wav':
              if listdir[i][-5:] != '.json':
                  filename=convert(listdir[i])
          else:
              filename=listdir[i]

          print(filename)

          if filename[0:-4]+'.json' not in listdir:
              
              features=featurize(filename)
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
                  classname=output
                  class_list.append(classname)

                  g=json.load(open(modelname[0:-7]+'.json'))
                  model_acc.append(g['accuracy'])
                  deviations.append(g['deviation'])
                  modeltypes.append(g['modeltype'])

              os.chdir(load_dir)

              meta_features=list()
              for i in range(len(class_list)):
                if class_list[i].find('control') or class_list[i] in ['badquality', 'fatigued', 'male', 'natural']:
                  meta_features.append(0)
                else:
                  meta_features.append(1)

              # show output in terminal 
              print('\n\n META FEATURES \n\n')
              print(meta_features)
              print('\n\n META CLASSES: \n\n')
              print(class_list)

              jsonfilename=filename[0:-4]+'.json'
              jsonfile=open(jsonfilename,'w')

              data={
                  'filename':filename,
                  'filetype':'audio file',
                  'class':class_list,
                  'model':model_list,
                  'model accuracies':model_acc,
                  'model deviations':deviations,
                  'model types':modeltypes,
                  'features':{
                              'librosa':features.tolist(),
                              'meta features': meta_features
                              },
                  'count':count,
                  'errorcount':errorcount,
                  }
              json.dump(data,jsonfile)
              jsonfile.close()
              
          count=count+1
    except:
      print('an error occurred')
      errorcount=errorcount+1
      count=count+1 



