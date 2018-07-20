
'''
audioset_features.py

Simple script to extract features using the VGGish model released by google.

follows instructions from
https://github.com/tensorflow/models/tree/master/research/audioset

'''
################################################################################
##                         IMPORT STATEMENTS                                 ##
################################################################################

import os, shutil, json 
import sounddevice as sd
import soundfile as sf
import numpy as np
import tensorflow as tf

################################################################################
##                         HELPER FUNCTIONS                                  ##
################################################################################

# define some initial helper functions 
def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

def setup_audioset(curdir):
    # Upgrade pip first.
    os.system('sudo python3 -m pip install --upgrade pip')

    # Install dependences. Resampy needs to be installed after NumPy and SciPy
    # are already installed.
    os.system('sudo pip3 install numpy scipy')
    os.system('sudo pip3 install resampy tensorflow six')

    # Clone TensorFlow models repo into a 'models' directory.
    os.system('git clone https://github.com/tensorflow/models.git')
    os.chdir(curdir+'/models/research/audioset')
    # add modified file in the current folder 
    os.remove('vggish_inference_demo.py')
    shutil.copy(curdir+'/vggish_inference_demo.py', os.getcwd()+'/vggish_inference_demo.py')

    # Download data files into same directory as code.
    os.system('curl -O https://storage.googleapis.com/audioset/vggish_model.ckpt')
    os.system('curl -O https://storage.googleapis.com/audioset/vggish_pca_params.npz')

    # Installation ready, let's test it.
    # If we see "Looks Good To Me", then we're all set.
    os.system('python3 vggish_smoke_test.py')

    # copy back into main directory and delete unnecessary models 
    shutil.copytree(curdir+'/models/research/audioset/', curdir+'/audioset')
    shutil.rmtree(curdir+'/models')
    
    # go back to main directory
    os.chdir(curdir)
    
def audioset_featurize(filename):
    # textfile definition to dump terminal outputs
    jsonfile=filename[0:-4]+'.json'
    # audioset folder
    curdir=os.getcwd()
    os.chdir(curdir+'/audioset')
    os.system('python3 vggish_inference_demo.py --wav_file %s/%s'%(curdir, filename))
    # now reference this .JSON file
    os.chdir(os.getcwd()+'/processdir')
    datafile=json.load(open(jsonfile))
    print(list(datafile))
    features=datafile['features']

    # GET MEAN FEATURES 

    # initialize numpy array to add features into
    new_features_mean=np.zeros(len(features[0]))
    for i in range(len(features)):
        new_features_mean=new_features+np.array(features[i])

    # now take mean of all these features 
    new_features_mean=(1/len(features))*new_features

    # GET STD FEATURES
    new_features_std=list()
    for i in range(len(features[0])):
        # i=element in array to std 
        tlist=list()
        for j in range(len(features)):
            tlist.append(features[j][i])
        feature=np.array(tlist)
        std_feature=np.std(feature)
        new_features_std.append(std_feature)
    new_features_std=np.array(new_features_std)

    # append new features into mean and std 
    new_features=np.append(new_features_mean, new_features_std)

    # output VGGish feature array and compressed means/stds 

    return features, new_features 

################################################################################
##                               MAIN SCRIPT                                  ##
################################################################################

# get current directory 
curdir=os.getcwd()

# download audioset files if audioset not in current directory 
if 'audioset' not in os.listdir():
    try:
        setup_audioset(curdir)
    except:
        print('there was an error installing audioset')

# record a 10 second, mono 16k Hz audio file in the current directory
sync_record('test2.wav',10,16000,1)

# now let's featurize an audio sample in the current directory, test.wav 
features=audioset_featurize('test.wav')
print(features)    




    
