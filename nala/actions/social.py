##############################################################################
##                         STRESSLEX - SOCIAL.PY                            ##
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

What's better than hanging out with friends to de-stress?

This action suggests some things to do in your location based on your defined 
budget in the registration process.

We believe if we got substantial growth we could build some channel partnerships
and drive people to bars and/or events throughout a city.

'''

##############################################################################
##                           IMPORT STATEMENTS                              ##
##############################################################################

import datetime, socket, requests, numpy, geocoder, json, smtplib, ftplib
import getpass, os, random, time, webbrowser, platform, json, sys 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders 

##############################################################################
##                            HELPER FUNCTIONS                              ##
##############################################################################

def nearestcity():
    
    # get current location, limit 1000 requests/day
    r=requests.get('http://ipinfo.io')
    location=r.json()
    
    return location['city'].lower()

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

def selectoption(thelist):
    thenum=random.randint(0,len(thelist)-1)
    return thelist[thenum]

def coffee(city):
    ###coffee shops in every city (x10) - get from google maps data
    ##order coffee now with a @link (referral link) 

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
        option=selectoption([one,two,three,four,five,six,seven,eight,nine,ten])
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
        option=selectoption([one,two,three,four,five,six,seven,eight,nine,ten])
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
        option=selectoption([one,two,three,four,five,six,seven,eight,nine,ten])
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
        option=selectoption([one,two,three,four,five,six,seven,eight,nine,ten])
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
        option=selectoption([one,two,three,four,five,six,seven,eight,nine,ten])
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
        option=selectoption([one,two,three,four,five,six,seven,eight,nine,ten])
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
        option=selectoption([one,two,three,four,five,six,seven,eight,nine,ten])
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
        option=selectoption([one,two,three,four,five,six,seven,eight,nine,ten])
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
        option=selectoption([one,two,three,four,five,six,seven,eight,nine,ten])
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
        option=selectoption([one,two,three,four,five,six,seven,eight,nine,ten])
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
        option=selectoption([one,two,three,four,five,six,seven,eight,nine,ten])
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
        option=selectoption([one,two,three,four,five,six,seven,eight,nine,ten])
    else:
        print("Your city currently not supported. Check back in a few months.")
    index1=option.index('stars')
    return 'Drink coffee @ ' + option[(index1+8):]

def beer(city):
###find nearest beer closest to you / recommend a bar 
##order beer now with this @link (referral link)
    if city == "boston":
        one="Row 34. This stylish brick-&-wood eatery serves an extensive oyster menu plus fish entrees & craft beers. 383 Congress St, Boston, MA 02210."
        two="Harpoon Brewry. This brewery, which offers tours, boasts a beer hall that serves pretzels, plus a gift shop. 306 Northern Ave, Boston, MA 02210."
        three="Bukowski Tavern. Hopping hangout offering a wide beer selection, comfort-food staples & a hip vibe. 50 Dalton St, Boston, MA 02115."
        four="The Urban Grape, South End. Sleek liquor store with wine tasting machines dispensing samples & a huge selection of craft brews. 303 Columbus Ave, Boston, MA 02116." 
        five="Trillium Beer Garden. Atlantic Ave & High St, Boston, MA 02110"
        six="Deep Ellum. Small, convivial gastropub with eclectic fare, a long craft beer list, classic cocktails & a patio. 477 Cambridge St, Allston, MA 02134"
        seven="Island Creek Oyster Bar. Farm-fresh raw bar, imaginative cocktails & an extensive wine & beer list in sleek surrounds. 500 Commonwealth Avenue, Boston, MA 02215"
        eight="Cheers. Faneuil Hall Marketplace, Quincy Market, Boston, MA 02109."
        nine="Saus Boston. Local spot featuring Belgian-style fries & beer, plus 15 sauces, is particularly popular late-night. 33 Union St, Boston, MA 02108"
        ten="Streetcar. Hip little wine & beer shop with a wide selection of local & craft brews. 488 Centre St, Jamaica Plain, MA 02130"
        option="Go drink some beer @ " + selectoption([one,two,three,four,five,six,seven,eight,nine,ten])
    else:
        option="Your city currently not supported. Check back in a few months."
    return option 

def gotogym(city):
##go to gym to life weights 
##database of all ymcas, LA fitness, or local workout facilities 
##start a gym membership now with @link (referral link)
    if city == "boston":
        one="Go work out @ Crossfit Fenway. 100 Brookline Ave, Boston, MA 02215"
        two="Go work out @ Planet Fitness. 17 Winter St, Boston, MA 02108"
        three="Go work out @ BRICK CrossFit. 133 Federal St, Boston, MA 02110"
        four="Go work out @ BodyScapes. 77 Avenue Louis Pasteur, Boston, MA 0211"
        five="Go work out @ Boston Sports Clubs.  800 Boylston St, Boston, MA 02199"
        six="Go work out @ Boston University Fitness and Recreation Center. 915 Commonwealth Avenue, Boston, MA 02215"
        seven="Go work out @ Beacon Hill Athletic Clubs. 261 Friend St, Boston, MA 02114"
        eight="Go work out @ 305 Fitness. 699 Boylston St, Boston, MA 02116"
        nine="Go work out @ Fisique Fitness. 50 Congress St, Boston, MA 02109"
        ten="Go work out @ Boston Sports Clubs. 100 Summer St, Boston, MA 02110"
        option=selectoption([one,two,three,four,five,six,seven,eight,nine,ten])
    else:
        option="Your city currently not supported. Check back in a few months."
    return option 

def movies(city):
###get a list of the playing movies right now in the movie theaters 
##book a movie ticket now with @link (referral link) 
    if city == "boston":
        one="Go watch a movie @ Regal Fenway Stadium 13 & RPX. 201 Brookline Ave, Boston, MA 02215"
        two="Go watch a movie @ AMC Loews Boston Common 19. 175 Tremont St, Boston, MA 02111"
        three="Go watch a movie @ Simons IMAX Theatere @ The New England Aquarium. 1 Central Wharf, Boston, MA 02110"
        four="Go watch a movie @ Mugar Omni Theater. 1 Museum Of Science Driveway, Boston, MA 02114"
        five="Go watch a movie @ the Gaiety Theatre. Washington St, Boston, MA 02111"
        option=selectoption([one,two,three,four,five])
    else:
        option="Your city currently not supported. Check back in a few months."
    return option 

def other(city):
    if city == "boston":
        one="Go see a comedy show @ the Wilbur (https://en.wikipedia.org/wiki/Wilbur_Theatre). 246 Tremont, Boston, MA 02116"
        two="Go see a concert @ Boston Symphony Orchestra: http://www.bso.org/brands/symphony-hall/tickets-events.aspx. Symphony Hall, 301 Massachusetts Ave, Boston, MA 02115"
        three="Go see some art @ the Institute of Contemporary Art in Seaport (https://en.wikipedia.org/wiki/Institute_of_Contemporary_Art,_Boston). 25 Harbor Shore Drive, Boston, MA 02210"
        four="Go on a Cruise around Boston! https://www.groupon.com/deals/boston-event-guide-68"
        option=selectoption([one,two,three,four])
    else:
        option="Your city currently not supported. Check back in a few months."
    return option 

#def dinner():
    #boston ICA 

def sports(city):
##golf, tennis, basketball, biking, etc. - do something out with friends 
##play golf at golf course now (referral link) 
##go bowling now (referral link) 
##gotogame(city)
    if city == "boston":
        one="Go golf @ William J. Devine Memorial Golf Course. 1 Circuit Dr, Dorchester, MA 02121"
        two="Go bowl @ Lucky Strike. Vintage-mod bowling spot offering 16 lanes, lounge, dancing & regular DJs, with 21+ policy at night. 145 Ipswich St, Boston, MA 02215"
        three="Play tennis on the Boston Commons. 139 Tremont St, Boston, MA 02111"
        four="Play basketball on the outdoor courts @ Back Bay Fens. 100 Park Dr, Boston, MA 02215"
        five="Play basketball on the outdoor courts @ Peters Park. 1277 Washington St, Boston, MA 02118"
        six="Play basketball on the outdoor courts @ Southwest Corridor Park. 38 New Heath St, Boston, MA 02130"
        seven="Play tennis at the Beren Tennis Center. 65 N Harvard St, Boston, MA 02134"
        eight="Go bowl @ Central Park Lanes. Veteran family-run alley featuring New England-style candlepin bowling, with shoe rentals.. 10 Saratoga St, East Boston, MA 02128"
        nine="Go mini-golfing: https://www.groupon.com/local/boston/mini-golf"
        ten="Go kayak on the Charles River! Charles River Canoe & Kayak in Allston. 1071 Soldiers Field Rd, Boston, MA 02134"
        option=selectoption([one,two,three,four,five,six,seven,eight,nine,ten])
    else:
        option="Your city currently not supported. Check back in a few months."
    return option 

def gametime(city):
##football teams in city
##basketball teams in city 
##soccer games in city with schedules
    if city == "boston":
        selectrand=random.randint(1,5)
        if month >= 9 or month < 2 and selectrand == 1: 
            option="Go see the New England Patriots play a football game. http://www.patriots.com/schedule-and-stats"
        elif month >= 10 or month <=4 and selectrand == 2:
            #October 17, 2017, with the 2017 runners-up Cleveland Cavaliers hosting a game against the Boston Celtics at Quicken Loans Arena in Cleveland, Ohio.[1] Christmas games will be played on December 25. The 2018 NBA All-Star Game will be played on February 18, 2018, at the Staples Center in Los Angeles, California. The regular season will end on April 11, 2018 
            option="Go see the Boston Celtics play a basketball game. http://www.nba.com/celtics/schedule/"
        elif month >=4 or month <= 10 and selectrand == 3: 
            #start April 2, 2017 with three games, including the 2016 World Series champions Chicago Cubs facing off against the St. Louis Cardinals, and is scheduled to end on October 1.
            option="Go see the Boston Red Sox play a baseball game. https://www.mlb.com/redsox"       
        elif month >= 10 or month <= 4 and selectrand == 4:
            #The 2017–18 NHL season is the 101st season of operation (100th season of play) of the National Hockey League. With the addition of a new expansion team, the Vegas Golden Knights, 31 teams compete in an 82-game regular season. The regular season will begin on October 4, 2017, and will end on April 7, 2018.
            option="Go see the Boston Bruins play a hockey game. http://www.ticketmaster.com/artist/805902?landing=c&c=SEM_TMNHL_ggl_616324697_30024689780_boston%20bruins&GCID=0&gclid=Cj0KCQjw6NjNBRDKARIsAFn3NMo6AVoAaryNfsD1pZmPlpLWHd9iSfWpmwBQBonkOobNgWU4rkpELUoaAgRcEALw_wcB&gclsrc=aw.ds&dclid=CMDalsfwndYCFUkGNwodj8EONg"
        elif month >= 2 or month <=10 and selectrand == 5:
            #https://www.mlssoccer.com/schedule/2017/announcement
            option="Go see the New England Revolution play a soccer game. https://www.revolutionsoccer.net/"
        elif month >= 9 or month < 2: 
            option="Go see the New England Patriots play a football game. http://www.patriots.com/schedule-and-stats"
        elif month >= 10 or month <=4:
            #October 17, 2017, with the 2017 runners-up Cleveland Cavaliers hosting a game against the Boston Celtics at Quicken Loans Arena in Cleveland, Ohio.[1] Christmas games will be played on December 25. The 2018 NBA All-Star Game will be played on February 18, 2018, at the Staples Center in Los Angeles, California. The regular season will end on April 11, 2018 
            option="Go see the Boston Celtics play a basketball game. http://www.nba.com/celtics/schedule/"
        elif month >=4 or month <= 10: 
            #start April 2, 2017 with three games, including the 2016 World Series champions Chicago Cubs facing off against the St. Louis Cardinals, and is scheduled to end on October 1.
            option="Go see the Boston Red Sox play a baseball game. https://www.mlb.com/redsox"       
        elif month >= 10 or month <= 4:
            #The 2017–18 NHL season is the 101st season of operation (100th season of play) of the National Hockey League. With the addition of a new expansion team, the Vegas Golden Knights, 31 teams compete in an 82-game regular season. The regular season will begin on October 4, 2017, and will end on April 7, 2018.
            option="Go see the Boston Bruins play a hockey game. http://www.ticketmaster.com/artist/805902?landing=c&c=SEM_TMNHL_ggl_616324697_30024689780_boston%20bruins&GCID=0&gclid=Cj0KCQjw6NjNBRDKARIsAFn3NMo6AVoAaryNfsD1pZmPlpLWHd9iSfWpmwBQBonkOobNgWU4rkpELUoaAgRcEALw_wcB&gclsrc=aw.ds&dclid=CMDalsfwndYCFUkGNwodj8EONg"
        else: 
            #https://www.mlssoccer.com/schedule/2017/announcement
            option="Go see the New England Revolution play a soccer game. https://www.revolutionsoccer.net/"
    else:
        option="Your city currently not supported. Check back in a few months."
    return option 

def shows(city):
###get a list of things coming up on TV to watch today (sports, movies, CNN, etc.)
##watch netflix episode now (referral link) 
    one="Watch Ronny Chieng: International Student on ABC iView. https://www.youtube.com/watch?v=q5HSsrjoedk"
    two="Watch Goliath on Amazon Prime. https://www.youtube.com/watch?v=uOPnIrjrDiE"
    three="Watch the Good Fight on CBS. The Good Fight season one will air on SBS, Wednesday August 2 with episodes also streaming on SBS On Demand. https://www.youtube.com/watch?v=ANNySAosDGs"
    four="Watch Legion on FX. https://www.youtube.com/watch?v=4SZ3rMMYBLY"
    five="Watch The Good Place on NBC. Many thought The Good Place wouldn’t survive but it has been given the go-ahead with a second season set to begin airing, September 28 2017. https://www.youtube.com/watch?v=RfBgT5djaQw"
    six="Watch Five Came Back on Netflix. https://www.youtube.com/watch?v=5JuiCTz6Khw"
    seven="Watch Big Little Lies on Showcase. https://www.youtube.com/watch?v=WpMa8YFcjtE"
    eight="Watch The Handmaid's Tale on SBS OnDemand. https://www.youtube.com/watch?v=PJTonrzXTJs"
    nine="Watch Amereican Gods on Amazon Prime. https://www.youtube.com/watch?v=oyoXURn9oK0"
    ten="Watch Glow on Netflix. https://www.youtube.com/watch?v=AZqDO6cTYVY"
    option=selectoption([one,two,three,four,five,six,seven,eight,nine,ten])

    return option 

def catchup(city):
###schedule a time to grab coffee using calendly API 
###takes in your location and finds the nearest coffee shop in city to get coffee with friend 
    if city == "boston":
        option=coffee(city)
    else:
        option="Your city currently not supported. Check back in a few months."
    return option 

def sendgif(city):
    #send this gif to your friends!!
    # python
    #enjoy life!!
    g = safygiphy.Giphy()
    r = g.random(tag="success")# Will return a random GIF with the tag "success"

def get_date():
    return str(datetime.datetime.now())

##############################################################################
##                            MAIN SCRIPT                                   ##
##############################################################################

#pull up webbrowser
webbrowser.open("http://actions.neurolex.co/uploads/social.m4a")
time.sleep(2)
webbrowser.open('http://actions.neurolex.co/uploads/social.png')
time.sleep(6)

#initialize 
month=datetime.datetime.now().month
# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('registration.json'))
action_log=database['action log']
name=database['name']
email=database['email']
city=database['location']['city'].lower()
if city == 'cambridge':
    city='boston'

budget=int(30)

#for demo purposes

notify=list()

for i in range(0,3):
    
    if budget>0 and budget<10:
        randomint=random.randint(1,4)
        if randomint==1:
            output=sports(city)
            print(output)
            notify.append(output)
        elif randomint==2:
            output=gotogym(city)
            print(output)
            notify.append(output)
            
        elif randomint==3:
            output=catchup(city)
            print(output)
            notify.append(output)
            
        else:
            output=shows(city)
            print(output)
            notify.append(output)
           
    elif budget>=10 and budget<=20:
        randomint=random.randint(1,4)
        if randomint==1:
            output=movies(city)
            print(output)
            notify.append(output)
        elif randomint==2:
            output=other(city)
            print(output)
            notify.append(output)
        elif randomint==3:
            output=sports(city)
            print(output)
            notify.append(output)
        elif randomint==4:
            output=beer(city)
            print(output)
            notify.append(output)
            
    elif budget>=20 and budget <=30:
        randomint=random.randint(1,8)
        if randomint==1:
            output=sports(city)
            print(output)
            notify.append(output)
        elif randomint==2:
            output=gotogym(city)
            print(output)
            notify.append(output)
        elif randomint==3:
            output=coffee(city)
            print(output)
            notify.append(output)
        elif randomint==4:
            output=shows(city)
            print(output)
            notify.append(output)
        elif randomint==5:
            output=movies(city)
            print(output)
            notify.append(output)
        elif randomint==6:
            output=other(city)
            print(output)
            notify.append(output)
        elif randomint==7:
            output=sports(city)
            print(output)
            notify.append(output)
        elif randomint==8:
            output=beer(city)
            print(output)
            notify.append(output)
            
    if budget>=40:
        randomint=random.randint(1,9)
        if randomint==1:
            output=sports(city)
            print(output)
            notify.append(output)
        elif randomint==2:
            output=gotogym(city)
            print(output)
            notify.append(output)
        elif randomint==3:
            output=coffee(city)
            print(output)
            notify.append(output)
        elif randomint==4:
            output=shows(city)
            print(output)
            notify.append(output)
        elif randomint==5:
            output=movies(city)
            print(output)
            notify.append(output)
        elif randomint==6:
            output=other(city)
            print(output)
            notify.append(output)
        elif randomint==7:
            output=sports(city)
            print(output)
            notify.append(output)
        elif randomint==8:
            output=beer(city)
            print(output)
            notify.append(output)
        elif randomint==9:
            output=gametime(city)
            print(output)
            notify.append(output)
notify=list()

for i in range(0,3):
    
    if budget>0 and budget<10:
        randomint=random.randint(1,4)
        if randomint==1:
            output=sports(city)
            print(output)
            notify.append(output)
        elif randomint==2:
            output=gotogym(city)
            print(output)
            notify.append(output)
            
        elif randomint==3:
            output=catchup(city)
            print(output)
            notify.append(output)
            
        else:
            output=shows(city)
            print(output)
            notify.append(output)
           
    elif budget>=10 and budget<=20:
        randomint=random.randint(1,4)
        if randomint==1:
            output=movies(city)
            print(output)
            notify.append(output)
        elif randomint==2:
            output=other(city)
            print(output)
            notify.append(output)
        elif randomint==3:
            output=sports(city)
            print(output)
            notify.append(output)
        elif randomint==4:
            output=beer(city)
            print(output)
            notify.append(output)
            
    elif budget>=20 and budget <=30:
        randomint=random.randint(1,8)
        if randomint==1:
            output=sports(city)
            print(output)
            notify.append(output)
        elif randomint==2:
            output=gotogym(city)
            print(output)
            notify.append(output)
        elif randomint==3:
            output=coffee(city)
            print(output)
            notify.append(output)
        elif randomint==4:
            output=shows(city)
            print(output)
            notify.append(output)
        elif randomint==5:
            output=movies(city)
            print(output)
            notify.append(output)
        elif randomint==6:
            output=other(city)
            print(output)
            notify.append(output)
        elif randomint==7:
            output=sports(city)
            print(output)
            notify.append(output)
        elif randomint==8:
            output=beer(city)
            print(output)
            notify.append(output)
            
    if budget>=40:
        randomint=random.randint(1,9)
        if randomint==1:
            output=sports(city)
            print(output)
            notify.append(output)
        elif randomint==2:
            output=gotogym(city)
            print(output)
            notify.append(output)
        elif randomint==3:
            output=coffee(city)
            print(output)
            notify.append(output)
        elif randomint==4:
            output=shows(city)
            print(output)
            notify.append(output)
        elif randomint==5:
            output=movies(city)
            print(output)
            notify.append(output)
        elif randomint==6:
            output=other(city)
            print(output)
            notify.append(output)
        elif randomint==7:
            output=sports(city)
            print(output)
            notify.append(output)
        elif randomint==8:
            output=beer(city)
            print(output)
            notify.append(output)
        elif randomint==9:
            output=gametime(city)
            print(output)
            notify.append(output)


# other data 
one=notify[0]
two=notify[1]
three=notify[2]
options=[one,two,three]
message="Hey %s, \n\n Perhaps go out with some friends to de-stress! Here are some options: \n\n %s \n\n %s \n\n %s \n\n Remember, be well! \n\n Cheers, \n\n -The NeuroLex Team"%(name.split()[0].title(),one,two,three)
sendmail([email],'NeuroLex: Go out tonight!', message, os.environ['NEUROLEX_EMAIL'], os.environ['NEUROLEX_EMAIL_PASSWORD'], [])

action={
    'action': 'social.py',
    'date': get_date(),
    'meta': [message, options],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('registration.json','w')
json.dump(database,jsonfile)
jsonfile.close()


