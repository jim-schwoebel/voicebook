'''
Get sports games.

ESPN website.
'''
import datetime, os, requests, webbrowser, sys, json
from bs4 import BeautifulSoup
import pyttsx3 as pyttsx
# get user location

def speaktext(text):
    # speak to user from a text sample (tts system)
    engine = pyttsx.init()
    engine.setProperty('voice','com.apple.speech.synthesis.voice.fiona')
    engine.say(text)
    engine.runAndWait()

def get_date():
    return str(datetime.datetime.now())

url='http://www.espn.com/'

# sport_type=['nba', 'wnba', 'nfl','mlb','nhl','mls','ncaaf']
sport_type=sys.argv[2].lower()
if sport_type not in ['nba', 'wnba', 'nfl','mlb','nhl','mls','ncaaf']:
    sport_type = 'nba'

now=str(datetime.datetime.now())[0:10]
date='/schedule/_/date/%s'%(now)

url=url+sport_type+date

page=requests.get(url)
soup=BeautifulSoup(page.content, 'lxml')

#get table elements 
y=soup.find_all('tr')
dates=soup.find_all(class_='table-caption')

datecount=0
datelist=list()
descriptions=list()

for i in range(len(y)):
    try:
        if y[i].get_text().lower() == 'no games scheduled':
            date=dates[datecount].get_text()
            description='no games scheduled'
            descriptions.append(description)
            datelist.append(date)
            datecount=datecount+1 
        elif y[i].find_all(class_='matchup')[0].get_text().lower()=='matchup':
            date=dates[datecount].get_text()
            description=y[i+2].get_text()
            description_2=y[i+1].get_text()
            i2=description_2.find('tickets')
            description_2=description_2[0:i2].replace(',','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')
            description=description+' '+description_2
            descriptions.append(description.replace('matchuptime\xa0(ET)nat tvaway tvhome tv ','').replace('matchuptime\xa0(ET)nat tvticketslocation ',''))
            datelist.append(date)
            datecount=datecount+1
        else:
            pass 
    except:
        pass 

print(descriptions)
print(datelist)

tonight=descriptions[0]
if tonight.lower()=='no games scheduled':
    speaktext('no games scheduled tonight')
else:
    speaktext('tonight %s is on ESPN'%(tonight))
        
# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('registration.json'))
action_log=database['action log']

action={
    'action': 'espn.py',
    'date': get_date(),
    'meta': [datelist, descriptions],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('registration.json','w')
json.dump(database,jsonfile)
jsonfile.close()
