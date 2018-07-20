'''
text_features.py

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
