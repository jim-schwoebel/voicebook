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
##           TRAIN_AUDIOREGRESSION.PY         ##    
================================================ 

Script that overviews implementation of various regression algorithms.
In this way, you can more easily get started on regression projects.

Goes through examples of:
1) linear regression
2) ridge regression
3) lasso regression
4) multi-task lasso
5) elastic net
6) multi-task elastic net
7) least-angle regression (LARS)
8) LARS lasso
9) orthogonal matching pursuit
10) bayesian ridge regression
11) automatic relevance determination
12) logistic regression
13) stochastic gradient descent
14) perceptron algorithms
15) pass-agressive algorithms
16) RANSAC
17) Theil-Sen
18) Huber Regression
19) Polynomial regression

These are the metrics for linear regression
# metrics.explained_variance_score(y_true, y_pred)	Explained variance regression score function
# metrics.mean_absolute_error(y_true, y_pred)	Mean absolute error regression loss
# metrics.mean_squared_error(y_true, y_pred[, …])	Mean squared error regression loss
# metrics.mean_squared_log_error(y_true, y_pred)	Mean squared logarithmic error regression loss
# metrics.median_absolute_error(y_true, y_pred)	Median absolute error regression loss
# metrics.r2_score(y_true, y_pred[, …])	R^2 (coefficient of determination) regression score function.

For more information about regression, feel free to read the
Scikit-learn linear model documentation here:

http://scikit-learn.org/stable/modules/linear_model.html

'''
##################################################
##               IMPORT STATMENTS               ##
##################################################

import os, json, xlsxwriter, pickle, shutil
from sklearn import linear_model
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.cross_validation import cross_val_predict
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
import numpy as np
from beautifultable import BeautifulTable

# helper function 
# eliminates redundant code 

def update_list(explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores):

	try:
		explained_variances.append(metrics.explained_variance_score(y_test,predictions))
	except:
		explained_variances.append('n/a')
	try:
		mean_absolute_errors.append(metrics.mean_absolute_error(y_test,predictions))
	except:
		mean_squared_errors.append('n/a')
	try:
		mean_squared_log_errors.append(metrics.mean_squared_log_error(y_test,predictions))
	except:
		mean_squared_log_errors.append('n/a')
	try:
		median_absolute_errors.append(metrics.median_absolute_error(y_test,predictions))
	except:
		median_absolute_errors.append('n/a')
	try:
		r2_scores.append(metrics.r2_score(y_test,predictions))
	except:
		r2_scores.append('n/a')

	return explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores

##################################################
##################################################
##              MAIN CODE BASE                  ##
##################################################
##################################################

import warnings
# numpy issues lots of warnings, so we can suppress them
warnings.filterwarnings("ignore")

# model dir 
modeldir=os.getcwd()+'/models'

# load data 
os.chdir(os.getcwd()+'/data')

name=input('what is the name of the file in /data directory you would like to analyze? \n')
i1=name.find('.json')
first=name[0:i1]
# assume binary classification
i2=first.find('_')
one=first[0:i2]
two=first[i2+1:]
g=json.load(open(name))

# get data 
aa=g[one]
co=g[two]

# prepare data into train and test tests 
# take first 104 features 
labels=list()
data=list()
for i in range(len(aa)):
	data.append(np.array(aa[i]))
	labels.append(float(0))
	
for i in range(len(co)):
	data.append(np.array(co[i]))
	labels.append(float(1))
	

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.33, random_state=42)
# 199 = len(X_train)
# 99 = len(X_test)

# metrics 
modeltypes=list()
explained_variances=list()
mean_absolute_errors=list()
mean_squared_errors=list()
mean_squared_log_errors=list()
median_absolute_errors=list()
r2_scores=list()

os.chdir(modeldir)

# make a temp folder to dump files into
foldername=one+'_'+two+'_regression'
tempdir=os.getcwd()+'/'+foldername 

try:
	os.mkdir(foldername)
	os.chdir(foldername)
except:
	shutil.rmtree(foldername)
	os.mkdir(foldername)
	os.chdir(foldername)

# metrics.explained_variance_score(y_true, y_pred)	Explained variance regression score function
# metrics.mean_absolute_error(y_true, y_pred)	Mean absolute error regression loss
# metrics.mean_squared_error(y_true, y_pred[, …])	Mean squared error regression loss
# metrics.mean_squared_log_error(y_true, y_pred)	Mean squared logarithmic error regression loss
# metrics.median_absolute_error(y_true, y_pred)	Median absolute error regression loss
# metrics.r2_score(y_true, y_pred[, …])	R^2 (coefficient of determination) regression score function.

##################################################
##               linear regression              ##
##################################################
'''
LinearRegression fits a linear model with coefficients w = (w_1, ..., w_p)
to minimize the residual sum of squares between the observed responses
in the dataset, and the responses predicted by the linear approximation.

Example:
http://scikit-learn.org/stable/modules/linear_model.html
'''
try:
	ols = linear_model.LinearRegression()
	ols.fit(X_train, y_train)
	#ols.predict(X_test, y_test)
	predictions = cross_val_predict(ols, X_test, y_test, cv=6)
	f=open('ols.pickle','wb')
	pickle.dump(ols,f)
	f.close()
except:
	print('error - ORDINARY LEAST SQUARES')

# get stats 
modeltypes.append('linear regression')
explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores = update_list(explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores)

##################################################
##              Ridge regression                ##
##################################################
'''
Ridge regression addresses some of the problems of
Ordinary Least Squares by imposing a penalty on the
size of coefficients.

The ridge coefficients minimize a penalized residual sum of squares.

Example:
http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge

'''
try:
	ridge = linear_model.Ridge(fit_intercept=True, alpha=0.0, random_state=0, normalize=True)
	ridge.fit(X_train, y_train)
	predictions = cross_val_predict(ridge, X_test, y_test, cv=6)
	f=open('ridge.pickle','wb')
	pickle.dump(ridge,f)
	f.close()
except:
	print('error - RIDGE REGRESSION')

# get stats 
modeltypes.append('ridge regression')
explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores = update_list(explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores)

##################################################
##                    LASSO                     ##
##################################################
'''
The Lasso is a linear model that estimates sparse coefficients.
It is useful in some contexts due to its tendency to prefer solutions
with fewer parameter values, effectively reducing the number of
variables upon which the given solution is dependent.

For this reason, the Lasso and its variants are fundamental
to the field of compressed sensing. Under certain conditions,
it can recover the exact set of non-zero weights
(see Compressive sensing: tomography reconstruction with L1 prior (Lasso)).

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html#sphx-glr-auto-examples-linear-model-plot-lasso-model-selection-py

'''
try:
	lasso = linear_model.Lasso(alpha = 0.1)
	lasso.fit(X_train, y_train)
	predictions = cross_val_predict(lasso, X_test, y_test, cv=6)
	f=open('lasso.pickle','wb')
	pickle.dump(lasso,f)
	f.close()
except:
	print('error - LASSO')

# get stats 
modeltypes.append('LASSO')
explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores = update_list(explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores)

##################################################
##              Multi-task LASSO                ##
##################################################
'''
The MultiTaskLasso is a linear model that estimates
sparse coefficients for multiple regression problems
jointly: y is a 2D array, of shape (n_samples, n_tasks).
The constraint is that the selected features are the same
for all the regression problems, also called tasks.

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html#sphx-glr-auto-examples-linear-model-plot-multi-task-lasso-support-py

'''
# # ONLY WORKS ON y_train that is multidimensional (one hot encoded)
# # Generate some 2D coefficients with sine waves with random frequency and phase
# mlasso = linear_model.MultiTaskLasso(alpha=0.1)
# mlasso.fit(X_train, y_train)
# predictions = cross_val_predict(mlasso, X_test, y_test, cv=6)
# accuracy = metrics.r2_score(y_test, predictions)

##################################################
##                  Elastic net                 ##
##################################################
'''
ElasticNet is a linear regression model trained with L1 and L2 prior as regularizer.
This combination allows for learning a sparse model where few of the weights are non-zero
like Lasso, while still maintaining the regularization properties of Ridge.

We control the convex combination of L1 and L2 using the l1_ratio parameter.

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html#sphx-glr-auto-examples-linear-model-plot-lasso-and-elasticnet-py

'''
# need training data 
try:
	enet = linear_model.ElasticNet()
	enet.fit(X_train, y_train)
	predictions = cross_val_predict(enet, X_test, y_test, cv=6)
	f=open('enet.pickle','wb')
	pickle.dump(enet,f)
	f.close()
except:
	print('error - ELASTIC NET')

# get stats 
modeltypes.append('elastic net')
explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores = update_list(explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores)

##################################################
##            Multi-task elastic net            ##
##################################################
'''
The MultiTaskElasticNet is an elastic-net model that estimates sparse coefficients
for multiple regression problems jointly: Y is a 2D array, of shape (n_samples, n_tasks).

The constraint is that the selected features are the same for all the regression problems,
also called tasks.

Example:
http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html
'''
# # # ONLY WORKS ON y_train that is multidimensional (one hot encoded)
# clf = linear_model.MultiTaskElasticNet()
# clf.fit(X_train, y_train)
# #print(clf.coef_)
# #print(clf.intercept_)

##################################################
##          Least angle regression (LARS)       ##
##################################################
'''
The advantages of LARS are:

-> It is numerically efficient in contexts where p >> n (i.e., when the number of dimensions is significantly greater than the number of points)
-> It is computationally just as fast as forward selection and has the same order of complexity as an ordinary least squares.
-> It produces a full piecewise linear solution path, which is useful in cross-validation or similar attempts to tune the model.
-> If two variables are almost equally correlated with the response, then their coefficients should increase at approximately the same rate. The algorithm thus behaves as intuition would expect, and also is more stable.
-> It is easily modified to produce solutions for other estimators, like the Lasso.

The disadvantages of the LARS method include:

-> Because LARS is based upon an iterative refitting of the residuals,
-> it would appear to be especially sensitive to the effects of noise.

Example:
http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lars.html
'''
try:
	lars = linear_model.Lars(n_nonzero_coefs=1)
	lars.fit(X_train, y_train)
	predictions = cross_val_predict(lars, X_test, y_test, cv=6)
	f=open('lars.pickle','wb')
	pickle.dump(lars,f)
	f.close()
except:
	print('error - LARS')

# get stats 
modeltypes.append('Least angle regression (LARS)')
explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores = update_list(explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores)

##################################################
##                 LARS LASSO                   ##
##################################################
'''
LassoLars is a lasso model implemented using the LARS algorithm,
and unlike the implementation based on coordinate_descent,
this yields the exact solution, which is piecewise linear
as a function of the norm of its coefficients.

Example:
http://scikit-learn.org/stable/modules/linear_model.html#passive-aggressive-algorithms

'''
try:
	lars_lasso = linear_model.LassoLars()
	lars_lasso.fit(X_train, y_train)
	predictions = cross_val_predict(lars_lasso, X_test, y_test, cv=6)
	f=open('lars_lasso.pickle','wb')
	pickle.dump(lars_lasso,f)
	f.close()
except:
	print('error - LARS LASSO')

# get stats 
modeltypes.append('LARS lasso')
explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores = update_list(explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores)

##################################################
##      Orthogonal Matching Pursuit (OMP)       ##
##################################################
'''
OrthogonalMatchingPursuit and orthogonal_mp implements the OMP
algorithm for approximating the fit of a linear model with
constraints imposed on the number of non-zero coefficients (ie. the L 0 pseudo-norm).

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_omp.html#sphx-glr-auto-examples-linear-model-plot-omp-py
'''
try:
	omp = linear_model.OrthogonalMatchingPursuit()
	omp.fit(X_train, y_train)
	predictions = cross_val_predict(omp, X_test, y_test, cv=6)
	f=open('omp.pickle','wb')
	pickle.dump(omp,f)
	f.close()
except:
	print('error - ORTHOGONAL MATCHING PURSUIT (OMP)')
# get stats 
modeltypes.append('orthogonal matching pursuit (OMP)')
explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores = update_list(explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores)

##################################################
##          Bayesian ridge regression           ##
##################################################
'''
The advantages of Bayesian Regression are:

-> It adapts to the data at hand.
-> It can be used to include regularization parameters in the estimation procedure.

The disadvantages of Bayesian regression include:

-> Inference of the model can be time consuming.

Example:
http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html
'''
# MULTI-DIMENSIONAL 
# clf = BayesianRidge()
# clf.fit(X_train, y_train)
# predictions = cross_val_predict(clf, X_test, y_test, cv=6)
# accuracy = metrics.r2_score(y_test, predictions)

##################################################
##      Automatic relevance determination       ## 
##################################################
'''
ARDRegression is very similar to Bayesian Ridge Regression,
but can lead to sparser weights w [1] [2]. ARDRegression poses
a different prior over w, by dropping the assumption of
the Gaussian being spherical.

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html#sphx-glr-auto-examples-linear-model-plot-ard-py
'''
# MULTI-DIMENSIONAL
# clf = ARDRegression(compute_score=True)
# clf.fit(X_train, y_train)
# predictions = cross_val_predict(clf, X_test, y_test, cv=6)
# accuracy = metrics.r2_score(y_test, predictions)

##################################################
##              Logistic regression             ##
##################################################
'''
Logistic regression, despite its name, is a linear model
for classification rather than regression. Logistic regression
is also known in the literature as logit regression,
maximum-entropy classification (MaxEnt) or the log-linear classifier.

In this model, the probabilities describing the possible outcomes
of a single trial are modeled using a logistic function.

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html#sphx-glr-auto-examples-linear-model-plot-logistic-l1-l2-sparsity-py
'''
try:
	lr = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
	lr.fit(X_train, y_train)
	predictions = cross_val_predict(lr, X_test, y_test, cv=6)
	f=open('lr.pickle','wb')
	pickle.dump(lr,f)
	f.close()
except:
	print('error - LOGISTIC REGRESSION')

# get stats 
modeltypes.append('logistic regression')
explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores = update_list(explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores)

##################################################
##      Stochastic gradient descent (SGD)       ##
##################################################
'''
Stochastic gradient descent is a simple yet very efficient
approach to fit linear models. It is particularly useful
when the number of samples (and the number of features) is very large.
The partial_fit method allows only/out-of-core learning.

The classes SGDClassifier and SGDRegressor provide functionality
to fit linear models for classification and regression using
different (convex) loss functions and different penalties.
E.g., with loss="log", SGDClassifier fits a logistic regression model,
while with loss="hinge" it fits a linear support vector machine (SVM).

Example:
http://scikit-learn.org/stable/modules/sgd.html#sgd
'''
try:
	# note you have to scale the data, as SGD algorithms are sensitive to 
	# feature scaling 
	scaler = StandardScaler()
	scaler.fit(X_train)
	X_train_2 = scaler.transform(X_train)
	X_test_2 = scaler.transform(X_test) 
	sgd = linear_model.SGDRegressor()
	sgd.fit(X_train_2, y_train)
	predictions = cross_val_predict(sgd, X_test_2, y_test, cv=6)
	f=open('sgd.pickle','wb')
	pickle.dump(sgd,f)
	f.close()
except:
 	print('error - STOCHASTIC GRADIENT DESCENT')

# get stats 
modeltypes.append('stochastic gradient descent (SGD)')
explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores = update_list(explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores)

##################################################
##          Perceptron algorithms               ## 
##################################################
'''
Multi-layer Perceptron is sensitive to feature scaling,
so it is highly recommended to scale your data.
For example, scale each attribute on the input vector X to [0, 1] or [-1, +1],
or standardize it to have mean 0 and variance 1.

Note that you must apply the same scaling to the test
set for meaningful results. You can use StandardScaler for standardization.

change the solver to 'lbfgs'. The default'adam' is a SGD-like method,
hich is effective for large & messy data but pretty useless for this kind of smooth & small data.

Example:
http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor
'''
try:
	nn = MLPRegressor(solver='lbfgs')
	nn.fit(X_train, y_train)
	predictions = cross_val_predict(nn, X_test, y_test, cv=6)
	f=open('nn.pickle','wb')
	pickle.dump(nn,f)
	f.close()
except:
	print('error - MLP REGRESSOR')

# get stats 
modeltypes.append('perceptron')
explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores = update_list(explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores)

##################################################
##          Passive-agressive algorithms        ##
##################################################
'''
The passive-aggressive algorithms are a family of algorithms
for large-scale learning. They are similar to the Perceptron
in that they do not require a learning rate. However,
contrary to the Perceptron, they include a regularization parameter C.

Example:
http://jmlr.csail.mit.edu/papers/volume7/crammer06a/crammer06a.pdf
'''
try:
	pa_regr = linear_model.PassiveAggressiveRegressor(random_state=0)
	pa_regr.fit(X_train, y_train)
	predictions = cross_val_predict(pa_regr, X_test, y_test, cv=6)
	f=open('pa_regr.pickle','wb')
	pickle.dump(pa_regr,f)
	f.close()
except:
	print('error - PASSIVE-AGGRESSIVE')

# get stats 
modeltypes.append('passive-agressive algorithm')
explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores = update_list(explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores)

##################################################
##                   RANSAC                     ## 
##################################################
'''
When in doubt, use RANSAC

RANSAC (RANdom SAmple Consensus) fits a model from random subsets of
inliers from the complete data set.

RANSAC is a non-deterministic algorithm producing only a reasonable
result with a certain probability, which is dependent on the number
of iterations (see max_trials parameter). It is typically used for
linear and non-linear regression problems and is especially popular
in the fields of photogrammetric computer vision.

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_ransac.html#sphx-glr-auto-examples-linear-model-plot-ransac-py
'''
try:
	ransac = linear_model.RANSACRegressor()
	ransac.fit(X_train, y_train)
	predictions = cross_val_predict(ransac, X_test, y_test, cv=6)
	f=open('ransac.pickle','wb')
	pickle.dump(ransac,f)
	f.close()
except:
	print('error - RANSAC')

# get stats 
modeltypes.append('RANSAC')
explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores = update_list(explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores)

##################################################
##              Theil-SEN                       ##
##################################################
'''
The TheilSenRegressor estimator uses a generalization of the median
in multiple dimensions. It is thus robust to multivariate outliers.

Note however that the robustness of the estimator decreases quickly
with the dimensionality of the problem. It looses its robustness
properties and becomes no better than an ordinary least squares
in high dimension.

Note takes a bit longer to train.

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_theilsen.html#sphx-glr-auto-examples-linear-model-plot-theilsen-py

'''
try:
	theilsen=linear_model.TheilSenRegressor(random_state=42)
	theilsen.fit(X_train, y_train)
	predictions = cross_val_predict(theilsen, X_test, y_test, cv=6)
	f=open('theilsen.pickle','wb')
	pickle.dump(theilsen,f)
	f.close()
except:
	print('error - THEILSEN')

# get stats 
modeltypes.append('Theil-Sen')
explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores = update_list(explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores)

##################################################
##              Huber Regression                ##
##################################################
'''
The HuberRegressor is different to Ridge because it applies a linear loss
to samples that are classified as outliers. A sample is classified as an
inlier if the absolute error of that sample is lesser than a certain threshold.

It differs from TheilSenRegressor and RANSACRegressor because it does not
ignore the effect of the outliers but gives a lesser weight to them.

Example:
http://scikit-learn.org/stable/auto_examples/linear_model/plot_huber_vs_ridge.html#sphx-glr-auto-examples-linear-model-plot-huber-vs-ridge-py
'''
try:
	huber = linear_model.HuberRegressor(fit_intercept=True, alpha=0.0, max_iter=100)
	huber.fit(X_train, y_train)
	predictions = cross_val_predict(huber, X_test, y_test, cv=6)
	f=open('huber.pickle','wb')
	pickle.dump(huber,f)
	f.close()
except:
	print('error - HUBER')

# get stats 
modeltypes.append('huber regression')
explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores = update_list(explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores)

##################################################
##              Polynomial Regression           ##
##################################################
'''
One common pattern within machine learning is to use linear models trained on
nonlinear functions of the data. This approach maintains the generally fast
performance of linear methods, while allowing them to fit a much wider range of data.

Example:
http://scikit-learn.org/stable/modules/linear_model.html#passive-aggressive-algorithms

'''
try:
	poly_lr = Pipeline([
					    ('poly', PolynomialFeatures(degree=5, include_bias=False)),
					    ('linreg', LinearRegression(normalize=True))
					    ])


	poly_lr.fit(X_train, y_train)
	predictions = cross_val_predict(poly_lr, X_test, y_test, cv=6)
	accuracy = metrics.r2_score(y_test, predictions)
	f=open('poly_lr.pickle','wb')
	pickle.dump(poly_lr,f)
	f.close()
except:
	print('error - POLYNOMIAL')

# get stats 
modeltypes.append('polynomial (linear regression)')
explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores = update_list(explained_variances, mean_absolute_errors, mean_squared_errors, mean_squared_log_errors, median_absolute_errors, r2_scores)

##################################################
##              Write session to .JSON          ##
##################################################

os.chdir(modeldir)

print('\n\n')
print('RESULTS: \n')

# print table in terminal 
table = BeautifulTable()
table.column_headers = ["model type", "R^2 score", "Mean Absolute Errors"]
for i in range(len(modeltypes)):
	table.append_row([modeltypes[i], str(r2_scores[i]), str(mean_absolute_errors[i])])

print(table)

filename=name[0:-5]+'.xlsx'
workbook  = xlsxwriter.Workbook(filename)
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Model type')
worksheet.write('B1', 'R^2 score')
worksheet.write('C1', 'Explained Variances')
worksheet.write('D1', 'Mean Absolute Errors')
worksheet.write('E1', 'Mean Squared Log Errors')
worksheet.write('F1', 'Median Absolute Errors')
#worksheet.write('G1', 'Mean Squared Errors')

# print the best model in terms of mean abolute error 
varnames=['ols.pickle', 'ridge.pickle', 'lasso.pickle', 'enet.pickle', 'lars.pickle', 
		  'lars_lasso.pickle','omp.pickle', 'lr.pickle','sgd.pickle', 'nn.pickle','pa_regr.pickle',
		  'ransac.pickle', 'theilsen.pickle', 'huber.pickle', 'poly_lr.pickle']

# make sure all numbers, make mae 10 (a large number, to eliminate it from the list of options)
mae=mean_absolute_errors
for i in range(len(mae)):
	if mae[i] == 'n/a':
		mae[i]=10
	else:
		mae[i]=float(mae[i])

# get minimim index and now delete temp folder, put master file in models directory 
minval=np.amin(mae)
ind=mae.index(minval)
print('%s has the lowest mean absolute error (%s)'%(modeltypes[ind], str(minval)))
# rename file 
os.chdir(tempdir)
newname= foldername+'.pickle'
print('saving file to disk (%s)...'%(newname))
os.rename(varnames[ind], newname)
# move to models directory
shutil.copy(os.getcwd()+'/'+newname, modeldir+'/'+newname)
# now delete temp folder 
os.chdir(modeldir)
shutil.rmtree(foldername)

# output stats of saved file (for analysis later)
classes=[one,two]
data={
	'model name':newname,
	'model type':modeltypes[ind],
	'stats':{
			'explained_variance':explained_variances[ind],
			'mean_absolute_error':mean_absolute_errors[ind],
			#'mean_squared_error': mean_squared_errors[ind-1],
			'mean_squared_log_error':mean_squared_log_errors[ind],
			'median_absolute_error':median_absolute_errors[ind],
			'r2_score':r2_scores[ind-1]
			},
	'classes':classes,
	}

jsonfilename=name[0:-5]+'_regression.json'
jsonfile=open(jsonfilename,'w')
json.dump(data,jsonfile)
jsonfile.close()

# output spreadsheet of results and open up for analyis
for i in range(len(modeltypes)):
	try:
		worksheet.write('A'+str(i+2), str(modeltypes[i]))
		worksheet.write('B'+str(i+2), str(r2_scores[i]))
		worksheet.write('C'+str(i+2), str(explained_variances[i]))
		worksheet.write('D'+str(i+2), str(mean_absolute_errors[i]))
		worksheet.write('E'+str(i+2), str(mean_squared_log_errors[i]))
		worksheet.write('F'+str(i+2), str(median_absolute_errors[i]))
		#worksheet.write('G'+str(i+2), str(mean_squared_errors[i]))
		
	except:
		pass

workbook.close()

os.system('open %s'%(filename))

