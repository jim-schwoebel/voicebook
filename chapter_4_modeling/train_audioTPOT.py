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
##             TRAIN_AUDIOTPOT.PY             ##    
================================================ 

Auto optimize the parameters for a classification model.

Follows TPOT documentation
https://github.com/EpistasisLab/tpot
'''
import json, os
import numpy as np
from tpot import TPOTClassifier
from tpot import TPOTRegressor
from sklearn.model_selection import train_test_split

## initialize directories and classes
model_dir=os.getcwd()+'/models/'
data_dir=os.getcwd()+'/data/'

os.chdir(data_dir)
mtype=input('classification (c) or regression (r) problem? \n').lower().replace(' ','')
while mtype not in ['c','r', 'classification','regression']:
    print('input not recognized')
    mtype=input('is this classification (c) or regression (r) problem? \n').lower().replace(' ','')

one=input('what is the name of class 1? \n')
two=input('what is the name of class 2? \n')

jsonfile=one+'_'+two+'.json'

try:
    g=json.load(open(jsonfile))
    one=g[one]
    two=g[two]
    os.chdir(model_dir)

    # now preprocess data 
    alldata=list()
    for i in range(len(one)):
        alldata.append(one[i])
    for i in range(len(two)):
        alldata.append(two[i])
        
    labels=list()
    for i in range(len(one)):
        labels.append(0)
    for i in range(len(two)):
        labels.append(1)

    alldata=np.asarray(alldata)
    labels=np.asarray(labels)

    # get train and test data 
    X_train, X_test, y_train, y_test = train_test_split(alldata, labels, train_size=0.750, test_size=0.250)
    if mtype in [' classification', 'c']:
        tpot=TPOTClassifier(generations=5, population_size=50, verbosity=2, n_jobs=-1)
        tpotname='%s_tpotclassifier.py'%(jsonfile[0:-5])
    elif mtype in ['regression','r']:
        tpot = TPOTRegressor(generations=5, population_size=20, verbosity=2)
        tpotname='%s_tpotregression.py'%(jsonfile[0:-5])
    tpot.fit(X_train, y_train)
    accuracy=tpot.score(X_test,y_test)
    tpot.export(tpotname)

    # export data to .json format 
    data={
        'data': alldata.tolist(),
        'labels': labels.tolist(),
    }

    jsonfilename='%s_.json'%(tpotname[0:-3])
    jsonfile=open(jsonfilename,'w')
    json.dump(data,jsonfile)
    jsonfile.close()

    # now edit the file and run it 
    g=open(tpotname).read()
    g=g.replace("import numpy as np", "import numpy as np \nimport json, pickle")
    g=g.replace("tpot_data = pd.read_csv(\'PATH/TO/DATA/FILE\', sep=\'COLUMN_SEPARATOR\', dtype=np.float64)","g=json.load(open('%s'))\ntpot_data=g['labels']"%(jsonfilename))
    g=g.replace("features = tpot_data.drop('target', axis=1).values","features=g['data']\n")
    g=g.replace("tpot_data['target'].values", "tpot_data")
    g=g.replace("results = exported_pipeline.predict(testing_features)", "print('saving classifier to disk')\nf=open('%s','wb')\npickle.dump(exported_pipeline,f)\nf.close()"%(jsonfilename[0:-6]+'.pickle'))
    g1=g.find('exported_pipeline = ')
    g2=g.find('exported_pipeline.fit(training_features, training_target)')
    modeltype=g[g1:g2]
    os.remove(tpotname)
    t=open(tpotname,'w')
    t.write(g)
    t.close()
    os.system('python3 %s'%(tpotname))

    # now write an accuracy label 
    os.remove(jsonfilename)

    jsonfilename='%s.json'%(tpotname[0:-3])
    print('saving .JSON file (%s)'%(jsonfilename))
    jsonfile=open(jsonfilename,'w')
    if mtype in ['classification', 'c']:
        data={
            'model name':jsonfilename[0:-5]+'.pickle',
            'accuracy':accuracy,
            'model type':'TPOTclassification_'+modeltype,
        }
    elif mtype in ['regression', 'r']:
        data={
            'model name':jsonfilename[0:-5]+'.pickle',
            'accuracy':accuracy,
            'model type':'TPOTregression_'+modeltype,
        }

    json.dump(data,jsonfile)
    jsonfile.close()
                        
except:    
    print('error, please put %s in %s'%(jsonfile, data_dir))
    print('note this can be done with train_audioclassify.py script')

