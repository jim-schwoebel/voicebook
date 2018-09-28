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
##               STORE_FTP.PY                 ##    
================================================ 

Collect a speech file and them upload it to a FTP server.

Note that this requires two environment variables:
os.environ['DOMAIN_USER']
os.environ['DOMAIN_PASSWORD']

These can be setup going to 
cd~
open .bash_profile

Then insert the domain user and password here like:
export DOMAIN_NAME='domainname'
export DOMAIN_USER='user'
export DOMAIN_PASSWORD='password'
'''
import sounddevice as sd
import soundfile as sf 
import time, os, shutil 
from ftplib import FTP

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')
    return filename 

def upload_file(file, session)
    uploadfile = open(file,'rb')
    session.storbinary('STOR %s'%(file),uploadfile,1024)
    uploadfile.close() 

# get environment variables 
domain=os.environ['DOMAIN_NAME']
username=os.environ['DOMAIN_USER']
password=os.environ['DOMAIN_PASSWORD']

# log into session
session = ftplib.FTP(domain,username,password)

# record sample (note, could loop through and record samples with while loop)
file = sync_record('test.wav',10,16000,1)

# upload to server
upload_file(file, session)
os.remove(file)

# log off server 
session.quit() 
