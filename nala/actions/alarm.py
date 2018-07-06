##############################################################################
##                         STRESSLEX - ALARM.PY                            ##
##############################################################################
'''

Author: @Jim Schwoebel
Role: Chief Executive Officer
Git Repo: git@github.com:NeuroLexDiagnostics/stresslex-py.git
Script: alarm.py
Version: 1.0
License: Trade Secret 
Contact: js@neurolex.co

(C) 2018 NeuroLex Laboratories, Inc.
All rights reserved.

THIS CODE IS PROTECTED BY UNITED STATES AND INTERNATIONAL LAW. It constitutes
a TRADE SECRET possessed by NeuroLex Laboratories, Inc. If you received this
code base by error, please delete this code immediately and do not read below.
Please do not distribute this code base outside of our company.

'''
##############################################################################
##                            DESCRIPTION                                   ##
##############################################################################

'''
Alarm.py

Really simple script to play an alarm to wake up in the morning.

Then plays the weather and also some music to gradually wake up.
'''

##############################################################################
##                           IMPORT STATEMENTS                              ##
##############################################################################
import webbrowser, ftplib, platform, json, getpass, datetime 
import pygame, os, time, sys
import pyttsx3 as pyttsx

##############################################################################
##                            HELPER FUNCTIONS                              ##
##############################################################################

def playbackaudio(filename):
#takes in a question and a filename to open and plays back the audio file and prints on the screen the question for the user 
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(10)
    
    return "playback completed"

def speaktext(text):
	# speak to user from a text sample (tts system)
    engine = pyttsx.init()
    engine.setProperty('voice','com.apple.speech.synthesis.voice.fiona')
    engine.say(text)
    engine.runAndWait()

def get_date():
    return str(datetime.datetime.now())

##############################################################################
##                            MAIN SCRIPT                                   ##
##############################################################################

speaktext('it is time to wake up!')

# loop and play this alarm for 1 minute (6 loops=1minute)
playbackaudio('wakeup.wav')
playbackaudio('wakeup.wav')
playbackaudio('wakeup.wav')
playbackaudio('wakeup.wav')
playbackaudio('wakeup.wav')
playbackaudio('wakeup.wav')

# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('registration.json'))
action_log=database['action log']

action={
    'action': 'alarm.py',
    'date': get_date(),
    'meta': [],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('registration.json','w')
json.dump(database,jsonfile)
jsonfile.close()



