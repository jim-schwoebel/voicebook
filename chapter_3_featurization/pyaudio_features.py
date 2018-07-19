'''
pyaudio_features.py

Extract 170 pyaudioanalysis features
https://github.com/tyiannak/pyAudioAnalysis

Need python 2 and 3 installed because we use python2 version
of pyaudioanalysis
'''
import os,json
import numpy as np

def stats(matrix):
    mean=np.mean(matrix)
    std=np.std(matrix)
    maxv=np.amax(matrix)
    minv=np.amin(matrix)
    median=np.median(matrix)
    output=np.array([mean,std,maxv,minv,median])
    return output

def pyaudio_featurize(file):
    # use pyaudioanalysis library to export features
    # exported as file[0:-4].json 
    os.system('python pyaudio_help.py %s'%(file))
    jsonfile=file[0:-4]+'.json'
    g=json.load(open(jsonfile))
    features=np.array(g['features'])
    # now go through all the features and get statistical features for array
    new_features=list()
    all_labels=['zero crossing rate','energy','entropy of energy','spectral centroid',
                'spectral spread', 'spectral entropy', 'spectral flux', 'spectral rolloff',
                'mfcc1','mfcc2','mfcc3','mfcc4',
                'mfcc5','mfcc6','mfcc7','mfcc8',
                'mfcc9','mfcc10','mfcc11','mfcc12',
                'mfcc13','chroma1','chroma2','chroma3',
                'chroma4','chroma5','chroma6','chroma7',
                'chroma8','chroma9','chroma10','chroma11',
                'chroma12','chroma deviation']
    labels=list()
                
    for i in range(len(features)):
        tfeature=stats(features[i])
        for j in range(len(tfeature)):
            new_features.append(tfeature[j])
            if j==0:
                labels.append('mean '+all_labels[i])
            elif j==1:
                labels.append('std '+all_labels[i])
            elif j==2:
                labels.append('max '+all_labels[i])
            elif j==3:
                labels.append('min '+all_labels[i])
            elif j==4:
                labels.append('median '+all_labels[i])
            
    new_features=np.array(new_features)
    os.remove(jsonfile)
    
    return new_features, labels
    
features, labels =pyaudio_featurize('test.wav')
