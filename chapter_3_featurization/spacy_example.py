'''
spacy_example.py

Example implementing spacy_features script

Compressed here and imported to allow for better
flow in textbook

315 features extracted in total.
'''
import spacy_features

# Alice’s Adventures in Wonderland = text 
transcript=open('alice.txt').read()
features, labels = spacy_featurize(transcript)
# shows feature array with labels = 315 features total 
print(features)
print(labels)
print(len(features))
print(len(labels))


