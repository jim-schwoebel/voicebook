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
##               APA_RECORD.PY                 ##    
================================================ 

Active-passive asynchronous (APA) method means that a voice sample is recorded
actively and then passively, and one of these modes is asynchronous.

In this case, we call a previous script aa_record.py with pa_record.py
to get the weather asynchronously and then record passively.

Note just one of these scripts needs to be asynchronous for the APA 
mode to take effect. Both can also be asynchronous and it would still
be an APA mode. 
'''
import os

# APA CONFIG 1 (AA → PA)
os.system('python3 aa_record.py')
os.system('python3 pa_record.py')

# APA CONFIG 2 (AS→ PA)
# os.system('python3 as_record.py')
# os.system('python3 pa_record.py')

# APA CONFIG 3 (AA→ PS)
# os.system('python3 aa_record.py')
# os.system('python3 ps_record.py')
