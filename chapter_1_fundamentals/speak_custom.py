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
has >10 world experts in kafka distributed architectures, microservices 
built on top of Node.JS / Python / Docker, and applying machine learning to 
model speech and text data. 

We have helped a wide variety of enterprises - small businesses, 
researchers, enterprises, and/or independent developers. 

If you would like to work with us let us know @ js@neurolex.co. 

================================================ 
##               SPEAK_CUSTOM.PY              ##    
================================================ 

This script customizes a voice to your needs and 
outputs the default voice to a defaults.json file.

Then you can use the voice into the future by calling 
the speak_text_custom(text, voiceid, rate) function.

Pyttx3 has great documentation. You should check it out here:
https://github.com/nateshmbhat/pyttsx3
'''
import pyttsx3, time, random, json, os

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speak_text_custom(text, voiceid, rate):
    # quick function to play back text
    # gives back the time it takes to speak back 
    start=time.time()
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('voice', voiceid)
    engine.say(text)
    engine.runAndWait()
    end=time.time()

    return end-start

def select_speed():
    # quick function to select the voice speed you like
    engine = pyttsx3.init()
    rate=engine.getProperty('rate')
    likes=list()

    speak_text('I will now go a bit slower. Let me know what you think.')
    slower_rates=[rate-25, rate-50, rate-75, rate-100]

    for i in range(len(slower_rates)):
        new_rate=slower_rates[i]
        engine.setProperty('rate', new_rate)
        engine.say('The quick brown fox jumped over the lazy dog.')
        engine.runAndWait()
        like=input('did you like this voice speed (%s)? yes or no.'%(str(new_rate)))
        if like not in ['y','n','yes','no']:
            like=input('input not recognized. Did you like this voice? yes or no.')
        likes.append(new_rate)
        
    # set back to normal speed to tell user to speed up 
    engine.setProperty('rate', rate)
    speak_text('I will now speak a bit faster. Let me know what you think.')
    faster_rates=[rate, rate+25, rate+50, rate+75, rate+100]

    for i in range(len(faster_rates)):
        new_rate=faster_rates[i]
        engine.setProperty('rate', new_rate)
        engine.say('The quick brown fox jumped over the lazy dog.')
        engine.runAndWait()
        like=input('did you like this voice speed (%s)? yes or no.'%(str(new_rate)))
        if like not in ['y','n','yes','no']:
            like=input('input not recognized. Did you like this voice? yes or no.')
        likes.append(new_rate)
        
    return likes

def select_voice(rate):
    # quick function to select the voices you like
    text='The quick brown fox jumped over the lazy dog.'
    likes=list()
    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    for voice in voices:
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)
        engine.setProperty('voice', voice.id)
        engine.say(text)
        engine.runAndWait()
        
        like=input('did you like this voice (%s)? yes or no.'%(str(voice.id)))
        if like not in ['y','n','yes','no']:
            like=input('input not recognized. Did you like this voice? yes or no.')
        if like in ['y','yes']:
            likes.append(voice.id)

    return likes

def rand_select(rand_list):
    # get a random element back from list
    # we're using this to select a voice we like and a rate
    randint=random.randint(0,len(rand_list)-1)
    
    return rand_list[randint]

# implement these functions to select a voice and rate that you like
if 'defaults.json' not in os.listdir():
    # make defaults.json for future voice sessions
    speak_text('I will now adjust my speaking rate')
    rates=select_speed()
    rate=rand_select(rates)
    speak_text('I will now let you select a new voice')
    voiceids=select_voice(rate)
    voiceid=rand_select(voiceids)

    # now save these variables as a default.json file
    jsonfile=open('defaults.json','w')
    data ={
        'rate': rate,
        'rates': rates,
        'voiceid': voiceid,
        'voiceids': voiceids,
        }
    json.dump(data,jsonfile)
    jsonfile.close()

else:
    # load file if it exists 
    defaults=json.load(open('defaults.json'))
    voiceid=defaults['voiceid']
    rate=defaults['rate']

# change text as necessary
# e.g. 'the weather is currently 90 degrees outside.'
text=input('type text to speak here: \n')

# speak output text 
spoken_time=speak_text_custom(text, voiceid, rate)
print('it took %s seconds to speak this text'%(str(spoken_time)))
    
