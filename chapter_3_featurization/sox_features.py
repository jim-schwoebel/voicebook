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
##              SOX_FEATURES.PY               ##    
================================================ 

Get features using SoX library

Workaround by outputting CLI in txt file and
use function to extract these features.
'''
import os
import numpy as np   

def clean_text(text):
    text=text.lower()
    chars=['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'o','p','q','r','s','t','u','v','w','x','y','z',' ',
           ':', '(',')','-','=',"'.'"]
    for i in range(len(chars)):
        text=text.replace(chars[i],'')

    text=text.split('\n')
    new_text=list()
    # now get new text
    for i in range(len(text)):
        try:
            new_text.append(float(text[i].replace('\n','').replace('n','')))
        except:
            pass
            #print(text[i].replace('\n','').replace('n',''))
                        
    return new_text

def sox_featurize(filename):
    # soxi and stats files 
    soxifile=filename[0:-4]+'_soxi.txt'
    statfile=filename[0:-4]+'_stats.txt'
    os.system('soxi %s > %s'%(filename, soxifile))
    os.system('sox %s -n stat > %s 2>&1'%(filename, statfile))
    # get basic info 
    s1=open(soxifile).read()
    s1_labels=['channels','samplerate','precision',
               'filesize','bitrate','sample encoding']
    s1=clean_text(s1)
    
    s2=open(statfile).read()
    s2_labels=['samples read','length','scaled by','maximum amplitude',
               'minimum amplitude','midline amplitude','mean norm','mean amplitude',
               'rms amplitude','max delta','min delta','mean delta',
               'rms delta','rough freq','vol adj']
    
    s2=clean_text(s2)

    labels=s1_labels+s2_labels
    features=np.array(s1+s2)
 
    return features,labels

# features, labels = sox_featurize('test.wav')
