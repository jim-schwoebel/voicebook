'''
Get flights.

'''
##############################################################################
##                           IMPORT STATEMENTS                              ##
##############################################################################

from bs4 import BeautifulSoup
import os, requests, json, webbrowser, sys, datetime

##############################################################################
##                            HELPER FUNCTIONS                              ##
##############################################################################

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

airports=json.load(open('airport_data.json'))
cities=list(airports)

origin=input('where are you traveling from? \n')
destination=input('where are you traveling to? \n')
origin_city=''
destination_city=''

for i in range(len(cities)):
    #get origin city / destination 
    
    if cities[i].lower().find(origin) >= 0:
        origin_city=cities[i]
        
    if cities[i].lower().find(destination) >= 0:
        destination_city=cities[i]

# get airport codes
origin_code=airports[origin_city]
destination_code=airports[destination_city]

leave_date=input('what date are you leaving? (e.g. 2018-06-05) \n')
return_date=input("what time are you returning? (e.g. 2018-06-07 \n")

url='https://www.kayak.com/flights/%s-%s/%s/%s?sort=bestflight_a'%(origin_code, destination_code, leave_date, return_date)
flighturl=url
# in this case opening up the webbrowser makes sense because the soup is not available
webbrowser.open(url)

# now open airbnb 
city=destination
url='https://www.airbnb.com/s/%s--United-States/homes?refinement_paths'%(city)
other='%5B%5D=%2Fhomes&allow_override%5B%5D=&'
other2='checkin=%s&checkout=%s&s_tag=GDvS2YuG'%(leave_date,return_date)
url=url+other+other2
airbnburl=url

webbrowser.open(url)

#page=requests.get(url)
#soup=BeautifulSoup(page.content,'lxml')

# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('registration.json'))
action_log=database['action log']

action={
    'action': 'plan_trip.py',
    'date': get_date(),
    'meta': [flighturl, airbnburl],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('registration.json','w')
json.dump(database,jsonfile)
jsonfile.close()

                  
