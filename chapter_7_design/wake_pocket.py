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
##              WAKE_POCKET.PY                ##    
================================================ 

Use PocketSphinx as a wakeword detector.

Run the app, if detection doesn’t seem to work well,
adjust kws_threshold in step 2 to give optimal results.

Following tutorial here:
https://github.com/nicholasjconn/python-always-listening/blob/master/always_listening.py
https://blog.fossasia.org/hotword-detection-with-pocketsphinx/ 
'''
import os, pyaudio, pyttsx3 
from pocketsphinx import *

def speak():
    engine = pyttsx3.init()
    engine.say("hello!!")
    engine.runAndWait() 

def pocket_detect(key_phrase):
    """ Starts a thread that is always listening for a specific key phrase. Once the
        key phrase is recognized, the thread will call the keyphrase_function. This
        function is called within the thread (a new thread is not started), so the
        key phrase detection is paused until the function returns.
    :param keyphrase_function: function that is called when the phrase is recognized
    :param key_phrase: a string for the key phrase
    """
    modeldir = os.path.dirname(pocketsphinx.__file__)+'/model'

    # Create a decoder with certain model
    config = pocketsphinx.Decoder.default_config()
    # config.set_string('-hmm', os.path.join(modeldir, 'en-us/en-us'))
    config.set_string('-dict', modeldir+'/cmudict-en-us.dict')
    config.set_string('-hmm', os.path.join(modeldir, 'en-us'))
    config.set_string('-keyphrase', key_phrase)
    config.set_float('-kws_threshold', 1)

    # Start a pyaudio instance
    p = pyaudio.PyAudio()
    # Create an input stream with pyaudio
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    # Start the stream
    stream.start_stream()

    # Process audio chunk by chunk. On keyword detected perform action and restart search
    decoder = pocketsphinx.Decoder(config)
    decoder.start_utt()
    # Loop forever
    while True:
        # Read 1024 samples from the buffer
        buf = stream.read(1024)
        # If data in the buffer, process using the sphinx decoder
        if buf:
            decoder.process_raw(buf, False, False)
        else:
            break
        # If the hypothesis is not none, the key phrase was recognized
        if decoder.hyp() is not None:
            keyphrase_function(keyword)
            # Stop and reinitialize the decoder
            decoder.end_utt()
            decoder.start_utt()
            speak()
            break 

def keyphrase_function(keyword):
    """ Dummy function that prints a notification when the key phrase is recognized.
    """
    print("Keyword %s detected!"%(keyword))

keyword='test'
pocket_detect(keyword)
