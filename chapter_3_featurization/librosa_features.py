'''
librosa_features.py

extracts acoustic features using the librosa library;
saves them as mean, standard devaition, amx, min, and median
in different classes:
onset, rhythm, spectral, and power categories.

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

# featurize with librosa following documentation
# https://librosa.github.io/librosa/feature.html 
def librosa_featurize(filename, categorize):
    # if categorize == True, output feature categories 
    print('librosa featurizing: %s'%(filename))

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
    tempo=librosa.beat.tempo(y)[0]
    onset_features=np.append(onset,tempo)
    onset_strength=librosa.onset.onset_strength(y)
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

    # power features
    power_features=np.concatenate(np.array([stats(zero_crossings),
                                         stats(rmse)])) 

    # you can also concatenate the features
    if categorize == True:
        # can output feature categories if true 
        features={'onset':onset_features,
                  'rhythm':rhythm_features,
                  'spectral':spectral_features,
                  'power':power_features}
    else:
        # can output numpy array of everything if we don't need categorizations 
        features = np.concatenate(np.array([onset_features,
                                       rhythm_features,
                                       spectral_features,
                                       power_features]))

    return features

features=librosa_featurize('test.wav', False)
