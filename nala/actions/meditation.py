
##############################################################################
##                         STRESSLEX - MEDITATION.PY                        ##
##############################################################################

'''
Author: @Jim Schwoebel
Role: Chief Executive Officer
Git Repo: git@github.com:NeuroLexDiagnostics/stresslex-py.git
Script: grateful.py
Version: 0.90
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

Meditation is known to help alleviate stress. In this action, we guide the 
user through a 60 second meditation to breathe deeply in and out.


'''

##############################################################################
##                            IMPORT STATEMENTS                             ##
##############################################################################

import time, pygame, datetime, webbrowser, ftplib, getpass, os, importlib
import random, platform, json, sys

##############################################################################
##                            HELPER FUNCTIONS                              ##
##############################################################################

def playbackaudio(question,filename):
#takes in a question and a filename to open and plays back the audio file and prints on the screen the question for the user 
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(0.5)
    print(question)
    return "playback completed"

def get_date():
    return str(datetime.datetime.now())

##############################################################################
##                            MAIN SCRIPT.                                  ##
##############################################################################

webbrowser.open('http://actions.neurolex.co/uploads/meditate.png')
time.sleep(3)

playbackaudio("Starting meditation", "startmeditation.mp3")

time.sleep(5)

for i in range(6):
    playbackaudio("Breathe in, deeply", "breathein.mp3")
    time.sleep(5)
    playbackaudio("Breathe out, deeply", "breatheout.mp3")
    time.sleep(5)

webbrowser.open('http://actions.neurolex.co/uploads/exit2.png')
time.sleep(2)

# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('registration.json'))
action_log=database['action log']

action={
    'action': 'meditation.py',
    'date': get_date(),
    'meta': ['60 seconds'],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('registration.json','w')
json.dump(database,jsonfile)
jsonfile.close()

