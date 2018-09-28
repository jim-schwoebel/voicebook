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
##               TEXT_FEATURES.PY             ##    
================================================ 

extract all text features:
nltk_features()
spacy_features()
gensim_features()

'''
import transcribe as ts
import sounddevice as sd
import soundfile as sf
import nltk_features as nf
import spacy_features as spf
import gensim_features as gf 
import numpy as np
import os, json

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

def text_featurize(filename,jsondump):
    # transcribe with sphinx 
    transcript=ts.transcribe_sphinx('test.wav')
    # now put transcript through various feature engines
    nltk_featureset, nltk_labels=nf.nltk_featurize(transcript)
    spacy_featureset, spacy_labels=spf.spacy_featurize(transcript)
    # make gensim embedding on alice and wonderland text
    # (or any text corpus you'd like)
    modelname='alice.pickle'
    if modelname not in os.listdir():
        text=open('alice.txt').read()
        gf.w2v_train(text,100,modelname)
    gensim_featureset=gf.sentence_embedding(transcript,100,modelname)

    data={
        'transcript':transcript,
        'transcript type':'sphinx',
        'nltk':np.array(nltk_featureset).tolist(),
        'spacy':np.array(spacy_featureset).tolist(),
        'gensim':np.array(gensim_featureset).tolist(),
        }
    
    if jsondump == True:
        jsonfilename=filename[0:-4]+'.json'
        jsonfile=open(jsonfilename,'w')
        json.dump(data,jsonfile)
        jsonfile.close()

    return data 

# # record and get transcript 
# if 'test.wav' not in os.listdir():
#     sync_record('test.wav', 10, 44100, 2)

# # now extract all text features
# data=text_featurize('test.wav', True)
