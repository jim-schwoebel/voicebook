##############################################################################
##                         STRESSLEX - NEWS.PY                              ##
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

News.py

Get major news events (in category of interest, just right after login).

Currently compatible with wikipedia, hacker news, statsbot blog, fast ML blog,
and cnn money.

'''

##############################################################################
##                           IMPORT STATEMENTS                              ##
##############################################################################

import requests, time, random, webbrowser, datetime, platform, sys
import ftplib, getpass, os, json 
from bs4 import BeautifulSoup
import pyttsx3 as pyttsx

##############################################################################
##                            HELPER FUNCTIONS                              ##
##############################################################################

def speaktext(text):
    # speak to a user from a text sample
    engine=pyttsx.init()
    engine.setProperty('voice','com.apple.speech.synthesis.voice.fiona')
    engine.say(text)
    engine.runAndWait()

def get_date():
    return str(datetime.datetime.now())

##############################################################################
##                            MAIN SCRIPT                                   ##
##############################################################################

# get a random news outlet to not spam all sites 

newstype=random.randint(0,4)

# WIKIPEDIA

if newstype == 0:
    
    url='https://en.wikipedia.org/wiki/Main_Page'
    page=requests.get(url)
    soup=BeautifulSoup(page.content, 'html.parser')

    mainpagelist=['Community portal – Bulletin board, projects, resources and activities covering a wide range of Wikipedia areas.',
                             'Help desk – Ask questions about using Wikipedia.',
                             'Local embassy – For Wikipedia-related communication in languages other than English.',
                             'Reference desk – Serving as virtual librarians, Wikipedia volunteers tackle your questions on a wide range of subjects.',
                             'Site news – Announcements, updates, articles and press releases on Wikipedia and the Wikimedia Foundation.',
                             'Village pump – For discussions about Wikipedia itself, including areas for technical issues and policies.',
                             'More than 1,000,000 articles:\n\n\nDeutsch\nEspañol\nFrançais\nItaliano\nNederlands\n日本語\nPolski\nРусский\nSvenska\nTiếng Việt\n中文\n\n\n', 'More than 250,000 articles:\n\n\nالعربية\nBahasa Indonesia\nBahasa Melayu\nCatalà\nČeština\nEuskara\nفارسی\n한국어\nMagyar\nNorsk\nPortuguês\nRomână\nSrpski\nSrpskohrvatski\nSuomi\nTürkçe\nУкраїнська\n\n\n', 'More than 50,000 articles:\n\n\nBosanski\nБългарски\nDansk\nEesti\nΕλληνικά\nEnglish (simple form)\nEsperanto\nGalego\nעברית\nHrvatski\nLatviešu\nLietuvių\nNorsk nynorsk\nSlovenčina\nSlovenščina\nไทย\n\n\n',
                             'Text is available under the Creative Commons Attribution-ShareAlike License;\nadditional terms may apply.  By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.']

    g=soup.find_all('li')

    didyouknow=list()
    onthisday=list()
    inthenews=list()

    for i in range(len(g)):
            if g[i].get_text()[0:8]=='... that':
                    didyouknow.append(g[i].get_text().replace('...','Did you know').replace('\xa0',''))
            elif g[i].get_text()[0:6].find('–') > 0:
                    onthisday.append('This day in ' + g[i].get_text())
            elif len(g[i].get_text())>40 and g[i].get_text() not in mainpagelist and g[i].get_text()[0:29] != ' This page was last edited on ':
                    inthenews.append('Today ' + g[i].get_text())

    rand=random.randint(0,2)
    if rand==0:
        rand=random.randint(0,len(didyouknow)-1)
        dyk=didyouknow[rand]
        speak_text=dyk

    elif rand==1:
        rand=random.randint(0,len(onthisday)-1)
        day=onthisday[rand]
        speak_text=day

    elif rand==2:
        rand=random.randint(0,len(inthenews)-1)
        news=inthenews[rand]
        speak_text=news
    
    link=url
    speaktext(speak_text)

# HACKER NEWS

elif newstype == 1:
    
    url='https://news.ycombinator.com/'
    page=requests.get(url)
    soup=BeautifulSoup(page.content, 'html.parser')
    g=soup.find_all('a',class_='storylink')

    ycnews=list()
    links=list()
    for i in range(len(g)):
        ycnews.append(g[i].get_text())
        links.append(g[i]['href'])

    rand=random.randint(0,len(ycnews)-1)
    title=ycnews[rand]
    link=links[rand]

    speak_text='perhaps check out '+ title+', posted on Hacker News'
    speaktext(speak_text)
    webbrowser.open(link)

# ML news websites

elif newstype == 2:

    links=list()
    
    url='https://blog.statsbot.co/'
    page=requests.get(url)
    soup=BeautifulSoup(page.content, 'html.parser')
    g=soup.find_all('a')
    for i in range(len(g)):
        if g[i]['href'].find('collection_home--')>0:
            links.append(g[i]['href'])

    rand=random.randint(0,len(links)-1)

    link=links[rand]
    i1=link.find('https://blog.statsbot.co/')
    i2=link.find('?source=collection_home')

    title=link[i1+len('https://blog.statsbot.co/'):i2]
    title=title.split('-')
    newtitle=''
    
    for i in range(len(title)):
        if i != len(title)-1:
            newtitle=newtitle+title[i]+' '
    
    speak_text='check out %s on the statsbot blog'%(newtitle)
    speaktext(speak_text)
    webbrowser.open(link)
    
elif newstype == 3:
    # fast ml blog

    links = list()
    titles=list()
    
    stoplinks=['https://github.com/zygmuntz',
               '/blog/categories/code/',
               'https://twitter.com/fastml_extra',
               'http://twitter.com/fastml',
               '/contents',
               '/blog/page/2/',
               '/popular/',
               '/about/',
               '/backgrounds/',
               '/links/',
               '/popular/',
               '/contents/',
               '/',
               '/atom.xml']
               
               
    
    url = 'http://fastml.com'
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    g=soup.find_all('a')
    for i in range(len(g)):
        if g[i]['href'].find('subscribers-only')>0:
            pass
        else:
            if g[i]['href'] not in stoplinks:
                if url+g[i]['href'] not in links:
                    links.append(url+g[i]['href'])
                    titles.append(g[i]['href'].replace('/','').replace('-',' '))
                              
    rand=random.randint(0,len(links)-1)
    link=links[rand]
    title=titles[rand]

    speak_text='check out %s on fastml blog'%(title)
    speaktext(speak_text)
    webbrowser.open(link)

elif newstype==4:

    links=list()

    url='http://money.cnn.com'
    page=requests.get(url)
    soup=BeautifulSoup(page.content, 'html.parser')
    g=soup.find_all('a')
    now=datetime.datetime.now()
    for i in range(len(g)):
        try:
            if g[i]['href'][0:5]=='/'+str(now.year) or g[i]['href'][0:6]=='/video':
                if url+g[i]['href'] not in links:
                    links.append(url+g[i]['href'])
        except:
            pass

    rand=random.randint(0,len(links)-1)
    link=links[rand]
    i1=link.find('/index.html')
    title=link[0:i1]
    i2=title[::-1]
    i3=i2.find('/')
    #i3=length of the title 
    title=title[-i3:].replace('-',' ').replace('.cnnmoney','')

    speak_text=title+' is in the news.'
    speaktext(speak_text)
    webbrowser.open(link)


# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('registration.json'))
action_log=database['action log']

action={
    'action': 'news.py',
    'date': get_date(),
    'meta': [speak_text, link],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('registration.json','w')
json.dump(database,jsonfile)
jsonfile.close()


