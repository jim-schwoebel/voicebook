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
##                TRANSCRIBE.PY               ##    
================================================ 

Overview of how to implement various transcriptions for offline or
online applications.

Note some of these transcription methods require environment variables
to be setup (e.g. Google). 
'''
import os, json, time, datetime 
import speech_recognition as sr_audio

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')
    
def convert_audio(file):
    # convert to proper format with FFmpeg shell script 
    filename=file[0:-4]+'_temp.wav'
    command='ffmpeg -i %s -acodec pcm_s16le -ac 1 -ar 16000 %s'%(file,filename)
    os.system(command)
    return filename


def transcribe_google(file):
    # transcribe with google speech API, $0.024/minute 
    r=sr_audio.Recognizer()
    with sr_audio.AudioFile(file) as source:
        audio = r.record(source) 
    transcript=r.recognize_google_cloud(audio)
    print('google transcript: '+transcript)

    return transcript 
    
# transcribe with pocketsphinx (open-source)
def transcribe_sphinx(file):
    r=sr_audio.Recognizer()
    with sr_audio.AudioFile(file) as source:
        audio = r.record(source) 
    transcript=r.recognize_sphinx(audio)
    print('sphinx transcript: '+transcript)
    
    return transcript 
    
# transcribe with deepspeech (open-source, but can be CPU-intensive)
def transcribe_deepspeech(file):
    # get the deepspeech model installed if you don't already have it (1.6 GB model)
    # can be computationally-intensive, so make sure it works on your CPU
    if 'models' not in os.listdir():
        os.system('brew install wget')
        os.system('pip3 install deepspeech')
        os.system('wget https://github.com/mozilla/DeepSpeech/releases/download/v0.1.1/deepspeech-0.1.1-models.tar.gz')
        os.system('tar -xvzf deepspeech-0.1.1-models.tar.gz')
    # make intermediate text file and fetch transcript 
    textfile=file[0:-4]+'.txt'
    command='deepspeech models/output_graph.pb %s models/alphabet.txt models/lm.binary models/trie >> %s'%(file,textfile)
    os.system(command)
    transcript=open(textfile).read()
    print('deepspeech transcript: '+transcript)
    # remove text file 
    os.remove(textfile)
    
    return transcript 

def transcribe_all(file):
    # get transcripts from all methods and store in .json file 
    filename=convert_audio(file)

    try:
        google_transcript=transcribe_google(filename)
    except:
        google_transcript=''
    try:
        sphinx_transcript=transcribe_sphinx(filename)
    except:
        sphinx_transcript=''
    try:
        deepspeech_transcript=transcribe_deepspeech(filename)
    except:
        deepspeech_transcript=''
        
    os.remove(filename)

    # write to .json
    jsonfilename=file[0:-4]+'.json'
    jsonfile=open(jsonfilename,'w')
    data={
        'filename': file,
        'date': str(datetime.datetime.now()), 
        'transcripts': {
            'google':google_transcript,
            'sphinx':sphinx_transcript,
            'deepspeech':deepspeech_transcript}
        }
    json.dump(data,jsonfile)

    return jsonfilename
