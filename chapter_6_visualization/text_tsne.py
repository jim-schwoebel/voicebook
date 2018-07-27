'''
text_tsne.py

t-SNE embeddings - help to visualize word representations.

Following tutorial here:
https://www.kaggle.com/jeffd23/visualizing-word-vectors-with-t-sne
'''
import pandas as pd
import numpy as np
import re, nltk, gensim
from sklearn.manifold import TSNE
import speech_recognition as sr_audio
import matplotlib.pyplot as plt

# helper funcitons 
def transcribe_pocket(filename):
    # transcribe the audio (note this is only done if a voice sample)
    try:
        r=sr_audio.Recognizer()
        with sr_audio.AudioFile(filename) as source:
            audio = r.record(source) 
        text=r.recognize_sphinx(audio)
    except:
        text=''
    print(text)
    
    return text

def tsne_plot(model):
    "Creates and TSNE model and plots it"
    labels = []
    tokens = []

    for word in model.wv.vocab:
        tokens.append(model[word])
        labels.append(word)
    
    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)

    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])
        
    plt.figure(figsize=(16, 16)) 
    for i in range(len(x)):
        plt.scatter(x[i],y[i])
        plt.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.savefig('tsne_word.png')
    plt.show()


# initialization
STOP_WORDS = nltk.corpus.stopwords.words()
transcript=open('./data/test.txt').read()
transcript=transcript.split('.')
vocabs=list()
for i in range(len(transcript)):
    vocabs.append(transcript[i].split())
vocabs=vocabs[0:-1]
# word2vec model 
model = gensim.models.Word2Vec(vocabs, min_count=1)
tsne_plot(model)

### A more selective model
##model = word2vec.Word2Vec(corpus, size=100, window=20, min_count=500, workers=4)
##tsne_plot(model)
##
### A less selective model
##model = word2vec.Word2Vec(corpus, size=100, window=20, min_count=100, workers=4)
##tsne_plot(model)

# can also get most similar words...
# model.most_similar('trump')
