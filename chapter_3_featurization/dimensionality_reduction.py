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
##        DIMENSIONALITY_REDUCTION.PY         ##    
================================================ 

Implement PCA dimensionality reduction technique;
uses sk-learn.

# read more about beginning dimensionality reduction techniques here
https://www.analyticsvidhya.com/blog/2015/07/dimension-reduction-methods/

Following tutorial here:
http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
'''

################################################################
##                 IMPORT STATEMENT                           ##
################################################################

import numpy as np
import json, os 

# load data (149 in each class)
data = json.load(open(os.getcwd()+'/data/africanamerican_controls.json'))
X= np.array(data['africanamerican'])
Y= np.array(data['controls']) 

'''
Feature output:

There are two mfcc and mfcc delta arrays, one that averages 
over 20 millisecond windows appended with one over 0.5 second windows.
In this way, there can be some heirarchy in the embedding. 

Particularly, here is the output

labels = ['mfcc1_mean_(0.02 second window)', 'mfcc1_std_(0.02 second window)', 'mfcc1_max_(0.02 second window)', 'mfcc1_min_(0.02 second window)', 
		'mfcc2_mean_(0.02 second window)', 'mfcc2_std_(0.02 second window)', 'mfcc2_max_(0.02 second window)', 'mfcc2_min_(0.02 second window)', 
		'mfcc3_mean_(0.02 second window)', 'mfcc3_std_(0.02 second window)', 'mfcc3_max_(0.02 second window)', 'mfcc3_min_(0.02 second window)', 
		'mfcc4_mean_(0.02 second window)', 'mfcc4_std_(0.02 second window)', 'mfcc4_max_(0.02 second window)', 'mfcc4_min_(0.02 second window)', 
		'mfcc5_mean_(0.02 second window)', 'mfcc5_std_(0.02 second window)', 'mfcc5_max_(0.02 second window)', 'mfcc5_min_(0.02 second window)', 
		'mfcc6_mean_(0.02 second window)', 'mfcc6_std_(0.02 second window)', 'mfcc6_max_(0.02 second window)', 'mfcc6_min_(0.02 second window)', 
		'mfcc7_mean_(0.02 second window)', 'mfcc7_std_(0.02 second window)', 'mfcc7_max_(0.02 second window)', 'mfcc7_min_(0.02 second window)', 
		'mfcc8_mean_(0.02 second window)', 'mfcc8_std_(0.02 second window)', 'mfcc8_max_(0.02 second window)', 'mfcc8_min_(0.02 second window)', 
		'mfcc9_mean_(0.02 second window)', 'mfcc9_std_(0.02 second window)', 'mfcc9_max_(0.02 second window)', 'mfcc9_min_(0.02 second window)', 
		'mfcc10_mean_(0.02 second window)', 'mfcc10_std_(0.02 second window)', 'mfcc10_max_(0.02 second window)', 'mfcc10_min_(0.02 second window)', 
		'mfcc11_mean_(0.02 second window)', 'mfcc11_std_(0.02 second window)', 'mfcc11_max_(0.02 second window)', 'mfcc11_min_(0.02 second window)', 
		'mfcc12_mean_(0.02 second window)', 'mfcc12_std_(0.02 second window)', 'mfcc12_max_(0.02 second window)', 'mfcc12_min_(0.02 second window)', 
		'mfcc13_mean_(0.02 second window)', 'mfcc13_std_(0.02 second window)', 'mfcc13_max_(0.02 second window)', 'mfcc13_min_(0.02 second window)', 
		'mfccdelta1_mean_(0.02 second window)', 'mfccdelta1_std_(0.02 second window)', 'mfccdelta1_max_(0.02 second window)', 'mfccdelta1_min_(0.02 second window)', 
		'mfccdelta2_mean_(0.02 second window)', 'mfccdelta2_std_(0.02 second window)', 'mfccdelta2_max_(0.02 second window)', 'mfccdelta2_min_(0.02 second window)', 
		'mfccdelta3_mean_(0.02 second window)', 'mfccdelta3_std_(0.02 second window)', 'mfccdelta3_max_(0.02 second window)', 'mfccdelta3_min_(0.02 second window)', 
		'mfccdelta4_mean_(0.02 second window)', 'mfccdelta4_std_(0.02 second window)', 'mfccdelta4_max_(0.02 second window)', 'mfccdelta4_min_(0.02 second window)', 
		'mfccdelta5_mean_(0.02 second window)', 'mfccdelta5_std_(0.02 second window)', 'mfccdelta5_max_(0.02 second window)', 'mfccdelta5_min_(0.02 second window)', 
		'mfccdelta6_mean_(0.02 second window)', 'mfccdelta6_std_(0.02 second window)', 'mfccdelta6_max_(0.02 second window)', 'mfccdelta6_min_(0.02 second window)', 
		'mfccdelta7_mean_(0.02 second window)', 'mfccdelta7_std_(0.02 second window)', 'mfccdelta7_max_(0.02 second window)', 'mfccdelta7_min_(0.02 second window)', 
		'mfccdelta8_mean_(0.02 second window)', 'mfccdelta8_std_(0.02 second window)', 'mfccdelta8_max_(0.02 second window)', 'mfccdelta8_min_(0.02 second window)', 
		'mfccdelta9_mean_(0.02 second window)', 'mfccdelta9_std_(0.02 second window)', 'mfccdelta9_max_(0.02 second window)', 'mfccdelta9_min_(0.02 second window)', 
		'mfccdelta10_mean_(0.02 second window)', 'mfccdelta10_std_(0.02 second window)', 'mfccdelta10_max_(0.02 second window)', 'mfccdelta10_min_(0.02 second window)', 
		'mfccdelta11_mean_(0.02 second window)', 'mfccdelta11_std_(0.02 second window)', 'mfccdelta11_max_(0.02 second window)', 'mfccdelta11_min_(0.02 second window)', 
		'mfccdelta12_mean_(0.02 second window)', 'mfccdelta12_std_(0.02 second window)', 'mfccdelta12_max_(0.02 second window)', 'mfccdelta12_min_(0.02 second window)', 
		'mfccdelta13_mean_(0.02 second window)', 'mfccdelta13_std_(0.02 second window)', 'mfccdelta13_max_(0.02 second window)', 'mfccdelta13_min_(0.02 second window)', 
		'mfcc1_mean_(0.50 second window)', 'mfcc1_std_(0.50 second window)', 'mfcc1_max_(0.50 second window)', 'mfcc1_min_(0.50 second window)', 
		'mfcc2_mean_(0.50 second window)', 'mfcc2_std_(0.50 second window)', 'mfcc2_max_(0.50 second window)', 'mfcc2_min_(0.50 second window)', 
		'mfcc3_mean_(0.50 second window)', 'mfcc3_std_(0.50 second window)', 'mfcc3_max_(0.50 second window)', 'mfcc3_min_(0.50 second window)', 
		'mfcc4_mean_(0.50 second window)', 'mfcc4_std_(0.50 second window)', 'mfcc4_max_(0.50 second window)', 'mfcc4_min_(0.50 second window)', 
		'mfcc5_mean_(0.50 second window)', 'mfcc5_std_(0.50 second window)', 'mfcc5_max_(0.50 second window)', 'mfcc5_min_(0.50 second window)', 
		'mfcc6_mean_(0.50 second window)', 'mfcc6_std_(0.50 second window)', 'mfcc6_max_(0.50 second window)', 'mfcc6_min_(0.50 second window)', 
		'mfcc7_mean_(0.50 second window)', 'mfcc7_std_(0.50 second window)', 'mfcc7_max_(0.50 second window)', 'mfcc7_min_(0.50 second window)', 
		'mfcc8_mean_(0.50 second window)', 'mfcc8_std_(0.50 second window)', 'mfcc8_max_(0.50 second window)', 'mfcc8_min_(0.50 second window)', 
		'mfcc9_mean_(0.50 second window)', 'mfcc9_std_(0.50 second window)', 'mfcc9_max_(0.50 second window)', 'mfcc9_min_(0.50 second window)', 
		'mfcc10_mean_(0.50 second window)', 'mfcc10_std_(0.50 second window)', 'mfcc10_max_(0.50 second window)', 'mfcc10_min_(0.50 second window)', 
		'mfcc11_mean_(0.50 second window)', 'mfcc11_std_(0.50 second window)', 'mfcc11_max_(0.50 second window)', 'mfcc11_min_(0.50 second window)', 
		'mfcc12_mean_(0.50 second window)', 'mfcc12_std_(0.50 second window)', 'mfcc12_max_(0.50 second window)', 'mfcc12_min_(0.50 second window)', 
		'mfcc13_mean_(0.50 second window)', 'mfcc13_std_(0.50 second window)', 'mfcc13_max_(0.50 second window)', 'mfcc13_min_(0.50 second window)', 
		'mfccdelta1_mean_(0.50 second window)', 'mfccdelta1_std_(0.50 second window)', 'mfccdelta1_max_(0.50 second window)', 'mfccdelta1_min_(0.50 second window)', 
		'mfccdelta2_mean_(0.50 second window)', 'mfccdelta2_std_(0.50 second window)', 'mfccdelta2_max_(0.50 second window)', 'mfccdelta2_min_(0.50 second window)', 
		'mfccdelta3_mean_(0.50 second window)', 'mfccdelta3_std_(0.50 second window)', 'mfccdelta3_max_(0.50 second window)', 'mfccdelta3_min_(0.50 second window)', 
		'mfccdelta4_mean_(0.50 second window)', 'mfccdelta4_std_(0.50 second window)', 'mfccdelta4_max_(0.50 second window)', 'mfccdelta4_min_(0.50 second window)', 
		'mfccdelta5_mean_(0.50 second window)', 'mfccdelta5_std_(0.50 second window)', 'mfccdelta5_max_(0.50 second window)', 'mfccdelta5_min_(0.50 second window)', 
		'mfccdelta6_mean_(0.50 second window)', 'mfccdelta6_std_(0.50 second window)', 'mfccdelta6_max_(0.50 second window)', 'mfccdelta6_min_(0.50 second window)', 
		'mfccdelta7_mean_(0.50 second window)', 'mfccdelta7_std_(0.50 second window)', 'mfccdelta7_max_(0.50 second window)', 'mfccdelta7_min_(0.50 second window)', 
		'mfccdelta8_mean_(0.50 second window)', 'mfccdelta8_std_(0.50 second window)', 'mfccdelta8_max_(0.50 second window)', 'mfccdelta8_min_(0.50 second window)', 
		'mfccdelta9_mean_(0.50 second window)', 'mfccdelta9_std_(0.50 second window)', 'mfccdelta9_max_(0.50 second window)', 'mfccdelta9_min_(0.50 second window)', 
		'mfccdelta10_mean_(0.50 second window)', 'mfccdelta10_std_(0.50 second window)', 'mfccdelta10_max_(0.50 second window)', 'mfccdelta10_min_(0.50 second window)', 
		'mfccdelta11_mean_(0.50 second window)', 'mfccdelta11_std_(0.50 second window)', 'mfccdelta11_max_(0.50 second window)', 'mfccdelta11_min_(0.50 second window)', 
		'mfccdelta12_mean_(0.50 second window)', 'mfccdelta12_std_(0.50 second window)', 'mfccdelta12_max_(0.50 second window)', 'mfccdelta12_min_(0.50 second window)', 

Or, represented simply:

mfcc 1-13 - mean, std, max, min
mfcc delta 1-13 - mean, std, max, min

for 0.020 and 0.5 second windows.
'''

################################################################
################################################################
##                 UNSUPERVISED TECHNIQUES                    ##
################################################################
################################################################
'''
Unsupervised techniques do not need to know anything about the dataset;
they are simple manipulations mathematically to compress features to
a smaller feature space.

They calculate things like variance and/or mean values of data and manipulate
the matrices to a smaller space.

Here are some common techniques:

(1) Principal component analysis (PCA)
(2) Independent component analysis (ICA)
(3) K-means clustering (vector quantization)
(4) Canonical correlation analysis 
(5) Partial least squares regression
(6) Manifold learning 

'''

################################################################
# Principal component analysis (PCA) - useful for Gaussian processes
# http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html 
################################################################
'''
PCA's main weakness is that it tends to be highly affected by outliers in the data. 
For this reason, many robust variants of PCA have been developed, many of which act to 
iteratively discard data points that are poorly described by the initial components. 
Scikit-Learn contains a couple interesting variants on PCA, including RandomizedPCA and SparsePCA, 
both also in the sklearn.decomposition submodule.
'''

from sklearn.decomposition import PCA

# calculate PCA for 50 components 
pca = PCA(n_components=50)
pca.fit(X)
X_pca = pca.transform(X)

print("PCA original shape:   ", X.shape)
print("PCA transformed shape:", X_pca.shape)

print(pca.explained_variance_ratio_)  
print(np.sum(pca.explained_variance_ratio_))


'''By using the explained_variance_ratio_, you can see that the the data is 
quite distributed, and no one component really makes up the mixture. This is 
expected, as mfcc coefficients are in different bands and represent the voice range,
meaning that we have a good, compressed feature representation for our dataset. 

array([4.36108568e-01, 2.30122532e-01, 9.30360419e-02, 3.50530237e-02,
       3.11003034e-02, 2.58828314e-02, 2.22265155e-02, 1.85299568e-02,
       1.42322686e-02, 1.24397825e-02, 9.44568239e-03, 8.88464867e-03,
       6.50330969e-03, 5.80186788e-03, 5.31114033e-03, 4.59182861e-03,
       4.34041947e-03, 3.74514144e-03, 3.38655973e-03, 2.87419155e-03,
       2.58491433e-03, 2.38243972e-03, 2.29385894e-03, 1.69828308e-03,
       1.57929416e-03, 1.45641917e-03, 1.33611976e-03, 1.23183500e-03,
       1.20274412e-03, 1.02064060e-03, 9.78714995e-04, 8.22881795e-04,
       7.62307128e-04, 7.02134801e-04, 6.61520330e-04, 5.71506430e-04,
       4.51561555e-04, 3.94488637e-04, 3.78635627e-04, 3.59457300e-04,
       3.40696332e-04, 2.69683415e-04, 2.44483556e-04, 2.22901479e-04,
       2.10448873e-04, 1.96806180e-04, 1.83114974e-04, 1.55056915e-04,
       1.36493195e-04, 1.24699968e-04])
'''

print(pca.singular_values_)  
''' Singular values are used to determine uniqueness of each variable
and directionality of variance in the dataset; useful for plotting things.
You don't really need to know much about this right now, though.'''


################################################################
# Independent component analysis (ICA)
# http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html
################################################################
'''
Useful for non-Gaussian processes / cocktail party

ICA assumes 
(1) independence of source signals; 
(2) sum of two signals tends toward a gaussian distribution more than each signal alone
(3) there is more complexity in the signal mixture than in the simplest source signal 

Useful to separate out signals in a complex mixture - for example, 
to hone in on a specific voice.
'''
from sklearn.decomposition import FastICA

ica = FastICA(n_components=50)
S_ = ica.fit_transform(X)  # Reconstruct signals

# The mixing matrix is analagous to PCA singular values
A_ = ica.mixing_  # Get estimated mixing matrix


################################################################
# K-means clustering ('vector quantization')
# http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html 
################################################################
'''
Example: http://scikit-learn.org/stable/auto_examples/text/document_clustering.html
- useful for speech recognition purposes
- useful to reconstruct datasets that have incomplete data (with .predict)
'''
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=50, random_state=0).fit_transform(X)

# can predict as well and get cluster centers...
# print(kmeans.labels_)
# print(kmeans.predict(X)
# print(kmeans.cluster_centers_)

################################################################
# Canonical correlation analysis
# http://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html
################################################################
'''
Uses information from two groups of data to best fit and transform this data.

Creates a new matrix in X and Y directions with dimensionality N, 50 
(if 50 clusters).
'''
from sklearn.cross_decomposition import CCA
cca = CCA(n_components=50).fit(X, Y).transform(X, Y)
new_X=cca[0]
new_Y=cca[1]

# if missing values 
# Y_pred=cca.predict(xval)

################################################################
# Partial least squares regression
# http://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html
################################################################
from sklearn.cross_decomposition import PLSRegression
pls = PLSRegression(n_components=50).fit(X, Y).transform(X, Y)
pls_X=pls[0]
pls_Y=pls[1]

# if missing values 
#Y_pred = pls2.predict(X)

################################################################
# Manifold learning - isomap algorithm
# http://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html 
################################################################
# (there are many types of algorithms here, just one for reference)
# check out [] for more examples
from sklearn import manifold

# make new dimensions for X and Y 
manifold_X = manifold.Isomap(10, 50).fit_transform(X)
manifold_Y = manifold.Isomap(10,50).fit_transform(Y)


################################################################
################################################################
##                  SUPERVISED TECHNIQUES                     ##
################################################################
################################################################
'''
Supervised dimensionality reduction techniques use some of the
data from the original feature set in order to extract patterns
and then reduce dimensionality

Here, there are three common techniques outlined:

(1) supervised dictionary learning
(2) linear discriminant analysis
(3) variational autoencoder
'''

# ################################################################
# supervised dictionary learning (SDL)
# http://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html
################################################################
'''
Takes a bit longer to execute, but has pros listed on table. 
'''
from sklearn.decomposition import MiniBatchDictionaryLearning
dico_X = MiniBatchDictionaryLearning(n_components=50, alpha=1, n_iter=500).fit_transform(X)
dico_Y = MiniBatchDictionaryLearning(n_components=50, alpha=1, n_iter=500).fit_transform(Y)

################################################################
# linear discriminant analysis (LDA)
# http://scikit-learn.org/stable/modules/lda_qda.html
################################################################
'''
Unlike PCA, LDA tries to reduce dimensions of the feature set while 
retaining the information that discriminates output classes. 

PCA reduces dimensions by focusing on the data with the most variations. 
This is useful for the high dimensional data because PCA helps us to draw a simple XY plot.

But we'll use LDA when we're interested maximizing the separability of the 
data so that we can make the best decisions. In other words, 
though LDA (supervised) is similar to PCA (unsupervised), 
but LDA focuses on maximizing the separability among known categories.

This is useful for things like phoneme detection in speech recognition projects.
'''
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA 
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis as QDA
from sklearn.model_selection import train_test_split

# make a train set and train labels 
Z=np.array(list(X)+list(Y))
newlabels=list()
for i in range(len(X)):
	newlabels.append('1')
for i in range(len(Y)):
	newlabels.append('0')

X_train, X_test, y_train, y_test = train_test_split(Z, newlabels, test_size=0.33, random_state=42)

lda = LDA(n_components=50).fit(X_train, y_train).transform(X)

################################################################ 
# variational autoencoder (deep learning technique)
# https://blog.keras.io/building-autoencoders-in-keras.html
################################################################ 
from keras.layers import Input, Dense
from keras.models import Model
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# preprocess labels (make into integers)
label_encoder = LabelEncoder()
y_train=label_encoder.fit_transform(y_train)
y_test=label_encoder.fit_transform(y_test)

# this is the size of our encoded representations (208 features in X)
encoding_dim = 32

# add a few dimensions for encoder and decoder 
input_dim = Input(shape=X_train[0].shape)
encoder=Dense(encoding_dim, activation='tanh')

autoencoder = Model(input_dim, decoded)

# this model maps an input to its encoded representation
encoder = Model(input_dim, encoded)

# create a placeholder for an encoded (50-dimensional) input
encoded_input = Input(shape=(encoding_dim,))
# retrieve the last layer of the autoencoder model
decoder_layer = autoencoder.layers[-1]
# create the decoder model
decoder = Model(encoded_input, decoder_layer(encoded_input))

# now train autoencoder 
autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')
autoencoder.fit(X_train, y_train,
                epochs=50,
                batch_size=256,
                shuffle=True,
                validation_data=(X_test, y_test))

# predict emebddings
encoded_audio = encoder.predict(X_test)
decoded_audio = decoder.predict(encoded_audio)
