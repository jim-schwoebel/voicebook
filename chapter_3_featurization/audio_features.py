'''

'''
import librosa_features as lf 
import pyaudio_features as pf 
import sox_features as sf
import audioset_features as af
import numpy as np 

def audio_featurize(filename, jsondump):
    # extract features, go back to this directory everytime 
    curdir=os.getcwd()
    pyaudio_features, pyaudio_labels = pf.pyaudio_featurize(filename)
    os.chdir(curdir)
    librosa_features=lf.librosa_featurize(filename, False)
    os.chdir(curdir)
    sox_features, sox_labels = sf.sox_featurize(filename)
    os.chdir(curdir)
    audioset_allfeatures, audioset_features =audioset_featurize(filename)
    os.chdir(curdir)

    features={
        'pyaudio':pyaudio_features.tolist(),
        'librosa':librosa_features.tolist(),
        'sox':sox_features.tolist(),
        'audioset':audioset_features.tolist(),
        }
    # now make an array with all these features 
    data={
        'filename':filename,
        'features':features,
        }

    # dump to .json database
    if jsondump==True:
        jsonfilename=filename[0:-4]+'.json'
        jsonfile=open(jsonfilename,'w')
        jsonfile.write(data, jsonfile)
        jsonfile.close()

    return data

data=audio_featurize('test.wav')
#print(data)
    
    
