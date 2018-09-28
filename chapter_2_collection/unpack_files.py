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
##               UNPACK_FILES.PY              ##    
================================================ 

This unpacks any .zip file that stored either .OPUS or .FLAC files.
Then, the files are converted back into .WAV format.

This should make it easier for you to analyze with python libraries,
as most python libraries prefer the .WAV format. 
'''
import zipfile, os, shutil

def unzip(file):
    filepath=os.getcwd()+'/'+file
    folderpath=os.getcwd()+'/'+file[0:-4]
    zip = zipfile.ZipFile(filepath)
    zip.extractall(path=folderpath)

def convert_wav(opusdir):
    curdir=os.getcwd()
    listdir=os.listdir()
    removedfiles=list()

    for i in range(len(listdir)):
        file=listdir[i]
        newfile=file[0:-5]+'.wav'
        if file[-5:] in ['.opus','.flac']:
            if file[-5:]=='.flac':
                os.system('ffmpeg -i %s %s'%(file, newfile))
                os.remove(file)
            elif file[-5:]=='.opus':
                # copy file to opus encoding folder 
                print(file)
                shutil.copy(curdir+'/'+file, opusdir+'/'+file)
                os.chdir(opusdir)
                # encode with opus codec 
                os.system('opusdec %s %s'%(file,newfile))
                shutil.copy(opusdir+'/'+newfile, curdir+'/'+newfile)
                # delete files in opus folder 
                os.remove(file)
                os.remove(newfile)
                # delete .wav file in original dir 
                os.chdir(curdir)
                os.remove(file)

# extract zip file into 'recordings' folder
unzip('recordings.zip')
# now cd into this folder and convert files to wav format
opusdir=os.getcwd()+'/opustools'
os.chdir('recordings')
print(os.listdir())
convert_wav(opusdir)


