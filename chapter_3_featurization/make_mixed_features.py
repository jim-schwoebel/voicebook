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
##           MAKE_MIXED_FEATURES.PY           ##    
================================================ 

Make some fixed features using random combinatinos of extracted
features from pyaudioanalysis and spacy. 

Mixed features are an emerging are of research; we still don't know
a lot about these types of features. Feel free to make some new 
ones and try them on your dataset!! 
'''
import pyaudio_features as pf 
import spacy_features as sf
import transcribe as ts
import random

# get features 
pyaudio_features, pyaudio_labels=pf.pyaudio_featurize('test.wav')
transcript=ts.transcribe_sphinx('test.wav')
spacy_features, spacy_labels=sf.spacy_featurize(transcript)

# relate some features to each other
# engineer 10 random features by dividing them and making new labels 
mixed_features=list()
mixed_labels=list()
for i in range(10):
    # get some random features from both text and audio 
    i1=random.randint(0,len(pyaudio_features)-1)
    label_1=pyaudio_labels[i1]
    feature_1=pyaudio_features[i1]
    i2=random.randint(0,len(spacy_features)-1)
    label_2=spacy_labels[i2]
    feature_2=spacy_features[i2]
    # make new label 
    mixed_label=label_2+' (spacy) ' + '| / | '+label_1 + ' (pyaudio)'
    print(mixed_label)
    mixed_labels.append(mixed_label)
    # make new feature from labels 
    mixed_feature=feature_2/feature_1
    print(mixed_feature)
    mixed_features.append(mixed_feature)

# Example output!! new features :)

# Xxx (spacy) | / | median chroma3 (pyaudio)
# 0.0
# ! (spacy) | / | min chroma2 (pyaudio)
# 0.0
# INTJ (spacy) | / | max chroma10 (pyaudio)
# 0.0
# # (spacy) | / | max spectral entropy (pyaudio)
# 0.0
# Xxxxx'x (spacy) | / | std mfcc12 (pyaudio)
# 0.0
# std sentence polarity (spacy) | / | mean chroma3 (pyaudio)
# 0.0
# Xx'xxxx (spacy) | / | min chroma2 (pyaudio)
# 0.0
# xxx”--xxx (spacy) | / | std mfcc5 (pyaudio)
# 0.0
# prt (spacy) | / | median spectral centroid (pyaudio)
# 6.730238582160183
# ! (spacy) | / | min chroma deviation (pyaudio)
# 0.0
