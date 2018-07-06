##############################################################################
##                         STRESSLEX - EXERCISE.PY                          ##
##############################################################################

'''

Author: @Jim Schwoebel
Role: Chief Executive Officer
Git Repo: git@github.com:NeuroLexDiagnostics/stresslex-py.git
Script: exercise.py
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

The exercise.py action module picks a place nearby to walk, bike, or run.
It chooses the type of activity based on how the user was baselined in the
database.

In this way, you can remain healthy and keep thinking about exercising when
you are under peak stress.

Note: it is a known bug that some of the links provided are depecated.
Plotaroute.com is an imperfect short-term solution. If you have any other
ideas to create new running/walking/biking routs, let me know.

'''

##############################################################################
##                           IMPORT STATEMENTS                              ##
##############################################################################

import datetime, os, random, numpy, geocoder, ftplib, requests, json
import webbrowser, time, smtplib, getpass, platform, sys
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

##############################################################################
##                            HELPER FUNCTIONS                              ##
##############################################################################

def get_date():
    return str(datetime.datetime.now())

def sendmail(to, subject, text, email, password, files=[]):
    
    try:
        msg = MIMEMultipart()
        msg['From'] = 'NeuroLex Labs'
        msg['To'] = COMMASPACE.join(to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        msg.attach( MIMEText(text) )

        for file in files:
            part = MIMEBase('application', "octet-stream")
            part.set_payload( open(file,"rb").read() )
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"'
                           % os.path.basename(file))
            msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo_or_helo_if_needed()
        server.starttls()
        server.ehlo_or_helo_if_needed()
        server.login(email,password)
        server.sendmail(email, to, msg.as_string())

        print('Done')

        server.quit()
        
    except:
        print('error')

def playbackaudio(question,filename):
#takes in a question and a filename to open and plays back the audio file and prints on the screen the question for the user 
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(0.5)
    print(question)
    return "playback completed"

def getlocation():
    g = geocoder.google('me')
    return g.latlng

def curloc():
    
    # get current location, limit 1000 requests/day
    r=requests.get('http://ipinfo.io')
    location=r.json()
    
    return location 

def randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10):
    thenum=random.randint(1,10)
    if thenum==1:
        route=route1
    if thenum==2:
        route=route2
    if thenum==3:
        route=route3
    if thenum==4:
        route=route4
    if thenum==5:
        route=route5
    if thenum==6:
        route=route6
    if thenum==7:
        route=route7
    if thenum==8:
        route=route8
    if thenum==9:
        route=route9
    if thenum==10:
        route=route10
    return route 

# this is the main module; I scraped most of these routes from plotaroute.com
def exercise(nearestcity, exercise, distance):
    if exercise == "walk":
	
        if nearestcity == "chicago":
            if distance >= 3:
                route1="River tour, 4.932 km: https://www.plotaroute.com/route/243600"
                route2="Boystown Tour, 5.021km: https://www.plotaroute.com/route/225793"
                route3="Museum Campus wlak, 6.285 km: https://www.plotaroute.com/route/3231"
                route4="Summar walk/run, 6.522 km: https://www.plotaroute.com/route/447000"
                route5="Explore music scene, Chicago, 5.974km: https://www.plotaroute.com/route/285781"
                route6="McKinley Park, 5.619km: https://www.plotaroute.com/route/432758"
                route7="Lake walk, 4.993km: https://www.plotaroute.com/route/218758"
                route8="Albany Tour, 5.210km: https://www.plotaroute.com/route/219460"
                route9="Chi buidings, 11.052km: https://www.plotaroute.com/route/268309"
                route10="Rogers Park Tour, 4.840km: https://www.plotaroute.com/route/303660"
                #randomly select one of these routes (same for all that follows)
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 3:
                route1="Diversity-north ave, 2.416km: https://www.plotaroute.com/route/11149"
                route2="Edgewater tour, 4.670km: https://www.plotaroute.com/route/283619"
                route3="The Bean, 3.503km: https://www.plotaroute.com/route/3271"
                route4="Do-Rite River, 3.376km: https://www.plotaroute.com/route/3271"
                route5="Buckingham, 3.417km: https://www.plotaroute.com/route/3219"
                route6="North Ave Bridge walk, 1.499km: https://www.plotaroute.com/route/11155"
                route7="Uptown Tour, 3.959km: https://www.plotaroute.com/route/378270"
                route8="Diversey-North Ave walk, 2.419km: https://www.plotaroute.com/route/11152"
                route9="Wicker Park Tour, 3.947km: https://www.plotaroute.com/route/265031"
                route10="Lunch walk, 3.512km: https://www.plotaroute.com/route/189823"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="boston":
            if distance >= 3:
                route1="Boston to Portland Maine, 250km hike: https://www.plotaroute.com/route/343290"
                route2="Ferguson March, 7,996km: https://www.plotaroute.com/route/24447"
                route3="Ferguson March, 7,996km: https://www.plotaroute.com/route/24447"
                route4="Boston walk, 5km: https://www.plotaroute.com/route/4644"
                route5="Boston special places, 10.366km: https://www.plotaroute.com/route/297587"
                route6="GoPuff Lake St. Route, 10.694km: https://www.plotaroute.com/route/94017"
                route7="Boston Common, 5.995km: https://www.plotaroute.com/route/276195"
                route8="Avenue of the Arts, 5.121km: https://www.plotaroute.com/route/404421"
                route9="Middle Route Boston, 10.816km: https://www.plotaroute.com/route/349306"
                route10="Boston Freedom Trail, 7,948km: https://www.plotaroute.com/route/365679"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 3:
                route1="March on Boston's Trails to Freedom, 2.573 km: https://www.plotaroute.com/route/272759"
                route2="Faneuil Hall Route, 3.318km: https://www.plotaroute.com/route/63494"
                route3="Northeastern, 4.232km: https://www.plotaroute.com/route/14597"
                route4="Charles River, 2.939km: https://www.plotaroute.com/route/63490"
                route5="Beacon Hill, 2.75km: https://www.plotaroute.com/route/63485"
                route6="Commonwealth Ave-  Back Bay, 3.086km: https://www.plotaroute.com/route/63492"
                route7="Waterfront Walk, 2.881km: https://www.plotaroute.com/route/70980"
                route8="Boston Walk, 4.227km: https://www.plotaroute.com/route/38657"
                route9="Wine Trail, 3.322km: https://www.plotaroute.com/route/405946"
                route10="Dog Parks, 3.159km: https://www.plotaroute.com/route/415753"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            #walk around downtown station to mass challenge 

        if nearestcity=="philadelphia":

            if distance >= 3:
                route1="Philly walk, 5km: https://www.plotaroute.com/route/239874"
                route2="Philly gets fit 5 miler, 7.925km: https://www.plotaroute.com/route/40424"
                route3="Skate Zone 8.3 Mile, 13.372km: https://www.plotaroute.com/route/67835"
                route4="Chesnut Hill 11k Walk: https://www.plotaroute.com/route/298922"
                route5="Ashton/Convent 3miles, 4.881km: https://www.plotaroute.com/route/298922"
                route6="South Street bridge, 4.862km: https://www.plotaroute.com/route/34887"
                route7="Chesnut Hill Walk 8km, https://www.plotaroute.com/route/345971"
                route8="Philadelpha Old Town: https://www.plotaroute.com/route/362209"
                route9="8th district walk, 8.780km: https://www.plotaroute.com/route/67831"
                route10="New Bethany 5k: https://www.plotaroute.com/route/189189"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 3:
                route1="East Passyunk Route, 1.151km: https://www.plotaroute.com/route/429485"
                route2="Caroling Route, 4.471km: https://www.plotaroute.com/route/328957"
                route3="Walk 30th to PMA, 1.393km: https://www.plotaroute.com/route/29882"
                route4="OYU Walking Path, 1.704km: https://www.plotaroute.com/route/295215"
                route5="OYU 16th St, 1.009km: https://www.plotaroute.com/route/295228"
                route6="E/S 3/4 mile loop, 1.197km: https://www.plotaroute.com/route/34534"
                route7="Lung Force Walk Route 2017, 4.182km: https://www.plotaroute.com/route/415734"
                route8="Blossom Philadelphia 2k Walk, 2.004km: https://www.plotaroute.com/route/419130"
                route9="Crispin, 2.795km: https://www.plotaroute.com/route/70458"
                route10="Route to Dunkin Donuts, 1.905 km: https://www.plotaroute.com/route/350183"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="new york city":
            #walk the high line 

            if distance >= 3:
                route1="Central Park, Pokemon Go Route, 30.205km: https://www.plotaroute.com/route/258559"
                route2="Brooklyn Bridge, 6.146km: https://www.plotaroute.com/route/3635"
                route3="NYC walk, 12.334km: https://www.plotaroute.com/route/180511"
                route4="Dratoni Route, 3.327 miles: https://www.plotaroute.com/route/264647"
                route5="Central Park, 6.142km: https://www.plotaroute.com/route/252050"
                route6="Central Park, 19.5km: https://www.plotaroute.com/route/255199"
                route7="Central Park II, 8.884km: https://www.plotaroute.com/route/267813"
                route8="Brooklyn Walk, 5.070km: https://www.plotaroute.com/route/432618"
                route9="NYC Chelsea Flat Iron, Chinatown, 8.589km: https://www.plotaroute.com/route/234207"
                route10="NYC midtown, 3.031miles: https://www.plotaroute.com/route/233988"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 3:
                route1="Walk MS route, 2.381km: https://www.plotaroute.com/route/353184"
                route2="Ollis - Walking Route, 2.935km: https://www.plotaroute.com/route/423594"
                route3="Central Park, 3.922km: https://www.plotaroute.com/route/216394"
                route4="9/11 memorial walk, 0.433km: https://www.plotaroute.com/route/180079"
                route5="Central Park walk II, 3.866km: https://www.plotaroute.com/route/251504"
                route6="Financial district walk, 3.008km: https://www.plotaroute.com/route/432615"
                route7="Bow Bridge to the Metropolitan Museum of Art, 1.499km: https://www.plotaroute.com/route/177715"
                route8="The High Line / Chelsea Market, 2.603km: https://www.plotaroute.com/route/432638"
                route9="Greenwich Y / Soho, 3.302km: https://www.plotaroute.com/route/432633"
                route10="Tribeca, 1.815km: https://www.plotaroute.com/route/432622"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="houston":
            #walk on paths 2 miles 

            if distance >= 3:
                route1="Grissom walk, 4041km: https://www.plotaroute.com/route/5321"
                route2="JWalker Mardi Gras Route, 14.643km: https://www.plotaroute.com/route/34785"
                route3="Walk, 6.3 miles: https://www.plotaroute.com/route/27050"
                route4="DoggieWalk, 7 miles: https://www.plotaroute.com/route/313066"
                route5="Tour of Starbucks, 18.847km: https://www.plotaroute.com/route/16798"
                route6="5 mile walk, 8.048km: https://www.plotaroute.com/route/24149"
                route7="5k walk: https://www.plotaroute.com/route/118729"
                route8="6k walk: https://www.plotaroute.com/route/242424"
                route9="5k walk: https://www.plotaroute.com/route/419492"
                route10="Long route, 3.752miles: https://www.plotaroute.com/route/242424"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 3:
                route1="National Walk, 1.949km: https://www.plotaroute.com/route/203394"
                route2="Walking Route, 2.99km: https://www.plotaroute.com/route/229719"
                route3="Walk near MD Anderson, 2.924km: https://www.plotaroute.com/route/124360"
                route4="2mile evening walk, 3.446km: https://www.plotaroute.com/route/20367"
                route5="Med Center Track, 3.606km: https://www.plotaroute.com/route/124362"
                route6="Arthur Storey Walk, 4.512km: https://www.plotaroute.com/route/281207"
                route7="HCC Route, 1.251km: https://www.plotaroute.com/route/337391"
                route8="Arthur Storey Park Walk, 4.509km: https://www.plotaroute.com/route/272618"
                route9="RTP walk, 3km: https://www.plotaroute.com/route/307138"
                route10="Arthur Storey Park II, 2.783miles: https://www.plotaroute.com/route/271880"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="dallas": 
            #walk around downtown dallas in Deep ellem 

            if distance >= 3:
                route1="Trinity River walk, 5.038km: https://www.plotaroute.com/route/216163"
                route2="Highland Park Walk, 9.125km: https://www.plotaroute.com/route/313976"
                route3="White Rock Trail, 26.210km: https://www.plotaroute.com/route/87402"
                route4="Tour of Bridges, 9.976k: https://www.plotaroute.com/route/176057"
                route5="Highland Park Walk II, 9.256km: https://www.plotaroute.com/route/322796"
                route6="Mean dering Way, 5.270km: https://www.plotaroute.com/route/371139"
                route7="3 mile walk: https://www.plotaroute.com/route/404330"
                route8="Addis Circle, 8.741km: https://www.plotaroute.com/route/371145"
                route9="Tom Thumb, 5.700km: https://www.plotaroute.com/route/371144"
                route10="Highland Park Walk III, 5.203km: https://www.plotaroute.com/route/322796"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 3:
                route1="Woodrow Parade Walk, 2.950km: https://www.plotaroute.com/route/118174"
                route2="Greater Dallas Walk to End Alzheimers, 4.714km: https://www.plotaroute.com/route/15545"
                route3="2015 Dallas WTEA, 4.698km: https://www.plotaroute.com/route/108423"
                route4="JDRF One Walk, 4.191km: https://www.plotaroute.com/route/63826"
                route5="Dog walk, 3.330km: https://www.plotaroute.com/route/272998"
                route6="Parade Walk, 0.836km: https://www.plotaroute.com/route/275949"
                route7="1 mile walk, 1.591km: https://www.plotaroute.com/route/404342"
                route8="2 mile walk, 3.33km: https://www.plotaroute.com/route/404338"
                route9="Kroger walk, 3.325km: https://www.plotaroute.com/route/371132"
                route10="Concert walk, 0.381km: https://www.plotaroute.com/route/385155"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="san antonio":
            #walk the river downtown 

            if distance >= 3:
                route1="Zoo Olmos Dam Hill, 8.019km: https://www.plotaroute.com/route/349953"
                route2="Hike for the 22 - San Antonio, 5.181km: https://www.plotaroute.com/route/66700"
                route3="CtF SA, 36.425km: https://www.plotaroute.com/route/6767"
                route4="Walking for Vets, 2513km: https://www.plotaroute.com/route/140487"
                route5="Winston path, 5.202km: https://www.plotaroute.com/route/169109"
                route6="3 mile Brooks, 5.187km: https://www.plotaroute.com/route/172245"
                route7="Tour de Las Misiones Walk, 10k, 9.884km: https://www.plotaroute.com/route/423704"
                route8="Alamo walk, 5.676km: https://www.plotaroute.com/route/356617"
                route9="Texas Trail Roundup, 4.990km: https://www.plotaroute.com/route/353659"
                route10="Morning walk, 11.860km: https://www.plotaroute.com/route/428137"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 3:
                route1="Madla Mile, 1.610km: https://www.plotaroute.com/route/154945"
                route2="Short walk, 0.919km: https://www.plotaroute.com/route/151896"
                route3="Haram, 3.700km: https://www.plotaroute.com/route/168581"
                route4="Tour De Las Misiones Walk, 4.652km: https://www.plotaroute.com/route/423695"
                route5="Winst on Path 1.28, 2.074km: https://www.plotaroute.com/route/166171"
                route6="Route 3, 4.007km: https://www.plotaroute.com/route/151948"
                route7="Alamo Beer to SARNR Marathon, 1.656km: https://www.plotaroute.com/route/310007"
                route8="SARNR Finish, 1.851km: https://www.plotaroute.com/route/310008"
                route9="Route 2, 4.772km: https://www.plotaroute.com/route/151946"
                route10="Winst on Path 2.7, 4.355km: https://www.plotaroute.com/route/142824"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="austin": 
            #walk downtown austin 

            if distance >= 3:
                route1="Colorado River Walk, 14.854km: https://www.plotaroute.com/route/61280"
                route2="4 mile walk: https://www.plotaroute.com/route/7859"
                route3="Walking Route, 11.559km: https://www.plotaroute.com/route/10468"
                route4="5th to Jo's and Back, 5.926km: https://www.plotaroute.com/route/27641"
                route5="River Place Nature Trail, 8.640km: https://www.plotaroute.com/route/234874"
                route6="Silkie March, 14.351km: https://www.plotaroute.com/route/287517"
                route7="3 mile walk, 5.174km: https://www.plotaroute.com/route/234563"
                route8="5 mile walk through neighborhood, 8.498km: https://www.plotaroute.com/route/165128"
                route9="5k walk, 5.062km: https://www.plotaroute.com/route/444319"
                route10="City Hiking, 20.430km: https://www.plotaroute.com/route/91750"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 3:
                route1="Harajuku Fashion Walk, 2.286km: https://www.plotaroute.com/route/47753"
                route2="12th Night Austin Procession, 1.464km: https://www.plotaroute.com/route/150239"
                route3="TBVME 2 walk, 2.103km: https://www.plotaroute.com/route/149790"
                route4="Panther Trail, 3.223km: https://www.plotaroute.com/route/234862"
                route5="Short walk, 1.497km: https://www.plotaroute.com/route/252071"
                route6="Springwoods Park Poke Crawl, 1.287km: https://www.plotaroute.com/route/253586"
                route7="Troop 505 urban Course 2.570km: https://www.plotaroute.com/route/331277"
                route8="Short Walk II, 0.737km: https://www.plotaroute.com/route/193691"
                route9="Rattan Creek Park Poke Crawl: 3.788km: https://www.plotaroute.com/route/254013"
                route10="San Jacinto walk, 1.177km: https://www.plotaroute.com/route/111042"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="atlanta":
           #walk the belt line 
           #show printed route here with link / .png
            if distance >= 3:
                route1="Ruck Cancer walk, 109km: https://www.plotaroute.com/route/318473"
                route2="Hunger walk, 4.83km: https://www.plotaroute.com/route/44669"
                route3="Atlanta to Savannah walk, 428km: https://www.plotaroute.com/route/61919"
                route4="Breast Cancer walk, 4.857km: https://www.plotaroute.com/route/113025"
                route5="Eracism 5k walk, 5.147km: https://www.plotaroute.com/route/185053"
                route6="Bobby Dodd to Herty Field, 107k: https://www.plotaroute.com/route/112240"
                route7="7 miles neighborhood walk, 11.283km: https://www.plotaroute.com/route/167393"
                route8="Morning Walkk, 6.891km: https://www.plotaroute.com/route/480634"
                route9="Great 8 walk, 5.898km: https://www.plotaroute.com/route/269617"
                route10="5k walk, 5km: https://www.plotaroute.com/route/239831"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 3:
                route1="Beltline walk, 2.756km: https://www.plotaroute.com/route/325704"
                route2="Brownwood Park walk, 1.250km: https://www.plotaroute.com/route/442470"
                route3="Short walk, 1.910km: https://www.plotaroute.com/route/408795"
                route4="Sultry Steppers route, 3.192km: https://www.plotaroute.com/route/358349"
                route5="West Paces Pacers Route, 2.760km: https://www.plotaroute.com/route/358356"
                route6="Short walk, 2.235km: https://www.plotaroute.com/route/272662"
                route7="Residential walk, 1.706km: https://www.plotaroute.com/route/358352"
                route8="1.52 mile walk: https://www.plotaroute.com/route/407868"
                route9="MAMA March walk, 2.268km: https://www.plotaroute.com/route/413693"
                route10="Ensign Park Loop, 3.193km: https://www.plotaroute.com/route/269611"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="seattle": 
            #walk around seattle city center 
            if distance >= 3:
                route1="Cheshiahud Loop - Dexter Alternative, 10.378km: https://www.plotaroute.com/route/156922"
                route2="University of Washington 5K Route, 3.106miles: https://www.plotaroute.com/route/191238"
                route3="SOA Meetup Feb 15, 4.368miles: https://www.plotaroute.com/route/159739"
                route4="Queen anne hilltop, 4.433miles: https://www.plotaroute.com/route/159741"
                route5="Queen Anne Loop, 7.647km: https://www.plotaroute.com/route/159735"
                route6="Inverness Loop, 8.639km: https://www.plotaroute.com/route/118485"
                route7="Chittenden Locks, 8.629km: https://www.plotaroute.com/route/123692"
                route8="Blue Ridge-North Beach, 8.860km: https://www.plotaroute.com/route/124123"
                route9="Locks to Discovery Park, 8.784km: https://www.plotaroute.com/route/130565"
                route10="Evergreen-Washelli Loop, 8.8289km: https://www.plotaroute.com/route/122210"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 3:
                route1="Shoreline Walk, 4.107km: https://www.plotaroute.com/route/280895"
                route2="Shoreline Walk II, 3.979km: https://www.plotaroute.com/route/276438"
                route3="SW Queen Anne, 4.249km: https://www.plotaroute.com/route/149242"
                route4="Longfellow Creek and Pigeon Point, 2.833km: https://www.plotaroute.com/route/152058"
                route5="Madrona and Leschi, 3.179km: https://www.plotaroute.com/route/151064"
                route6="North Acres Park, 2.765km: https://www.plotaroute.com/route/98302"
                route7="CHIM walk, 2.769km: https://www.plotaroute.com/route/157386"
                route8="Mt. Baker walk, .802km: https://www.plotaroute.com/route/200944"
                route9="Beacon Hill 5k walk, 4.435km:https://www.plotaroute.com/route/205543"
                route10="QFC walk, 1.335km: https://www.plotaroute.com/route/264523"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="san francisco": 
            #walk from union square to the ferry 
            if distance >= 3:
                route1="SF Pokemon Go route, 18.678km: https://www.plotaroute.com/route/259756"
                route2="SF Pier Tour, 19.088km: https://www.plotaroute.com/route/263487"
                route3="OLLI Hikers McLaren Park, 6.259km: https://www.plotaroute.com/route/164821"
                route4="Mt. Sutro & Cole Valley, 5.934km: https://www.plotaroute.com/route/193262"
                route5="Eureka Valley, 5.428km: https://www.plotaroute.com/route/148087"
                route6="Mission Bay, 8.340km: https://www.plotaroute.com/route/136483"
                route7="The Castro, 6.306km: https://www.plotaroute.com/route/324244"
                route8="SF WALKING TOUR, 15.88km: https://www.plotaroute.com/route/104173"
                route9="Golden Gate 5 mile loop, 8.068km: https://www.plotaroute.com/route/326247"
                route10="Golden Gate Park, 11.226km: https://www.plotaroute.com/route/470534"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 3:
                route1="Easy Walking route, 2.407km: https://www.plotaroute.com/route/195864"
                route2="Bernal Heights, 1.963km: https://www.plotaroute.com/route/199029"
                route3="Yerba Buena and Terasure Island, 2.713km: https://www.plotaroute.com/route/194551"
                route4="Baker Beach to Mountain Lake, 3.996km: https://www.plotaroute.com/route/457574"
                route5="Chinatown, 2.2883km: https://www.plotaroute.com/route/24350"
                route6="Ballpark walk, 3.416km: https://www.plotaroute.com/route/306599"
                route7="Pacific Heights, 4.44km: https://www.plotaroute.com/route/142121"
                route8="Mission to Embarcadero, 3.101km: https://www.plotaroute.com/route/347030"
                route9="Exploratorium, 3.298km: https://www.plotaroute.com/route/326973"
                route10="Ferry Building walk, 2.658km: https://www.plotaroute.com/route/307709"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="los angeles":
            #n/a 
            if distance >= 3:
                route1="5k walk, 5.4km: https://www.plotaroute.com/route/11959"
                route2="Remedial Hike, 4.997km: https://www.plotaroute.com/route/202002"
                route3="Hollywood Hike, 5.478km: https://www.plotaroute.com/route/405788"
                route4="LA 25th, 8.729km: https://www.plotaroute.com/route/268987"
                route5="BH Walk, 8.288km: https://www.plotaroute.com/route/244614"
                route6="Fryman Canyon, 6.066km: https://www.plotaroute.com/route/372914"
                route7="Mt. Washington 3.14 mile loop: https://www.plotaroute.com/route/354257"
                route8="4 mile Hollywood Walk, 5.893km: https://www.plotaroute.com/route/372941"
                route9="Downtown Culver City, 5.305km: https://www.plotaroute.com/route/390120"
                route10="Beach Walk, 11.328km: https://www.plotaroute.com/route/378852"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 3:
                route1="Barber town, 1.329km: https://www.plotaroute.com/route/318494"
                route2="LA downtown, 4.090km: https://www.plotaroute.com/route/165729"
                route3="Short walk, 3km: https://www.plotaroute.com/route/207934"
                route4="Short walk II, 2.484km: https://www.plotaroute.com/route/274082"
                route5="Short route, 2.483km: https://www.plotaroute.com/route/274087"
                route6="Mt. Washington 2.7 mile st loop, 4.231km: https://www.plotaroute.com/route/354258"
                route7="2.5 mile good walk, 4.025km: https://www.plotaroute.com/route/274097"
                route8="30 minute park walk, 2.132km: https://www.plotaroute.com/route/378857"
                route9="Downtown LA II, 2.563km: https://www.plotaroute.com/route/416632"
                route10="Otis College of Art and Design to Farmer's Market, 1.367miles: https://www.plotaroute.com/route/382194"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

    if exercise == "run":

        if nearestcity == "chicago":
            if distance >= 10:
                route1="Chicity to northwestern run, 14.379 miles: https://www.plotaroute.com/route/490411"
                route2="Tough mudder, Chicago, 10.1 miles: https://www.plotaroute.com/route/482818"
                route3="Chicago marathon, 26.797 miles: https://www.plotaroute.com/route/424209"
                route4="Jogunitas 2017, 16.934 km: https://www.plotaroute.com/route/363863"
                route5="Half Marathon, Lakeview, 21 km: https://www.plotaroute.com/route/262226"
                route6="10 mile west town loop, 17.084 km: https://www.plotaroute.com/route/176494"
                route7="Lakeview to River Walk Loop - 14 miles: https://www.plotaroute.com/route/258564"
                route8="19 miles run home: https://www.plotaroute.com/route/383405"
                route9="13.1 Route A, 21.848 km: https://www.plotaroute.com/route/383453"
                route10="10 Mile A, 16.725 km: https://www.plotaroute.com/route/383450"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance >= 5 and distance < 10:
                route1="Downtown Chicago run, 6.856 miles: https://www.plotaroute.com/route/464547"
                route2="Chicago Dual, 8.774 miles: https://www.plotaroute.com/route/430476"
                route3="West Chicago, 5 miles: https://www.plotaroute.com/route/426540"
                route4="South chicago, Lakeshore, 6.0 miles: https://www.plotaroute.com/route/405638"
                route5="North chicago, Lakeshore, 7.518 miles: https://www.plotaroute.com/route/405637"
                route6="Chicago run, 7.939 miles: https://www.plotaroute.com/route/273418"
                route7="Kessel Run, 12.594 km: https://www.plotaroute.com/route/177766"
                route8="Chi Buildings, 11.052 km: https://www.plotaroute.com/route/268309"
                route9="Pop Eagle Trail, 12.749 km: https://www.plotaroute.com/route/460598"
                route10="Lakerun, 8.368km: https://www.plotaroute.com/route/19883"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 5: 
                route1="Downtown chicago 5 mile run: https://www.plotaroute.com/route/467998"
                route2="Chicago grand prix, 3.6 miles: https://www.plotaroute.com/route/464547"
                route3="Short Chicago Run, 4.651 miles: https://www.plotaroute.com/route/307431"
                route4="Music run!!, 3.712 miles: https://www.plotaroute.com/route/285781"
                route5="Calumet Workout Road, 2.55 miles: https://www.plotaroute.com/route/447039"
                route6="6k route near Chicago: 3.7 miles: https://www.plotaroute.com/route/442841"
                route7="5k Route near Chicago: 3.1 miles: https://www.plotaroute.com/route/376621"
                route8="Jackson 5Mi - 2017, 5 miles: https://www.plotaroute.com/route/356500"
                route9="Home 5k near Chicago: 3 miles: https://www.plotaroute.com/route/324202"
                route10="5K route near Chicago: 3.2 miles: https://www.plotaroute.com/route/135063"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="boston":
            #run along kendall sq, run in tufts, etc. 
            if distance >= 10:
                route1="Veterans Day Run, 21.3km: https://www.plotaroute.com/route/136449"
                route2="Half Marathon Prep, 21km: https://www.plotaroute.com/route/137111"
                route3="Mystic River Loop, 20.735km: https://www.plotaroute.com/route/139496"
                route4="Long run, 22.8km: https://www.plotaroute.com/route/386352"
                route5="Allston/Dot Half Marathon, 21.273km: https://www.plotaroute.com/route/273756"
                route6="Long Boston route, 20.072km: https://www.plotaroute.com/route/332298"
                route7="11 mile route, 17.779km: https://www.plotaroute.com/route/310884"
                route8="Boston Hilly 10 miler, 16.271km: https://www.plotaroute.com/route/338230"
                route9="Harboarwalk 10 mile, 16.287km: https://www.plotaroute.com/route/319111"
                route10="Charles River Route, 21.485km: https://www.plotaroute.com/route/243929"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance >= 5 and distance < 10:
                route1="The Boston Common Loop, 8.516km: https://www.plotaroute.com/route/267323"
                route2="Harvard Run, 12.878km: https://www.plotaroute.com/route/429896"
                route3="Olmsted + Fenway 10k, 10.225km: https://www.plotaroute.com/route/293440"
                route4="Fenway and HMS, 10.779km: https://www.plotaroute.com/route/285976"
                route5="6 miler from Charles River and WGBH, 9.656km: https://www.plotaroute.com/route/252271"
                route6="Charles River, 10.041km: https://www.plotaroute.com/route/458023"
                route7="Fenway loop, 9.952km: https://www.plotaroute.com/route/385220"
                route8="Boston 9 miles, 15.390km: https://www.plotaroute.com/route/284141"
                route9="North/South End Rune, 15.401km: https://www.plotaroute.com/route/280293"
                route10="Esplanade 10k, 10.047km: https://www.plotaroute.com/route/294097"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 5: 
                route1="Castle Island 5k, 5.056km: https://www.plotaroute.com/route/146492"
                route2="Fort Point, 5.282km: https://www.plotaroute.com/route/139066"
                route3="Fenway quick run near Esplanade, 5 miles: https://www.plotaroute.com/route/490550"
                route4="Copley run, 6.359km: https://www.plotaroute.com/route/303270"
                route5="Fenway 4 miles, 6.486km: https://www.plotaroute.com/route/453394"
                route6="Boston Common Loop, 8.516km: https://www.plotaroute.com/route/267323"
                route7="3.5mile run, 5.757km: https://www.plotaroute.com/route/57700"
                route8="Short route, 5.33km: https://www.plotaroute.com/route/294739"
                route9="Harborside 5k, 5.266km: https://www.plotaroute.com/route/262735"
                route10="Longwood route, 4.798km: https://www.plotaroute.com/route/402796"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="philadelphia":
            #parks 
            if distance >= 10:
                route1="15 mile run, 14.544miles: https://www.plotaroute.com/route/269097"
                route2="12 mile Hood Run, 19.403km: https://www.plotaroute.com/route/186078"
                route3="Philly Half Marathon, 21.748km: https://www.plotaroute.com/route/310914"
                route4="28 mile route, 45.325km: https://www.plotaroute.com/route/262115"
                route5="Liberty Bell Route, 16.693km: https://www.plotaroute.com/route/444132"
                route6="18 mile long run, 29.121km: https://www.plotaroute.com/route/228489"
                route7="10 mile long run, 16.139km: https://www.plotaroute.com/route/182565"
                route8="Bridge Cambridge Run, 20.011km: https://www.plotaroute.com/route/453044"
                route9="11 miles end at toast, 17.557km: https://www.plotaroute.com/route/312638"
                route10="The Franklin Mills 19 miler club, 30.957km: https://www.plotaroute.com/route/450105"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance >= 5 and distance < 10:
                route1="Rocky Balboa Run 10k, 10.094km: https://www.plotaroute.com/route/135912"
                route2="6 mile run, 9.706km: https://www.plotaroute.com/route/28446"
                route3="Forbidden Trial, 11.799km: https://www.plotaroute.com/route/73814"
                route4="5 mile run, 8.311km: https://www.plotaroute.com/route/28443"
                route5="Wissahikon, 10.66km: https://www.plotaroute.com/route/29169"
                route6="10 miles in Philly, 15.967km: https://www.plotaroute.com/route/255069"
                route7="7 miles in Philly, 11.273km: https://www.plotaroute.com/route/344648"
                route8="Navy Yard, 8.271km: https://www.plotaroute.com/route/453759"
                route9="The Prison Run, 11.613km: https://www.plotaroute.com/route/450098"
                route10="8 mile run, 13.506km: https://www.plotaroute.com/route/313055"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 5: 
                route1="Firebolt 5k, 5km: https://www.plotaroute.com/route/118224"
                route2="5k in Philly, 5.140km: https://www.plotaroute.com/route/215940"
                route3="FDR 5k Food Run, 5.093km: https://www.plotaroute.com/route/50905"
                route4="Moyamensinig Loop, 4 miles: https://www.plotaroute.com/route/423104"
                route5="1.2 mile run to city hall, 2.054km: https://www.plotaroute.com/route/147848"
                route6="3 mile square run, 4.794km: https://www.plotaroute.com/route/264662"
                route7="Philadelphia Soul 5k, 5.244km: https://www.plotaroute.com/route/403490"
                route8="Clinton Run South, 4.987km: https://www.plotaroute.com/route/161707"
                route9="Zoo 5k, 5.322km: https://www.plotaroute.com/route/390350"
                route10="Oregon Loop around Wharton, 4 miles: https://www.plotaroute.com/route/478448"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="new york city":
            if distance >= 10:
                route1="Bay Ridge Run, 23.409km: https://www.plotaroute.com/route/435225"
                route2="10 mile NYC run, 16.530km: https://www.plotaroute.com/route/298072"
                route3="13 mile Manhattan/Williamburg Run, 21.078km: https://www.plotaroute.com/route/456186"
                route4="16 mile long run, 26.128km: https://www.plotaroute.com/route/278247"
                route5="Flushing to Fort Totten Loop, 30.230km: https://www.plotaroute.com/route/154310"
                route6="9 mile run, 17.339km: https://www.plotaroute.com/route/227234"
                route7="13.1 mile run, 21.128km: https://www.plotaroute.com/route/287512"
                route8="NYC Marathon training run, 42.129km: https://www.plotaroute.com/route/221638"
                route9="Last 10 miles of the Brooklyn Half, 16.658km: https://www.plotaroute.com/route/404113"
                route10="Brooklyn-Manhattan Loop, 23.728km: https://www.plotaroute.com/route/376867"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance >= 5 and distance < 10:
                route1="Gap to Mini 10k, 15.449km: https://www.plotaroute.com/route/226528"
                route2="Gap to NYC Half Cheering, 9.793km: https://www.plotaroute.com/route/373863"
                route3="Brooklyn Bridge Park, 8.305km: https://www.plotaroute.com/route/295224"
                route4="Prospect Park Loop, 9.444km: https://www.plotaroute.com/route/399377"
                route5="Central Park, 14.770km: https://www.plotaroute.com/route/257939"
                route6="Yankee Stadium, 11.521km: https://www.plotaroute.com/route/272288"
                route7="Roosevelt Island and Back, 13.618km: https://www.plotaroute.com/route/210742"
                route8="East River Run, 8.478km: https://www.plotaroute.com/route/391510"
                route9="Central Park Loop, 15.66km: https://www.plotaroute.com/route/292847"
                route10="East Bushwick 5.4 mile run, 8.805km: https://www.plotaroute.com/route/154495"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 5: 
                route1="Ollis Running Route, 5.005km: https://www.plotaroute.com/route/423590"
                route2="Prospect Park Run, 3.433miles: https://www.plotaroute.com/route/341044"
                route3="Run around St. Nicholas Park, 3.360km: https://www.plotaroute.com/route/10007"
                route4="Central Park Run, 0.735km: https://www.plotaroute.com/route/251942"
                route5="Gap to Brooklyn Roasting Company, 6.416km: https://www.plotaroute.com/route/350389"
                route6="Madison Square Park Run, 5.506km: https://www.plotaroute.com/route/357035"
                route7="Riverside Park, 4.318km: https://www.plotaroute.com/route/10008"
                route8="4 miles in Brooklyn, 6.451km: https://www.plotaroute.com/route/229079"
                route9="Roosevelt Island Run, 6.520km: https://www.plotaroute.com/route/415570"
                route10="Meadow Park, 6.081km: https://www.plotaroute.com/route/154516"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            #parks 

        if nearestcity=="houston":
            if distance >= 10:
                route1="Green Belt Run, 16.250km: https://www.plotaroute.com/route/19132"
                route2="2017 Chevron Houston Marathon, 41.486km: https://www.plotaroute.com/route/327701"
                route3="Memorial Park to Buffalo Bayou Loop, 17.041km: https://www.plotaroute.com/route/174521"
                route4="Half marathon run, 22.077km: https://www.plotaroute.com/route/131369"
                route5="White Oak 15 mile route, 24.146km: https://www.plotaroute.com/route/315006"
                route6="12 mile long run, 19.345km: https://www.plotaroute.com/route/331374"
                route7="Sabine from Straetching Deck, 16.786km: https://www.plotaroute.com/route/482335"
                route8="Half marathon, 21.234km: https://www.plotaroute.com/route/172689"
                route9="15 mile run, 23.706km: https://www.plotaroute.com/route/313870"
                route10="White Oak run, 20.240km: https://www.plotaroute.com/route/478187"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance >= 5 and distance < 10:
                route1="Houston Westchase, 8.623km: https://www.plotaroute.com/route/81614"
                route2="8 mile run, 12.876km: https://www.plotaroute.com/route/83736"
                route3="6 mile run, 9.719km: https://www.plotaroute.com/route/114943"
                route4="5 mile run, 8.258km: https://www.plotaroute.com/route/315529"
                route5="Neighborhood run, 8.295km: https://www.plotaroute.com/route/24342"
                route6="Bay Oaks, 12.037km: https://www.plotaroute.com/route/97411"
                route7="Rice 7 mile run, 11.623km: https://www.plotaroute.com/route/315540"
                route8="5 mile route, 8.439km: https://www.plotaroute.com/route/315535"
                route9="Kirkwood, 13.686km: https://www.plotaroute.com/route/240044"
                route10="Rice 12k, 12.312km: https://www.plotaroute.com/route/238350"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 5: 
                route1="Town Lake, 3.899km: https://www.plotaroute.com/route/181331"
                route2="5k run, 5.003km: https://www.plotaroute.com/route/278966"
                route3="Kung Fu Run Club, 3 mile route, 5.003km: https://www.plotaroute.com/route/315537"
                route4="Nana's Loop, 0.939km: https://www.plotaroute.com/route/385153"
                route5="5 mile run, 4.025km: https://www.plotaroute.com/route/434392"
                route6="Short 5k, 5.453km: https://www.plotaroute.com/route/441262"
                route7="Torry Pines Loop, 1.614km: https://www.plotaroute.com/route/293307"
                route8="Memorial to Chatsworth 5 Miles, 7.885km: https://www.plotaroute.com/route/482328"
                route9="Bromptom Around the Block, 2.264km: https://www.plotaroute.com/route/321764"
                route10="5 Mile run, 7.637km: https://www.plotaroute.com/route/315538"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="dallas": 
            #parks 
            if distance >= 10:
                route1="18 mile dallas marathon preview, 29.023km: https://www.plotaroute.com/route/282863"
                route2="Dallas Marathon route, 43.171km: https://www.plotaroute.com/route/280904"
                route3="13.1 mile run: https://www.plotaroute.com/route/17388"
                route4="10 mile run: https://www.plotaroute.com/route/145890"
                route5="10 mile run: https://www.plotaroute.com/route/153095"
                route6="M Strees/Lakewood, 16.103km: https://www.plotaroute.com/route/184050"
                route7="17.212k run: https://www.plotaroute.com/route/170261"
                route8="46.3k run: https://www.plotaroute.com/route/5475"
                route9="BMW Dallas Marathon 18.058km: https://www.plotaroute.com/route/328056"
                route10="Brookhaven College 16k run: https://www.plotaroute.com/route/145890"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance >= 5 and distance < 10:
                route1="Tour Des Fleur, Quarter Marathon, 10.636km: https://www.plotaroute.com/route/445878"
                route2="Dallas 10k, 10.479km: https://www.plotaroute.com/route/445878"
                route3="Dallas 14k, 14.269km: https://www.plotaroute.com/route/433285"
                route4="Bridges Downtown, 9.976km: https://www.plotaroute.com/route/176072"
                route5="Oaklaw 10k, 9.659km: https://www.plotaroute.com/route/169255"
                route6="Social Growler, 8.137km: https://www.plotaroute.com/route/322805"
                route7="8 mile run, 13.341km: https://www.plotaroute.com/route/170659"
                route8="Downtown run, 10.205km: https://www.plotaroute.com/route/178260"
                route9="6 mile loop, 9.418km: https://www.plotaroute.com/route/254550"
                route10="7 mile loop, 11.398km: https://www.plotaroute.com/route/265780"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 5: 
                route1="Lakewood 5k, 5.311km: https://www.plotaroute.com/route/69915"
                route2="1 mile run, 1.691km: https://www.plotaroute.com/route/27933"
                route3="Social from Growler, 5.204km: https://www.plotaroute.com/route/322803"
                route4="Biergarten at the Omni, 4 miles, 6.661km: https://www.plotaroute.com/route/173878"
                route5="Short run, 3.115km: https://www.plotaroute.com/route/78414"
                route6="Short run II, 5.864km: https://www.plotaroute.com/route/146505"
                route7="Deep Ellem 5km: https://www.plotaroute.com/route/319184"
                route8="3 mile route, 4.817km: https://www.plotaroute.com/route/252242"
                route9="Baileys 5k, 5.153km: https://www.plotaroute.com/route/146467"
                route10="Exall Park Jog, 4.208km: https://www.plotaroute.com/route/347227"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))


        if nearestcity=="san antonio":
            #parks 
            if distance >= 10:
                route1="Dragons Half Marathon Loop: 21.0km: https://www.plotaroute.com/route/263995"
                route2="16.694k run: https://www.plotaroute.com/route/369665"
                route3="10 mile run: https://www.plotaroute.com/route/369661"
                route4="McAllister 10 Mile Loop: https://www.plotaroute.com/route/302799"
                route5="Fleetfeet Marathon Run, 43.227km: https://www.plotaroute.com/route/239226"
                route6="Salado Creek Greenway, 32.2km: https://www.plotaroute.com/route/308044"
                route7="Battle of Leon Creek 10 miler, 16.067km: https://www.plotaroute.com/route/309628"
                route8="Bulverde 15 24km, https://www.plotaroute.com/route/286810"
                route9="Prickly Pear 50k: https://www.plotaroute.com/route/306675"
                route10="Battle of Leon 15 mile route: https://www.plotaroute.com/route/309625"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance >= 5 and distance < 10:
                route1="Battle of Salado 16km: https://www.plotaroute.com/route/292447"
                route2="Dragon's Deno Final 10km: https://www.plotaroute.com/route/264001"
                route3="Battle of Salado 8km: https://www.plotaroute.com/route/292450"
                route4="Winter Dragon Half Loop, 10.564km: https://www.plotaroute.com/route/335997"
                route5="Museum Reach Tour, 9.678km: https://www.plotaroute.com/route/113417"
                route6="Carnival of Venice 13.1 relay, 8.475km: https://www.plotaroute.com/route/177965"
                route7="Mcallister run, 8.864km: https://www.plotaroute.com/route/480366"
                route8="6 mile run, 10.040km: https://www.plotaroute.com/route/265619"
                route9="6M route, rim perimeter, 9.656km: https://www.plotaroute.com/route/256457"
                route10="9 mile route zarzamora, 14.485km: https://www.plotaroute.com/route/121166"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 5: 
                route1="SA 5k series 2 course, 4.990km: https://www.plotaroute.com/route/390262"
                route2="SA 5k Series 1 & 4 course, 5.022km: https://www.plotaroute.com/route/390267"
                route3="SA 5k series 3 course, 4.961km: https://www.plotaroute.com/route/390289"
                route4="Freedom Day Four Miler, 6.445km: https://www.plotaroute.com/route/235987"
                route5="Dragon's Den Final 5k: https://www.plotaroute.com/route/263986"
                route6="Windcrest 5k, 4.902km: https://www.plotaroute.com/route/186871"
                route7="Historic Downtown Tour, 4.979km: https://www.plotaroute.com/route/113445"
                route8="Midsummer Nights Women 5k run, 5.005km: https://www.plotaroute.com/route/194805"
                route9="Carnival 5k, 5.05km: https://www.plotaroute.com/route/387656"
                route10="4 Mile run, 6.437km: https://www.plotaroute.com/route/120914"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="austin": 
            #parks 
            if distance >= 10:
                route1="Congress Boardwalk Loop, 18.009km: https://www.plotaroute.com/route/31563"
                route2="10 mile run, 17.071km: https://www.plotaroute.com/route/169305"
                route3="3M Half Marathon, 21.257km: https://www.plotaroute.com/route/34766"
                route4="Run Austin --> Dallas, 30.559km: https://www.plotaroute.com/route/9945"
                route5="10 mile run II, 16.441km: https://www.plotaroute.com/route/306166"
                route6="Austin Park Run, 17.016km: https://www.plotaroute.com/route/322121"
                route7="Bluegrass loop, 16.472km: https://www.plotaroute.com/route/175931"
                route8="Gorzycky Beckett, 16.230km: https://www.plotaroute.com/route/390762"
                route9="Juiceland Marafun, 20.515km: https://www.plotaroute.com/route/278471"
                route10="The Haunted Half Marathon, 21.083km: https://www.plotaroute.com/route/442259"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance >= 5 and distance < 10:
                route1="8 mile run: https://www.plotaroute.com/route/19749"
                route2="Zimlow 7 run, 12.011km: https://www.plotaroute.com/route/29507"
                route3="Riverside / UT Staduim, 8 miles: https://www.plotaroute.com/route/169334"
                route4="Zilker Loo, 8 miles: https://www.plotaroute.com/route/169307"
                route5="North 5.6 miles, 9.074km: https://www.plotaroute.com/route/113095"
                route6="10k loop, 10.101km: https://www.plotaroute.com/route/306782"
                route7="6 miles inside marathon course, 9.690km: https://www.plotaroute.com/route/37608"
                route8="6 mile run II, 10.034km: https://www.plotaroute.com/route/292862"
                route9="Riverside to Capitol, 6 miles: https://www.plotaroute.com/route/169330"
                route10="8 mile lake run, 13.414km: https://www.plotaroute.com/route/146984"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 5: 
                route1="1 mile: https://www.plotaroute.com/route/44755"
                route2="2 mile run: https://www.plotaroute.com/route/57831"
                route3="Wework Beer Run, 5.711km: https://www.plotaroute.com/route/163635"
                route4="3.411 miles from River Oaks, 5.489km: https://www.plotaroute.com/route/163322"
                route5="Desultory Empire Run, 6.438km: https://www.plotaroute.com/route/165014"
                route6="Lyde to Tower, 1.119km: https://www.plotaroute.com/route/456283"
                route7="2.8 mile, road/trail, 4.644km: https://www.plotaroute.com/route/210094"
                route8="Sandra small loop, 2.174km: https://www.plotaroute.com/route/224900"
                route9="UT Texas, short route, 4.715km: https://www.plotaroute.com/route/310952"
                route10="UT Texas, short route 2, 3.067km: https://www.plotaroute.com/route/310959"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="atlanta": 
            #piedmont park, georgia tech pi mile 
            if distance >= 10:
                route1="Publix Marathon, 43.364km: https://www.plotaroute.com/route/180944"
                route2="Atlanta Marathon, 43.154km: https://www.plotaroute.com/route/234010"
                route3="10 mile route, 16.2km: https://www.plotaroute.com/route/116671"
                route4="10 mile route 2, 16.596km: https://www.plotaroute.com/route/356877"
                route5="10 mile loop, 16.318km: https://www.plotaroute.com/route/126246"
                route6="Half Marathon, 21.083km: https://www.plotaroute.com/route/235109"
                route7="11 mile route, 18.166km: https://www.plotaroute.com/route/316333"
                route8="16 mile run, 25.943km: https://www.plotaroute.com/route/477076"
                route9="11 mile rune, 17.853km: https://www.plotaroute.com/route/401244"
                route10="10 mile, Cumberland Mall Route, 10.118miles: https://www.plotaroute.com/route/371409"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance >= 5 and distance < 10:
                route1="Freedom Trail, 8.035km: https://www.plotaroute.com/route/122829"
                route2="5 mile run, 8.439km: https://www.plotaroute.com/route/407922"
                route3="Peachtree Road Race, 9.978km: https://www.plotaroute.com/route/234912"
                route4="10k route: https://www.plotaroute.com/route/44805"
                route5="Brookhaven 10k, 10.167km: https://www.plotaroute.com/route/137157"
                route6="Belt Line 6 miles, 9.77km: https://www.plotaroute.com/route/331729"
                route7="Piedmont Park, 5.965 miles: https://www.plotaroute.com/route/165300"
                route8="7 mile run, 11.91km: https://www.plotaroute.com/route/390280"
                route9="Running into the city, 9.144km: https://www.plotaroute.com/route/44876"
                route10="Piedmont Park, 6.5miles, 10.483km: https://www.plotaroute.com/route/246373"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 5: 
                route1="Divine Nine 5k, 4.994km: https://www.plotaroute.com/route/207919"
                route2="Garden Hills 5k run, 5.018km: https://www.plotaroute.com/route/66019"
                route3="CoC 5k run, 4.828km: https://www.plotaroute.com/route/289513"
                route4="ILab Freedom Parkway Loop, 4.768km: https://www.plotaroute.com/route/136368"
                route5="Grant Park, 7.186km: https://www.plotaroute.com/route/350198"
                route6="Atlantic Station 2 miles, 3.325km: https://www.plotaroute.com/route/204033"
                route7="Dragon Con 3.5 mile, 5.758km: https://www.plotaroute.com/route/102843"
                route8="4 mile Beltline Run, 6.438km: https://www.plotaroute.com/route/407986"
                route9="3 mile Brookhaven, 5.100km: https://www.plotaroute.com/route/131940"
                route10="2 park run, 7.238km: https://www.plotaroute.com/route/462587"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="seattle": 
            #run near reza 
            if distance >= 10:
                route1="12 mile run, 20.190km: https://www.plotaroute.com/route/43875"
                route2="16 mile run, 25.324km: https://www.plotaroute.com/route/43869"
                route3="Half maraton, 19.196km: https://www.plotaroute.com/route/22077"
                route4="20 mile run, 29.995km: https://www.plotaroute.com/route/369844"
                route5="12 mile run, 19.123km: https://www.plotaroute.com/route/296297"
                route6="Seattle Half Interlaken, 18.280km: https://www.plotaroute.com/route/308406"
                route7="14 mile run, 22.122km: https://www.plotaroute.com/route/280796"
                route8="10 mile run, 16.694km: https://www.plotaroute.com/route/424552"
                route9="No bones run, 21.375km: https://www.plotaroute.com/route/480872"
                route10="12.5miles, 20.109km: https://www.plotaroute.com/route/216039"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance >= 5 and distance < 10:
                route1="7 Mile loop, 11.128km: https://www.plotaroute.com/route/42441"
                route2="Madrona/CD, 8.031km: https://www.plotaroute.com/route/42428"
                route3="65th and OVer, 10.752km: https://www.plotaroute.com/route/142833"
                route4="6 mile run, 9.390km: https://www.plotaroute.com/route/47340"
                route5="Madrona, 12.948km: https://www.plotaroute.com/route/133522"
                route6="Seward Park, 8 miles, 13.707km: https://www.plotaroute.com/route/419618"
                route7="10k loop, 10.040km: https://www.plotaroute.com/route/198275"
                route8="Fremont to Ballard to Sea view and Back, 8 miles, 12.633km: https://www.plotaroute.com/route/224914"
                route9="5 mile run, 8.410km: https://www.plotaroute.com/route/34627"
                route10="Lincoln Park Trail Loop, 8 miles, 13.436km: https://www.plotaroute.com/route/472580"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 5: 
                route1="5K Clvoer Dash, 5.0km: https://www.plotaroute.com/route/163014"
                route2="Pennys4Change Sunset Run 5k, 4.99km: https://www.plotaroute.com/route/211266"
                route3="Ballard/Golden Gardens Loop, 7.452km: https://www.plotaroute.com/route/252792"
                route4="Motive Runinng Route, 5.544km: https://www.plotaroute.com/route/247738"
                route5="32nd & Cherry 4 Miler, 6.468km: https://www.plotaroute.com/route/44659"
                route6="Hot Chocolate 5k, 5.576km: https://www.plotaroute.com/route/175787"
                route7="I90 Tunnel 5 Mile, 7.986km: https://www.plotaroute.com/route/42435"
                route8="3 mile run, 5.080km: https://www.plotaroute.com/route/34465"
                route9="Spring Forward 2017 5k, 2.423km: https://www.plotaroute.com/route/347232"
                route10="3.5 mile loop, 6.138km: https://www.plotaroute.com/route/195123"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="san francisco": 
            #run along the bay 
            if distance >= 10:
                route1="HeyHeys SF Trail Challenge, 21.275km: https://www.plotaroute.com/route/173801"
                route2="10 Mile Ocean Beach - Lake Merced, 16.136km: https://www.plotaroute.com/route/74273"
                route3="Best of SF, 19.749km: https://www.plotaroute.com/route/130399"
                route4="Presidio, 17.104km: https://www.plotaroute.com/route/247153"
                route5="Footing Long, 17.019km: https://www.plotaroute.com/route/123496"
                route6="SF Long Run, 23.180km: https://www.plotaroute.com/route/123500"
                route7="10 mile route in SF, 16.101km: https://www.plotaroute.com/route/193670"
                route8="14 mile route, SF, 22.608km: https://www.plotaroute.com/route/284042"
                route9="Dolores Park 12 Miles, 19.462km: https://www.plotaroute.com/route/276013"
                route10="Ocean Beach Run, 22.959km: https://www.plotaroute.com/route/245642"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance >= 5 and distance < 10:
                route1="10k Open XC Chaps, 10.091km: https://www.plotaroute.com/route/142409"
                route2="8 mile Ocean Beach Run, 12.899km: https://www.plotaroute.com/route/66389"
                route3="8.2 Mile Downtown & Mission, 13.163km: https://www.plotaroute.com/route/9745"
                route4="15.6km Golden Gate and Buena Vista, 15.654km: https://www.plotaroute.com/route/9748"
                route5="5 mile run, 8.058km: https://www.plotaroute.com/route/223190"
                route6="SF Marina Green Triangle Presidio, 8.243km: https://www.plotaroute.com/route/186576"
                route7="12k Presidio, 11.973km: https://www.plotaroute.com/route/9750"
                route8="5 mile Mission Bay, 8.291km: https://www.plotaroute.com/route/9750"
                route9="Hills of SFO, 8.90km: https://www.plotaroute.com/route/25579"
                route10="Embarcadero run, 8.178km: https://www.plotaroute.com/route/244111"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))
            
            if distance < 5: 
                route1="VFit community Run, 5.412km: https://www.plotaroute.com/route/100909"
                route2="Hayes Valley Loop, 3.331km: https://www.plotaroute.com/route/275994"
                route3="Clayton to Twin Peaks, 1.992km: https://www.plotaroute.com/route/169120"
                route4="Pier39, 1.127km: https://www.plotaroute.com/route/251261"
                route5="Alamo Square Park, 4.701km: https://www.plotaroute.com/route/109208"
                route6="5k San Fran, 5.035km: https://www.plotaroute.com/route/89131"
                route7="Lake Merced, 7.312km: https://www.plotaroute.com/route/66327"
                route8="The Mission, 5.332km: https://www.plotaroute.com/route/244112"
                route9="Kaiser PErmanente 5k, 5.074km: https://www.plotaroute.com/route/162859"
                route10="Strawberry Hill, 4.132km: https://www.plotaroute.com/route/316222"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="los angeles":
            #run in city somewhere..
            if distance >= 10:
                route1="Elysian to Sunset, 20.302km: https://www.plotaroute.com/route/341428"
                route2="20.5 mile trianing run, 33.011km: https://www.plotaroute.com/route/284151"
                route3="14 miles, 22.429km: https://www.plotaroute.com/route/327353"
                route4="Westwood - UCLA, 28.690km:https://www.plotaroute.com/route/327374 "
                route5="11 mile run, 17.858km: https://www.plotaroute.com/route/327089"
                route6="10 mile Westwood, 16.985km: https://www.plotaroute.com/route/352173"
                route7="Taco Bell Woodley-Aliso Tral, 16.464km: https://www.plotaroute.com/route/220432"
                route8="Elysian to West Hollywood, 10 miles, 17.338km: https://www.plotaroute.com/route/351761"
                route9="16 mile LAX, 26.617km: https://www.plotaroute.com/route/357624"
                route10="15 mile LAX, 24.149km: https://www.plotaroute.com/route/288024"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance >= 5 and distance < 10:
                route1="Acari, 9.284km: https://www.plotaroute.com/route/159734"
                route2="Elysian 6 mile loop, 10.473km: https://www.plotaroute.com/route/322094"
                route3="Camp Josepho, 9.493km: https://www.plotaroute.com/route/310121"
                route4="Grove 10k, 9.466km: https://www.plotaroute.com/route/156823"
                route5="5 mile rune, 8.082km: https://www.plotaroute.com/route/20304"
                route6="9 miles in Edmond, 15.157km: https://www.plotaroute.com/route/165816"
                route7="Cal State Neighborhood Hill Run, 8.368km: https://www.plotaroute.com/route/298635"
                route8="MDR Pier2, 11.343km: https://www.plotaroute.com/route/348076"
                route9="Hansen Dam, 9 miles, 15.827km: https://www.plotaroute.com/route/343374"
                route10="5.31 mile Hill Run/hike, 8.549km: https://www.plotaroute.com/route/298648"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 5: 
                route1="CAA Run Club, 2.705km: https://www.plotaroute.com/route/20687"
                route2="CAA Run Club II, 5.137km: https://www.plotaroute.com/route/13957"
                route3="LA City Route, 7.376km: https://www.plotaroute.com/route/3942"
                route4="LACMA & Farmers Market, 3.952km: https://www.plotaroute.com/route/333793"
                route5="3 mile run, 5.060km: https://www.plotaroute.com/route/263999"
                route6="Nike Tower Run, 2.723km: https://www.plotaroute.com/route/237653"
                route7="3 mile run II, 4.852km: https://www.plotaroute.com/route/263940"
                route8="LA Short Run, 3.245km: https://www.plotaroute.com/route/333649"
                route9="2 mile mini hill, 3.354km: https://www.plotaroute.com/route/422508"
                route10="Longridge Hill Route, 5.813km: https://www.plotaroute.com/route/334469"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

    if exercise == "bike":
        
        if nearestcity == "chicago":
            if distance>=100:
                route1="Chicago to Cleveland: https://www.plotaroute.com/route/473197"
                route2="Chicago to Grand Rapids, 323.0569km: https://www.plotaroute.com/route/238168"
                return str(randomrouteselection(route1,route1,route1,route1,route1,route2,route2,route2,route2,route2))
            
            if distance >= 10 and distance <100:
                route1="Chicity to northwestern bike, 14.379 miles: https://www.plotaroute.com/route/490411"
                route2="Northwestern to Chicity bike, 13.214 miles: https://www.plotaroute.com/route/490416"
                route3="Chicago Botanical Gardens and back, 18.791 miles: https://www.plotaroute.com/route/457007"
                route4="Ride Ataxia Chicago, 27 miles: https://www.plotaroute.com/route/453860"
                route5="Chicago road loop, 20.638 miles: https://www.plotaroute.com/route/440633"
                route6="Chicago long distance, 84 miles: https://www.plotaroute.com/route/379170"
                route7="10 mile west town loop, 17.084 km: https://www.plotaroute.com/route/176494"
                route8="Clybourn Clark - 24.994 km: https://www.plotaroute.com/route/199590"
                route9="Bike route - 26.779 km: https://www.plotaroute.com/route/265519"
                route10="10 miles the hard way, 17.037 km: https://www.plotaroute.com/route/251044"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 10:
                route1="Kessel run, 12.594 km: https://www.plotaroute.com/route/177766"
                route2="5k DIA, 8.642 km: https://www.plotaroute.com/route/285758"
                route3="5 mile west town loop: https://www.plotaroute.com/route/177295"
                route4="Bud Biliken Route, 14.718 km: https://www.plotaroute.com/route/243477"
                route5="To the Dingo Palace, 12.521 km: https://www.plotaroute.com/route/197828"
                route6="Home to work, 10.510 km: https://www.plotaroute.com/route/440464"
                route7="7 mile west town, 11.242 km: https://www.plotaroute.com/route/378930"
                route8="1 mile loop, 1.690km: https://www.plotaroute.com/route/11847"
                route9="Reside on Clark 4 miles, 6.433 km: https://www.plotaroute.com/route/230292"
                route10="Belmont 2.5 miles, 3.967 km: https://www.plotaroute.com/route/312303"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))
            
        if nearestcity=="boston":
            #bikepaths
            if distance >= 100:
                route1="Boston Town Route, 205.135km: https://www.plotaroute.com/route/108985"
                route2="Boston to Providence, 180.853km: https://www.plotaroute.com/route/325399"
                return str(randomrouteselection(route1,route1,route1,route1,route1,route2,route2,route2,route2,route2))
            
            if distance >= 10 and distance <100:
                route1="TD Hub on Wheel, 40 miles, 64.203km: https://www.plotaroute.com/route/216179"
                route2="Ride to Hopkinton, 43.603km: https://www.plotaroute.com/route/197842"
                route3="Boston-NYC bike, 82.823km: https://www.plotaroute.com/route/88945"
                route4="Walden Pond Allston, 62.007km: https://www.plotaroute.com/route/398850"
                route5="33 mile road bike route, 64.482km: https://www.plotaroute.com/route/89059"
                route6="50 mile bike route, 81.358km: https://www.plotaroute.com/route/423208"
                route7="Greenways Research, 20.541km: https://www.plotaroute.com/route/15188"
                route8="Greenway Pierre-Lamont Loop, 19.417km: https://www.plotaroute.com/route/272596"
                route9="Brookline Loop, 19.352km: https://www.plotaroute.com/route/250301"
                route10="Esplanade, 17.150km: https://www.plotaroute.com/route/429763"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 10: 
                route1="Arbouretum Loop, 8.016km: https://www.plotaroute.com/route/233931"
                route2="JPond & Olmstead Loop, 8.673km: https://www.plotaroute.com/route/233944"
                route3="Bike Route, 13.989km: https://www.plotaroute.com/route/429091"
                route4="Charles River, 13.074km: https://www.plotaroute.com/route/454237"
                route5="6 miler from Charles River and WGBH, 9.656km: https://www.plotaroute.com/route/252271"
                route6="Charles River, 10.041km: https://www.plotaroute.com/route/458023"
                route7="Fenway loop, 9.952km: https://www.plotaroute.com/route/385220"
                route8="Boston 9 miles, 15.390km: https://www.plotaroute.com/route/284141"
                route9="North/South End Rune, 15.401km: https://www.plotaroute.com/route/280293"
                route10="Esplanade 10k, 10.047km: https://www.plotaroute.com/route/294097"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="philadelphia":
            #bikepaths
            if distance >= 100:
                route1="Tour De Shore, 161.214km: https://www.plotaroute.com/route/183882"
                route2="Philly French Creek, 165km: https://www.plotaroute.com/route/107333"
                return str(randomrouteselection(route1,route1,route1,route1,route1,route2,route2,route2,route2,route2))
            
            if distance >= 10 and distance<100:
                route1="Atlantic City Bike Ride, 100km: https://www.plotaroute.com/route/456050"
                route2="56 mile route: https://www.plotaroute.com/route/457393"
                route3="15 mile bike: https://www.plotaroute.com/route/363797"
                route4="35 mile bike ride: https://www.plotaroute.com/route/477035"
                route5="Philly to Prinecton, 67.271km; https://www.plotaroute.com/route/385205"
                route6="Biking on a few hills, 54.304km: https://www.plotaroute.com/route/283664"
                route7="Philly to Bethlehem District, 95.409km: https://www.plotaroute.com/route/433409"
                route8="Philly to Morgantown, 85.995km: https://www.plotaroute.com/route/395998"
                route9="155.548 km bike: https://www.plotaroute.com/route/395998"
                route10="Hilly Philly, 48.071km: https://www.plotaroute.com/route/395998"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))
            
            if distance < 10: 
                route1="Around Philly, 14.418km: https://www.plotaroute.com/route/122091"
                route2="Philly-Phyler Circuit, 10.661km: https://www.plotaroute.com/route/368980"
                route3="Philadelphia Zoo, Liberty Bell, Canden, 6.169miles: https://www.plotaroute.com/route/250858"
                route4="Easy Riverside, 14.003km: https://www.plotaroute.com/route/453084"
                route5="Bike Ride, 11.2189km: https://www.plotaroute.com/route/219671"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route1,route2,route3,route4,route5))

        if nearestcity=="new york city":
            #bikepaths
            if distance >= 100:
                route1="Park Route, 299.283km: https://www.plotaroute.com/route/157252"
                route2="Nye State, 2385.550km: https://www.plotaroute.com/route/271160"
                return str(randomrouteselection(route1,route1,route1,route1,route1,route2,route2,route2,route2,route2))
            
            if distance >= 10 and distance<100:
                route1="64.533km bike, https://www.plotaroute.com/route/188311"
                route2="40.942km bike ride, https://www.plotaroute.com/route/188344"
                route3="Five Boro bike tour, 66.713km: https://www.plotaroute.com/route/409309"
                route4="Manhattan distance, 40.778km: https://www.plotaroute.com/route/183912"
                route5="Bronx, 38.290km: https://www.plotaroute.com/route/265072"
                route6="Central Park distance, 47.635km: https://www.plotaroute.com/route/264936"
                route7="Roosevelt Island, 27.825km: https://www.plotaroute.com/route/17747"
                route8="Bike to Hoboken, 43.965km: https://www.plotaroute.com/route/215575"
                route9="Corona Park, 16.351km: https://www.plotaroute.com/route/195567"
                route10="Alpine Loop, 59.485km: https://www.plotaroute.com/route/438239"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 10: 
                route1="Brooklyn Bridge, 8577km: https://www.plotaroute.com/route/233974"
                route2="Central Park, 14.221km: https://www.plotaroute.com/route/195568"
                route3="Central Park II, 10.400km: https://www.plotaroute.com/route/264948"
                route4="Harlem, 9.799km: https://www.plotaroute.com/route/190042"
                route5="Empire State Building to Brooklyn, 6.409 miles: https://www.plotaroute.com/route/452374"
                route6="Harlem - Central Park, 2.859 miles: https://www.plotaroute.com/route/175775"
                route7="Midtown to Forest Hills, 9.853 miles: https://www.plotaroute.com/route/396010"
                route8="Central Park Loop to Midtown, 8.937miles: https://www.plotaroute.com/route/403960"
                route9="Queens College Bike Route, 8.231 miles: https://www.plotaroute.com/route/195566"
                route10="Manhattan, Riverside Drive, 7.538miles: https://www.plotaroute.com/route/489197"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="houston":
            #bikepaths
            if distance >= 100:
                route1="no bike routes here"
                route2="no bike routes here"
                return str(randomrouteselection(route1,route1,route1,route1,route1,route2,route2,route2,route2,route2))
            
            if distance >= 10 and distance<100:
                route1="Park to Port, 32.818km: https://www.plotaroute.com/route/291180"
                route2="Park to Port II, 32.837km: v"
                route3="Brays Bayou Trail Loop, 22.694km: https://www.plotaroute.com/route/76588"
                route4="George Bush and Bayou 50 Miles: https://www.plotaroute.com/route/74639"
                route5="Tour De Breweries =, Houston, 51.874km: https://www.plotaroute.com/route/347675"
                route6="Terry Hershey / George Bush 50 Mile Route, 80.725km: https://www.plotaroute.com/route/53359"
                route7="Addicks Reservoir, 34.727km: https://www.plotaroute.com/route/186699"
                route8="Neighborhood Bike, 32.228km: https://www.plotaroute.com/route/88233"
                route9="Huffman Loop, 43.435km: https://www.plotaroute.com/route/149624"
                route10="Van Fleet to Eupora, 57.039km: https://www.plotaroute.com/route/325779"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))
            if distance < 10: 
                route1="BBVA Route, 5.960km: https://www.plotaroute.com/route/109556"
                route2="George Bush Park Houston, 14.007km: https://www.plotaroute.com/route/72517"
                route3="Hersey Park, 13.253km: https://www.plotaroute.com/route/147306"
                route4="Short 14km Cycle, 14.864km: https://www.plotaroute.com/route/7344"
                route5="TC Jester Route, 10.720km: https://www.plotaroute.com/route/201163"
                route6="Heights Bike Trail Brewery Tour, 7.029km: https://www.plotaroute.com/route/403911"
                route7="Easy Bike Route Heights, 8.347km: https://www.plotaroute.com/route/206255"
                route8="Donut Route, 6.004km: https://www.plotaroute.com/route/201735"
                route9="Bike museum, 11.793km: https://www.plotaroute.com/route/429226"
                route10="Cedar Creek, 1.161km: https://www.plotaroute.com/route/204176"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="dallas": 
            #bikepaths
            if distance >= 100:
                route1="Penn 110 route, 164km: https://www.plotaroute.com/route/126070"
                route2="Interstate 45 South, 461.947km: https://www.plotaroute.com/route/25267"
                return str(randomrouteselection(route1,route1,route1,route1,route1,route2,route2,route2,route2,route2))
            
            if distance >= 10 and distance<100:
                route1="White Rock Ride, 37.541km: https://www.plotaroute.com/route/4139"
                route2="40 Miles South and West Dallas, 66.931km: https://www.plotaroute.com/route/5412"
                route3="Hill Route, 45.771km: https://www.plotaroute.com/route/5478"
                route4="Lake Lap with Hills, 16.010km: https://www.plotaroute.com/route/5480"
                route5="Lake Lap, 20.624km: https://www.plotaroute.com/route/5479"
                route6="White Rock, 52 miles, 84.165km: https://www.plotaroute.com/route/116779"
                route7="Dallas White Rock Creek, 74.982km: https://www.plotaroute.com/route/93663"
                route8="75 Mile White Rock Training with Stops, 122.069km: https://www.plotaroute.com/route/90165"
                route9="NE Dallas into East Planto, 18.517km: https://www.plotaroute.com/route/247144"
                route10="LBJ-Lake and Downtown to LBJ, 58.078km: https://www.plotaroute.com/route/95377"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 10: 
                route1="Parade Route, 3.099km: https://www.plotaroute.com/route/275763"
                route2="La Vista, 3.821km: https://www.plotaroute.com/route/274681"
                route3="White Rock Lake, 15.590km: https://www.plotaroute.com/route/90093"
                route4="Swiss Longer Loop, 4.268km: https://www.plotaroute.com/route/275063"
                route5="White Rock Short, 13.273km: https://www.plotaroute.com/route/22358"
                route6="La Vista Shortcut, 3.589km: https://www.plotaroute.com/route/274686"
                route7="Castle Hill, 12.743km: https://www.plotaroute.com/route/441700"
                route8="8.509km bike: https://www.plotaroute.com/route/367737"
                route9="3.403km route: https://www.plotaroute.com/route/274673"
                route10="3.430km route: https://www.plotaroute.com/route/274675"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="san antonio":
            #bikepaths
            if distance >= 100:
                route1="171 km bike ride, 171.447km: https://www.plotaroute.com/route/32703"
                route2="171 km bike ride, 171.447km: https://www.plotaroute.com/route/32703"
                return str(randomrouteselection(route1,route1,route1,route1,route1,route2,route2,route2,route2,route2))
            
            if distance >= 10 and distance<100:
                route1="Tour de Las Misiones, 22 Mile Route, 34.829km: https://www.plotaroute.com/route/263934"
                route2="Tour de Las Misiones, 14 mile route, 21.865km: https://www.plotaroute.com/route/284498"
                route3="16km Bike ride: https://www.plotaroute.com/route/420677"
                route4="47.904km bike ride: https://www.plotaroute.com/route/784"
                route5="Flying J to Monkey Island, 122.726km: https://www.plotaroute.com/route/64317"
                route6="35.195km bike ride: https://www.plotaroute.com/route/365251"
                route7="West SSide, 74.227km: https://www.plotaroute.com/route/43506"
                route8="Brackenridge to Missions, 46.724km: https://www.plotaroute.com/route/93728"
                route9="The Raspa Ride, 29.715km: https://www.plotaroute.com/route/430697"
                route10="Sam Houston to Northwest Crossing, 34.663km: https://www.plotaroute.com/route/230873"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 10: 
                route1="Tour de Las Misiones, 7 mile optional, 10.569km: https://www.plotaroute.com/route/264366"
                route2="5k cycle path, 5.511km: https://www.plotaroute.com/route/356774"
                route3="7 mile bike ride, 12.154km: https://www.plotaroute.com/route/365264"
                route4="12.092km bike ride, South San Antonio: https://www.plotaroute.com/route/25261"
                route5="Watermelon rise, 13.926km: https://www.plotaroute.com/route/430685"
                route6="Downtown to Brack, 13.058km: https://www.plotaroute.com/route/356493"
                route7="9.012km bike ride: https://www.plotaroute.com/route/190484"
                route8="Short bike route, 1.173km: https://www.plotaroute.com/route/253292"
                route9="12.087km bike ride north, https://www.plotaroute.com/route/25259"
                route10="Chung Time Trial, 12.082km: https://www.plotaroute.com/route/347028"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="austin": 
            #bikepaths
            if distance >= 100:
                route1="Livestrong 2015, 161.254km: https://www.plotaroute.com/route/125087"
                route2="Tour de Texas, Hill Country, 504.470km: https://www.plotaroute.com/route/424506"
                route3="Liege Bastogne Austin, 177.146km: https://www.plotaroute.com/route/105743"
                return str(randomrouteselection(route1,route1,route1,route1,route1,route2,route2,route3,route3,route3))
            
            if distance >= 10 and distance<100:
                route1="30km bike ride: https://www.plotaroute.com/route/326385"
                route2="24km bike ride: https://www.plotaroute.com/route/73847"
                route3="Dawn Patrol, 29.023km: https://www.plotaroute.com/route/255793"
                route4="Triangle, 38.363km: https://www.plotaroute.com/route/113372"
                route5="26km bike ride: https://www.plotaroute.com/route/237719"
                route6="Two Loops, 59.256km: https://www.plotaroute.com/route/161174"
                route7="Moonlight Tower Route, 41.439km: https://www.plotaroute.com/route/83593"
                route8="Tough Route, 49.633km: https://www.plotaroute.com/route/91399"
                route9="27 Mile South Austin Loop, 45.269km: https://www.plotaroute.com/route/96871"
                route10="City Hall 30 Miles, 47.601km: https://www.plotaroute.com/route/7952"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 10: 
                route1="McNeil Bypass on Parmer, 6.723km: https://www.plotaroute.com/route/10947"
                route2="Westside to ABGB, 15.466km: https://www.plotaroute.com/route/275793"
                route3="9km route, 9.838km: https://www.plotaroute.com/route/243455"
                route4="City Hall, 9.632km: https://www.plotaroute.com/route/7955"
                route5="Home to Rising Sun, 5.457km: https://www.plotaroute.com/route/27643"
                route6="Neighborhood Spin, 5.388km: https://www.plotaroute.com/route/458243"
                route7="Loop, 6 miles, 9.623km: https://www.plotaroute.com/route/440643"
                route8="To Downtown, 8.887km: https://www.plotaroute.com/route/452004"
                route9="7.066km route: https://www.plotaroute.com/route/396311"
                route10="4.719km route: https://www.plotaroute.com/route/122880"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="atlanta": 
            #bikepaths
            if distance >= 100:
                route1="Atlanta to Washington DC, 2024.760km: https://www.plotaroute.com/route/287039"
                route2="East coast, 8963km: https://www.plotaroute.com/route/364935"
                return str(randomrouteselection(route1,route1,route1,route1,route1,route2,route2,route2,route2,route2))
            if distance >= 10 and distance<100:
                route1="Roswell Hillfest, 73.691km: https://www.plotaroute.com/route/108453"
                route2="Oak Grove, 13.435km: https://www.plotaroute.com/route/12"
                route3="40 mile route, 67.173km: https://www.plotaroute.com/route/91088"
                route4="Piedmont Park Route, 50.814km: https://www.plotaroute.com/route/331528"
                route5="Chastain 20 miles, 32.653km: https://www.plotaroute.com/route/314464"
                route6="Mt. Paran Ridgewood, 33.843km: https://www.plotaroute.com/route/284824"
                route7="Avondale and Back, 39.657km: https://www.plotaroute.com/route/398753"
                route8="Midtown and Back, 53.045km: https://www.plotaroute.com/route/436200"
                route9="Stone Mountain, 56.478km: https://www.plotaroute.com/route/436201"
                route10="Whetstone Creek, 14.812km: https://www.plotaroute.com/route/305634"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 10: 
                route1="AlleyCross Route, 11.491km: https://www.plotaroute.com/route/435064"
                route2="Oak Grove, 13.435km: https://www.plotaroute.com/route/12"
                route3="Old Fourth Ward, Midtown, Virginia Highlands, 8.373km: https://www.plotaroute.com/route/30286"
                route4="Freedom Park and Beltline, 12.486km: https://www.plotaroute.com/route/430359"
                route5="Emory Bike, 8.952km: https://www.plotaroute.com/route/94065"
                route6="Emory Bike II, 9.040km: https://www.plotaroute.com/route/94070"
                route7="Beltline and Virginia Highlands, 12.916km: https://www.plotaroute.com/route/430360"
                route8="Whetstone Creek, 14.812km: https://www.plotaroute.com/route/305634"
                route9="Georgia Tech and Piedmont Park, 9.134km: https://www.plotaroute.com/route/374893"
                route10="Ponce City Market Route, 5.190miles: https://www.plotaroute.com/route/284893"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="seattle": 
            #bikepaths 
            if distance >= 100:
                route1="Seattle to Yellowstone, 1286km: https://www.plotaroute.com/route/86765"
                route2="Seattle to Alaska, 3570km: https://www.plotaroute.com/route/162499"
                route3="Seattle route, 342.234km: https://www.plotaroute.com/route/245793"
                return str(randomrouteselection(route1,route1,route1,route1,route1,route2,route3,route3,route3,route3))
            if distance >= 10 and distance<100:
                route1="Seattle Hill Climb, 36.148km: https://www.plotaroute.com/route/161752"
                route2="Crazy... route, 30.688km: https://www.plotaroute.com/route/82873"
                route3="Warren Magnuson Park and GreenLake, 22.022km: https://www.plotaroute.com/route/80782"
                route4="Road Bike Exploration, 21.451km: https://www.plotaroute.com/route/138853"
                route5='Ride Aroiund Das Lachen, 24.797km: https://www.plotaroute.com/route/85091'
                route6="Comcast, BB&B, Up and Down Queen Anne, 16.681km: https://www.plotaroute.com/route/132450"
                route7="Woodland Park Zoo and University of Washington loop, 13.027miles: https://www.plotaroute.com/route/125825"
                route8="Greenlake Edmonds, 51.666km: https://www.plotaroute.com/route/213266"
                route9="Zipcard, Piroshki, and Locks, 19.040km: https://www.plotaroute.com/route/131138"
                route10="Gasworks-Seattle Market Loop, 40.245km: https://www.plotaroute.com/route/457322"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 10: 
                route1="12.241km route: https://www.plotaroute.com/route/93441"
                route2="Wings of an Eagle route, 15.552km: https://www.plotaroute.com/route/68167"
                route3="BF to FC Route, 1.678km: https://www.plotaroute.com/route/206162"
                route4="14.497km route: https://www.plotaroute.com/route/429365"
                route5="Blue blaze, 10.813km: https://www.plotaroute.com/route/382131"
                route6="Consider biking to work, like this route, 4.648km: https://www.plotaroute.com/route/448057"
                route7="White Center route, 6.671km: https://www.plotaroute.com/route/461564"
                route8="North Beacon Hill to Georgetown, 5.082km: https://www.plotaroute.com/route/204465"
                route9="Consider biking home from work, like this route, 13.541km: https://www.plotaroute.com/route/487575"
                route10="Bike across Lkae Union, 3.708miles: https://www.plotaroute.com/route/73591"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="san francisco": 
            #bikepaths 
            if distance >= 100:
                route1="no routes this distance"
                route2="no routes this distance"
                return str(randomrouteselection(route1,route1,route1,route1,route1,route2,route2,route2,route2,route2))
            
            if distance >= 10 and distance<100:
                route1="Presidio and Lands End Loop, 20.399km: https://www.plotaroute.com/route/122557"
                route2="Alpine Dam, 85.546km: https://www.plotaroute.com/route/440164"
                route3="SF to Sausalito, 40.510km: https://www.plotaroute.com/route/9058"
                route4="20.138km route: https://www.plotaroute.com/route/195871"
                route5="Fisherman's Wharf to San Quentin Prison, 43.580km: https://www.plotaroute.com/route/53259"
                route6="TW to Beach, 24.223km: https://www.plotaroute.com/route/328019"
                route7="Ferry to Hilton, 28.239 miles: https://www.plotaroute.com/route/186486"
                route8="Caltrain to Capitola, 157.107km: https://www.plotaroute.com/route/121843"
                route9="Sunset Laps, 70.636km: https://www.plotaroute.com/route/7786"
                route10="Golden Gate Park, 32.817km: https://www.plotaroute.com/route/258673"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 10: 
                route1="Twin Peaks, 12.785km: https://www.plotaroute.com/route/234983"
                route2="7.682km route: https://www.plotaroute.com/route/9218"
                route3="Hill Billy Route, 8.419km: https://www.plotaroute.com/route/223611"
                route4="GGB to Rodeo Beach, 11.111km: https://www.plotaroute.com/route/84849"
                route5="Fisherman's Wharf to Sausalito Ferry, 13.708km: https://www.plotaroute.com/route/130996"
                route6="Weekend workout loop, 9.759km: https://www.plotaroute.com/route/127032"
                route7="Embarcadero BART to Montgomery St, 2.017km: https://www.plotaroute.com/route/277815"
                route8="The Presidio, 11.892km: https://www.plotaroute.com/route/222029"
                route9="Loop around the Lake, 11.471km: https://www.plotaroute.com/route/127033"
                route10="Treasure Island, 4.806km: https://www.plotaroute.com/route/470554"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

        if nearestcity=="los angeles":
            #bikepaths 
            if distance >= 100:
                route1="Olymptic Road Race, 184.253km: https://www.plotaroute.com/route/265213"
                route2="Summer LA Trail, 2629km: https://www.plotaroute.com/route/187756"
                return str(randomrouteselection(route1,route1,route1,route1,route1,route2,route2,route2,route2,route2))
            if distance >= 10 and distance<100:
                route1="Eagle Rock Loop, 38.540km: https://www.plotaroute.com/route/27144"
                route2="30.975km route: https://www.plotaroute.com/route/25612"
                route3="112.885km route: https://www.plotaroute.com/route/25653"
                route4="Beach Barter, 87.004km: https://www.plotaroute.com/route/181614"
                route5="Laurel Canyon - OUtpost, 39.570km: https://www.plotaroute.com/route/27757"
                route6="48 miles, Pasadena + Altadena, 77.687km: https://www.plotaroute.com/route/24491"
                route7="85.347km route: https://www.plotaroute.com/route/173036"
                route8="19 mile observatory, 31.386km: https://www.plotaroute.com/route/24273"
                route9="24 mile Pico Melrose, 39.208km: https://www.plotaroute.com/route/24490"
                route10="31 miles, Olympic Wilshire, 49.893km: https://www.plotaroute.com/route/24492"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

            if distance < 10: 
                route1="Wilmington to San Pedro, 14.628km: https://www.plotaroute.com/route/204607"
                route2="Chinatown Bike Tour, 7.004km: https://www.plotaroute.com/route/388477"
                route3="Southeast Exploratory Ride, 11.387km: https://www.plotaroute.com/route/206205"
                route4="LAPL Bike Ride, 9.271km: https://www.plotaroute.com/route/254521"
                route5="11.273km route: https://www.plotaroute.com/route/261587"
                route6="3.225km route: https://www.plotaroute.com/route/298187"
                route7="Little Tokyo Bike Tour, 6.562km: https://www.plotaroute.com/route/478801"
                route8="Consider biking to work, like this route, 4.856km: https://www.plotaroute.com/route/164921"
                route9="Battleship USS Iowa Museum to Cabrillo Aquarium, 6.077miles: https://www.plotaroute.com/route/365989"
                route10="Loop around Highland Park, 8.346 miles: https://www.plotaroute.com/route/245115"
                return str(randomrouteselection(route1,route2,route3,route4,route5,route6,route7,route8,route9,route10))

##############################################################################
##                            MAIN SCRIPT                                   ##
##############################################################################

distance=3

exercisetype="run"

if exercisetype == "run":
    webbrowser.open("http://actions.neurolex.co/uploads/run.m4a")
    time.sleep(2)
    webbrowser.open('http://actions.neurolex.co/uploads/run.png')
    time.sleep(5)

elif exercisetype=="walk":
    webbrowser.open("http://actions.neurolex.co/uploads/walk.m4a")
    time.sleep(2)
    webbrowser.open('http://actions.neurolex.co/uploads/walk.png')
    time.sleep(5)

elif exercisetype=="bike":
    webbrowser.open("http://actions.neurolex.co/uploads/bike.m4a")
    time.sleep(2)
    webbrowser.open('http://actions.neurolex.co/uploads/bike.png')
    time.sleep(5)
    
location=curloc()
city=location['city'].lower()
if city == 'cambridge':
    city = 'boston'
listofcities=['chicago','boston','philadelphia','new york city', 'houston"', 'dallas', 'san antonio', 'austin', 'atlanta', 'seattle', 'san francisco', 'los angeles']

# go through script only if the city is in the listofcities 
if city not in listofcities:
    message="sorry we currently do not support exercise routes for your city. Check back in a few months and we'll probably be there."
    print(message)

    # update database 
    hostdir=sys.argv[1]
    os.chdir(hostdir)
    database=json.load(open('registration.json'))
    action_log=database['action log']

    action={
        'action': 'exercise.py',
        'date': get_date(),
        'meta': ['',message],
    }

    action_log.append(action)
    database['action log']=action_log

    jsonfile=open('registration.json','w')
    json.dump(database,jsonfile)
    jsonfile.close()

else:
    
    try:   
        g=exercise(city,exercisetype,distance)
        linkindex=g.index('https')
        link=g[linkindex:]
        print('You should %s '%(exercisetype)+exercise(city,exercisetype,distance).replace(link,''))
        time.sleep(1)
        webbrowser.open_new(link)
    except:
        print("no link")
    
    # update database 
    hostdir=sys.argv[1]
    os.chdir(hostdir)
    database=json.load(open('registration.json'))
    action_log=database['action log']
    name=database['name']
    email=database['email']

    message='Hey %s, \n\n Looks like you are stressed today. Perhaps go out and %s! \n\n Here is a good route: \n\n  %s \n\n Remember, be well! \n\n Cheers, \n\n -The NeuroLex Team'%(name.split()[0].title(), exercisetype, g)
    sendmail([email],'NeuroLex: Go exercise!', message, os.environ['NEUROLEX_EMAIL'], os.environ['NEUROLEX_EMAIL_PASSWORD'], [])

    action={
        'action': 'exercise.py',
        'date': get_date(),
        'meta': [link, message],
    }

    action_log.append(action)
    database['action log']=action_log

    jsonfile=open('registration.json','w')
    json.dump(database,jsonfile)
    jsonfile.close()


                
