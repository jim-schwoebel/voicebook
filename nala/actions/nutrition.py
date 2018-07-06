##############################################################################
##                         STRESSLEX - NUTRITION.PY                         ##
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

I often eat terrible food. I've tried 2 main diets: vegan and the Atkins diet.

The Atkins diet works by putting the body into ketosis and promotes higher 
brain functioning. This is mimicked by many religious traditions like 
Ramadon in Islam. In this way, you try to eat few carbohydrates and you burn
fat instead of glucose for fuel.

Veganism is when you do not eat anything related to animal products. You 
can't eat any meat, cheeses, or diary. It's quite tough the first time around,
but it definitely detoxed my body when I did it for 30 days.

I believe a 30 day diet challenge for people can have a lifetime benefit by 
forcing you to think about new food options. I now eat way more veggies 
as a result of my 30 day vegan diet and I think twice before eating 2 slices
of Sourdough bread. I believe others can have such control

This script thus tries to help jumpstart you into eating healthy by promoting
healthy food options - whether ou cook at home or going out. It separates out
breakfast, lunch, and dinner and is tailored to your location. I pulled much
of this information from google manually, but likely could scrape it into the 
future.

'''

##############################################################################
##                           IMPORT STATEMENTS                              ##
##############################################################################

import os, datetime, random, socket, pygame, time, ftplib, random, sys, json
import numpy, geocoder, getpass, json, requests, smtplib, webbrowser, platform
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders 

##############################################################################
##                            HELPER FUNCTIONS                              ##
##############################################################################

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
        server.sendmail('neurolexlabs@gmail.com', to, msg.as_string())

        print('Done')

        server.quit()
        
    except:
        print('error')
        
def getlocation():
    g = geocoder.google('me')
    return g.latlng

def internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except:
        return False

def selectoption(one,two,three,four,five,six,seven,eight,nine,ten):
    thenum=random.randint(1,10)
    if thenum==1:
        option=one
    if thenum==2:
        option=two
    if thenum==3:
        option=three
    if thenum==4:
        option=four
    if thenum==5:
        option=five
    if thenum==6:
        option=six
    if thenum==7:
        option=seven
    if thenum==8:
        option=eight
    if thenum==9:
        option=nine
    if thenum==10:
        option=ten
    return option

def curloc():
    
    # get current location, limit 1000 requests/day
    r=requests.get('http://ipinfo.io')
    location=r.json()
    
    return location 

def gettime():
	#get time 
	now=datetime.datetime.now()
	year=now.year
	#year - e.g. 2017 
	month=now.month
	#month - e.g. 7 = July
	day=now.day 
	#this is the day of the month - e.g. 5 
	time=now.hour
	#this is hour currently in 24 hour time - e.g. 14 for 2 pm 
	return [year, month, day, time]

def playbackaudio(question,filename):
#takes in a question and a filename to open and plays back the audio file and prints on the screen the question for the user 
    print(question)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(5)
    return "playback completed"

def get_date():
    return str(datetime.datetime.now())

#nutrition actions 
def breakfast(coffee, tea, city):
    #maybe separate breakfast by city like in exercise 
    #go off google reviews or something to buy 
    #sell ads on here into future to restaurants 

    if city == "chicago":
        #coffee options
        one="4.5/5.0 stars - Intelligentsia Coffee Millennium Park Coffeebar - High-end coffee bar chain serving daily roasted brews in an industrial-chic setting. 53 E Randolph St, Chicago, IL 60601"
        two="4.6/5.0 stars - The Wormhole Coffee - '80s-themed rustic coffee shop, complete with a DeLorean, pouring locally roasted coffee. 1462 N Milwaukee Ave, Chicago, IL 60622"
        three="4.7/5.0 stars - Sawada Coffee - Chill spot for creative & classic coffee drinks in cozy, rustic-chic digs with Ping-Pong. 112 N Green St, Chicago, IL 60607"
        four="4.5/5.0 stars - Gaslight Coffee Roasters - Hip, shabby-chic coffeehouse featuring a changing roster of house-roasted java plus tea & pastries. 2385 N Milwaukee Ave, Chicago, IL 60647 "
        five="4.5/5.0 stars - Metropolis Coffee Company - Indie cafe serving coffee, sandwiches & pastries in a colorful space decorated with local art.  1039 W Granville Ave, Chicago, IL 60660."
        six="4.7/5.0 stars - Dark Matter Coffee, the Mothership - Offbeat coffee bar & roasting facility offering tours & artisanal brews in a mural-covered space.. - 738 N Western Ave, Chicago, IL 60612"
        seven="4.7/5.0 stars - Ipsento Coffee - Hip counter-serve cafe with funky furnishings & a menu of sandwiches, pastries & light bites. - 2035 N Western Ave, Chicago, IL 60647"
        eight="4.9/5.0 stars - Metric Coffee Company - Industrial-chic spot featuring house-roasted beans brewed in hot or cold drinks. - 2021 W Fulton St, Chicago, IL 60612"
        nine="4.5/5.0 stars - Bridgeport Coffeehouse - Corner cafe serving fair-trade coffee & light fare in a quaint, casual setting with a tin ceiling. - 3101 S Morgan St, Chicago, IL 60608"
        ten="4.6/5.0 stars - Big Shoulders Coffee - Low-key cafe serving coffee (roasted on-site), tea & signature marshmallow lattes in a modern space. - 1105 W Chicago Ave, Chicago, IL 60642"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city =="boston":
        one="4.4/5.0 stars - Pavement Coffee House - High-end coffee, espresso drinks & tea go with baked goods at this outpost of a local mini-chain. 1334 Boylston St, Boston, MA 02215"
        two="4.5/5.0 stars - Barrington Coffee Roasting Company - Artsy cafe with global javas brewed in a state-of-the-art machine, plus artisanal teas & pastries. 303 Newbury St, Boston, MA 02115"
        three="4.3/5.0 stars - Wired Puppy - Snug subterranean cafe offering coffee, tea, espresso & baked goods plus free WiFi & a patio. 250 Newbury St, Boston, MA 02116"
        four="4.7/5.0 stars - Render Coffee - Cozy daytime gathering spot where artisanal coffee shares the menu with quiche, bagels & sandwiches. 563 Columbus Ave, Boston, MA 02118"
        five="4.1/5.0 stars - Jaho Coffee & Tea - Artisanal coffee roasters, teahouse & bakery offering drinks, light fare & fresh pastries. 1651 Washington St, Boston, MA 02118"
        six="4.2/5.0 stars - Blue State Coffee - Socially conscious cafe chain know for its menu of coffee & sandwiches & its charitable donations. 957 Commonwealth Avenue, Boston, MA 02215."
        seven="4.5/5.0 stars - Thinking Cup - Charming cafe featuring high-end coffee & espresso drinks, housemade pastries & sandwiches. 165 Tremont St, Boston, MA 02111"
        eight="4.1/5.0 stars - Boston Common Coffee Co - Locally roasted coffees are the star at this chill cafe that also serves panini, soups & pastries. 515 Washington St, Boston, MA 02111"
        nine="4.8/5.0 stars - Gracenote Coffee Boston - Tiny gourmet espresso bar from a local coffee roaster serving nitrogen cold brews & more. 108 Lincoln St, Boston, MA 02111"
        ten="4.8/5.0 stars - Boston Brewin Organic Coffee - Popular, eco-conscious coffee shop offering fair-trade espresso drinks & local, organic baked goods. 45 Bromfield St, Boston, MA 02108"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="philadelphia":
        one="4.6/5.0 stars - Elixr Coffee Roasters - Single-origin, hand-poured brews & espresso drinks offered up in an eco-friendly marble & wood cafe. 207 S Sydenham St, Philadelphia, PA 19102"
        two="4.5/5.0 stars - Menagerie Coffee - Artisanal java drinks & snacks in a brick-walled space with retro-style lighting & a homey vibe. 18 S 3rd St, Philadelphia, PA 19106"
        three="4.6/5.0 stars - La Colombe Coffee Roasters - Trendy cafe serving house-brand artisanal coffee, pastries & snacks in a sleek space. 1414 S Penn Square, Philadelphia, PA 19102"
        four="4.5/5.0 stars - ReAnimator Coffee - Local micro coffee roasters share brews & expertise in a snug, chic hangout with hardwood floors. 1523 E Susquehanna Ave, Philadelphia, PA 19125"
        five="4.7/5.0 stars - Grindcore Houst - Hip coffeehouse where the drinks & eats are vegan-friendly & the grindcore soundtrack is intense. 1515 S 4th St, Philadelphia, PA 19147"
        six="4.6/5.0 stars - Shot Tower Coffee - Industrial-chic cafe providing espresso drinks & tea, plus communal tables & some patio seating. 542 Christian St, Philadelphia, PA 19147"
        seven="4.7/5.0 stars - Ox Coffee - Espresso, brewed coffee & pastries served in a relaxed spot with a backyard patio. 616 S 3rd St, Philadelphia, PA 19147"
        eight="4.6/5.0 stars - Bodhi Coffee - Artisanal coffee specialist in a historic townhouse also serving tea, pastries & other light fare. 410 S 2nd St, Philadelphia, PA 19147"
        nine="4.7/5.0 stars - Ultimo Coffee - Specialty espresso & java drinks using gourmet beans served amid industrial decor. 2149 Catharine St, Philadelphia, PA 19146"
        ten="4.7/5.0 stars - Lucky Goat Coffee House - Quaint coffeehouse featuring classic & specialty espresso drinks, plus baked goods & soups. 888 N 26th St, Philadelphia, PA 19130"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="new york city":
        one="4.5/5.0 stars - Stumptown Coffee Roasters. Coffee bar chain offering house-roasted direct-trade coffee, along with brewing gear & whole beans. 18 W 29th St, New York, NY 10001"
        two="4.7/5.0 stars - Coffee Project New York. Cozy, brick-lined haunt for inventive drinks such as deconstructed lattes & nitro cold-brew coffee. 239 E 5th St, New York, NY 10003"
        three="4.6/5.0 stars - Oslo Coffee Company. Snug, minimalist chain coffee shop outpost that roasts its premium beans in-house. 422 E 75th St, New York, NY 10021"
        four="4.5/5.0 stars - Blue Bottle Coffee. Trendy cafe chain offering upscale coffee drinks & pastries, plus beans & brewing equipment. 1 Rockefeller Plaza Concourse Level Suite D, New York, NY 10020"
        five="4.7/5.0 stars - Abraco Coffee. Espresso, baked goods & savory small plates are served at this busy East Village counter-serve spot. 81 E 7th St, New York, NY 10003"
        six="4.4/5.0 stars - Kava Coffee. Modern coffee shop also serving sandwiches, pastries, salads, antipasti, beer, wine & cheese plates. 803 Washington St, New York, NY 10014"
        seven="4.3/5.0 stars - Roasting Plant Coffee. Coffeehouse with a cutting-edge roasting system that freshly grounds beans while customers watch. 75 Greenwich Ave, New York, NY 10014"
        eight="4.6/5.0 stars - Everyman Expresso. Compact coffee & espresso bar turning out drinks made from direct-trade beans in a low-key setting. 301 W Broadway, New York, NY 10013"
        nine="4.2/5.0 stars - Joe's Coffee. Coffee spot offering free-trade brews, baked goods, classes & catering in a buzzy modern space. 187 Columbus Ave, New York, NY 10023"
        ten="4.4/5.0 stars - Birch Coffee. Local coffeehouse chain serving thoughtfully-sourced, house-roasted brews in a hip, bustling space. 56 7th Ave, New York, NY 10011"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="houston":
        one="4.4/5.0 stars - Siphon Coffee. Coffee shop featuring siphon-made joe, craft beer & wines on tap, plus a sit-down video-game table. 701 W Alabama St, Houston, TX 77006"
        two="4.6/5.0 stars - Catalina Coffee. Airy spot for fresh-roasted coffee, seasonal loose-leaf tea & fresh pastries delivered daily. 2201 Washington Ave, Houston, TX 77007"
        three="4.5/5.0 stars - Boomtown Coffee. Comfy cafe serving small-batch house-roasted brews & light bites in a modern setting with local art. 242 W 19th St, Houston, TX 77008"
        four="4.4/5.0 stars - Antidote. Neighborhood hangout open early & late for coffee & locally sourced light bites, plus beer & wine. 729 Studewood St, Houston, TX 77007"
        five="4.4/5.0 stars - Blacksmith. Coffeehouse with gourmet, barista-made drinks, home-baked goods & light fare in an industrial space. 1018 Westheimer Rd, Houston, TX 77006"
        six="4.5/5.0 stars - Paper Co. Cafe. Serving a host of coffee drinks plus classic cafe fare in an industrial, loftlike setting. 1100 Elder St, Houston, TX 77007"
        seven="4.3/5.0 stars - Black Hole Coffee House. Students & remote workers populate this loungey coffee shop with free WiFi & eclectic furniture. 4504 Graustark St, Houston, TX 77006"
        eight="4.4/5.0 stars - AHH, Coffee! Coffeehouse offering beverages made with locally roasted beans, plus craft beer & teas. 2018 Rusk St A, Houston, TX 77003"
        nine="4.5/5.0 stars - Campesino Coffee House. Modern, stylish cafe serving coffee & Latin American specialty drinks, plus empanadas & sandwiches. 2602 Waugh Dr, Houston, TX 77006"
        ten="4.9/5.0 stars - Al Vetro: Coffee and Expresso Bar. Exotic coffee tastes, really good reviews. 6560 Fannin St #245, Houston, TX 77030"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="dallas":
        one="4.5/5.0 stars - Ascension Coffee. Stylish coffeehouse serving premium slow-roasted coffee, boutique wine, plus brunch & bar bites. 1621 Oak Lawn Ave A, Dallas, TX 75207"
        two="4.6/5.0 stars - Cultivar Coffee Bar & Roaster. Good reviews. 313 W Jefferson Blvd, Dallas, TX 75208"
        three="4.6/5.0 stars - Davis Street Expression. Locally roasted coffee, espresso & baked goods served in a chill, industrial space. 819 W Davis St, Dallas, TX 75208"
        four="4.6/5.0 stars - Weekend Coffee. Espresso drinks, pour-over coffee & pastries served in a hip, bright space inside the Joule Hotel. 1511 Commerce St, Dallas, TX 75201"
        five="4.6/5.0 stars - Houndstooth Coffee. Branch of the funky Austin-based chain, serving coffee drinks, tea, beer & wine, plus pastries. 1900 N Henderson Ave, Dallas, TX 75206"
        six="4.8/5.0 stars - Magnolias Sous Le Pont. Espresso drinks & take-away bites offered in a cool, well-appointed space with patio seating. 2727 N Harwood St, P2, Dallas, TX 75201"
        seven="4.6/5.0 stars - Opening Bell Coffee. Breakfast tacos, sandwiches, coffee, wine & beer at hip, relaxed hangout with live music & WiFi. 1409 S Lamar St, Dallas, TX 75215"
        eight="4.8/5.0 stars - Stupid Good Coffee. Local java joint offering coffee drinks, sweets & root beer from early morning to early evening. 1910 Pacific Ave #2060, Dallas, TX 75201"
        nine="4.6/5.0 stars - Union. Community-oriented coffeehouse with spoken-word nights & a portion of sales going to nonprofits. 5622 DYER ST #100, DALLAS, TX 75206"
        ten="4.6/5.0 stars - Urban Blend Coffee Co. 805 Elm Street, West End DART Station, Dallas, TX 75202"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="san antonio":
        one="4.5/5.0 stars - Revolucion Coffee + Juice. 7959 Broadway St #500, San Antonio, TX 78209"
        two="4.5/5.0 stars - Rosella Coffee Company. Espresso drinks, snacks, beer & wine served in industrial-chic digs with free WiFi & patio seats. 203 E Jones Ave #101, San Antonio, TX 78215"
        three="4.8/5.0 stars - White Elephant Coffee Company. Popular joint serving house-roasted coffee, plus sweet & savory bites, in a cool, relaxed space. 110 W Carolina St, San Antonio, TX 78210"
        four="4.6/5.0 stars - Aspen's Brew Coffee, Cafe & Catering. Chill counter-serve coffee shop, doling out sandwiches, pastries & a selection of imported beans. 11255 Huebner Rd #100, San Antonio, TX 78230"
        five="4.7/5.0 stars - Barrio Barista. Rustic-chic cafe offering creative coffee drinks & breakfast/lunch fare, including tacos & burgers. 3735 Culebra Rd, San Antonio, TX 78228"
        six="5.0/5.0 stars - What's Brewing Coffee Roasters. Longtime, family-owned gourmet coffee provider offers specialty roasted-to-order beans & blends. 138 West Rhapsody Drive, San Antonio, TX 78216"
        seven="5.0/5.0 stars - Theory Coffee. 2347 Nacogdoches Rd, San Antonio, TX 78209"
        eight="4.8/5.0 stars - Estate Coffee Company. Bright, modern cafe with a few seats, pouring craft coffee & espresso behind a dark wood bar. 1320 E Houston St A101, San Antonio, TX 78205"
        nine="4.6/5.0 stars - Local Coffee. Buzzy coffeehouse offering a changing selection of brews in an intimate, industrial-chic setting. 302 Pearl Pkwy, San Antonio, TX 78215"
        ten="4.5/5.0 stars - Mildfire Coffee Roasters. Narrow, colorful coffee spot, with brews made from beans roasted on-site, plus smoothies & tea. 15502 Huebner Rd # 101, San Antonio, TX 78248"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="austin":
        one="4.5/5.0 stars - Mozart's Coffee Roasters. Beans flame-roasted on-site, plus bakery goods, frequent live music & patio seating on Lake Austin. 3825 Lake Austin Blvd, Austin, TX 78703"
        two="4.5/5.0 stars - Houndstooth Coffee. This chill, airy hangout serves carefully sourced coffees, teas, wines & craft beer, plus snacks. 4200 North Lamar Boulevard, 120, Austin, TX 78756"
        three="4.7/5.0 stars - Fleet Coffee Co. Petite cafe serving classic & inventive coffee drinks, plus local tacos & pastries. 2427 Webberville Rd, Austin, TX 78702"
        four="4.5/5.0 stars - Caffe Medici. French-pressed coffee blends plus a selection of single-origin & sustainable, direct-trade options. 200 Congress Ave, Austin, TX 78701"
        five="4.5/5.0 stars - Radio Coffee & Beer. Hip spot for coffee, beer & pastries in wood-paneled digs, plus tables & a taco truck out back. 4204 Manchaca Rd, Austin, TX 78704"
        six="4.6/5.0 stars - Figure 8 Coffee Purveyors. Artisan java & bites are served at this cafe with industrial–chic decor, a patio & a laid-back vibe. 1111 Chicon St, Austin, TX 78702"
        seven="4.5/5.0 stars - Hip cafe brewing locally-roasted beans & offering baked goods (with vegan options) & free WiFi. 1405 E 7th St, Austin, TX 78702"
        eight="4.8/5.0 stars - Texas Coffee Traders. Longtime coffee roaster with patio seating & free WiFi, selling a wide range of java beans & drinks. 1400 E 4th St, Austin, TX 78702"
        nine="4.7/5.0 stars - Cuppa Austin. Relaxed coffee shop serving espresso, blended drinks, tea, fruit smoothies & more. 9225 W Parmer Ln b101, Austin, TX 78717"
        ten="4.8/5.0 stars - Flitch Coffee. Amarillo's Evocation coffee & local pastry brands served from quaint, retro camper with patio seats. 641 Tillery, Austin, TX 78702"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="atlanta":
        one="4.5/5.0 stars - Dancing Goats. Modern haunt with espresso, single-origin coffee & free WiFi inside a restored, historic building. 650 North Avenue NE, Atlanta, GA 30308"
        two="4.6/5.0 stars - Octane Coffee Bar. 3423 Piedmont Rd NE, Atlanta, GA 30305"
        three="4.7/5.0 stars - Joe's East Atlanta Coffee Shop. Coffee, baked goods & snacks in a quirky, art-filled space with couches, tables & free Wi-Fi. 510 Flat Shoals Ave SE, Atlanta, GA 30316"
        four="4.5/5.0 stars - Codensa Coffee. Industrial-modern espresso bar creates an inviting atmosphere with cocktails, beer & small plates. 480 John Wesley Dobbs Ave NE #100, Atlanta, GA 30312"
        five="4.7/5.0 stars - Taproom Coffee. Informal option offering espresso & coffee drinks, pastries & craft beers on tap. R106, 1963 Hosea L Williams Dr NE, Atlanta, GA 30317"
        six="4.6/5.0 stars - Hodgepodge Coffeehouse and Gallery. Homey, art-filled coffee shop with sandwiches, from-scratch baked goods & open-mike nights. 720 Moreland Ave SE, Atlanta, GA 30316"
        seven="4.6/5.0 stars - Brash Coffee. Tiny cafe in a converted shipping container pouring craft coffee & roasting their own beans. 1168 Howell Mill Rd, Atlanta, GA 30318"
        eight="4.6/5.0 stars - Land of a Thousand Hills. Chic spot serving single-origin coffee drinks, craft beer & wine, plus hot & cold light cafe fare. 232 19th St NW #7100, Atlanta, GA 30363"
        nine="4.8/5.0 stars - Ebrik Coffee Room. Coffee house featuring hot drinks, baked goods & art events in a chic, contemporary space. 16 Park Pl SE, Atlanta, GA 30303"
        ten="4.4/5.0 stars - West Egg Cafe. Southern fare, including all-day breakfasts, draws fans to this hot spot with minimalist decor. 1100 Howell Mill Rd, Atlanta, GA 30318"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="seattle":
        one="4.5/5.0 stars - Seattle Coffee Works. Unpretentious coffeehouse with an espresso bar & a slow bar for comparing single-origin beans. 107 Pike St, Seattle, WA 98101"
        two="4.5/5.0 stars - Ballard Coffee Works. Bustling corner coffee shop features varied espresso blends & treats in a light-filled modern venue. 2060 NW Market St, Seattle, WA 98107"
        three="4.5/5.0 stars - Caffe Vita. Pacific Northwest chain serving house-roasted coffee in hip, relaxed surroundings. 813 5th Ave N, Seattle, WA 98109"
        four="4.7/5.0 stars - Storyville Coffee. Market-based spot for artisanal coffee & baked goods in stylish wood-clad digs with fireplace. 94 Pike Street , top floor, Seattle, WA 98101"
        five="4.6/5.0 stars - Caffe Fiore. 2206b California Ave SW, Seattle, WA 98116"
        six="4.8/5.0 stars - Milstead & Co. Art lines the walls of this rustic-chic coffeehouse that pours brews & sells bags of beans too. 754 N 34th St, Seattle, WA 98103"
        seven="4.5/5.0 stars - Tougo Coffee Co. Modern coffeehouse offering slow-brewed drinks, tea & baked goods. 1410 18th Ave, Seattle, WA 98122"
        eight="4.7/5.0 stars - C&P Coffee Company. Comfy cafe with locally sourced coffee & baked goods, hosting events like craft fairs & live music. 5612 California Ave SW, Seattle, WA 98136"
        nine="4.5/5.0 stars - Moore Coffee Shop. Known for its latte art, this family-owned coffee spot with a loungey vibe offers breakfast & lunch. 1930 2nd Ave, Seattle, WA 98101"
        ten="4.7/5.0 stars - Lighthouse Roasters. Small corner cafe known for roasting coffee beans on-site in vintage cast-iron roasters. 400 N 43rd St, Seattle, WA 98103"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="san francisco":
        one="4.5/5.0 stars - Sightglass Coffee. Coffee made from house-roasted beans served along with baked goods in a bi-level, industrial space. 270 7th St, San Francisco, CA 94103"
        two="4.6/5.0 stars - Philz Coffee. Laid-back local chain specializes in custom-blended coffees, plus teas, specialty drinks & pastries. 3101 24th St, San Francisco, CA 94110"
        three="4.5/5.0 stars - Four Barrel Coffee. Exposed beams create a sleek & rustic ambiance for this Mission cafe specializing in drip coffee. 375 Valencia St, San Francisco, CA 94103"
        four="4.6/5.0 stars - Reveille Coffee Co. Coffee meets New American fare, including breakfast, at this bright, modern food-truck spinoff. 4076 18th St, San Francisco, CA 94114"
        five="4.5/5.0 stars - Flywheel Coffee Roasters. Family-owned coffee roaster offering exotic brews in a stripped-down, industrial setting. 672 Stanyan St, San Francisco, CA 94117"
        six="4.6/5.0 stars - Ritual Coffee Roasters. Artisanal coffeehouse chain that cultivates relationships with growers & roasts their beans on-site. 432b Octavia St, San Francisco, CA 94102"
        seven="4.4/5.0 stars - Blue Bottle Coffee. Trendy cafe chain offering upscale coffee drinks & pastries, plus beans & brewing equipment. 115 Sansome St, San Francisco, CA 94104"
        eight="4.5/5.0 stars - Mazarine Coffee. Modern, industrial space for espresso drinks & pour-over coffee as well as salads & sandwiches. 720 Market St, San Francisco, CA 94102"
        nine="4.3/5.0 stars - Red Door Coffee. Local draw for Four Barrel Coffee, Dynamo Donuts & other cafe fare in a bright, wood-decked space. 111 Minna St, San Francisco, CA 94105"
        ten="4.5/5.0 stars - Saint Frank Coffee. Sunny, bi-level neighborhood coffeehouse pairing its java with pastries in airy, minimalist digs.2340 Polk St, San Francisco, CA 94109"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="los angeles":
        one="4.6/5.0 stars - Alfred Coffee Melrose Place. Stylish yet whimsical coffee shop serving coffee & juice, plus salads, sandwiches & pastries. 8428 Melrose Pl, Los Angeles, CA 90069"
        two="4.5/5.0 stars - Verve Coffee. NorCal-originated chain known for its coffee offers an outdoor patio & home brewing materials. 833 S Spring St, Los Angeles, CA 90014"
        three="4.6/5.0 stars - Stumptown Coffee Roasters. Coffee bar chain offering house-roasted direct-trade coffee, along with brewing gear & whole beans. 806 S Santa Fe Ave, Los Angeles, CA 90021"
        four="4.6/5.0 stars - Blue Bottle Coffee. Trendy cafe chain offering upscale coffee drinks & pastries, plus beans & brewing equipment. 8301 Beverly Blvd, Los Angeles, CA 90048"
        five="4.6/5.0 stars - Philz Coffee. Laid-back local chain specializes in custom-blended coffees, plus teas, specialty drinks & pastries. 801 S Hope St A, Los Angeles, CA 90017"
        six="4.5/5.0 stars - G&B Coffee. Relaxed wraparound counter dispensing sophisticated coffee & tea creations & pastries. 317 S Broadway C19, Los Angeles, CA 90013"
        seven="4.8/5.0 stars - Balconi Coffee Company. Arty, industrial-chic shop specializing in siphon-brewed coffee & high-end espresso drinks. 11301 W Olympic Blvd #124, Los Angeles, CA 90064"
        eight="4.5/5.0 stars - Found Coffee. Specialty coffee & tea drinks served with a curated selection of baked goods in a stylish setting. 1355 Colorado Blvd, Los Angeles, CA 90041"
        nine="4.6/5.0 stars - Chimney Coffee House. This hip, casual cafe specializes in locally roasted coffee, elevated breakfast fare & sandwiches. 1100 N Main St, Los Angeles, CA 90012"
        ten="4.6/5.0 stars - Muddy Paw Coffee Company. This easygoing, dog-themed coffee shop offering shade-grown, organic java also has patio seating. 3320 Sunset Blvd, Los Angeles, CA 90026"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    else:
        print("Your city currently not supported to recommend breakfast. Check back in a few months.")

    #takes in number of cups of coffee consumed each day and current hour and outputs breakfast selection randomly (healthy)
    #options for breakfast (x11)
    homeorout=random.randint(0,1)
    if homeorout==0:
        #going out option 
        return option 
    elif homeorout==1:
        #make something at home - add some links on amazon to buy into future 
        one="Eat 1 banana! \n\n Bananas contain antioxidants (phenolics, carotenoids, biogenic amines, and phytosterols) which have multiple health benefits by protecting the body against various oxidative stresses."
        two="Make a Blueberry smoothie (1/2 cup bluberries, 1/2 cup milk)! \n\n Blueberries contain polyphenolic compounds, most prominently anthocyanins, which have antioxidant and anti-inflammatory effects. In addition, anthocyanins have been associated with increased neuronal signaling in brain centers, mediating memory function as well as improved glucose disposal, benefits that would be expected to mitigate neurodegeneration."
        three="Eat a yogurt! \n\n Yogurt has probiotics, which helps to increase good gut microflora."
        four="Eat 1/2 cup nuts! \n\n Nuts boost the immune system to prevent getting sick."
        five="Eat a bowel of oatmeal! \n\n Oatmeal helps upregulate serotonin to improve overall mood. Seeds contain magnesium - which helps fight anxiety, panic attacks, and depression."
        six="Eat a bagel and cream cheese! Carbs are good for energy after a run."
        seven="Eat some carrots! \n\n Munching on crunchy foods helps beat stress. Nutrient-rich carrots, celery and other crunchy, fresh veggies offer satisfying crispness that won't bog you down with too many calories."
        eight="Eat some blackberries! \n\n Blackberries have antioxidants to help fight stress."
        nine="Eat an orange! \n\n Oranges contain Vitamin C which can lower blood pressure and the stress hormone cortisol. For a quick burst of vitamin C, simply eat a whole orange or drink a glass of freshly squeezed orange juice without added sugar. Or take a stroll down to the local Jamba Juice and pick yourself up one. Go with the Purely Orange."
        ten="Eat 2 eggs! Eggs contain protein to help with building muscles."
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
        option=str(option)
        index1=option.index('!')
        cofran=random.randint(0,1)
        if coffeenum>0 and tea==True:
            if cofran==0:
                return str(option[:(index1)]+" and drink one cup of coffee with soymilk!"+option[(index1+1):] + " And coffee helps dilate blood vessels to reduce headaches. Just don't overdo it: limit to one cup.").replace('\xa0','')
            if cofran==1:
                return str(option[:(index1)]+" and drink one cup of green tea"+option[(index1+1):] +" Green tea has some healthy antioxidants to reduce stress. Just don't overdo it: limit to one cup.").replace('\xa0','')
        elif coffeenum>0:
            return str(option[:(index1)]+" and drink one cup of coffee with soymilk!"+option[(index1+1):] + " And coffee helps dilate blood vessels to reduce headaches. Just don't overdo it: limit to one cup.").replace('\xa0','')
        elif tea == 'yes':
            return str(option[:(index1)]+" and drink one cup of green tea"+option[(index1+1):] +" Green tea has some healthy antioxidants to reduce stress. Just don't overdo it: limit to one cup.").replace('\xa0','')
        elif tea == 'no':
            return str(option).replace('\xa0','')
        else:
            print("error.")
    
def lunch(city):
    
    #maybe separate lunches by city like in exercise 

    if city == "chicago":
        one="4.6/5.0 stars - Saucy Porka. A modern fusion of Latin & Asian comfort foods from a buzzy spot with food-truck roots. 400 S Financial Pl, Chicago, IL 60605"
        two="4.4/5.0 stars - XOCO. Counter serving chef Rick Bayless's take on Mexican street food, plus tap beers. 449 N Clark St, Chicago, IL 60654"
        three="4.7/5.0 stars - Blackwood BBQ Lake Street. BBQ as sandwich, salad or platter served with regional sauces & sides in modern, counter-serve digs. 307 W Lake St, Chicago, IL 60606"
        four="4.6/5.0 stars - RPM Steak. Chophouse with a modern menu of prime cuts, raw-bar items & more in a sleek setting with banquettes. 66 W Kinzie St, Chicago, IL 60654"
        five="4.5/5.0 stars - Hash Chicago. Eatery serves its namesake dish, plus other breakfast & lunch fare amid '70s rock-inspired decor. 1357 N Western Ave, Chicago, IL 60622"
        six="4.5/5.0 stars - Cindy's Rooftop Restauarant. Hip, stylish rooftop bar/eatery at the Chicago Athletic Association Hotel with choice seasonal fare. 12 S Michigan Ave, Chicago, IL 60603"
        seven="4.6/5.0 stars - Dove's Luncheonette. Tex-Mex diner eats plus cocktails & lots of tequila in retro digs with counter seats & a jukebox. 1545 N Damen Ave, Chicago, IL 60622"
        eight="4.6/5.0 stars - Au Cheval. The open kitchen at this upscale diner works with ingredients ranging from bologna to foie gras. 800 W Randolph St, Chicago, IL 60607"
        nine="4.5/5.0 stars - Little Goat Diner. Stephanie Izard's diner serving a huge menu of creative, gourmet takes on comfort food classics. 820 W Randolph St, Chicago, IL 60607"
        ten="4.5/5.0 stars - Sopraffina Marketcaffe. Counter-serve mini-chain member with indoor-outdoor seats serving Italian breakfast, lunch & coffee. 200 E Randolph St, Chicago, IL 60601"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city =="boston":
        one="4.6/5.0 stars - The Courtyard Restaurant. Bookworms snack on New American fare by an Italianate courtyard at the Boston Public Library. 700 Boylston St, Boston, MA 02116"
        two="4.5/5.0 stars - Fogo de Chao Brazilian Steakhouse. Upscale Brazilian chain for all-you-can-eat meat carved tableside plus an extensive salad bar. 200 Dartmouth St, Boston, MA 02116"
        three="4.7/5.0 stars - Mike & Patty's. Corner cafe prepares a variety of sandwiches for breakfast & lunch including different egg versions. 12 Church St, Boston, MA 02116"
        four="4.7/5.0 stars - Casa Razdora. Housemade pasta, pizza, sandwiches & Italian eats in a cozy, bustling setting; open weekdays. 115 Water St, Boston, MA 02109"
        five="5.0/5.0 stars - Sal's Lunch. Small, no-frills diner with a retro feel, serving classic American fare for breakfast & lunch. 31 Thacher St, Boston, MA 02113"
        six="4.6/5.0 stars - Wheelhouse Boston. Counter-serve nook offering build-your-own-burgers & other old-school staples for breakfast & lunch. 63 Broad St, Boston, MA 02109"
        seven="4.5/5.0 stars - Island Creek Oyster Bar. Farm-fresh raw bar, imaginative cocktails & an extensive wine & beer list in sleek surrounds. 500 Commonwealth Avenue, Boston, MA 02215"
        eight="4.5/5.0 stars - Toro. Small, stylish spot from Chef Ken Oringer serves up celebrated tapas, cocktails & Spanish wines. 1704 Washington St, Boston, MA 02118"
        nine="4.7/5.0 stars - Bean & Leaf Co. Take-out deli/cafe offering a diverse choice of breakfast, sandwiches & coffees, plus a few seats. 20 Custom House St, Boston, MA 02109"
        ten="4.5/5.0 stars - Tasty Cafe, Boston. 321 Boston Ave, Medford, MA 02153"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="philadelphia":
        one="4.5/5.0 stars - High Street on Market. Eli Kulp's edgy American cooking with a rustic twist & an artisanal bakery in a country-chic space. 308 Market St, Philadelphia, PA 19106"
        two="4.8/5.0 stars - Dizengoff. Bright, industrial eat-in/take-out spot for varieties of hummus, fresh pita & Middle Eastern salads. 1625 Sansom St, Philadelphia, PA 19103"
        three="4.5/5.0 stars - Talula's Daily - Market & Cafe. Farm-to-table market & cafe providing pastries & prepared foods plus set-price American dinners. 208 W Washington Square, Philadelphia, PA 19106"
        four="4.5/5.0 stars - Little Nonna's. Traditional Italian dishes delivered in a homey trattoria setting with an open kitchen & a garden. 1234 Locust St, Philadelphia, PA 19107"
        five="4.5/5.0 stars - Farmer's Keep. Diners choose ingredients to make their own meals at this farm-to-table fast-casual spot. 10 S 20th St, Philadelphia, PA 19103"
        six="4.5/5.0 stars - wedge + fig. Cozy BYOB restaurant offering bistro fare & a grilled cheese bar, plus cheese boards & charcuterie. 160 N 3rd St, Philadelphia, PA 19106"
        seven="4.6/5.0 stars - Sandy's. Breakfast & lunch spot serving eggs, sandwiches & other diner staples, plus a few Greek specialties. 231 S 24th St, Philadelphia, PA 19103"
        eight="4.5/5.0 stars - Butcher and Singer - Steakhouse. Trendy take on an Old Hollywood chophouse offering classic surf 'n' turf plus a raw bar & cocktails. 1500 Walnut St, Philadelphia, PA 19102"
        nine="4.6/5.0 stars - The Dandelion. This spot serves craft beers & modern takes on British cuisine in a pubby setting. 124 S 18th St, Philadelphia, PA 19103"
        ten="4.5/5.0 stars - Sabrina's Cafe & Spencer's Too. Relaxed New American cafe with a devoted following for its breakfast & brunch offerings. 1804 Callowhill St, Philadelphia, PA 19130"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="new york city":
        one="4.6/5.0 stars - Gramercy Tavern. Danny Meyer's Flatiron District tavern with a fixed-price-only dining room & a bustling bar area. 42 E 20th St, New York, NY 10003"
        two="4.5/5.0 stars - The Modern. French/New American fare in a modernist space with garden views at the Museum of Modern Art. 9 W 53rd St, New York, NY 10019"
        three="4.7/5.0 stars - Le Bernardin. Elite French restaurant offers chef Eric Ripert's refined seafood, expert service & luxurious decor. 155 W 51st St, New York, NY 10019"
        four="4.5/5.0 stars - Friedman's. Contemporary spot specializing in seasonal, locally sourced & mostly gluten-free comfort classics. 450 10th Ave, New York, NY 10018"
        five="4.7/5.0 stars - Downtown Bakery. All-day counter-service spot serving Mexican fast food like burritos & tacos in a no-frills space. 69 1st Avenue, New York, NY 10003"
        six="4.6/5.0 stars - Lunch Box. Pocket-sized lunch counter for sandwiches, salads & soups plus smoothies & fresh-squeezed juice. 886 9th Ave, New York, NY 10019"
        seven="4.5/5.0 stars - Momofuku Ko. Tiny, tough-to-reserve eatery via David Chang offering multicourse, Asian-accented American meals. 8 Extra Pl, New York, NY 10003"
        eight="4.5/5.0 stars - Magon. Small Latin counter-service spot serving Cuban sandwiches, American breakfasts & salads.  136 W 46th St, New York, NY 10036"
        nine="4.4/5.0 stars - Gansevoort Market. Rustic-industrial food hall with a variety of popular counter-serve eateries, produce stalls & more. 353 W 14th St, New York, NY 10014"
        ten="4.5/5.0 stars - Chelsea Market. Chelsea Market is a food hall, shopping mall, office building and television production facility located in the Chelsea neighborhood of the borough of Manhattan, in New York City. 75 9th Ave, New York, NY 10011 "
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="houston":
        one="4.6/5.0 stars - Local Foods. Counter-service deli using local & housemade ingredients in its soups, salads & giant sandwiches. 2424 Dunstan Rd, Houston, TX 77005"
        two="4.3/5.0 stars - B&B Butchers & Restaurant. A vintage bakery has been converted into an upscale steakhouse with an attached butcher shop & deli. 1814 Washington Ave, Houston, TX 77007"
        three="4.5/5.0 stars - Paulie's. Counter-serve Italian cafe/espresso bar serving housemade pastas, pizza & famous shortbread cookies. 1834 Westheimer Rd, Houston, TX 77018"
        four="4.4/5.0 stars - Lankford's Grocery & Market. No-frills spot for classic American eats including burgers & hearty breakfasts in a kitschy space. 88 Dennis St, Houston, TX 77006"
        five="4.3/5.0 stars - Weights + Measures. Combo restaurant/bar/bakery with bright, mod style offering seasonal American fare & baked goods. 2808 Caroline St, Houston, TX 77004"
        six="4.3/5.0 stars - Tiny Boxwoods. Upscale-casual cafe serving classic breakfast & lunch fare amidst lush greenery & an outdoor patio. 3614 W Alabama St, Houston, TX 77027"
        seven="4.3/5.0 stars - Adair Kitchen. Simple, spacious cafe highlighting lightened-up New American comfort food with a modern twist. 5161 San Felipe St, Houston, TX 77056"
        eight="4.5/5.0 stars - Peli Peli. Robust South African eats such as curried chicken & herb-crusted lamb served in a dimly lit space. 110 Vintage Park Boulevard, P, Houston, TX 77070"
        nine="4.3/5.0 stars - Barnaby's Cafe. Local chain member offering American comfort food in pooch-themed digs with a dog-friendly patio. 1701 S Shepherd Dr, Houston, TX 77019"
        ten="4.3/5.0 stars - Rainbow Lodge. Upscale spot for American fare including wild game & seafood served in an elegant, historic cabin."
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="dallas":
        one="4.7/5.0 stars - Uncle Uber's Sammich Shop. Funky little sandwich shop offering hearty, eclectic bites & beers amid colorful, nostalgic decor. 2713 Commerce St, Dallas, TX 75226"
        two="4.6/5.0 stars - Pecan Lodge. A variety of smoked meats, sides & desserts are served at this BBQ eatery along with beer & wine. 2702 Main St, Dallas, TX 75226"
        three="4.4/5.0 stars - The Porch. Happening gastropub featuring upscale comfort chow paired with creative cocktails, wine & brews. 2912 N Henderson Ave, Dallas, TX 75206"
        four="4.6/5.0 stars - Rodeo Goat. Casual joint offering inventive variations on house-ground burgers & a lengthy craft-beer lineup. 1926 Market Center Blvd, Dallas, TX 75207"
        five="4.7/5.0 stars - The Zodiac. A landmark since 1957, this Neiman Marcus eatery serves traditional American fare in chic surrounds. 1618 Main St, Dallas, TX 75201"
        six="4.6/5.0 stars - Unleavened Fresh Kitchen. Casual neighborhood cafe with a patio offering refined, health-conscious wraps & salads. 1900 Abrams Pkwy, Dallas, TX 75214"
        seven="4.4/5.0 stars - East Hampton Sandwich Co. Casual, stylish venue offering salads & refined sandwiches with creative sauces, plus beer & wine. 6912 Snider Plaza, Dallas, TX 75205"
        eight="4.4/5.0 stars - Flower Child. Fast-casual cafe featuring organic, locally sourced ingredients, with gluten-free & vegan choices. 5450 W Lovers Ln Suite 133, Dallas, TX 75209"
        nine="4.2/5.0 stars - The Common Table. Homey bar/eatery features unfussy American fare along with craft brews, patio seating & live music. 2917 Fairmount St, Dallas, TX 75201"
        ten="4.5/5.0 stars - Meso Maya. Contemporary Mexican eatery serving Oaxaca- & Puebla-inspired recipes to a trendy crowd. 1611 McKinney Ave, Dallas, TX 75202"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="san antonio":
        #started vegan search here 'vegan lunch..'
        one="4.5/5.0 stars - Green Vegetarian Cuisine. Eco-friendly spot serving a wide range of vegetarian, vegan & kosher fare in a bright, buzzy space. 10003 NW Military Hwy #2115, San Antonio, TX 78231"
        two="4.3/5.0 stars - Senor Veggie. Low-key, colorful BYOB eatery featuring an eclectic menu of organic, locally sourced vegan eats. 620 S Presa St, San Antonio, TX 78210"
        three="4.3/5.0 stars - Viva Vegeria. A vegan, gluten-free menu of Tex-Mex eats & baked goods served in colorful digs with a garden. 1422 Nogalitos St, San Antonio, TX 78204"
        four="4.6/5.0 stars - Bok Choy. 5130 Broadway, San Antonio, TX 78209"
        five="4.6/5.0 stars - 5 Points Local. Rustic-chic, counter-serve eatery offering coffee, tea, all-day breakfast & gluten-free/vegan fare. 1017 N Flores St, San Antonio, TX 78212"
        six="4.3/5.0 stars - La Botanica. Colorful cantina featuring a vegetarian-heavy menu of Mexican & Tex Mex eats & a patio with music. 2911 N St Mary's St, San Antonio, TX 78212"
        seven="4.2/5.0 stars - Adelante Restaurant. Unique, cash-only mainstay serving lard-free Tex-Mex, plus beer & wine in a folk-art-filled setting. 21 Brees Blvd, San Antonio, TX 78209"
        eight="4.6/5.0 stars - Earth Burger. Upbeat fast-food joint supplying vegetarian burgers & sandwiches, with a drive-thru & vegan options. 818 NW Loop 410, San Antonio, TX 78216"
        nine="4.3/5.0 stars - Tarka Indian Kitchen. Local counter-serve chain dishing up Indian curries, kebabs & more in a contemporary setting. 427 North Loop 1604 W #101, San Antonio, TX 78232"
        ten="4.9/5.0 stars - Sweet Yams. Small, funky cafe offering a healthy menu with organic, gluten-free & vegan options, plus takeout. 218 N Cherry St, San Antonio, TX 78202"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="austin":
        one="4.6/5.0 stars - Counter Culture. Innovative vegan fare (plus beer & wine) served in a blue-walled dining room or on an outdoor patio. 2337 E Cesar Chavez St, Austin, TX 78702"
        two="4.2/5.0 stars - Mr. Natural. Juice bar, bakery & eatery rolled into one, with vegetarian Mexican eats served in a modest setting. 1901 E Cesar Chavez St, Austin, TX 78702"
        three="4.6/5.0 stars - Arlo's. Food trailer outside Cheer Up Charlie's for vegan tacos & burgers, plus beer & picnic-table seats. 900 Red River, Austin, TX 78702"
        four="4.5/5.0 stars - Bouldin Creek Cafe. Eco-friendly, bohemian cafe offering hearty meatless meals, coffees & a rotating monthly art show. 1900 S 1st St, Austin, TX 78704"
        five="4.3/5.0 stars - Mother's Cafe & Garden. Chill, cheerful staple for vegetarian eats from the creative to the familiar, plus beer & wine. 4215 Duval St, Austin, TX 78751"
        six="4.1/5.0 stars - Swad Indian Vegetarian Restaurant. Ultracasual eatery serving meat-free Southern Indian fare such as its infamous dosa (filled crêpe). 9515 N Lamar Blvd, Austin, TX 78753"
        seven="4.8/5.0 stars - Sweet Ritual. Colorful ice cream parlor serving gluten-free & vegan scoops in cups, cones, shakes & sundaes. 4631 Airport Blvd #125, Austin, TX 78751"
        eight="4.8/5.0 stars - Bistro Vonish. Food truck with a fire pit & picnic tables, offering modern vegan meals made with local ingredients. 701 E 53rd St, Austin, TX 78751"
        nine="4.5/5.0 stars - The Vegan Nom. 2324 E Cesar Chavez St, Austin, TX 78702"
        ten="4.8/5.0 stars - Cool Beans. 2908 Fruth St, Austin, TX 78705"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="atlanta":
        one="4.5/5.0 stars - Cafe Sunflower. Relaxed locale offering a global vegetarian menu, including organic dishes & gluten-free options. 2140 Peachtree Rd NW, Atlanta, GA 30309"
        two="4.6/5.0 stars - Herban Fix - Vegan Kitchen. Pan-Asian dishes using strictly vegan, plant-based ingredients served in open, contemporary digs. 565 Peachtree St NE, Atlanta, GA 30308"
        three="4.6/5.0 stars - Green Sprout Vegetarian. Vegetarian Chinese cuisine, including meat substitutes, in a simple, strip-mall diner space. 1529 Piedmont Ave NE, Atlanta, GA 30324"
        four="4.3/5.0 stars - Soul Vegetarian. Southern, meat-free menu (with gluten-free & vegan options) served in a casual storefront space. 879 Ralph David Abernathy SW, Atlanta, GA 30310"
        five="4.7/5.0 stars - Viva la Vegan. Unfussy vegan restaurant serving wraps, sandwiches, burgers & sides in simple surrounds. 1265 Lee St SW, Atlanta, GA 30310"
        six="4.6/5.0 stars - Tassili's Raw Reality Cafe. Raw, vegetarian eatery fixing up an array of wraps, salads & mains in quaint environs. 1059 Ralph David Abernathy Blvd, Atlanta, GA 30310"
        seven="4.3/5.0 stars - R. Thomas' Deluxe Grill. Funky outdoor spot open 24/7 for organic menu of burgers & vegetarian fare amid greenery & birds. 1812 Peachtree Street, NW, Atlanta, GA 30309"
        eight="4.4/5.0 stars - True Food Kitchen. Relaxed, eco-chic chain serving health-conscious fare, including vegan options, plus cocktails. 3393 Peachtree Rd NE #3058b, Atlanta, GA 30326"
        nine="4.6/5.0 stars - Dulce Vegan Bakery & Cafe. Quaint spot preparing vegan baked goods, with gluten-, soy- & nut-free treats, plus espresso & tea. 1994 Hosea L Williams Dr NE, Atlanta, GA 30317"
        ten="4.8/5.0 stars. Aviva by Kameel. Easygoing counter-serve cafe & juice bar providing locally sourced, classic Mediterranean meals. 225 Peachtree St NW, Atlanta, GA 30303"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="seattle":
        one="4.4/5.0 stars. Vegan chain offering sandwiches, salads, faux meats & sides in a modern, counter-service setting. 1427 4th Ave, Seattle, WA 98101"
        two="4.3/5.0 stars. Vegetarian eats are served in this light-filled, bustling spot with a courtyard. 2901 E Madison St, Seattle, WA 98112"
        three="4.4/5.0 stars. Organic, sustainable vegan dishes featuring seitan & tofu in an industrial-chic space. 1429 12th Ave, Seattle, WA 98122"
        four="4.4/5.0 stars. Chaco Canyon Organic Cafe. Quirky setting with vegan offerings, including raw food & smoothies, plus organic beer & wine. 4757 12th Ave NE, Seattle, WA 98105"
        five="4.2/5.0 stars. Casual mainstay near the Seattle Center delivering vegetarian versions of Asian specialties. 364 Roy St, Seattle, WA 98109"
        six="4.6/5.0 stars. Arya's Place. Refined, artful restaurant serving a vegan-only Thai menu including a lunch buffet & cocktails. 5240 University Way NE, Seattle, WA 98105"
        seven="4.9/5.0 stars. Harvest Beat. Eco-friendly destination offering intricate garden-to-table vegan dishes in set-price dinners. 1711 N 45th St, Seattle, WA 98103"
        eight="4.5/5.0 stars. Wayward Vegan Cafe. Informal counter-service spot with a wide range of vegan fare, including all-day breakfast & lunch. 801 NE 65th St, Seattle, WA 98115"
        nine="4.7/5.0 stars. Eggs and Plants. Casual Middle Eastern cafe serving egg- & veggie-based pita sandwiches for breakfast & lunch. 2229 5th Ave, Seattle, WA 98121"
        ten="4.4/5.0 stars. HeartBeet Organic Superfoods Cafe. Casual spot known for its gluten- & diary-free food & smoothies also sells juice cleanses. 1026 Northeast 65th Street #A102, Seattle, WA 98115"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="san francisco":
        one="4.3/5.0 stars - Golden Era. Vegan eatery for Asian-fusion dishes served in a bright, casual space with banquette seating. 395 Golden Gate Ave, San Francisco, CA 94102"
        two="4.4/5.0 stars - Enjoy Vegetarian Restaurant. Casual Chinatown restaurant serving mock-meat & faux-fish versions of Chinese standards. 839 Kearny St, San Francisco, CA 94108"
        three="4.3/5.0 stars - Ananda Fuara. Spiritual guru Sri Chinmoy is the driving force behind this celebrated vegetarian & vegan eatery. 1298 Market St, San Francisco, CA 94102"
        four="4.3/5.0 stars - Indochine Vegan. Comfortable cafe with a neighborhood vibe featuring vegan Asian dishes, from pho to curries. 508 Valencia St, San Francisco, CA 94110"
        five="4.1/5.0 stars - Greens Restaurant. Celebrated mainstay for inventive & sustainable vegetarian dishes as well as panoramic bay views. Landmark Building A, Fort Mason Center, 2 Marina Blvd, San Francisco, CA 94123"
        six="4.8/5.0 stars - Shizen Vegan Shushi Bar & Izakaya. Vegan fare, from faux-sushi & ramen to meatless small plates, in an inventive, wood-decked space. 370 14th St, San Francisco, CA 94103"
        seven="4.1/5.0 stars -Vegan Picnic. Vegan cafe & market for plant-based American deli classics, gluten-free eats & gourmet groceries. 1977 Union St, San Francisco, CA 94123"
        eight="4.4/5.0 stars - VeganBurg SF. Well-styled counter-serve cafe offering vegan burgers and plant-based New American standards. 1466 Haight St, San Francisco, CA 94117"
        nine="4.2/5.0 stars - The Plant Cafe Organic. 250 Montgomery St #101, San Francisco, CA 94104"
        ten="4.6/5.0 stars - The FLying Falafel. Casual, colorful stop for counter-serve falafel sandwiches & other housemade Mediterranean eats. 1051 Market St, San Francisco, CA 94103"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="los angeles":
        one="4.5/5.0 stars - Crossroads Kitchen. Upscale eatery provides an elegant backdrop for refined vegan dishes paired with wines & cocktails. 8284 Melrose Ave, Los Angeles, CA 90046"
        two="4.5/5.0 stars - Sage Vegan Bistro and Brewery. Casual neighborhood spot offering a long list of vegan & veggie dishes, including desserts. 1700 Sunset Blvd, Los Angeles, CA 90026"
        three="4.5/5.0 stars - Au Lac LA. Strip-mall eatery serving creative vegan fare with Asian influence in a serene dining room. 710 W 1st St, Los Angeles, CA 90012"
        four="4.6/5.0 stars - Elf Cafe. Organic, locally sourced, Mediterranean-style vegetarian dishes in a tiny but welcoming space. 2135 Sunset Blvd, Los Angeles, CA 90026"
        five="4.6/5.0 stars - Shojin. Spicy tofu replaces the tuna in the sushi served at this refined vegan Japanese eatery. Little Tokyo Shopping Center, 333 Alameda St #310, Los Angeles, CA 90013"
        six="4.3/5.0 stars - Native Foods Cafe. Chain for creative, Californian-style vegan fare, including mock-meat dishes, ordered at a counter. 1114 Gayley Ave, Los Angeles, CA 90024"
        seven="4.7/5.0 stars - Azla Ethiopian Vegan Cuisine. Casual, cheery counter-serve with small tables specializing in vegan renditions of Ethiopian dishes. 3655 S Grand Ave, Los Angeles, CA 90007"
        eight="4.6/5.0 stars - Fore Vegan. Neighborhood standby lures locals with a large vegan menu with gluten-free options in a homey space. 3818 Sunset Blvd, Los Angeles, CA 90026"
        nine="4.4/5.0 stars - Veggie Grill. Vegan chain offering sandwiches, salads, faux meats & sides in a modern, counter-service setting. 110 S Fairfax Ave, Los Angeles, CA 90036"
        ten="4.6/5.0 stars - The Grain Cafe. This relaxed eatery features an eclectic menu of vegan, natural & organic sandwiches, pizza & more. 4222 W Pico Blvd, Los Angeles, CA 90019"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    else:
        print("Your city currently not supported to recommend breakfast. Check back in a few months.")
   
    homeorout=random.randint(0,1)
    if homeorout==0:
        #go out suggestion
        return option 
    elif homeorout==1:
        one="Make a spinach salad! \n\n This leafy-green veggie is rich in stress-busting magnesium. People with low magnesium levels (most of us, actually) are more likely to have elevated C-reactive protein levels—and research shows people with high CRP levels are more stressed and at a greater risk for depression. Magnesium helps regulate cortisol and blood pressure too. And since magnesium gets flushed out of the body when you’re stressed, it’s crucial to get enough. Other solid magnesium sources: beans, brown rice." 
        two="Eat some vegetable curry! \n\n Vegetable curry has spices that reduce stress."
        three="Make an avocado-swiss turkey sandwich! \n\n Turkey breast is cheap at the store and good for general health. Avocados reduce stress with antioxidants."
        four="Eat dark chocolate as a snack! Skip milk chocolate and go for dark chocolate to lower stress hormone (cortisol)."
        five="Eat whole wheat pretzels! \n\n When staring down the vending machine, opt for whole-grain snacks like whole-wheat pretzels or crackers. Not only will you feel fuller from the fiber, but also the carbohydrates offer an energy boost and trigger the brain to release a feel-good chemical called serotonin."
        #fix this info below, need more lunch options 
        six="Make a Peanutty Edamame and Noodle Salad! Nutrition Information (per serving): About 455 calories, 22 g protein, 50 g carbs, 22 g fat (3 g saturated fat), 13 g fiber, 540 mg sodium. http://www.goodhousekeeping.com/food-recipes/healthy/a42200/peanutty-edamame-and-noodle-salad-recipe/"
        seven="Make a Roasted Squash and Pumpkin Seed Mole Bowl! Nutritional Information (per serving): About 440 cals, 10 g protein, 60 g carbs, 19 g fat (6 g sat), 5 g fiber, 605 mg sodium. http://www.goodhousekeeping.com/food-recipes/easy/a36255/roasted-squash-and-pumpkin-seed-mole-bowls/"
        eight="Make a Creamy Vegan Linguine with Mild Mushrooms! Nutritional Information (per serving): About 430 cals, 15 g protein, 62 g carbs, 15 g fat (2 g sat), 5 g fiber, 175 mg sodium. http://www.goodhousekeeping.com/food-recipes/easy/a36260/creamy-vegan-linguine-with-wild-mushrooms/"
        nine="Make Crispy Potatoes with Vegan Nacho Sauce! Nutritional Information (per serving): About 380 cals, 10 g protein, 47 g carbs, 18 g fat (2 g sat), 6 g fiber, 520 mg sodium. http://www.goodhousekeeping.com/food-recipes/easy/a36256/crispy-potatoes-with-vegan-nacho-sauce/"
        ten="Make Garden Greens and Pumpernickel Panzanella! Nutritional Nutritional Information (per serving): Calories 330; Protein 11g; Carbohydrate 51g; Total Fat 10g; Saturated Fat 1g; Dietary Fiber 9g; Sodium 870mg http://www.goodhousekeeping.com/food-recipes/a38313/garden-greens-and-pumpernickel-panzanella-recipe/"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
        option=str(option)
        index1=option.index('!') 
        if coffeenum >= 2: 
            return str(option[:(index1)]+" and drink one cup of coffee!"+option[(index1+1):]).replace('\xa0','')
        else:
            return str(option).replace('\xa0','')

def dinner(alcohol,coffee,city):
   #playbackaudio("making dinner", "dinner.mp3")

   #maybe separate dinner by city like in exercise 
    if city == "chicago":
        #vegan dinner search on google.com created these datasets 
        one="4.6/5.0 stars - Chicago Diner. No-frills diner serving a large menu of creative vegetarian & vegan comfort food since 1983. 3411 N Halsted St, Chicago, IL 60657"
        two="4.6/5.0 stars - Native Foods Cafe. Chain for creative, Californian-style vegan fare, including mock-meat dishes, ordered at a counter. 218 S Clark St, Chicago, IL 60604"
        three="4.8/5.0 stars - Upton's Breakroom. Cafe serving light vegan fare in a bright, modern space attached to Upton's Naturals seitan factory. 2054 W Grand Ave, Chicago, IL 60612"
        four="4.8/5.0 stars - Amitabul. Modest restaurant serving a vegan, organic Korean menu that includes noodle soups, tofu & bibimbop. 6207 N Milwaukee Ave, Chicago, IL 60646"
        five="4.2/5.0 stars - Green Zebra. Vegetarian restaurant with seasonal, creative small plates in a sleek setting. 1460 W Chicago Ave, Chicago, IL 60642"
        six="4.5/5.0 stars - Handlebar. Small, bustling neighborhood restaurant & bar serving seafood & vegetarian/vegan comfort food. 2311 W North Ave, Chicago, IL 60647"
        seven="4.5/5.0 stars - Urban Vegan. Vegan food, including dumplings, noodles, rice, curry & burgers, made with seitan & soy-meat. 1605 W Montrose Ave, Chicago, IL 60613"
        eight="4.6/5.0 stars - Kitchen 17. Seitan is housemade at this snug vegan BYOB cafe, which offers Middle Eastern & American light fare. 3132 N Broadway St, Chicago, IL 60657"
        nine="4.9/5.0 stars - Loving Heart Vegan Cafe. Relaxed all-vegan eatery offering coffee, tea, wraps, salads, smoothies & desserts. 838 W Montrose Ave, Chicago, IL 60613"
        ten="4.5/5.0 stars - Mana Food Bar. Trendy, intimate spot with global vegetarian/vegan food, smoothies, sake cocktails & sidewalk seats. 1742 W Division St, Chicago, IL 60622"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city =="boston":
        one="4.1/5.0 stars - Sweetgreen. Locavore-friendly counter-serve chain specializing in organic salads, soup & bowls. 800 Boylston St #17, Boston, MA 02199"
        two="4.4/5.0 stars - My Thai Vegan Cafe. Meatless options abound at this informal 2nd-story spot, also known for its range of bubble teas. 3 Beach St #2, Boston, MA 02111"
        three="4.5/5.0 stars - Clover Food Lab - LMA. 360 Longwood Ave, Boston, MA 02215"
        four="4.3/5.0 stars - Grasshopper. Casual vegetarian/vegan Asian eatery, specializing in meat & seafood substitutes & vegan desserts. 1 N Beacon St, Boston, MA 02134"
        five="4.7/5.0 stars - Life Alive Urban Oasis and Organic Cafe. Friendly, funky, quick-serve spot for organic veggie/vegan wraps, salads & smoothies. 765 Massachusetts Ave, Cambridge, MA 02139"
        six="4.2/5.0 stars - by CHLOE. Popular NYC-founded chain for vegan dishes, sweets & juices in a trendy quick-serve space. 107 Seaport Blvd, Boston, MA 02210"
        seven="4.5/5.0 stars - Veggie Galaxy. Imaginative twist on an old-school diner specializing in from-scratch vegan & vegetarian options. 450 Massachusetts Ave, Cambridge, MA 02139"
        eight="4.7/5.0 stars - Cornish Pasty Co. 51 Massachusetts Ave, Boston, MA 02115"
        nine="4.4/5.0 stars - Red Lentil Vegetarian & Vegan Restaurant. Vegetarian & vegan destination with seasonal ingredients, wine & beer, plus gluten-free options. 600 Mt Auburn St, Watertown, MA 02472"
        ten="4.7/5.0 stars - Taco Party. Colorful, kitschy counter-serve spot with a meatless Mexican menu starring inventive veggie tacos. 711 Broadway, Somerville, MA 02144"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="philadelphia":
        one="4.3/5.0 stars - New Harmony Vegetarian Restaurant. Chinese BYOB venue with a vegan & veggie menu of lighter & fried items, including meat substitutes. 135 N 9th St, Philadelphia, PA 19107"
        two="4.7/5.0 stars - Vedge. Restaurant serving inventive vegan & vegetarian small plates in a charming old mansion. 1221 Locust St, Philadelphia, PA 19107"
        three="4.6/5.0 stars - HipCityVeg. Healthful dine-in or take-out vegan food & smoothies served in a small, industrial-looking space. 127 S 18th St, Philadelphia, PA 19103"
        four="4.4/5.0 stars - Vegan Tree. Cozy vegan venue serving sushi, burgers & bubble tea along with vegetarian options in cheerful digs. 742 South St, Philadelphia, PA 19147 "
        five="4.6/5.0 stars - Charlie was a sinner. Vegan cafe/bar dishing up creative, plant-based small plates & drinks in sexy, dark environs. 131 S 13th St, Philadelphia, PA 19107"
        six="4.6/5.0 stars - V Street. Vegan riffs on global street food served in small wood-and-brick space with a bar & kitchen counter. 126 S 19th St, Philadelphia, PA 19103"
        seven="4.8/5.0 stars - Miss Rachel's Pantry. Sunny storefront serving a prix fixe vegan menu on Saturdays, plus light market-style bites. 1938 S Chadwick St, Philadelphia, PA 19145"
        eight="4.5/5.0 stars - Blackbird Pizzeria. Artisanal pizzas, sandwiches & more made with ingredients like seitan sausage, garlic butter & tofu. 507 S 6th St, Philadelphia, PA 19147"
        nine="4.6/5.0 stars - The Nile Cafe. Laid-back, counter-serve eatery specializing in plentiful portions of vegan & vegetarian soul food. 6008 Germantown Ave, Philadelphia, PA 19144"
        ten="4.7/5.0 stars - Grindcore House. Hip coffeehouse where the drinks & eats are vegan-friendly & the grindcore soundtrack is intense. 1515 S 4th St, Philadelphia, PA 19147"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="new york city":
        one="4.5/5.0 stars - Blossom. Vegan dishes, wine & an intimate setting in a historical 9th Avenue building. 187 9th Ave, New York, NY 10011"
        two="4.4/5.0 stars - Franchia Vegan Cafe. Creative, vegan Asian fusion dishes presented in a serene, tea-house-inspired setting. 12 Park Ave, New York, NY 10016"
        three="4.5/5.0 stars - Seasoned Vegan. This counter-serve offers vegan dishes from organic ingredients prepared with global flavors. 55 St Nicholas Ave, New York, NY 10026"
        four="4.3/5.0 stars - by CHLOE. Vegan counter-serve pit stop with creative fare, juices & baked goods in trendy digs. 185 Bleecker St, New York, NY 10012"
        five="4.3/5.0 stars - VSPOT Organic. 12 St Marks Pl, New York, NY 10003"
        six="4.5/5.0 stars - Blossom Du Jour. This health-conscious cafe with juice bar serves vegan American fare including gluten-free options. 259 W 23rd St, New York, NY 10011"
        seven="4.4/5.0 stars - Terri. A brightly decorated counter-service spot with vegetarian sandwiches, salads, juices & sweets. 60 W 23rd St, New York, NY 10010"
        eight="4.7/5.0 stars - Beyond Sushi Union Square. A vet of TV's Hell's Kitchen makes fish-free sushi & other bites with seasonal veggies & fruit. 229 E 14th St, New York, NY 10003"
        nine="4.5/5.0 stars - Peacefood. Casual, stylish cafe with an arty vibe serving creative vegan fare, plus desserts & smoothies. 41 E 11th St, New York, NY 10003"
        ten="4.6/5.0 stars - Le Botaniste. Homey, apothecary-inspired counter serve for vegan, organic bowls, juices & natural wines. 833 Lexington Ave, New York, NY 10065"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="houston":
        one="4.5/5.0 stars - green seed vegan. Casual spot for raw & vegan gourmet sandwiches, juices & smoothies in an airy, open space. 4320 Almeda Rd, Houston, TX 77004"
        two="4.5/5.0 stars - Green Vegetarian Cuisine. 6720 Chimney Rock Rd, Houston, TX 77081"
        three="4.4/5.0 stars - Loving Hut. Outpost of a vegan counter-serve chain with Asian-accented menus that vary by location. 2825 S Kirkwood Rd, Houston, TX 77082"
        four="4.4/5.0 stars - Healthy Cow Pizza. 3005 West Loop S, Houston, TX 77027"
        five="4.6/5.0 stars - Govinda's Vegetarian Cuisine. Hand-painted murals highlight this roomy eatery serving a buffet of vegetarian Indian cuisine. 1320 W 34th St, Houston, TX 77018"
        six="4.4/5.0 stars - True Food Kitchen. Relaxed, eco-chic chain serving health-conscious fare, including vegan options, plus cocktails. 1700 Post Oak Blvd, Houston, TX 77056"
        seven="4.0/5.0 stars - Field of Greens. Vegetarian & vegan dishes, including raw & macrobiotic items, in a relaxed, counter-serve setting. 2320 W Alabama St, Houston, TX 77098"
        eight="4.4/5.0 stars - Pepper Tree Veggie Cuisine. Asian-style vegan eats ordered a la carte or as part of an all-you-can-eat lunch buffet. 3821 Richmond Ave, Houston, TX 77027"
        nine="4.5/5.0 stars - Aladdin Mediterranean Cuisine. Laid-back eatery with ample seating offering shawarma, kebabs, gyros & other Mediterranean staples. 912 Westheimer Rd, Houston, TX 77006"
        ten="4.5/5.0 stars - Caracol. Upscale eatery offering Mexican seafood dishes, booze, an oyster bar & more in a bright, arty space. 2200 Post Oak Blvd #160, Houston, TX 77056"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="dallas":
        one="4.6/5.0 stars - Spiral Diner & Bakery. Branch of a small chain offering creative, organic-leaning vegan fare in funky, retro-themed digs. 1101 N Beckley Ave, Dallas, TX 75203"
        two="4.7/5.0 stars - D'Vegan. This petite shopping center food-court pit stop specializes in all-vegan Vietnamese cuisine. 9780 Walnut St, Dallas, TX 75243"
        three="4.5/5.0 stars - Be Raw Food and Juice. Casual modern cafe serving a full menu of vegan foods, craft smoothies & gluten-free desserts. 6005 Berkshire Ln, Dallas, TX 75225"
        four="4.6/5.0 stars - Kalachandji's. Vegetarian Indian buffet with garden courtyard seating within an exotic Hare Krishna temple. 5430 Gurley Ave, Dallas, TX 75223"
        five="4.3/5.0 stars - Cosmic Cafe. Creative, Indian-accented vegetarian eats & smoothies in a cozy house with on-site yoga classes. 2912 Oak Lawn Ave, Dallas, TX 75219"
        six="4.4/5.0 stars - Sundown at Granada. Eatery & beer garden offering farm-to-table fare, 60+ beers & live music amid plank & brick walls. 3520 Greenville Ave, Dallas, TX 75206"
        seven="4.4/5.0 stars - Flower Child. Fast-casual cafe featuring organic, locally sourced ingredients, with gluten-free & vegan choices. 5450 W Lovers Ln Suite 133, Dallas, TX 75209"
        eight="4.8/5.0 stars - Goji Cafe. Relaxed cafe offering a menu of inventive vegan Asian dishes, salads & wraps, with a lunch buffet. 2330 Royal Ln #900, Dallas, TX 75229"
        nine="4.6/5.0 stars - True Food Kitchen. Relaxed, eco-chic chain serving health-conscious fare, including vegan options, plus cocktails. 8383 Preston Center Plaza #100, Dallas, TX 75225"
        ten="4.6/5.0 stars - Velvet Taco. Tacos with global flavor inspirations plus boutique sodas & beers in hip, fast-food-style joint 3012 N Henderson Ave, Dallas, TX 75206"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="san antonio":
        one="4.5/5.0 stars - Green Vegetarian Cuisine. Chill eatery doling out vegetarian & vegan versions of everyday dishes in funky, industrial digs. 200 E Grayson St #120, San Antonio, TX 78215"
        two="4.3/5.0 stars - Senor Veggie. Low-key, colorful BYOB eatery featuring an eclectic menu of organic, locally sourced vegan eats. 620 S Presa St, San Antonio, TX 78210"
        three="4.3/5.0 stars - La Botanica. Colorful cantina featuring a vegetarian-heavy menu of Mexican & Tex Mex eats & a patio with music. 2911 N St Mary's St, San Antonio, TX 78212"
        four="4.6/5.0 stars - Bok Choy. 5130 Broadway, San Antonio, TX 78209"
        five="4.4/5.0 stars - Bejing Restaurant & Gift Shop. Unfussy counter dishing up familiar Chinese grub, including sesame chicken & wonton soup. 13730 Embassy Row, San Antonio, TX 78216"
        six="4.5/5.0 stars - Louie Italian Restaurant. Homemade pastas, pizza flat breads & more served in a rustic, relaxed atmosphere with a full bar. 4979 NW Loop 410, San Antonio, TX 78229"
        seven="4.2/5.0 stars - Chipotle (get tofu option). Fast-food chain offering Mexican fare, including design-your-own burritos, tacos & bowls. 3928 Broadway St, San Antonio, TX 78209"
        eight="4.7/5.0 stars - Zedric's: Fit with Flavor. This takeaway outfit dispenses pre-packaged, health-focused meals prepared each day. 9873 Interstate 10, Colonnade I, San Antonio, TX 78230"
        nine="4.5/5.0 stars - Healthy Me. 209 E Travis St, San Antonio, TX 78205"
        ten="4.9/5.0 stars - Sweet Yams. Small, funky cafe offering a healthy menu with organic, gluten-free & vegan options, plus takeout. 218 N Cherry St, San Antonio, TX 78202"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="austin":
        one="3.9/5.0 stars - Chipotle (get tofu option). 801 Congress Ave, Austin, TX 78701"
        two="4.3/5.0 stars - Koriente. Pan-Asian fare, including vegan & gluten-free options, in a homey, easygoing eatery with a patio. 621 E 7th St, Austin, TX 78701"
        three="4.5/5.0 stars - Blue Dahlia Bistro. Light bites, tartines & big plates served in a casual interior or on the gardenlike back patio. 1115 E 11th St, Austin, TX 78702"
        four="4.0/5.0 stars - Thai Fresh. Cooked-to-order dishes & homemade ice creams, plus market with hard-to-find Thai ingredients. 909 W Mary St, Austin, TX 78704"
        five="4.4/5.0 stars - Eastside Cafe. They grow their own veggies at this American eatery serving simple, seasonal food in a bungalow. 2113 Manor Rd, Austin, TX 78722"
        six="4.6/5.0 stars - Counter Culture. Innovative vegan fare (plus beer & wine) served in a blue-walled dining room or on an outdoor patio. 2337 E Cesar Chavez St, Austin, TX 78702"
        seven="4.7/5.0 stars - Uchiko. Offshoot of the famed Uchi restaurant with upscale sushi & small plates in a farmhouse-chic space. 4200 N Lamar Blvd, Austin, TX 78756"
        eight="4.3/5.0 stars - The Steeping Room. Selection of teas, sandwiches, salads & baked goods plus sidewalk seating in Domain outdoor mall. 11410 Century Oaks Terrace #112, Austin, TX 78758"
        nine="4.2/5.0 stars - Roaring Fork. Wood-fired steaks & slow-roasted pork, plus cocktails & dessert in the InterContinental Hotel. 701 Congress Ave, Austin, TX 78701"
        ten="4.3/5.0 stars - THe Carillon. High-end restaurant within the AT&T Center serving American fare, also with a lounge menu. 1900 University Ave, Austin, TX 78705"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="atlanta":
        one="3.7/5.0 stars - Chipotle (get tofu option). 718 Ponce De Leon Ave NE, Atlanta, GA 30306"
        two="4.4/5.0 stars - Fresh too Order - Midtown. Chain restaurant serving deli-style American fare, including salads, paninis & long plates. 860 Peachtree St NE, Atlanta, GA 30308"
        three="4.4/5.0 stars - True Food Kitchen. Relaxed, eco-chic chain serving health-conscious fare, including vegan options, plus cocktails. 3393 Peachtree Rd NE #3058b, Atlanta, GA 30326"
        four="4.7/5.0 stars - MetroFresh. Tiny eatery with shaded patio offering a simple, daily changing menu of soups & sandwiches. 931 Monroe Dr NE a106, Atlanta, GA 30308"
        five="4.4/5.0 stars - Bistro Niko. Bustling hot spot presents classic French bistro fare amid warm lighting & elegant decor. 3344 Peachtree Road, Atlanta, GA 30326"
        six="4.2/5.0 stars - Ray's in the City. Upscale setting for seafood, prime cuts & an extensive wine list, plus live jazz Thursday-Saturday. 240 Peachtree St NW, Atlanta, GA 30303"
        seven="4.8/5.0 stars - Kitchen Six. A compact New American menu highlighting local ingredients offered in an intimate, chic setting. 2751 Lavista Rd, Decatur, GA 30033"
        eight="4.6/5.0 stars - Herban Fix - Vegan Kithen. Pan-Asian dishes using strictly vegan, plant-based ingredients served in open, contemporary digs. 565 Peachtree St NE, Atlanta, GA 30308"
        nine="4.5/5.0 stars - Cafe Sunflower. Relaxed locale offering a global vegetarian menu, including organic dishes & gluten-free options. 2140 Peachtree Rd NW, Atlanta, GA 30309"
        ten="4.7/5.0 stars - Viva la Vegan. Unfussy vegan restaurant serving wraps, sandwiches, burgers & sides in simple surrounds. 1265 Lee St SW, Atlanta, GA 30310"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="seattle":
        one="3.9/5.0 stars - Chipotle (get tofu option). 1501 3rd Ave, Seattle, WA 98101"
        two="4.4/5.0 stars - Caco Canyon Organic Cafe. Quirky setting with vegan offerings, including raw food & smoothies, plus organic beer & wine. 4757 12th Ave NE, Seattle, WA 98105"
        three="4.1/5.0 stars - Local 360. Ingredients, beer & wine are all obtained within 360 miles of this rustic comfort-food resource. 2234 1st Ave, Seattle, WA 98121"
        four="4.4/5.0 stars - Plum Bistro. Organic, sustainable vegan dishes featuring seitan & tofu in an industrial-chic space. 1429 12th Ave, Seattle, WA 98122"
        five="4.9/5.0 stars - Harvest Beat. Eco-friendly destination offering intricate garden-to-table vegan dishes in set-price dinners. 1711 N 45th St, Seattle, WA 98103"
        six="4.6/5.0 stars - Bounty Kitchen. Organic ingredients are highlighted at this bright eatery known for its healthy-focused menu. 7 Boston St, Seattle, WA 98109"
        seven="4.4/5.0 stars - Chaco Canyon Organic Cafe. Vegan, raw & mostly organic eats, plus smoothies & juices, served in an upbeat, airy space. 3770 SW Alaska St, Seattle, WA 98126"
        eight="4.7/5.0 stars - Eggs and Plants. Casual Middle Eastern cafe serving egg- & veggie-based pita sandwiches for breakfast & lunch. 2229 5th Ave, Seattle, WA 98121"
        nine="4.7/5.0 stars - dueminuti healthy pasta. Bright, relaxed cafe serving health-conscious, handmade pastas topped with seasonal sauces. 412 Broadway E, Seattle, WA 98102"
        ten="4.5/5.0 stars - Gorditos. Casual standby serving large portions of Mexican fare made with healthier ingredients. 213 N 85th St, Seattle, WA 98103"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    elif city=="san francisco":
        one="3.7/5.0 stars - Chipotle (get tofu option). 232 O'Farrell St, San Francisco, CA 94102"
        two="4.4/5.0 stars - Picnic on Third. Charming, petite spot serving a rotating menu of New American fare, plus beer, wine & coffee. 493 3rd St, San Francisco, CA 94107"
        three="4.1/5.0 stars - Greens Restaurant. Celebrated mainstay for inventive & sustainable vegetarian dishes as well as panoramic bay views. Landmark Building A, Fort Mason Center, 2 Marina Blvd, San Francisco, CA 94123"
        four="4.3/5.0 stars - Lite Bite. Bright, low-key cafe offering calorie-conscious American fare such as organic salads, salmon & soup. 1796 Union St, San Francisco, CA 94123"
        five="4.5/5.0 stars - Souvla. Hip haunt featuring roasted meat sandwiches & salads, plus Greek yogurt, beer & wine. 517 Hayes St, San Francisco, CA 94102"
        six="4.3/5.0 stars - Judhlicious Juice. Cafe specializing in locally sourced, organic coffee, smoothies & juices plus raw & vegan snacks. 3906 Judah St, San Francisco, CA 94122"
        seven="4.7/5.0 stars - Vegan Picnic. Vegan cafe & market for plant-based American deli classics, gluten-free eats & gourmet groceries. 1977 Union St, San Francisco, CA 94123"
        eight="4.2/5.0 stars - Loving Hut. Outpost of a vegan counter-serve chain with Asian-accented menus that vary by location. 845 Market St, San Francisco, CA 94103"
        nine="4.4/5.0 stars - Millennium. Vegetarian restaurant for inventive, locally sourced dishes in a rustic-modern space with a patio. 5912 College Ave, Oakland, CA 94618"
        ten="4.3/5.0 stars - Shangrila Vegetarian Rest. Chinese eatery serves noodle dishes, faux meats & other vegetarian, vegan & kosher dishes. 2026 Irving St, San Francisco, CA 94122"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)        
    elif city=="los angeles":
        one="4.0/5.0 stars - Chipotle (get tofu option). 3748 S Figueroa St, Los Angeles, CA 90007"
        two="4.6/5.0 stars - sweetgreen. Locavore-friendly counter-serve chain specializing in organic salads, soup & bowls. 8055 W 3rd St, Los Angeles, CA 90048"
        three="4.5/5.0 stars - Cafe Gratitude. Vegan organic fare & smoothies with hippie-inspired names served in a casual interior or on a patio. 639 N Larchmont Blvd, Los Angeles, CA 90004"
        four="4.4/5.0 stars - Evo Kitchen. Veggie, vegan & gluten-free options are made from organic, local ingredients at this green eatery. 7950 Sunset Blvd #104, Los Angeles, CA 90046"
        five="4.1/5.0 stars - Locali Hollywood.  Casual, yet chic cafe focusing on local fare, with options for vegan & gluten-free diets. 5825 Franklin Ave, Los Angeles, CA 90028"
        six="4.5/5.0 stars - Crossroads Kitchen. Upscale eatery provides an elegant backdrop for refined vegan dishes paired with wines & cocktails. 8284 Melrose Ave, Los Angeles, CA 90046"
        seven="4.7/5.0 stars - Kye's. Smoothies, mocktails, shakes & burrito-wrap hybrids are on offer at this health-focused eatery. 1518 Montana Ave, Santa Monica, CA 90403"
        eight="4.5/5.0 stars - SunCafe. Sit-down spot featuring a multilevel patio, beer & wine bar & a variety of raw, vegan cuisine. 10820 Ventura Blvd, Studio City, CA 91604"
        nine="4.4/5.0 stars - Forage. Small, family-owned eatery serves seasonal, locally sourced Californian fare for dine-in or takeout. 3823 Sunset Blvd, Los Angeles, CA 90026"
        ten="4.6/5.0 stars - The Springs. Casual vegan eatery & wine bar in eco-friendly digs with bare cinder-block walls & concrete floors. 608 Mateo St, Los Angeles, CA 90021"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
    else:
        print("Your city currently not supported to recommend breakfast. Check back in a few months.")

    homeorout=random.randint(0,1)
    if homeorout==0:
        #go out suggestion
        return option 
    elif homeorout==1:
    #need to add to this dinner list. get 10 options. 
        one="Make a salmon dinner with asparagus! \n\n salmon is rich in omega 3 fatty acids EPA and DHA, which can reduce inflammation, lower blood pressure, and decrease risk factors for disease (http://www.healthline.com/nutrition/11-benefits-of-salmon)." 
        two="Make cod with nuts! \n\n Cod is rich in omega-3 fatty acids and vitamin B6 and B12, helping to keep homocysteine levels low and reducing risk of heart attach and stroke and nuts are good source of protein (http://www.whfoods.com/genpage.php?tname=foodspice&dbid=133)."
        three="Make spaghetti with meatballs! \n\n Spaghetti is a dietary source of vitamins, minerals and fiber --especially if you purchase whole grain or whole-wheat pasta (http://www.livestrong.com/article/512565-what-are-the-benefits-of-spaghetti/)."
        #fix this info below, need more dinner options 
        four="Eat dark chocolate as a snack! Skip milk chocolate and go for dark chocolate to lower stress hormone (cortisol)."
        five="Eat whole wheat pretzels! \n\n When staring down the vending machine, opt for whole-grain snacks like whole-wheat pretzels or crackers. Not only will you feel fuller from the fiber, but also the carbohydrates offer an energy boost and trigger the brain to release a feel-good chemical called serotonin."
        six="Make a Crispy Tofu Bowl! About 440 cals/serving, 18 g protein, 45 g carbs, 20 g fat (2 g sat), 5 g fiber, 310 mg sodium. http://www.goodhousekeeping.com/food-recipes/easy/a45226/crispy-tofu-bowl-recipe/"
        seven="Make Summer Vegan Pesto Pasta! About 370 cals/serving, 12 g protein, 54 g carbs, 12 g fat (2 g sat), 5 g fiber, 435 mg sodium. http://www.goodhousekeeping.com/food-recipes/a44097/summer-pesto-pasta-recipe/"
        eight="Make a Beet, Mushroom, and Avocado Salad! About 370 cals/serving, 7 g protein, 32 g carbs, 26 g fat (4 g sat), 11 g fiber, 490 mg sodium. http://www.goodhousekeeping.com/food-recipes/a43225/beet-mushroom-avocado-salad-recipe/"
        nine="Make Gegan Spring Minestrone! About 330 cals/serving, 7 g protein, 62 g carbs, 7 g fat (1 g sat), 7 g fiber, 1,030 mg sodium. http://www.goodhousekeeping.com/food-recipes/a43221/spring-minestrone-recipe/"
        ten="Make BBQ Chickpea & Cauliflower Flatbreads with Avocado Mash!  Calories 500/serving; Protein 11g; Carbohydrate 65g; Total Fat 25g; Saturated Fat 4g; Dietary Fiber 13g; Sodium 915mg. http://www.goodhousekeeping.com/food-recipes/a40929/bbq-chickpea-cauliflower-flatbreads-with-avocado-mash-recipe/"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten)
        option=str(option)
        index1=option.index('!')
        if alcoholnum > 0: 
            if alcoholnum > 7:
                return str(option[:(index1)]+" and drink one cup of red wine!"+option[(index1+1):]+" Red wine has antioxidants to help you de-stress. Just don't overdo it: limit to one glass.").replace('\xa0','')
            else:
                x=random.randint(0,1)
                if x==0:
                    return option
                if x==1:
                    return str(option[:(index1)]+" and drink one cup of red wine!"+option[(index1+1):]+" Red wine has antioxidants to help you de-stress. Just don't overdo it: limit to one glass.").replace('\xa0','')

        elif coffee > 2:
            return option[:(index1)]+" and drink one cup of coffee!"+option[(index1+1):].replace('\xa0','')
        else:
            return option.replace('\xa0','')


def get_date():
    return str(datetime.datetime.now())

##############################################################################
##                            MAIN SCRIPT                                   ##
##############################################################################

# some other initial variables 
coffeenum=1
coffee='yes'
alcoholnum=2
tea='yes'
now=datetime.datetime.now().hour

#pull up webbrowser
webbrowser.open("http://actions.neurolex.co/uploads/nutrition.m4a")
time.sleep(2)
webbrowser.open('http://actions.neurolex.co/uploads/nutrition.png')
time.sleep(6) 

#for demo purposes 
try:
    city = curloc()['city'].lower()
    if city == 'cambridge':
        city='boston'
except:
    print('error, defaulting to boston')
    city='boston'

notify=list()

for i in range(3):
    
    if datetime.datetime.now().hour >=0 and datetime.datetime.now().hour <12:
        output=breakfast(coffeenum,tea,city)
        print("Go eat some breakfast! " + output)
        mealtype='breakfast'
        notify.append(output)
    elif datetime.datetime.now().hour >=12 and datetime.datetime.now().hour <16:
        output=lunch(city)
        print("Go eat some lunch! " + output)
        mealtype='lunch'
        notify.append(output)
    elif datetime.datetime.now().hour >=16 and datetime.datetime.now().hour <=24:
        output=dinner(alcoholnum,coffee,city)
        print("Go eat some dinner! " + output)
        mealtype='dinner'
        notify.append(output)

# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('registration.json'))
action_log=database['action log']
name=database['name']
email=database['email']

# send email to user 
one=notify[0]
two=notify[1]
three=notify[2]
options=[one,two,three]
message="Hey %s, \n\n Perhaps eat some healthy %s in %s! \n\n Here are some options: \n\n %s \n\n %s \n\n %s \n\n Remember, be well! \n\n Cheers, \n\n -The NeuroLex Team"%(name.split()[0].title(),mealtype, city, one,two, three)
sendmail([email],'NeuroLex: Eat healthy!', message, os.environ['NEUROLEX_EMAIL'], os.environ['NEUROLEX_EMAIL_PASSWORD'], [])

action={
    'action': 'nutrition.py',
    'date': get_date(),
    'meta': [message, options],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('registration.json','w')
json.dump(database,jsonfile)
jsonfile.close()
