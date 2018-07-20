'''
make_mixed_features.py

make some fixed features using random combinatinos of extracted
features from pyaudioanalysis and spacy. 

mixed features are an emerging are of research; we still don't know
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