'''
fingerprint w2v models in a streaming folder,
load_dir.

'''

from gensim.models import Word2Vec
import speech_recognition as sr  
import getpass 
import numpy as np
import random, os, json
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
load_dir=cur_dir
size=100

def sentence_embedding(sentence,size,modelname):
    model=Word2Vec.load(modelname)
    sentences2=sentence.split()
    w2v_embed=list()
    for i in range(len(sentences2)):
        try:
            w2v_embed.append(model[sentences2[i]])
        except:
            pass
    out_embed=np.zeros(size)
    for j in range(len(w2v_embed)):
        out_embed=out_embed+w2v_embed[j]
    out_embed=(1/size)*out_embed
    return out_embed

def embedding(sentence, size, modelname):
    o1=sentence_embedding(sentence,size,modelname[len('w2vec_'):]+'_1.pickle')
    o2=output=sentence_embedding(sentence,size,modelname[len('w2vec_'):]+'_2.pickle')
    embedding=np.append(o1,o2)
    return embedding


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

def transcribe(wavfile):
    r = sr.Recognizer()
    # use wavfile as the audio source (must be .wav file)
    with sr.AudioFile(wavfile) as source:
        #extract audio data from the file
        audio = r.record(source)                    

    transcript=r.recognize_sphinx(audio)
    print(transcript)
    return transcript

# NOW LOAD ALL MODELS AND W2V MODELS

model_list=list()
os.chdir(model_dir)
listdir=os.listdir()

for i in range(len(listdir)):
    # this makes it portable to any w2vfile 
    i1=listdir[i].find('_sc_w2v')+len('_sc_w2v')
    if listdir[i][-10:]=='w2v.pickle' and listdir[i][0:i1]+'_1.pickle' in listdir:
        model_list.append(listdir[i])

w2v_models=list()
count=0
for i in range(len(model_list)):
    print(model_list[i][0:-7]+'.json')
    g=json.load(open(model_list[i][0:-7]+'.json'))['model']
    count=g.count('_')-1

    w2v_model=list()
    for j in range(count):
        filename=g+'_%s.pickle'%(str(j+1))
        w2v_model.append(filename)

    w2v_models.append(w2v_model)

print(w2v_models)

# NOW FEATURIZE INCOMING SAMPLE BY TRANSCRIBING AND APPLYING W2V MODELS
count=0
errorcount=0

try:
    os.chdir(load_dir)
except:
    os.mkdir(load_dir)
    os.chdir(load_dir)
    
listdir=os.listdir()
print(os.getcwd())

model_acc=list()
deviations=list()
modeltypes=list()

for i in range(len(listdir)):
    #try:
    if listdir[i][-5:] not in ['Store','.json']:
        if listdir[i][-4:] != '.wav':
            if listdir[i][-5:] != '.json':
                filename=convert(listdir[i])
        else:
            filename=listdir[i]

        print(filename)

        if filename[0:-4]+'_w2v.json' not in listdir:
            print('transcribing %s'%(filename))
            transcript=transcribe(filename)
            features_list=list()
            
            # now load all w2v models to determine array size
            class_list=list()
            for j in range(len(model_list)):
                modelname=model_list[j]

                names=list()
                
                classifier=modelname
                w2v_model=w2v_models[j]
                sentence=transcript
                embedding=np.array([])
                os.chdir(model_dir)
                
                for l in range(len(w2v_model)-1):
                    if l == 0:
                        output=sentence_embedding(sentence,size,w2v_model[l])
                        output2=sentence_embedding(sentence,size,w2v_model[l+1])
                        embedding_temp=np.append(output,output2)
                        embedding=np.append(embedding,embedding_temp)
                        #print(embedding)
                    else:
                        embedding_temp=sentence_embedding(sentence,size,w2v_model[l+1])
                        embedding=np.append(embedding,embedding_temp)
                        #print(embedding)
                    #print(l)

                features=embedding.tolist()
                features_list.append(features)

                features=np.array(features)
                loadmodel=open(modelname, 'rb')
                model = pickle.load(loadmodel)
                loadmodel.close()
                
                output=str(model.predict(features.reshape(1,-1))[0])
                print(output)
                classname=output
                class_list.append(classname)

                g=json.load(open(modelname[0:-7]+'.json'))
                
                model_acc.append(g['accuracy'])
                deviations.append(g['deviation'])
                modeltypes.append(g['modeltype'])

            os.chdir(load_dir)

            jsonfilename=filename[0:-4]+'_w2v.json'
            jsonfile=open(jsonfilename,'w')
            data={
                'filename':filename,
                'filetype':'mixed file',
                'class':class_list,
                'model':model_list,
                'w2v models':w2v_models,
                'model accuracies':model_acc,
                'model deviations':deviations,
                'model types':modeltypes,
                'transcript':transcript,
                'features':features_list,
                'count':count,
                'errorcount':errorcount,
                }
            json.dump(data,jsonfile)
            jsonfile.close()
            
        count=count+1
    #except:
    else:
        errorcount=errorcount+1
        count=count+1 

