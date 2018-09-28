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
##              VISUALIZEMODELS.PY            ##    
================================================ 
Load all model accuracies, names, and standard deviations
and output them in a spreadsheet.

This is intended for any model file directory using the following scripts:

train_audioclassify.py
train_textclassify.py
train_audiotextclassify.py
train_w2vclassify.py

In this way, if you train a lot of models you can quickly get a summary of 
all of them. 
'''

import json, os, xlsxwriter

os.chdir(os.getcwd()+'/models')

listdir=os.listdir()

names=list()
accs=list()
stds=list()
modeltypes=list()

for i in range(len(listdir)):
    if listdir[i][-5:]=='.json':
        try:
            g=json.load(open(listdir[i]))
            acc=g['accuracy']
            name=g['model']
            std=g['deviation']
            modeltype=g['modeltype']

            names.append(name)
            accs.append(acc)
            stds.append(std)
            modeltypes.append(modeltype)
        except:
            print('error %s'%(listdir[i]))


workbook = xlsxwriter.Workbook('summary.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Model Name')
worksheet.write('B1', 'Accuracy')
worksheet.write('C1', 'Standard Deviation')
worksheet.write('D1', 'Modeltype')

for j in range(len(names)):
    worksheet.write('A%s'%(str(j+2)), names[j])
    worksheet.write('B%s'%(str(j+2)), accs[j])
    worksheet.write('C%s'%(str(j+2)), stds[j])
    worksheet.write('D%s'%(str(j+2)), modeltypes[j])

workbook.close()

os.system('open %s'%(os.getcwd()+'/summary.xlsx'))
