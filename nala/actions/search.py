'''
Bing search via python.

Open up a url that is relevant to a query; attach voice interface to this.

'''

##############################################################################
##                            IMPORT STATEMENTS                             ##
##############################################################################

import requests, random, webbrowser, sys, os, json, datetime
from bs4 import BeautifulSoup
import pyttsx3 as pyttsx 

##############################################################################
##                            HELPER FUNCTIONS                              ##
##############################################################################

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
##                            MAIN SCRIPT.                                  ##
##############################################################################

# if local search 
# city=curloc()['city']
# query=str(input('what are you searching for in %s?'%(city)) + ' '+city).replace(' ','+')

# if global search
query=sys.argv[2].replace(' ','+')
url='https://www.bing.com/search/?q=%s'%(query)

page=requests.get(url)
soup=BeautifulSoup(page.content,'lxml')
g=soup.find_all('a')
stopwords=['Images','Maps','Play','News','Drive',
           'More »','Web History','Settings', 'Sign in', '', 'Videos',
           'Shopping','Books','Past hour','Past 24 hours','Past week',
           'Past month','Past year','Verbatim','Cached','Similar', 'Next',
           'Advanced search','Search Help','Send feedback','Google Home',
           'Advertising Programs','Business Solutions','Privacy and Cookies','Terms',
           'Legal','All','1','2','3','4','5','Next']

links=list()
descriptions=list()

for i in range(len(g)):
    if g[i].get_text() not in stopwords and g[i]['href'][0] != '/' and g[i]['href'] not in ['javascript:void(0);','javascript:','#'] and g[i]['href'].find('microsoft.com') == -1:
        links.append(g[i]['href'])
        descriptions.append(g[i].get_text())

randint=random.randint(0,len(links)-1)
link=links[randint]

webbrowser.open(link)

page=requests.get(link)
soup=BeautifulSoup(page.content,'lxml')
speak_stopwords=['403 - Forbidden: Access is denied.']
title=soup.title.get_text()
print(title)

if soup not in speak_stopwords:
    speaktext(title)

# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('registration.json'))
action_log=database['action log']

action={
    'action': 'search.py',
    'date': get_date(),
    'meta': [links, title, link],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('registration.json','w')
json.dump(database,jsonfile)
jsonfile.close()

