'''
PCA_drt.py

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

# numpy is used by everything...
import numpy as np

################################################################
##                 UNSUPERVISED TECHNIQUES                    ##
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
(3) Manifold learning 
'''

# PCA - useful for Gaussian processes
# http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html 
################################################################
from sklearn.decomposition import PCA

# put real features in here (audio features)
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(n_components=2)
pca.fit(X)
PCA(copy=True, iterated_power='auto', n_components=1, random_state=None,
  svd_solver='auto', tol=0.0, whiten=False)
print(pca.explained_variance_ratio_)  
print(pca.singular_values_)  

# ICA - useful for non-Gaussian processes / cocktail party
# http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html
################################################################
from sklearn.decomposition import FastICA

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
ica = FastICA(n_components=2)
S_ = ica.fit_transform(X)  # Reconstruct signals
A_ = ica.mixing_  # Get estimated mixing matrix

# K-means clustering - useful for speech recognition purposes
# http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html 
################################################################
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print(kmeans.labels_)
print(kmeans.predict([[0, 0], [4, 4]]))
print(kmeans.cluster_centers_)

# Canonical correlation analysis
# http://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html
################################################################
from sklearn.cross_decomposition import CCA
X = [[0., 0., 1.], [1.,0.,0.], [2.,2.,2.], [3.,5.,4.]]
Y = [[0.1, -0.2], [0.9, 1.1], [6.2, 5.9], [11.9, 12.3]]
cca = CCA(n_components=1)
cca.fit(X, Y)
CCA(copy=True, max_iter=500, n_components=1, scale=True, tol=1e-06)
X_c, Y_c = cca.transform(X, Y)

# Partial least squares regression
# http://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html
################################################################
from sklearn.cross_decomposition import PLSRegression
X = [[0., 0., 1.], [1.,0.,0.], [2.,2.,2.], [2.,5.,4.]]
Y = [[0.1, -0.2], [0.9, 1.1], [6.2, 5.9], [11.9, 12.3]]
pls2 = PLSRegression(n_components=2)
pls2.fit(X, Y)
PLSRegression(copy=True, max_iter=500, n_components=2, scale=True,
        tol=1e-06)
Y_pred = pls2.predict(X)

# Manifold learning - isomap algorithm
# http://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html 
################################################################
# (there are many types of algorithms here, just one for reference)
# check out [] for more examples
from sklearn import manifold
n_points = 1000
X, color = datasets.samples_generator.make_s_curve(n_points, random_state=0)
n_neighbors = 10
n_components = 2
t0 = time()

Y = manifold.Isomap(n_neighbors, n_components).fit_transform(X)

################################################################
##                  SUPERVISED TECHNIQUES                     ##
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
# supervised dictionary learning
# http://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html
################################################################
from sklearn.decomposition import MiniBatchDictionaryLearning

dico = MiniBatchDictionaryLearning(n_components=100, alpha=1, n_iter=500)
V = dico.fit(data).components_

# linear discriminant analysis
# http://scikit-learn.org/stable/modules/lda_qda.html
################################################################
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

lda = LinearDiscriminantAnalysis(solver="svd", store_covariance=True)
y_pred = lda.fit(X, y).predict(X)

qda = QuadraticDiscriminantAnalysis(store_covariances=True)
y_pred = qda.fit(X, y).predict(X)

# variational autoencoder (deep learning technique)
# https://blog.keras.io/building-autoencoders-in-keras.html
################################################################ 
from keras.layers import Input, Dense
from keras.models import Model

# this is the size of our encoded representations
encoding_dim = 32

# add a few dimensions for encoder and decoder 
input_img = Input(shape=(784,))
encoded = Dense(128, activation='relu')(input_img)
encoded = Dense(64, activation='relu')(encoded)
encoded = Dense(32, activation='relu')(encoded)

decoded = Dense(64, activation='relu')(encoded)
decoded = Dense(128, activation='relu')(decoded)
decoded = Dense(784, activation='sigmoid')(decoded)

