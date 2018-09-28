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
##            GENSIM_FEATURES.PY              ##    
================================================ 
Use gensim to make a word2vec model and then use this model
to featurize a string of text.
'''
import os
import numpy as np 
from gensim.models import Word2Vec

def w2v_train(textlist,size,modelname):
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

    return out_embed

# EXAMPLE:
# load alice and wonderland corpus and build w2v model
# text=open('alice.txt').read()
# transcript='I had a great time at the bar today.'
# modelname='alice.pickle'
# w2v_train(text,100,modelname)
# features=sentence_embedding(transcript, 100,modelname)
# print(features)
# print(len(features))
