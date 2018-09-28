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
##                CLEAN_TEXTS.PY              ##    
================================================ 

Takes in the SMS text corpus dataset and cleans it,
outputting the texts as a .txt file that can be loaded
in and processed with textgenrnn library.

'''
import os, json

# get 55,835 messages
os.chdir('data')
data=json.load(open('smsCorpus_en_2015.03.09_all.json'))
t_messages=data['smsCorpus']['message']
messages=list()
for i in range(len(t_messages)):
    messages.append(t_messages[i]['text']['$'])

# write them to a text file for training purposes (if file doesn't exist)
if 'textmessages.txt' not in os.listdir():
    textfile=open('textmessages.txt','w')
    for i in range(len(messages)):
        # every new line is a new entry
        # skip ones that have odd characters by adding error handling 
        try:
            textfile.write(messages[i])
            textfile.write('\n')
        except:
            pass 
    textfile.close()
