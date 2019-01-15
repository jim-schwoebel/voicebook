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
##            LIBROSA_FEATURES.PY             ##    
================================================ 

Extracts acoustic features using the LibROSA library;
saves them as mean, standard devaition, amx, min, and median
in different classes: onset, rhythm, spectral, and power categories.

Note this is quite a powerful audio feature set that can be used
for a variety of purposes. 
'''
import librosa
import numpy as np 

# get statistical features in numpy
def stats(matrix):
    mean=np.mean(matrix)
    std=np.std(matrix)
    maxv=np.amax(matrix)
    minv=np.amin(matrix)
    median=np.median(matrix)

    output=np.array([mean,std,maxv,minv,median])
    
    return output

# get labels for later 
def stats_labels(label, sample_list):
    mean=label+'_mean'
    std=label+'_std'
    maxv=label+'_maxv'
    minv=label+'_minv'
    median=label+'_median'
    sample_list.append(mean)
    sample_list.append(std)
    sample_list.append(maxv)
    sample_list.append(minv)
    sample_list.append(median)

    return sample_list

# featurize with librosa following documentation
# https://librosa.github.io/librosa/feature.html 
def librosa_featurize(filename, categorize):
    # if categorize == True, output feature categories 
    print('librosa featurizing: %s'%(filename))

    # initialize lists 
    onset_labels=list()

    y, sr = librosa.load(filename)

    # FEATURE EXTRACTION
    ######################################################
    # extract major features using librosa
    mfcc=librosa.feature.mfcc(y)
    poly_features=librosa.feature.poly_features(y)
    chroma_cens=librosa.feature.chroma_cens(y)
    chroma_cqt=librosa.feature.chroma_cqt(y)
    chroma_stft=librosa.feature.chroma_stft(y)
    tempogram=librosa.feature.tempogram(y)

    spectral_centroid=librosa.feature.spectral_centroid(y)[0]
    spectral_bandwidth=librosa.feature.spectral_bandwidth(y)[0]
    spectral_contrast=librosa.feature.spectral_contrast(y)[0]
    spectral_flatness=librosa.feature.spectral_flatness(y)[0]
    spectral_rolloff=librosa.feature.spectral_rolloff(y)[0]
    onset=librosa.onset.onset_detect(y)
    onset=np.append(len(onset),stats(onset))
    # append labels 
    onset_labels.append('onset_length')
    onset_labels=stats_labels('onset_detect', onset_labels)

    tempo=librosa.beat.tempo(y)[0]
    onset_features=np.append(onset,tempo)

    # append labels
    onset_labels.append('tempo')

    onset_strength=librosa.onset.onset_strength(y)
    onset_labels=stats_labels('onset_strength', onset_labels)
    zero_crossings=librosa.feature.zero_crossing_rate(y)[0]
    rmse=librosa.feature.rmse(y)[0]

    # FEATURE CLEANING 
    ######################################################

    # onset detection features
    onset_features=np.append(onset_features,stats(onset_strength))


    # rhythm features (384) - take the first 13
    rhythm_features=np.concatenate(np.array([stats(tempogram[0]),
                                      stats(tempogram[1]),
                                      stats(tempogram[2]),
                                      stats(tempogram[3]),
                                      stats(tempogram[4]),
                                      stats(tempogram[5]),
                                      stats(tempogram[6]),
                                      stats(tempogram[7]),
                                      stats(tempogram[8]),
                                      stats(tempogram[9]),
                                      stats(tempogram[10]),
                                      stats(tempogram[11]),
                                      stats(tempogram[12])]))
    rhythm_labels=list()
    for i in range(13):
        rhythm_labels=stats_labels('rhythm_'+str(i), rhythm_labels)

    # spectral features (first 13 mfccs)
    spectral_features=np.concatenate(np.array([stats(mfcc[0]),
                                        stats(mfcc[1]),
                                        stats(mfcc[2]),
                                        stats(mfcc[3]),
                                        stats(mfcc[4]),
                                        stats(mfcc[5]),
                                        stats(mfcc[6]),
                                        stats(mfcc[7]),
                                        stats(mfcc[8]),
                                        stats(mfcc[9]),
                                        stats(mfcc[10]),
                                        stats(mfcc[11]),
                                        stats(mfcc[12]),
                                        stats(poly_features[0]),
                                        stats(poly_features[1]),
                                        stats(spectral_centroid),
                                        stats(spectral_bandwidth),
                                        stats(spectral_contrast),
                                        stats(spectral_flatness),
                                        stats(spectral_rolloff)])) 

    spectral_labels=list()
    for i in range(13):
        spectral_labels=stats_labels('mfcc_'+str(i), spectral_labels)
    for i in range(2):
        spectral_labels=stats_labels('poly_'+str(i), spectral_labels)
    spectral_labels=stats_labels('spectral_cenroid', spectral_labels)
    spectral_labels=stats_labels('spectral_bandwidth', spectral_labels)
    spectral_labels=stats_labels('spectral_contrast', spectral_labels)
    spectral_labels=stats_labels('spectral_flatness', spectral_labels)
    spectral_labels=stats_labels('spectral_rolloff', spectral_labels)

    # power features
    power_features=np.concatenate(np.array([stats(zero_crossings),
                                         stats(rmse)]))
    power_labels=list()
    power_labels=stats_labels('zero_crossings',power_labels)
    power_labels=stats_labels('RMSE', power_labels) 

    # you can also concatenate the features
    if categorize == True:
        # can output feature categories if true 
        features={'onset':onset_features,
                  'rhythm':rhythm_features,
                  'spectral':spectral_features,
                  'power':power_features}

        labels={'onset':onset_labels,
                'rhythm':rhythm_labels,
                'spectral':spectral_labels,
                'power': power_labels}
    else:
        # can output numpy array of everything if we don't need categorizations 
        features = np.concatenate(np.array([onset_features,
                                       rhythm_features,
                                       spectral_features,
                                       power_features]))
        labels=onset_labels+rhythm_labels+spectral_labels+power_labels

    return features, labels

# features, labels =librosa_featurize('test.wav', True)
# print(len(features['power']))
# print(len(labels['power']))