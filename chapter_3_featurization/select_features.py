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
##              SELECT_FEATURES.PY            ##    
================================================ 

Select the most relevant features.

Examples include:

(1) Filter method - Chi squared
(2) Wrapper method - Recursive feature elimination
(3) Embedded method - LASSO

Additional models can be read here:
https://towardsdatascience.com/why-how-and-when-to-apply-feature-selection-e9c69adfabf2

'''
import os, json
import numpy as np

# load data 
data = json.load(open(os.getcwd()+'/data/africanamerican_controls.json'))
X=np.array(data['africanamerican'])
Y=np.array(data['controls'])
training=list()
for i in range(len(X)):
	training.append(X[i])
for i in range(len(Y)):
	training.append(Y[i])

# get labels (as binary class outputs)
labels=list()
for i in range(len(X)):
    labels.append(1)
for i in range(len(Y)):
    labels.append(0)

#########################################################
##                  Chi Square test                    ##
#########################################################
'''
This score can be used to select the n_features features with the 
highest values for the test chi-squared statistic from X, which must 
contain only non-negative features such as booleans or frequencies 
(e.g., term counts in document classification), relative to the classes.

Recall that the chi-square test measures dependence between stochastic variables, 
so using this function “weeds out” the features that are the most 
likely to be independent of class and therefore irrelevant for classification.

http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html
'''
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(training, labels, test_size=0.20, random_state=42)
X_train=np.array(X_train)
X_test=np.array(X_test)
y_train=np.array(y_train).astype(int)
y_test=np.array(y_test).astype(int)

# normalize features so they are non-negative [0,1], or chi squared test will fail
# it assumes all values are positive 
min_max_scaler = preprocessing.MinMaxScaler()
chi_train = min_max_scaler.fit_transform(X_train)
chi_labels = y_train 

# Select 50 features with highest chi-squared statistics
chi2_selector = SelectKBest(chi2, k=50)
X_kbest = chi2_selector.fit_transform(chi_train, chi_labels)


#########################################################
##           Recursive feature elimination             ##
#########################################################
'''
Recursive feature elmination works by recursively removing 
attributes and building a model on attributes that remain. 
It uses model accuracy to identify which attributes
(and combinations of attributes) contribute the most to predicting the
target attribute. You can learn more about the RFE class in
the scikit-learn documentation.
'''
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.svm import SVR

model = LogisticRegression() 
rfe = RFE(model, 50)
fit = rfe.fit(X_train, y_train)

# list out number of features and selected features 
print("Num Features: %d"% fit.n_features_) 
print("Selected Features: %s"% fit.support_) 
print("Feature Ranking: %s"% fit.ranking_)

#########################################################
##                   LASSO technique                   ##
#########################################################
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel

'''
Reconstruction with L1 (Lasso) penalization
the best value of alpha can be determined using cross validation
with LassoCV

http://scikit-learn.org/stable/modules/feature_selection.html#l1-feature-selection
https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/
'''

lsvc = LinearSVC(C=0.01, penalty="l1", dual=False).fit(X_train, y_train)
model = SelectFromModel(lsvc, prefit=True)
X_new = model.transform(X_train)
print(X_new.shape)
# (238, 208) --> (238, 22), dramatic reduction of features using LASSO
