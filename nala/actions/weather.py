##############################################################################
##                         STRESSLEX - WEATHER.PY                           ##
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
Get weather. Intended to be run as an action upon boot process. 

This is following the tutorial found here: https://www.dataquest.io/blog/web-scraping-tutorial-python/

Thus, it depends on the weather.gov website being up and running for it to pull forecast and that internet
connection exists.

'''

##############################################################################
##                           IMPORT STATEMENTS                              ##
##############################################################################

import requests, time, datetime, ftplib, platform, json, getpass, os, sys
from bs4 import BeautifulSoup
import pyttsx3 as pyttsx

##############################################################################
##                            HELPER FUNCTIONS                              ##
##############################################################################


def connected_to_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

def speaktext(text):
    # speak to user from a text sample (tts system)
    engine = pyttsx.init()
    engine.setProperty('voice','com.apple.speech.synthesis.voice.fiona')
    engine.say(text)
    engine.runAndWait()

def curloc():
    
    # get current location, limit 1000 requests/day
    
    r=requests.get('http://ipinfo.io')
    location=r.json()
    
    return location

def get_date():
    return str(datetime.datetime.now())

##############################################################################
##                            MAIN SCRIPT                                   ##
##############################################################################

internet_access=connected_to_internet()

if internet_access==True:

    # get location to know what URL to pull
    location=curloc()
    all_loc_data=location
    city=location['city']
    coords=location['loc'].split(',')
    latitude=coords[0]
    longitude=coords[1]

    # get current conditions 
    url="http://forecast.weather.gov/MapClick.php?lat=%s&lon=%s"%(latitude,longitude)
    page=requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    h=soup.find_all('div',class_='panel panel-default',id='current-conditions')
    text=h[0].get_text()
    text=text.split('\n\n\n\n')

    # get current weather results 
    location=text[1].split('\n')[1]
    cur_conditions=text[2].split('\n')[3].lower()
    cur_temp=text[2].split('\n')[4].replace('°F',' degrees Fahrenheit')

    # get forecast rest of day 
    seven_day = soup.find(id="seven-day-forecast")
    forecast_items = seven_day.find_all(class_="tombstone-container")
    tonight = forecast_items[0]
    img = tonight.find("img")
    desc = img['title']

    # now speak current temperature and conditions
    speak_text='It is %s and %s in %s'%(cur_temp, cur_conditions,city)
    print(speak_text)
    speaktext(speak_text)
    #time.sleep(0.5)
    #print(desc)
    #speaktext(desc)
    
    #if desc.find('showers')!= -1:
        #speaktext('You may want to bring an umbrella with you. It may rain.')

    # update database 
    hostdir=sys.argv[1]
    os.chdir(hostdir)
    database=json.load(open('registration.json'))
    action_log=database['action log']

    action={
        'action': 'weather.py',
        'date': get_date(),
        'meta': [all_loc_data, speak_text],
    }

    action_log.append(action)
    database['action log']=action_log

    jsonfile=open('registration.json','w')
    json.dump(database,jsonfile)
    jsonfile.close()


else:
    # don't get the weather if not connected to the internet 
    speak_text='no internet access, cannot get weather from the national weather service'
    print(speak_text)
    speaktext(speak_text)

    # update database 
    hostdir=sys.argv[1]
    os.chdir(hostdir)
    database=json.load(open('registration.json'))
    action_log=database['action log']

    action={
        'action': 'weather.py',
        'date': get_date(),
        'meta': [[], speak_text, ''],
    }

    action_log.append(action)
    database['action log']=action_log

    jsonfile=open('registration.json','w')
    json.dump(database,jsonfile)
    jsonfile.close()

