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
##              NUMPY_COMMANDS.PY             ##    
================================================ 

Quick overview of some basic numpy commands.

Although this was done in the IDLE3 window, I have commented
out those sections so you can follow along.
'''
import numpy as np

# convert a list into an array 
g=[5,2,61,1]
type(g)
g=np.array(g)
type(g)

# index an array 
g[0]

# serialize array data into .json database
# note you need to make numpy data into a list before allowing it to be
# stored in .JSON 
import json

data={
    'data':g.tolist(),
    }
jsonfile=open('test.json','w')
json.dump(data,jsonfile)
jsonfile.close()

# load .json data and make the list back into a numpy array 
newdata=json.load(open('test.json'))
numpydata=np.array(newdata['data'])
type(numpydata)
print(numpydata)

# get shape and size of numpy array
numpydata.shape
numpydata.size

# get mean, std, min, and max of numpy array 
np.mean(numpydata)
np.std(numpydata)
np.amin(numpydata)
np.amax(numpydata)

# make zeros 
makezeros=np.zeros(5)
print(makezeros)

# array operations (add, subtract, multiply by scalar)
A=np.zeros(4)
# add
print(A+numpydata)
# substract
print(A-np.array([2,-1,5,8]))
# multiply by scalar 
print(5*numpydata)
