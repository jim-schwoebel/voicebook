'''
gensim_featurize.py

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

# load alice and wonderland corpus and build w2v model
text=open('alice.txt').read()
transcript='I had a great time at the bar today.'
modelname='alice.pickle'
w2v_train(text,100,modelname)
features=sentence_embedding(transcript, 100,modelname)
print(features)
print(len(features))
