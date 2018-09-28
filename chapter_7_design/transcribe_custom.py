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
##            TRANSCRIBE_CUSTOM.PY            ##    
================================================ 

Record a short sample and get back a transcription in a loop.

This is to just show how to load a custom transcription model
inside of pocketsphinx. 
'''
import os, sys
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
import sounddevice as sd
import soundfile as sf

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

# Get all the directories right
def transcribe(sample):

    modeldir=os.getcwd()+'/data'
    # Create a decoder with certain model
    config = Decoder.default_config()
    config.set_string('-hmm', modeldir+'/en-us')
    config.set_string('-lm', modeldir+'/TAR4311/4311.lm')
    config.set_string('-dict', modeldir+'/TAR4311/4311.dic')
    decoder = Decoder(config)

    # Decode streaming data.
    decoder = Decoder(config)
    decoder.start_utt()
    stream = open(sample, 'rb')
    while True:
      buf = stream.read(1024)
      if buf:
        decoder.process_raw(buf, False, False)
      else:
        break
    decoder.end_utt()

    #print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])
    output=[seg.word for seg in decoder.seg()]
    try:
        output.remove('<s>')
        output.remove('</s>')

        transcript = ''
        for i in range(len(output)):
            if output[i] == '<sil>':
                pass 
            elif i == 0:
                transcript=transcript+output[i]
            else:
                transcript=transcript+' '+output[i]

        transcript=transcript.lower()
        print('transcript: '+transcript)
    except:
        transcript=''

    return transcript

t=1
i=0

while t>0:
    sync_record('test.wav',3,16000,1)
    transcribe('test.wav')
