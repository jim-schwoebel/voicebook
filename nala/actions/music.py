##############################################################################
##                         STRESSLEX - MUSIC.PY                             ##
##############################################################################

'''
Author: @Jim Schwoebel
Role: Chief Executive Officer
Git Repo: git@github.com:NeuroLexDiagnostics/stresslex-py.git
Script: music.py
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

The music.py action module alleviates stress with music.

When we baseline users we ask them what genre they like. That is explicitly 
for this module. 

In this way you can chill out and take breaks listening to a song for 3-5 
minutes in a new way - with a music video :-).

Note: some links are deprecated. We're working on this.

'''

##############################################################################
##                           IMPORT STATEMENTS                              ##
##############################################################################

import os, datetime, pygame, socket, time, random, ftplib, numpy, sys
import geocoder, getpass, requests, webbrowser, smtplib, json
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import platform

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
        server.sendmail('neurolexlabs@gmail.com', to, msg.as_string())

        print('Done')

        server.quit()
        
    except:
        print('error')

def totalmin(hours=datetime.datetime.now().hour, minutes=datetime.datetime.now().minute):
    return minutes+hours*60

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

def speaktext(hostdir,text):
    # speak to user from a text sample (tts system)  
    curdir=os.getcwd()
    os.chdir(hostdir+'/actions') 
    os.system("python3 speak.py '%s'"%(text))
    os.chdir(curdir)

def selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty):
    thenum=random.randint(1,30)
    if thenum==1:
        option=one
    elif thenum==2:
        option=two
    elif thenum==3:
        option=three
    elif thenum==4:
        option=four
    elif thenum==5:
        option=five
    elif thenum==6:
        option=six
    elif thenum==7:
        option=seven
    elif thenum==8:
        option=eight
    elif thenum==9:
        option=nine
    elif thenum==10:
        option=ten
    elif thenum==11:
        option=eleven
    elif thenum==12:
        option=twelve
    elif thenum==13:
        option=thirteen
    elif thenum==14:
        option=fourteen
    elif thenum==15:
        option=fifteen
    elif thenum==16:
        option=sixteen
    elif thenum==17:
        option=seventeen
    elif thenum==18:
        option=eighteen
    elif thenum==19:
        option=nineteen
    elif thenum==20:
        option=twenty
    elif thenum==21:
        option=twentyone
    elif thenum==22:
        option=twentytwo
    elif thenum==23:
        option=twentythree
    elif thenum==24:
        option=twentyfour
    elif thenum==25:
        option=twentyfive
    elif thenum==26:
        option=twentysix
    elif thenum==27:
        option=twentyseven
    elif thenum==28:
        option=twentyeight
    elif thenum==29:
        option=twentynine
    elif thenum==30:
        option=thirty
    return option

def curloc():
    currentloc=getlocation()
    chicago=[41.8781,87.6298]
    #can add new cities via geocoder.google('Chicago, IL').latlng (more accurate into future)
    boston =[42.21,71.04]
    philadelphia=[39.9526,75.1652]
    newyorkcity = [40.7128,74.0059]
    houston = [29.7604,95.3698]
    dallas=[32.7767,96.7970]
    sanantonio=[29.4241,98.4936]
    austin=[30.2672,97.7431]
    atlanta = [33.7490,84.3380]
    seattle = [47.6062,122.3321]
    sanfrancisco = [37.7749,122.4194]
    losangeles = [34.0522,118.2437]
    
    cityarray=[chicago,boston,philadelphia,newyorkcity,houston,dallas,sanantonio,austin,atlanta,seattle,sanfrancisco,losangeles]
    locarray=["chicago","boston","philadelphia","new york city", "houston", "dallas", "san antonio", "austin", "atlanta", "seattle", "san francisco", "los angeles"]
    t=0
    newlist=list()
    #initialize for while loop
    while t < len(cityarray)-1:
        distance=[currentloc[0]-cityarray[t][0], currentloc[1]-cityarray[t][1]]
        newdist=(distance[0]**2+distance[1]**2)**(0.5)
        newlist.append(newdist)
        t=t+1
    
    minvalue=min(newlist)
    indexofmax=newlist.index(minvalue)
    return locarray[indexofmax]

def getmusic(musictype):
    if musictype==17:
        musictype=random.randint(1,16)
        #if random entry generate int for one of the options below (more efficient than recursion)
    if musictype==1: #alternative
        #taken from http://www.billboard.com/charts/alternative-songs
        one="'Feel it Still' by Portugal. The Man. https://www.youtube.com/watch?v=pBkHHoOIIn8"
        #tone=duration of track one in seconds 
        two="'Feels like Summer' by Wheezer. https://www.youtube.com/watch?v=efPWrIvzGgc"
        #ttwo=duration of track two in seconds 
        three="'The Man' by the Killers. https://www.youtube.com/watch?v=w3xcybdis1k"
        four="'Thunder' by Imagine Dragons. https://www.youtube.com/watch?v=fKopy74weus"
        five="'Wish I knew You' by the Rivavlists. https://www.youtube.com/watch?v=o0Pt7M0weUI"
        six="'Believer' by Imagine Dragons. https://www.youtube.com/watch?v=7wtfhZwyrcc"
        seven="'Suit and Jacket' by Judah & the Lion. https://www.youtube.com/watch?v=AigOUsOEhSY"
        eight="'High' by Sir Sly. https://www.youtube.com/watch?v=qIOaU7Sm-ZE"
        nine="'Dig Down' by Muse. https://www.youtube.com/watch?v=b4ozdiGys5g"
        ten="'Lay It On Me' by Vance Joy. https://www.youtube.com/watch?v=VXXD1Qxpisw"
        eleven="'Whole Wide World' by Cage The Elephant. https://www.youtube.com/watch?v=cYGakznEllM"
        twelve="'Everything Now' by Arcade Fire. https://www.youtube.com/watch?v=zC30BYR3CUk"
        thirteen="'Ahead of Myself' by X Ambassadors. https://www.youtube.com/watch?v=z-Jsc8TmcAU"
        fourteen="'The Way You Used To Do' by Queens of the Stnoe Age. https://www.youtube.com/watch?v=GvyNyFXHj4k"
        fifteen="'Angela' by the Lumineers. https://www.youtube.com/watch?v=_II0fc7hgNY"
        sixteen="'Walk On Water' by Thirty Seconds to Mars. https://www.youtube.com/watch?v=FA2w-PMKspo"
        seventeen="'Perfect Places' by Lorde. https://www.youtube.com/watch?v=J0DjcsK_-HY"
        eighteen="'Champion' by Fall Out Boy. https://www.youtube.com/watch?v=JJJpRl2cTJc"
        nineteen="'Vacation' by Thr Dirty Heads. https://www.youtube.com/watch?v=7zok9co_8E4"
        twenty="'Lights Out' by Royal Blood. https://www.youtube.com/watch?v=ZSznpyG9CHY"
        twentyone="'Revolution Radio' by Green Day. https://www.youtube.com/watch?v=B4zc-f0TIZ4"
        twentytwo="'Less Than' by Nine Inch Nails. https://www.youtube.com/watch?v=gDV-dOvqKzQ"
        twentythree="'So Close' by Andrew McMahon in the Wilderness. https://www.youtube.com/watch?v=e5ZUfzJoG1E"
        twentyfour="'The Violence' by Rise Against. https://www.youtube.com/watch?v=Y7bvMlfmTm4"
        twentyfive="'The Sky Is a Neighborhood' by Foo Fighters. https://www.youtube.com/watch?v=TRqiFPpw2fY"
        twentysix="'Golden Dandelions' by Barns Courtney. https://www.youtube.com/watch?v=u8ymzuwrS6M"
        twentyseven="'Its a Trip!' by Joywave. https://www.youtube.com/watch?v=0xfXcZSb8LE"
        twentyeight="'Run' by Foo Fighters. https://www.youtube.com/watch?v=ifwc5xgI3QM"
        twentynine="'Little One' by Highly Suspect. https://www.youtube.com/watch?v=eKcIedFBiVU"
        thirty="'The Wanting' by J Roddy Walston & The Business. https://www.youtube.com/watch?v=S6VhNqKaKj0"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty)
        return 'Listen to ' + option

    elif musictype==2: #classical
        #first 30 taken from https://en.wikipedia.org/wiki/The_50_Greatest_Pieces_of_Classical_Music
        one="Edvard Grieg – Peer Gynt Suite No. 1, Op. 46: Morning Mood. https://www.youtube.com/watch?v=kzTQ9fjforY"
        two="Ludwig van Beethoven – Symphony No. 5 In C Minor, Op. 67, Fate: I. Allegro Con Brio. https://www.youtube.com/watch?v=tV6CpVfU7ig"
        three="Antonio Vivaldi – The Four Seasons, Op. 8, Spring: Allegro. https://www.youtube.com/watch?v=ygpf6mxTUeY"
        four="Samuel Barber – Adagio for Strings. https://www.youtube.com/watch?v=izQsgE0L450"
        five="Richard Wagner – The Valkyrie: Ride of the Valkyries. https://www.youtube.com/watch?v=GGU1P6lBW6Q"
        six="Frédéric Chopin – Nocturne No. 2 In E-Flat Major, Op. 9. https://www.youtube.com/watch?v=9E6b3swbnWg"
        seven="Johann Pachelbel – Canon in D major. https://www.youtube.com/watch?v=NlprozGcs80"
        eight="Carl Orff – Carmina Burana: O Fortuna. https://www.youtube.com/watch?v=GXFSK0ogeg4"
        nine="Johann Sebastian Bach – Orchestral Suite No. 3 in D major, BWV 1068: Air. https://www.youtube.com/watch?v=GkWjO8ZJcpc"
        ten="Gustav Holst – The Planets, Op. 32: Jupiter, the Bringer of Jollity. https://www.youtube.com/watch?v=Nz0b4STz1lo"
        eleven="Claude Debussy – Suite bergamasque, L 75: Clair de Lune. https://www.youtube.com/watch?v=vG-vmVrHOGE"
        twelve="Giuseppe Verdi – Nabucco: Chorus of the Hebrew Slaves (Va', Pensiero, Sull'ali Dorate). https://www.youtube.com/watch?v=-DIcS5-8RD8"
        thirteen="Wolfgang Amadeus Mozart – Piano Concerto No. 21 in C major, K. 467: II. Andante. https://www.youtube.com/watch?v=LA_BYwlzDVQ"
        fourteen="Johann Sebastian Bach – Brandenburg Concerto No. 3 in G major, BWV 1048: Allegro. https://www.youtube.com/watch?v=Xq2WTXtKurk"
        fifteen="Jules Massenet – Thaïs: Meditation. https://www.youtube.com/watch?v=luL1T1WQC2k"
        sixteen="Antonín Dvořák – Symphony No. 9 In E Minor, Op. 95, From the New World: II. Largo. https://www.youtube.com/watch?v=Aa-aD0SdxTY"
        seventeen="Johann Strauss II – On the Beautiful Blue Danube, Op. 314. https://www.youtube.com/watch?v=EHt2tW_nvp8"
        eighteen="Johannes Brahms – Hungarian Dance No. 5 In G Minor. https://www.youtube.com/watch?v=3X9LvC9WkkQ"
        nineteen="Pyotr Ilyich Tchaikovsky – Swan Lake Suite, Op. 20: Scene. https://www.youtube.com/watch?v=wEgOM9iYETg"
        twenty="Erik Satie – Gymnopédie No. 1. https://www.youtube.com/watch?v=S-Xm7s9eGxU"
        twentyone="Wolfgang Amadeus Mozart – Requiem, K. 626: Lacrimosa Dies Illa. https://www.youtube.com/watch?v=5IFtGSaFzbM"
        twentytwo="Ludwig van Beethoven – Bagatelle In A Minor, WoO 59, Für Elise. https://www.youtube.com/watch?v=NShTqdkCrXQ"
        twentythree="Edward Elgar – Pomp and Circumstance, Op. 39: Land of Hope and Glory. https://www.youtube.com/watch?v=0bknTe9nM8A"
        twentyfour="Georges Bizet – Carmen Suite No. 2: Habanera. https://www.youtube.com/watch?v=EcFJTc28soQ"
        twentyfive="Ludwig van Beethoven – Symphony No. 9 In D Minor, Op. 125, Choral: Ode an Die Freude"
        twentysix="Jacques Offenbach – The Tales of Hoffmann: Barcarolle. https://www.youtube.com/watch?v=g7czptgEvvU"
        twentyseven="Remo Giazotto – Adagio In G Minor for Strings and Organ (after T. Albinoni). https://www.youtube.com/watch?v=fzOLoIu4Gw8"
        twentyeight="Wolfgang Amadeus Mozart – Serenade No. 13 In G Major, K. 525, Eine Kleine Nachtmusik: I. Allegro. https://www.youtube.com/watch?v=z4Hfv00eqoI"
        twentynine="Gioachino Rossini – The Barber of Seville: Overture. https://www.youtube.com/watch?v=OloXRhesab0"
        thirty="W. A. Mozart - Die Zauberflöte (The Magic Flute), K. 620 - Overture. https://www.youtube.com/watch?v=_kgcu8yhojc"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty)
        return 'Listen to ' + option
    elif musictype==3: #country 
        #taken from http://www.billboard.com/charts/country-songs
        one="'Body Like A Back Road' by Sam Hunt. https://www.youtube.com/watch?v=Mdh2p03cRfw"
        two="'Small Town Boy' by Dustin Lynch. https://www.youtube.com/watch?v=pz9yRC-LWhU"
        three="'What Ifs' by Kane Brown. https://www.youtube.com/watch?v=fM8V1XOI-14"
        four="'No Such Thing As A Broken Heart' by Old Dominion. https://www.youtube.com/watch?v=MZdpppFRLqw"
        five="'In Case You Didnt Know' by Brett Young. https://www.youtube.com/watch?v=7qaHdHpSjX8"
        six="'When It Rains It Pours' by Luke Combs. https://www.youtube.com/watch?v=uXyxFMbqKYA"
        seven="'Heartache On the Dance Floor' by Jon Pardi. https://www.youtube.com/watch?v=Cg4Eui4sGlk"
        eight="'Unforgettable' by Thomas Rhett. https://www.youtube.com/watch?v=84hwjCnAVjU"
        nine="'Drinkin' Problem' by Midland. https://www.youtube.com/watch?v=g7f6HiQ2LuU"
        ten="'All The Pretty Girls' by Kenny Chesney. https://www.youtube.com/watch?v=embINtOC_i0"
        eleven="'Light It Up' by Lukey Bryan. https://www.youtube.com/watch?v=8wpUv4I_fQk"
        twelve="'Craving You' by Thomas Rhett. https://www.youtube.com/watch?v=zruDce8zbEo"
        thirteen="'They Don't Know' by Jason Aldean. https://www.youtube.com/watch?v=SQZPIsGoR1M"
        fourteen="'Every Little Thing' by Carly Pearce. https://www.youtube.com/watch?v=pm6DHCpmIWg"
        fifteen="'More Girls Like You' by Kip Moore. https://www.youtube.com/watch?v=6-UHrVz1pR8"
        sixteen="'It Ain't my Fault' by Brothers Osborne. https://www.youtube.com/watch?v=MyOGVk_ypnM"
        seventeen="'For Her' by Chris Lane. https://www.youtube.com/watch?v=tyFY2I2Qlyk"
        eighteen="'Greatest Love Story' by LANCO. https://www.youtube.com/watch?v=aHl0tlUYDBI"
        nineteen="'I Could Use A Love Song' by Maren Morris. https://www.youtube.com/watch?v=ErdZ_W35xRs"
        twenty="'Fix A Drink' by Chris Janson. https://www.youtube.com/watch?v=-_Op0bQfMoo"
        twentyone="'Round Here Buzz' by Eric Church. https://www.youtube.com/watch?v=Z3Zj2RgNyj0"
        twentytwo="'Ring on Every Finger' by LOCASH. https://www.youtube.com/watch?v=LMDDdj_M0js"
        twentythree="'Ask Me How I Know' by Garth Brooks. https://www.youtube.com/watch?v=Dsxiw-d9Qmg"
        twentyfour="'Losing Sleep' by Chris Young. https://www.youtube.com/watch?v=NShYb80xnjw"
        twentyfive="'You Broke Up With Me' by Walker Hayes. https://www.youtube.com/watch?v=z6jfEH7D5bg"
        twentysix="'Yours' by Russell Dickerson. https://www.youtube.com/watch?v=gFccdvKehQI"
        twentyseven="'Smooth' by Florida Georgia Line. https://www.youtube.com/watch?v=QZD5TCFpNXg"
        twentyeight="'Last Time For Everything' by Brad Paisley. https://www.youtube.com/watch?v=LWkoquUvD98"
        twentynine="'Like I Loved You' by Brett Young. https://www.youtube.com/watch?v=PG2azZM4w4o"
        thirty="'All On Me' by Devin Dawson. https://www.youtube.com/watch?v=ntCMoh-0ogo"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty)
        return 'Listen to ' + option
    elif musictype==4: #edm
        #taken from http://www.billboard.com/charts/dance-electronic-songs
        one="'Feels' by Calvin Harris. https://www.youtube.com/watch?v=ozv4q2ov3Mk"
        two="'Something Just Like This' by the Chainsmokers & Coldplay. https://www.youtube.com/watch?v=FM7MFYoylVs"
        three="'Stay' by Zedd & Alessia Cara. https://www.youtube.com/watch?v=h--P8HzYZ74"
        four="'No Promises' by Cheat Codes. https://www.youtube.com/watch?v=jn40gqhxoSY"
        five="'It Ain't Me' by Kygo x Selena Gomez. https://www.youtube.com/watch?v=D5drYkLiLI8"
        six="'Swish Swish' by Katy Perry Featuring Nicki Minaj. https://www.youtube.com/watch?v=iGk5fR-t5AU"
        seven="'Silence' by Marshmello, featuring Khalid. https://www.youtube.com/watch?v=tk36ovCMsU8"
        eight="'Rockabye' by Clean Bandit featuring Sean Paul & Anne-Marie. https://www.youtube.com/watch?v=papuvlVeZg8"
        nine="'2U' by David Guetta featuring Justin Bieber. https://www.youtube.com/watch?v=RqcjBLMaWCg"
        ten="'Slide' by Calvin Harris. https://www.youtube.com/watch?v=8Ee4QjCEHHc"
        eleven="'Mama' by Jonas Blue. https://www.youtube.com/watch?v=qPTfXwPf_HM"
        twelve="'Know No Better' by Major Lazer. https://www.youtube.com/watch?v=Sgp0WDMH88g"
        thirteen="'Honest' by the Chainsmokers. https://www.youtube.com/watch?v=Lsv5IeI8bA8"
        fourteen="'Get Low' by Zedd & Liam Payne. https://www.youtube.com/watch?v=cSX0-MP6tjw"
        fifteen="'Rollin' by Calvin Harris. https://www.youtube.com/watch?v=5f_JiibvQAM"
        sixteen="'Symphony' by Clean Bandit. https://www.youtube.com/watch?v=aatr_2MstrI" 
        seventeen="'Would You Ever' by Skrillex. https://www.youtube.com/watch?v=r-SurvChGFk"
        eighteen="'More Than You Know' by Axwell & Ingrosso. https://www.youtube.com/watch?v=GsF05B8TFWg"
        nineteen="'Lonely Together' by Avicii. https://www.youtube.com/watch?v=ruDrVMBCLaw"
        twenty="'Without You' by Avicii. https://www.youtube.com/watch?v=jUe8uoKdHao"
        twentyone="'Rich Love' by OneRepublic. https://www.youtube.com/watch?v=sJ6hAQjW9Aw"
        twentytwo="'Instruction' by Jax Jones. https://www.youtube.com/watch?v=MQXLpSl26q4"
        twentythree="'There For You' by Martin Garrix x Troye Sivan. https://www.youtube.com/watch?v=pNNMr5glICM"
        twentyfour="'All My Love' by Cash Cash. https://www.youtube.com/watch?v=HYrvDBgKAPo"
        twentyfive="'First Time' by Kygo & Ellie Goulding. https://www.youtube.com/watch?v=OlH1RCs96JA"
        twentysix="'OK' by Robin Schultz. https://www.youtube.com/watch?v=P9-4xHVc7uk"
        twentyseven="'Moving On' by Marshmello. https://www.youtube.com/watch?v=yU0tnrEk8H4"
        twentyeight="'Tired' by Alan Walker. https://www.youtube.com/watch?v=g4hGRvs6HHU"
        twentynine="'Find Me' by Marshmello. https://www.youtube.com/watch?v=ymq1WdGUcw8" 
        thirty="'Pizza' by Martin Garrix. https://www.youtube.com/watch?v=JsKIAO11q1Y"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty)
        return 'Listen to ' + option
    elif musictype==5: #jazz
        #taken from http://www.billboard.com/charts/jazz-songs
        one="'Caminando' by David Benoit and Marc Antoine. https://www.youtube.com/watch?v=zo_RELAS7V0"
        two="'Frankie B' by Gerald Albright. https://www.youtube.com/watch?v=3GemcfAYuvw"
        three="'Girl Talk' by Cindy Bradley. https://www.youtube.com/watch?v=oHrm8dvPDWs" 
        four="'Next To Me' by Lindsey Webster. https://www.youtube.com/watch?v=-zdMwQ2cWnY"
        five="'Let's Take A Ride' by Brian Culbertson. https://www.youtube.com/watch?v=dTmsemPB9TY"
        six="'Between You and I' by Riley Richard. https://www.youtube.com/watch?v=OBHHy2LJFZc"
        seven="'Uncle Nick' by Nick Colionne. https://www.youtube.com/watch?v=_ozECYHNaJk"
        eight="'Piccadilly Circus' by Paul Brown. https://www.youtube.com/watch?v=zJosV9Bw3DE"
        nine="'Trininty' by Jackiem Joyner. https://www.youtube.com/watch?v=EHG_43UczAo" 
        ten="'Let It Go' by Jonathan Fritzen. https://www.youtube.com/watch?v=FJ9x-CZGq1k"
        eleven="'Down The Road' by Paul Jackson, Jr. https://www.youtube.com/watch?v=MnlFINIQpJI"
        twelve="'Vivid' by Blake Aron. https://www.youtube.com/watch?v=qgBJI8KEeC8"
        thirteen="'Happy Hour' by Chuck Loeb. https://www.youtube.com/watch?v=Zom2UbDm52Q"
        fourteen="'I Don't Mind' by Adam Hawley. https://www.youtube.com/watch?v=P4MlGsVh24c"
        fifteen="'Tick Tock' by Boney James. https://www.youtube.com/watch?v=UnC8bkwPo2w"
        sixteen="'Deixa' by Marc Antoine. https://www.youtube.com/watch?v=via8CmbNA8Q"
        seventeen="'Here to Stay' by Darryl Williams. https://www.youtube.com/watch?v=ejRX6KaG2e4"
        eighteen="'Now What' by Walter Beasley. https://www.youtube.com/watch?v=JyOBHB8NQTc"
        nineteen="'Road Trip' by Andre Cavor. https://www.youtube.com/watch?v=eU_-xKtutdI"
        twenty="'Going Out' by Julian Vaughn. https://www.youtube.com/watch?v=dBaIaZy1-I4"
        twentyone="'Baby Coffee' by Michael J. Thomas. https://www.youtube.com/watch?v=cM4Q0v01wQU"
        twentytwo="'Early Arrival' by Ragan Whiteside. https://www.youtube.com/watch?v=GSqHRblW9UI"
        twentythree="'Carmanology' by the Allen Carman Project. https://www.youtube.com/watch?v=3BVDhAN41DE"
        twentyfour="'Where I Left Off' by Oli Silk. https://www.youtube.com/watch?v=eC6ikAWRq9E"
        twentyfive="'Let's Take It Back' by Najee. https://www.youtube.com/watch?v=N_UqrRjs9r0"
        twentysix="'Lay Lady Lay' by Jack DeJohnette, Larry Grenadier, John Medeski, & John Scofield. https://www.youtube.com/watch?v=BjZC9G4p4Hw"
        twentyseven="'The Edge of Twilight' by Keiko Matsui. https://www.youtube.com/watch?v=csg-7f539CI&list=PL6-ukl_LI7_TM1msq2UW9XpbHYsyMImeq&index=15"
        twentyeight="'Water Lily' by Keiko Matsui. https://www.youtube.com/watch?v=g2ia7ogeEwE&list=PL6-ukl_LI7_TM1msq2UW9XpbHYsyMImeq&index=22"
        twentynine="'Angel of the South' by Acoustic Alchemy. https://www.youtube.com/watch?v=qKgRrqgAvho&index=2&list=PLvBIYgM9CkyQqvJJqVKRJdbu_w5VG6dS4"
        thirty="'Passion Play' by Acoustic Alchemy. https://www.youtube.com/watch?v=vkXpS8oBt2A&index=16&list=PLvBIYgM9CkyQqvJJqVKRJdbu_w5VG6dS4"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty)
        return 'Listen to ' + option
    elif musictype==6: #rap
        #taken from http://www.billboard.com/charts/rap-song and http://www.billboard.com/charts/r-b-hip-hop-songs
        one="'Bodak Yellow (Money Moves)' by Cardi B. https://www.youtube.com/watch?v=PEGccV-NOm8"
        two="'Unforgettable' by French Montana. https://www.youtube.com/watch?v=CTFtOOh47oo"
        three="'1-800-273-8255' by Logic. https://www.youtube.com/watch?v=Kb24RrHIbFk"
        four="'Bank Account' by 21 Savage. https://www.youtube.com/watch?v=eCK772REqw0"
        five="'Rake It Up' by Yo. https://www.youtube.com/watch?v=OrSadmwmmAs"
        six="'Humble' by Kendrick Lamar. https://www.youtube.com/watch?v=tvTRZJ-4EyI"
        seven="'XO Tour Llif3' by Lil Uzi Vert. https://www.youtube.com/watch?v=WrsFXgQk5UI"
        eight="'Congratulations' by Post Malone. https://www.youtube.com/watch?v=SC4xMk98Pdc"
        nine="'I'm The One' by DJ Khaled. https://www.youtube.com/watch?v=weeI1G46q0o"
        ten="'Jocelyn Flores' by XXXTENTACION. https://www.youtube.com/watch?v=C1D3G2VGQ_8"
        eleven="'Loyalty' by Kendrick Lamar. https://www.youtube.com/watch?v=Dlh-dzB2U4Y"
        twelve="'The Way Life Goes' by Lil Uzi Vert. https://www.youtube.com/watch?v=oKu2FVy0oUo"
        thirteen="'I Get The Bag' by Gucci Mane. https://www.youtube.com/watch?v=uo14xGYwWd4"
        fourteen="'It's A Vibe' by 2 Chainz. https://www.youtube.com/watch?v=tU3p6mz-uxU"
        fifteen="'Sauce It Up' by Lil Uzi Vert. https://www.youtube.com/watch?v=BnRNXWAGENE"
        sixteen="'Crew' by Goldlink. https://www.youtube.com/watch?v=nhNqbe6QENY"
        seventeen="'Everyday We Lit' by YFN Lucci. https://www.youtube.com/watch?v=44Vk5KyQbiA"
        eighteen="'Drowning' by A Boogie Wit da Hoodie. https://www.youtube.com/watch?v=rvaJ7QlhH0g"
        nineteen="'Magnolia' by Playboi Carti. https://www.youtube.com/watch?v=oCveByMXd_0"
        twenty="'Everybody Dies in Their Nightmares' by XXXTENTACION. https://www.youtube.com/watch?v=Tg6HGcj7pGo"
        twentyone="'Transportin' by Kodk Black. https://www.youtube.com/watch?v=Ns167_llTiA"
        twentytwo="'Butterfly Effect' by Travis Scott. https://www.youtube.com/watch?v=_EyZUTDAH0U"
        twentythree="'444+222' by Lil Uzi Vert. https://www.youtube.com/watch?v=9qfUYeMfl2Q"
        twentyfour="'Roll In Peace' by Kodak Black. https://www.youtube.com/watch?v=hwCLVBCNIt0"
        twentyfive="'DNA' by Kendrick Lamar. https://www.youtube.com/watch?v=NLZRYQMLDW4"
        twentysix="'Versace On The Floor' by Bruno Mars. https://www.youtube.com/watch?v=-FyjEnoIgTM"
        twentyseven="'Revenge' by XXXTENTACION. https://www.youtube.com/watch?v=3CJsqGa1ltM"
        twentyeight="'B.E.D. by Jacquees. https://www.youtube.com/watch?v=ul1H_p_FeaA"
        twentynine="'For Real' by Lil Uzi Vert. https://www.youtube.com/watch?v=xnnfQ0inQp8"
        thirty="'Questions' by Chris Brown. https://www.youtube.com/watch?v=mH76VvWkNwA"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty)
        return 'Listen to ' + option
    elif musictype==7: #holiday
        #taken from http://www.billboard.com/charts/hot-holiday-songs
        one="'All I Want For Christmas Is You' by Mariah Carey. https://www.youtube.com/watch?v=yXQViqx6GMY"
        two="'Hallelujah' by Pentatonix. https://www.youtube.com/watch?v=LRP8d7hhpoQ"
        three="'Rockin' Around the Christmas Tree.' by Brenda Lee. https://www.youtube.com/watch?v=_6xNuUEnh2g"
        four="'Jingle Bell Rock' by Bobby Helms. https://www.youtube.com/watch?v=itcMLwMEeMQ"
        five="'Feliz Navidad' by Jose Feliciano. https://www.youtube.com/watch?v=xMtuVP8Mj4o"
        six="'Mary, Did You Know?' by Pentatonix. https://www.youtube.com/watch?v=ifCWN5pJGIE"
        seven="'A Holly Jolly Christmas' by Burl Ives. https://www.youtube.com/watch?v=nVMCUtsmWmQ"
        eight="'The Christmas Song' by Nat King Cole. https://www.youtube.com/watch?v=hwacxSnc4tI"
        nine="'It's the Most Wonderful Time Of The Year' by Andy Williams. https://www.youtube.com/watch?v=gFtb3EtjEic"
        ten="'Last Christmas' by Wham! https://www.youtube.com/watch?v=4hhew1QKi-U"
        eleven="'Rudolph The Red-Nosed Reindeer' by Gene Autry. https://www.youtube.com/watch?v=7ara3-hDH6I"
        twelve="'White Christmas' by Bing Crosby. https://www.youtube.com/watch?v=GJSUT8Inl14"
        thirteen="'Christmas Eve' by Trans-Siberian Orchestra. https://www.youtube.com/watch?v=xJ_OnN5F4Yw"
        fourteen="'You're One Mean One', Mr. Grinch' https://www.youtube.com/watch?v=WxVqliZCNw0"
        fifteen="'Let It Snow, Let It Snow, Let It Snow' by Dean Martin. https://www.youtube.com/watch?v=mN7LW0Y00kE"
        sixteen="'Blue Chrismas' by Elvis Presley. https://www.youtube.com/watch?v=Uwfz5mMLSDM"
        seventeen="'Christmas Time Is Here' by Vince Guaraldi Trio. https://www.youtube.com/watch?v=YvI_FNrczzQ"
        eighteen="'It's Beginning To Look A Lot Like Christmas' by Michael Buble. https://www.youtube.com/watch?v=EyKMPXqKlFk"
        nineteen="'Wonderful Christmastime' by Paul McCartney. https://www.youtube.com/watch?v=V9BZDpni56Y"
        twenty="'Sleigh Ride' by Ronettes. https://www.youtube.com/watch?v=Y6rDA2Czz0E"
        twentyone="'Happy Xmas' by John Lennon & Yoko Ono. https://www.youtube.com/watch?v=z8Vfp48laS8" 
        twentytwo="'Christmas Soon' by the Trans-Siberian Orhcestra. https://www.youtube.com/watch?v=4cP26ndrmtg"
        twentythree="'Santa Tell Me' by Ariana Grande. https://www.youtube.com/watch?v=nlR0MkrRklg"
        twentyfour="'Mistletoe' by Justin Bieber. https://www.youtube.com/watch?v=LUjn3RpkcKY"
        twentyfive="'Have Yourself A Merry Little Christmas' by Frank Sinatra. https://www.youtube.com/watch?v=nZ6yQgBvuoI"
        twentysix="'Merry Christmas Darling' by Carpenters. https://www.youtube.com/watch?v=YR1ujXx2p-I"
        twentyseven="'Linus & Lucy' and Vince Guaraldi Trio. https://www.youtube.com/watch?v=x6zypc_LhnM"
        twentyeight="'St. Brick Intro' by Guci Mane. https://www.youtube.com/watch?v=ywaX-veaB40"
        twentynine="'I Want A Hippopotamus For Christmas' by Gayla Peevey. https://www.youtube.com/watch?v=7oOzszFIBcE"
        thirty="'Little Saint Nick' by the Beach Boys. https://www.youtube.com/watch?v=aSynDh_K0EE" 
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty)
        return 'Listen to ' + option
    elif musictype==8: #indie
        #taken from top 100 indie songs on spotify
        one="'Feel It Still' by Portugal. The Man. https://www.youtube.com/watch?v=pBkHHoOIIn8"
        two="'Do I Wanna Know' by Artic Monkeys. https://www.youtube.com/watch?v=bpOSxM0rNPM"
        three="'Beezeblocks' by atl-J. https://www.youtube.com/watch?v=rVeMiVU77wo"
        four="'Sweater Weather' by The Neighbourhood. https://www.youtube.com/watch?v=GCdwKhTtNNw"
        five="'Take a Walk' by Passion Pit. https://www.youtube.com/watch?v=dZX6Q-Bj_xg"
        six="'Chocolate' by The 1975. https://www.youtube.com/watch?v=CHk5SWVO4p8"
        seven="'Angels' by The xx. https://www.youtube.com/watch?v=_nW5AF0m9Zw"
        eight="'My Number' by Foals. https://www.youtube.com/watch?v=bAsGFnLl2u0"
        nine="'Entertainment' by Phoenix. https://www.youtube.com/watch?v=qaMyr36uIv8"
        ten="'Falling' by HAIM. https://www.youtube.com/watch?v=AIjVpRAXK18"
        eleven="'Sun' by Two Door Cinema Club. https://www.youtube.com/watch?v=sKyK1Mme9Sc"
        twelve="'Feels Like We Only Go Backwards' by Tame Impala."
        thirteen="'Recovery' by Frank Turner. https://www.youtube.com/watch?v=F1L5zJ2afLs"
        fourteen="'Don't Save Me' by HAIM. https://www.youtube.com/watch?v=kiqIush2nTA"
        fifteen="'Global Concepts' by Robert DeLong. https://www.youtube.com/watch?v=JND-sxlg7YU"
        sixteen="'Miracle Mile' by Cold War Kids. https://www.youtube.com/watch?v=1F6gAN6MOII"
        seventeen="'Song For Zula' by Phosphorescent. https://www.youtube.com/watch?v=ZPxQYhGpdvg"
        eighteen="'Tessellate' by alt-J. https://www.youtube.com/watch?v=Qg6BwvDcANg"
        nineteen="'Oblivion' by M83. https://www.youtube.com/watch?v=822P87a773c" 
        twenty="'Tap Out' by The Strokes. https://www.youtube.com/watch?v=-7PINAYE4z4"
        twentyone="'Matilda' by alt-J. https://www.youtube.com/watch?v=Q06wFUi5OM8"
        twentytwo="'Carried Away' by Passion Pit. https://www.youtube.com/watch?v=Evz03lIJ3f0"
        twentythree="'Heavy Feet' by Local Natives. https://www.youtube.com/watch?v=h2zWfxW60z0"
        twentyfour="'Trying To Be Cool' by Phoenix. https://www.youtube.com/watch?v=OePvsCfKHJg"
        twentyfive="'Trembling Hands' by The Temper Trap. https://www.youtube.com/watch?v=iW0uYfq3VLU"
        twentysix="'Kemosabe' by Everything Everything. https://www.youtube.com/watch?v=TKKMfJ8cZoQ"
        twentyseven="'The Way I Tend To Be' by Frank Turner. https://www.youtube.com/watch?v=Cf5O2M5GaEA"
        twentyeight="'Sunset' by The xx. https://www.youtube.com/watch?v=M2JrAhmZmpM"
        twentynine="'The Bay' by Metronomy. https://www.youtube.com/watch?v=9PnOG67flRA"
        thirty="'Time To Run' by Lord Huron. https://www.youtube.com/watch?v=5_e8RRTT0r8"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty)
        return 'Listen to ' + option
    elif musictype==9: #christian
        #toby mac 
        one="'Real Love' by Blanca. https://www.youtube.com/watch?v=AKG_3u_kdJ8"
        two="'Old Church Choir' by Zach Williams. https://www.youtube.com/watch?v=yOEviTLJOqo"
        three="'O Come to the Altar' by Elevation Worship. https://www.youtube.com/watch?v=ycWDFd0yCHA"
        four="'Love Broke Thru' by Toby Mac. https://www.youtube.com/watch?v=44l9PRI4c2M"
        five="'Full of Faith' by Cody Carnes. https://www.youtube.com/watch?v=IPPGvudBaiM"
        six="'Gracefully Broken' by Matt Redman. https://www.youtube.com/watch?v=__haUJns_b8"
        seven="'I'll Find You' by Lecrae. https://www.youtube.com/watch?v=Jv8IqJm6q7w"
        eight="'So Will I (100 Billion X)' Hillsong United. https://www.youtube.com/watch?v=EuYOnYL6G0Y"
        nine="'Broken Things' by Matthew West. https://www.youtube.com/watch?v=WdUu6ZsdVfM&list=RDWdUu6ZsdVfM"
        ten="'The Gospel' by Ryan Stevenson. https://www.youtube.com/watch?v=NTdFEZhjiko"
        eleven="'Hard Love' by NEEDTOBREATHE. https://www.youtube.com/watch?v=tE3Fp8C_ufg"
        twelve="'Hills and Valleys' by Tauren Wells. https://www.youtube.com/watch?v=p4rRCjrAyCs"
        thirteen="'Bleed the Same' by Mandisa. https://www.youtube.com/watch?v=UEzCQBwQkdA"
        fourteen="'The Answer' by Jeremy Camp. https://www.youtube.com/watch?v=rQHXJi1EhDM"
        fifteen="'A Million Lights' by Michael W. Smith. https://www.youtube.com/watch?v=DaTcRrINSXo"
        sixteen="'Death Was Arrested' by North Point InsideOut. https://www.youtube.com/watch?v=uMsMiluCUUI"
        seventeen="'Hold You Down' by Deraj. https://www.youtube.com/watch?v=ZXgiea7hW90"
        eighteen="'What A Beautiful Name' by Hillsong Worship. https://www.youtube.com/watch?v=nQWFzMvCfLE"
        nineteen="'Jesus & You' by Matthew West. https://www.youtube.com/watch?v=kJhVA8YW5yY"
        twenty="'Details' by Sarah Reeves. https://www.youtube.com/watch?v=gTICoQC8PRw"
        twentyone="'Bulletproof' by Citizen Way. https://www.youtube.com/watch?v=RzqpK7ZaH6o"
        twentytwo="'Rescuer (Good News)' by Rend Collective. https://www.youtube.com/watch?v=sAg7rn7fH3Q"
        twentythree="'You Belong' by Jasmine Murray. https://www.youtube.com/watch?v=4-GIcCOHoMw"
        twentyfour="'Even If' by MercyMe. https://www.youtube.com/watch?v=B6fA35Ved-Y"
        twentyfive="'Build My Life' by Christy Nockels. https://www.youtube.com/watch?v=QJCxe0cd15A"
        twentysix="'Mountain - Radio Version' by Bryan & Katie Torwalt. https://www.youtube.com/watch?v=IUAOF5LLXDc"
        twentyseven="'Control (Somehow You Want Me)' by Tenth Avenue North. https://www.youtube.com/watch?v=kFfztu8-bBQ"
        twentyeight="'Different' by Micah Tyler. https://www.youtube.com/watch?v=3MtfLap4qcc"
        twentynine="'I know' by Kim Walker Smith. https://www.youtube.com/watch?v=mAq-74wRSFQ"
        thirty="'Home' by Chris Tomlin. https://www.youtube.com/watch?v=BCiBQqfHSvQ"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty)
        return 'Listen to ' + option
    elif musictype==10: #latin
        one="'Bella y Sensual' by Romeo Santos. https://www.youtube.com/watch?v=ybzDgGCL1Xk"
        two="'Felices los 4' by Maluma. https://www.youtube.com/watch?v=n6WUcjyagN8"
        three="'Mayores' by Becky G'Krippy Kush' by Farruko. https://www.youtube.com/watch?v=GMFewiplIbw"
        four="'Krippy Kush' by Farruko. https://www.youtube.com/watch?v=j1_JW7An2l0"
        five="'Se Preparo' by Ozuna. https://www.youtube.com/watch?v=KWGrPNqz4uc"
        six="'Escapate Conmigo' by Wisin. https://www.youtube.com/watch?v=3X9wEwulYhk"
        seven="Una Lady Como Tu' by Mnaual Turizo. https://www.youtube.com/watch?v=T3pstB1gWyo" 
        eight="'Robarte un Beso' by Carlos Vives. https://www.youtube.com/watch?v=Mtau4v6foHA"
        nine="'Mi Gente' by J. Balvin. https://www.youtube.com/watch?v=wnJ6LuUFpMo"
        ten="'Explicale' by Yandel. https://www.youtube.com/watch?v=U516oP9nt2o"
        eleven="'Ni Tu Ni Yo' by Jennifer Lopez. https://www.youtube.com/watch?v=V5_tnpdnNz4"
        twelve="Hey DJ' by CNCO. https://www.youtube.com/watch?v=X6wQOW9ihDA"
        thirteen="Doble Personalidad' by Noriel. https://www.youtube.com/watch?v=1qpKJJgBXmw"
        fourteen="'Perro Fiel' by Shakira. https://www.youtube.com/watch?v=o5U5ivOnJjs"
        fifteen="'Ganas Locas' by Prince Royce. https://www.youtube.com/watch?v=Ztf7QEetikY"
        sixteen="Imitadora' by Romeo Santos. https://www.youtube.com/watch?v=mhHqonzsuoA"
        seventeen="'Si Tu La Ves' by Nicky Jam. https://www.youtube.com/watch?v=mcGBVy3-W4s"
        eighteen="'Internacionales' by Bomba Estereo. https://www.youtube.com/watch?v=tWwWoDFoubw"
        nineteen="'Loco Enamorado' by Abrham Mateo. https://www.youtube.com/watch?v=cmIKUyUrKl4"
        twenty="'Unforgettable' by French Montana. https://www.youtube.com/watch?v=CTFtOOh47oo"
        twentyone="'Sastre de Tu Amor' by Orishas. https://www.youtube.com/watch?v=n_CLTHgFF4c"
        twentytwo="'Me Rehuso' by Danny Ocean. https://www.youtube.com/watch?v=aDCcLQto5BM"
        twentythree="'Hey Guapo' by Play-N-Skillz. https://www.youtube.com/watch?v=Vzs9JgtW_lI"
        twentyfour="'No Le Hablen de Amor' by CD9. https://www.youtube.com/watch?v=_ixn-FRppEk"
        twentyfive="'Criminal' by Natti Natasha. https://www.youtube.com/watch?v=VqEbCxg2bNI"
        twentysix="'Muevete' by MIX5. https://www.youtube.com/watch?v=KfaU_RY14HQ"
        twentyseven="'Que Me Has Hecho' by Chayanne. https://www.youtube.com/watch?v=q_OGqmx3DNQ"
        twentyeight="'Just As I am' by Spiff TV. https://www.youtube.com/watch?v=i1dVohtr4Uk"
        twentynine="'SUBEME LA RADIO' by Enrique Iglesias. https://www.youtube.com/watch?v=9sg-A-eS6Ig"
        thirty="'El Amante' by Nicky Jam. https://www.youtube.com/watch?v=YG2p6XBuSKA"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty)
        return 'Listen to ' + option
    elif musictype==11: #newage
        #phillip wesley 
        #ludivico einvaldi 
        one="'River Flows In You' by Yuruma. https://www.youtube.com/watch?v=XsTjI75uEUQ"
        two="'Comptine d'un autre ete, l'apres-midi' by Yann Tierson. https://www.youtube.com/watch?v=NvryolGa19A"
        three="'Watermark' by Enya. https://www.youtube.com/watch?v=NO5tb20qQnA"
        four="'Song For Sienna' by Brian Crain. https://www.youtube.com/watch?v=2MYXZi2q02A"
        five="'Nuvole bianche' by Ludovico Einaudi. https://www.youtube.com/watch?v=kcihcYEOeic"
        six="'One Man's Dream' by Yanni. https://www.youtube.com/watch?v=STSzCX36U6o"
        seven="'Sundial Dreams' by Kevin Kern. https://www.youtube.com/watch?v=ERGGPB_ok18"
        eight="'Chrisofori's Dream' by David Lanz. https://www.youtube.com/watch?v=9wxrB41PMhw"
        nine="'Near light' by Olafur Arnalds. https://www.youtube.com/watch?v=0kYc55bXJFI"
        ten="'Waterfall' by Jon Schmidt. https://www.youtube.com/watch?v=8P9hAN-teOU"
        eleven="'Opus 28' by Dustin O'Halloran. https://www.youtube.com/watch?v=iQTWbS2SlVY"
        twelve="'Angel Eyes' by Jim Brickman. https://www.youtube.com/watch?v=3jcN20Efpq0"
        thirteen="'The Approaching Night.' by Philip Wesley. https://www.youtube.com/watch?v=MsTQjB1f4-A"
        fourteen="'A Beautiful Distraction' by Michele McLaughlin. https://www.youtube.com/watch?v=erbuUytTB44"
        fifteen="'Breathe' by Greg Maroney. https://www.youtube.com/watch?v=9eqyir5JGpA"
        sixteen="'Winter Walk' by David Nevue. https://www.youtube.com/watch?v=g9J4GPURT0s"
        seventeen="'Rococo' by Brique a Braq. https://www.youtube.com/watch?v=XpZn_8Nx9w4"
        eighteen="'Love's River' by Laura Sullivan. https://www.youtube.com/watch?v=bzHgyYj2-8I"
        nineteen="'Simply Satie' by Michael Dulin. https://www.youtube.com/watch?v=xcArvm3yCOI" 
        twenty="'Walk With Me' by Joe Bongiorno. https://www.youtube.com/watch?v=IY7btFAPl1M"
        twentyone="'Surrender' by Solomon Keal. https://www.youtube.com/watch?v=y2u0IE_adDM" 
        twentytwo="'For Ross' by Thad Fiscella. https://www.youtube.com/watch?v=aM4bYq98hpI"
        twentythree="'Sunrise' by Doug Hammer. https://www.youtube.com/watch?v=8lUVJcRFUR8"
        twentyfour="'Thanksgiving' by George Winston. https://www.youtube.com/watch?v=5yhpDzsz2ps"
        twentyfive="'Ambre' by Nils Frahm. https://www.youtube.com/watch?v=wkbf1-cVUuY"
        twentysix="'Foxglove' by Liz Story. https://www.youtube.com/watch?v=pNCWqDdnsDw"
        twentyseven="'Diva - Sentimental Walk' by Philip Aaberg. https://www.youtube.com/watch?v=97bWyr3eClI"
        twentyeight="'Natalie's Song' by Wayne Gratz. https://www.youtube.com/watch?v=23hrfnbZCdc"
        twentynine="'From the Outside' by Fiona Joy Hawkins. https://www.youtube.com/watch?v=fM4yA_z51-8"
        thirty="'Gone' by Jim Chappell. https://www.youtube.com/watch?v=dGlR9p7lBZM"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty)
        return 'Listen to ' + option
    elif musictype==12: #pop
        #from spotify
        one="'Pull-Up' by Jason Derulo. https://www.youtube.com/watch?v=OYjuuzPFmMc"
        two="'Faded' by Alann Walker. https://www.youtube.com/watch?v=60ItHLz5WEA"
        three="'The Greatest' by Kendrick Lamar. https://www.youtube.com/watch?v=sG6aWhZnbfw"
        four="'Greenlight' by Pitbull. https://www.youtube.com/watch?v=R7xbhKIiw4Y"
        five="'Future Pt. 2' by DJ Snake. https://www.youtube.com/watch?v=6NwozFIR-Xc"
        six="'Locked Away' by R. City. https://www.youtube.com/watch?v=6GUm5g8SG4o"
        seven="'Stressed Out' by Twenty One Pilots. https://www.youtube.com/watch?v=pXRviuL6vMY"
        eight="'Never Give Up' by Sia. https://www.youtube.com/watch?v=h6Ol3eprKiw"
        nine="'Starving' by Hailee Steinfeld. https://www.youtube.com/watch?v=xwjwCFZpdns"
        ten="'I Feel It Coming' by The Weeknd. https://www.youtube.com/watch?v=qFLhGq0060w"
        eleven="'Umbrella' by Rihanna. https://www.youtube.com/watch?v=CvBfHwUxHIk"
        twelve="'I Don't Wanna Live Forever' by ZAYN. https://www.youtube.com/watch?v=7F37r50VUTQ"
        thirteen="'Last Friday Night (T.G.I.F.) by Katy Perry. https://www.youtube.com/watch?v=KlyXNRrsk4A"
        fourteen="'Good News' by Ocean Park Standoff. https://www.youtube.com/watch?v=TX9ODx2_Vqk"
        fifteen="'Shape of You' by Ed Sheeran. https://www.youtube.com/watch?v=JGwWNGJdvx8"
        sixteen="'Crazy In Love' by Beyonce. https://www.youtube.com/watch?v=ViwtNLUqkMY"
        seventeen="'Sign of the TImes' by Harry Styles. https://www.youtube.com/watch?v=qN4ooNx77u0"
        eighteen="'I'm The One' by DJ Khaled. https://www.youtube.com/watch?v=weeI1G46q0o"
        nineteen="'Got 2 Luv U' by Sean Paul. https://www.youtube.com/watch?v=tDq3fNew1rU"
        twenty="'Swalla' by Jason Derulo. https://www.youtube.com/watch?v=NGLxoKOvzu4"
        twentyone="'Slide' by Calvin Harris. https://www.youtube.com/watch?v=8Ee4QjCEHHc"
        twentytwo="'Where is the Love?' by the Black Eyed Peas. https://www.youtube.com/watch?v=WpYeekQkAdc" 
        twentythree="'We Can't Stop' by Miley Cyrus. https://www.youtube.com/watch?v=LrUvu1mlWco"
        twentyfour="'Stereo Hearts' by Gym Class Heroes. https://www.youtube.com/watch?v=T3E9Wjbq44E"
        twentyfive="'Issues' by Julia Michaels. https://www.youtube.com/watch?v=9Ke4480MicU"
        twentysix="'Still Got TIme' by ZAYN. https://www.youtube.com/watch?v=cHOrHGpL4u0"
        twentyseven="'No Promises' by Cheat Codes. https://www.youtube.com/watch?v=jn40gqhxoSY"
        twentyeight="'Cold' by Maroon 5. https://www.youtube.com/watch?v=XatXy6ZhKZw"
        twentynine="'It Ain't Me' by Kygo and Selena Gomez. https://www.youtube.com/watch?v=D5drYkLiLI8"
        thirty="'Symphony' by Clean Bandit. https://www.youtube.com/watch?v=aatr_2MstrI"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty)
        return 'Listen to ' + option
    elif musictype==13: #reggae
        #bob marley - 3 little birds
        one="'La Rompe Corazones' by Daddy Yankee. https://www.youtube.com/watch?v=ks1CBTwtaU8"
        two="'Despacito' by Luis Fonsi. https://www.youtube.com/watch?v=kJQP7kiw5Fk"
        three="'Dispuesto' by Xcelencia. https://www.youtube.com/watch?v=cxaPQC2dBHM" 
        four="'Se Preparo' by Ozuna. https://www.youtube.com/watch?v=KWGrPNqz4uc"
        five="'Humo y Alcohol' by Eloy. https://www.youtube.com/watch?v=FcUPASmfzsQ"
        six="'Amame o Matame' by Ivy Queen. https://www.youtube.com/watch?v=gYLiq3cmRC8"
        seven="'El Amante' by Nicky Jam. https://www.youtube.com/watch?v=YG2p6XBuSKA"
        eight="'Otra Cosa' by Daddy Yankee. https://www.youtube.com/watch?v=XKqSpbbM-UI"
        nine="'Has Cambiado' by Gadiel. https://www.youtube.com/watch?v=VVweJj_ddRQ"
        ten="'Sola' by Anuel Aa. https://www.youtube.com/watch?v=AnKdQ5p5Ks8"
        eleven="'Otra Vez' by Zion & Lennox. https://www.youtube.com/watch?v=6R5i6wQCOCQ"
        twelve="'Si Ella Quisiera' by Justin Quiles. https://www.youtube.com/watch?v=80XGBMLXTEg"
        thirteen="'Detras De Ti' by Jory Boy. https://www.youtube.com/watch?v=nLNu3Mzs1O0"
        fourteen="'Dile Que Tu Me Quieres' by Ozuna. https://www.youtube.com/watch?v=WAcnWtZjDWE"
        fifteen="'Yo Sabia' by Jey M. https://www.youtube.com/watch?v=jm6loGj-gY0"
        sixteen="'Me Mata' by Excelencia. https://www.youtube.com/watch?v=TwTcwrzZw8Q"
        seventeen="'Shaky Shaky' by Daddy Yankee. https://www.youtube.com/watch?v=aKuivabiOns"
        eighteen="'Hasta el Amanecer - The Remix.' by Nicky Jam. https://www.youtube.com/watch?v=Oa6NPqcWbiY"
        nineteen="'Acercate' by De La Ghetto. https://www.youtube.com/watch?v=ti-pC0zZEMs"
        twenty="'A Donde Voy' by Cosculluela. https://www.youtube.com/watch?v=iwgu9WISwXI"
        twentyone="'Embriagame' by Zion & Lennox. b"
        twentytwo="'Crush' by Jahzel. https://www.youtube.com/watch?v=0MDs6trRCDw"
        twentythree="'Si Tu Cama Hablara' by Lenny Tavarez. https://www.youtube.com/watch?v=nyqOWhYsRb4"
        twentyfour="'Fotos de Varano' by Clandestino & Yailemm. https://www.youtube.com/watch?v=yfBABILjUE0"
        twentyfive="'Request' by Kelmitt. https://www.youtube.com/watch?v=-srbwgMhR40"
        twentysix="'Bebe' by Brytiago. https://www.youtube.com/watch?v=-3DgVwfdNvI"
        twentyseven="'Adderall' by Mym. https://www.youtube.com/watch?v=7xHzsDbt5MQ"
        twentyeight="'Cuando Me Vaya' by Gerry Capo. https://www.youtube.com/watch?v=-nriNj8CrYg"
        twentynine="'Bailame' by Nacho. https://www.youtube.com/watch?v=a1J44C-PZ3E"
        thirty="'Three Little Birds' by Bob Marley. https://www.youtube.com/watch?v=zaGUr6wzyT8" 
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty)
        return 'Listen to ' + option
    elif musictype==14: #rock
        #taken from spotify list (Top Rock of the 90s and 00s')
        one="'How You Remind Me' by Nickelback. https://www.youtube.com/watch?v=1cQh1ccqu8M"
        two="'In the end' by Linkin Park. https://www.youtube.com/watch?v=eVTXPUF4Oz4"
        three="'Kryptonite' by 3 Doors Down. https://www.youtube.com/watch?v=xPU8OAjjS4k"
        four="'Blurry' by Puddle of Mudd. https://www.youtube.com/watch?v=5RisBAkC0x8"
        five="'Like a Stone' by Audioslave. https://www.youtube.com/watch?v=7QU1nvuxaMA"
        six="'23' by Jimmy Eat World. https://www.youtube.com/watch?v=sqvix4pbVZ0"
        seven="'Megalomaniac' by Incubus. https://www.youtube.com/watch?v=MuZhnNR6vzc"
        eight="'Beautiful Day' by U2. https://www.youtube.com/watch?v=co6WMzDOh1o"
        nine="'Use Somoebody' by Kings of Leon. https://www.youtube.com/watch?v=gnhXHvRoUd0"
        ten="'45' by Shinedown. https://www.youtube.com/watch?v=MLeIyy2ipps"
        eleven="'From The Inside' by Linkin Park. https://www.youtube.com/watch?v=YLHpvjrFpe0" 
        twelve="'One X' by Three Days Grace. https://www.youtube.com/watch?v=5RBWdZ-VRIM" 
        thirteen="'B.Y.O.B' by System Of A Down. https://www.youtube.com/watch?v=zUzd9KyIDrM"
        fourteen="'Striken' by Disturbed. https://www.youtube.com/watch?v=3moLkjvhEu0"
        fifteen="'Under The Bridge' by Red Hot Chilli Peppers. https://www.youtube.com/watch?v=lwlogyj7nFE"
        sixteen="'Otherside' by Red Hot Chilli Peppers. https://www.youtube.com/watch?v=rn_YodiJO6k"
        seventeen="'Insterstate Love Song' by Stone Temple Pilots. https://www.youtube.com/watch?v=yjJL9DGU7Gg"
        eighteen="'I'll be Here While' by 311. https://www.youtube.com/watch?v=1BPm6wX7-Bo"
        nineteen="'No Excuses' by Alice In Chains. https://www.youtube.com/watch?v=r80HF68KM8g"
        twenty="'Fell On Black Days' by Soundgarden. https://www.youtube.com/watch?v=ySzrJ4GRF7s"
        twentyone="'Jane Says' by Jane's Addiction. https://www.youtube.com/watch?v=anWmfN-dODs"
        twentytwo="'Tonight, Tonight' by the Smashing Pumpkins. https://www.youtube.com/watch?v=NOG3eus4ZSo"
        twentythree="'1979' by the Smashing Pumpkins. https://www.youtube.com/watch?v=4aeETEoNfOg"
        twentyfour="'Say It Ain't So' by Wheezer. https://www.youtube.com/watch?v=ENXvZ9YRjbo"
        twentyfive="'Come As You Are' by Nirvana. https://www.youtube.com/watch?v=vabnZ9-ex7o"
        twentysix="'Even Flow' by Pearl Jam. https://www.youtube.com/watch?v=CxKWTzr-k6s"
        twentyseven="'Where Is My Mind?' by Pixies. https://www.youtube.com/watch?v=-gkibxWr0DY"
        twentyeight="'The Unforgiven' by Metallica. https://www.youtube.com/watch?v=Ckom3gf57Yw"
        twentynine="'Zombie' by The Cranberries. https://www.youtube.com/watch?v=6Ejga4kJUts"
        thirty="'What I Got' by Sublime. https://www.youtube.com/watch?v=0Uc3ZrmhDN4"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty)
        return 'Listen to ' + option
    elif musictype==15: #folk
        #taken from spotify (Indie Folk Top Tracks)
        one="'Can't See Straight' by Jamie Lawson. https://www.youtube.com/watch?v=u-wOyNiQtUg"
        two="'Place We Were Made' by Maisie Peters. https://www.youtube.com/watch?v=EauYea9MyLE"
        three="'Please Keep Loving Me' by James TW. https://www.youtube.com/watch?v=9QHyBNzxDmM" 
        four="'Bitter Truth' by Iron & Wine. https://www.youtube.com/watch?v=khHMwXOtQBQ"
        five="'I Will Spend My Whole Life Loving You' by Imaginary Future. https://www.youtube.com/watch?v=3dVhZuyltII"
        six="'Dark Four Door' by Billy Raffoul. https://www.youtube.com/watch?v=v1Z4GWQcnPQ"
        seven="'The Observatory' by The White Buffalo. https://www.youtube.com/watch?v=b1TE4ekRVdg"
        eight="'Untamed' by Eddie Berman. https://www.youtube.com/watch?v=4_4kqRYbhv0"
        nine="'Blend' by Aldous Harding. https://www.youtube.com/watch?v=jHR3uEOkkSo"
        ten="'Don't Let Me Get Me' by James Gillespie. https://www.youtube.com/watch?v=fYCYNIcZp3A"
        eleven="'If You Need To, Keep Time On Me' by Fleet Foxes. https://www.youtube.com/watch?v=T6rVJYmQFiY"
        twelve="'Chemicals' by Dean Lewis. https://www.youtube.com/watch?v=1F66YbQLVO0"
        thirteen="'Mountain To Move' by Nick Mulvey. https://www.youtube.com/watch?v=xSoirvVIKJg"
        fourteen="'Rebellion (Lies)' by Benjamin Francis Leftwich. https://www.youtube.com/watch?v=gHSOnXJMDgk"
        fifteen="'Colder Heavens' by Blanco White. https://www.youtube.com/watch?v=HFh377W9zvY"
        sixteen="'Never in My Wildest Dreams' by Dan Auerbach. https://www.youtube.com/watch?v=wP1mSyJFJ-c"
        seventeen="'All The Pretty Girls' by Kaleo. https://www.youtube.com/watch?v=FNwgOkl5nRY"
        eighteen="'All On My Mind' by Anderson East. https://www.youtube.com/watch?v=1zSczaSm60U"
        nineteen="'Lay It On Me' by Vance Joy. https://www.youtube.com/watch?v=VXXD1Qxpisw"
        twenty="'Lost On YOU' by Lewis Capaldi. https://www.youtube.com/watch?v=PUZqMw4rkVs"
        twentyone="'Sink' by Noah Kahan. https://www.youtube.com/watch?v=ahX_CuhNd4c"
        twentytwo="'Simple Song' by Passenger. https://www.youtube.com/watch?v=RfSVFtv7-90"
        twentythree="'Call It Dreaming' by Iron & Wine. https://www.youtube.com/watch?v=BXC80ZXQhvQ"
        twentyfour="'Fine' by Noah Kahan. https://www.youtube.com/watch?v=ihVIIvPTSPw"
        twentyfive="'You Would Have to Lose Your Mind' by the Barr Brothers. https://www.youtube.com/watch?v=Gg3Vlc5u2tA"
        twentysix="'Change It All' by Harrison Storm. https://www.youtube.com/watch?v=dOOW95P8LB4"
        twentyseven="'Standing in the Doorway' by Hiss Golden Messenger. https://www.youtube.com/watch?v=SOCNZsa6UTM"
        twentyeight="'Don't Matter Now' by George Ezra. https://www.youtube.com/watch?v=lM5mM-QDg24"
        twentynine="'Six Years' by A Blaze of Feather. https://www.youtube.com/watch?v=xX7RgjPeGg4"
        thirty="'Chicago Song' by Stu Larsen. https://www.youtube.com/watch?v=dvxn1TYWoJ0"
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty)
        return 'Listen to ' + option
    elif musictype==16: #soundtrack
        #Hans Zimmer
        #John Williams
        one="'Cloud and Confessions' by Patrick Doyle. https://www.youtube.com/watch?v=feOazX4AZY4" 
        two="'Fargo Main Theme' by Jeff Russo. https://www.youtube.com/watch?v=aM2l8TPzKmY"
        three="'Manny Village' by Junkie XL. https://www.youtube.com/watch?v=6XfZ7jXEsaI"
        four="'Migration' by Michael Giacchino. https://www.youtube.com/watch?v=jjMkxck_ipk"
        five="'Memory of a Happy Day' by Rael Jones. https://www.youtube.com/watch?v=joRKeFkp-W0"
        six="'Ocean Photographs' by Ludwig Goransson. https://www.youtube.com/watch?v=0YY2ZS31SCs"
        seven="'Snow Wolf' by Nick Cave. https://www.youtube.com/watch?v=gnj50QiI4bg"
        eight="'Intake' by Danny Elfman. https://www.youtube.com/watch?v=ARunKzrUWmw"
        nine="'Theme from Schindler's List' by John Williams. https://www.youtube.com/watch?v=gZs9uksEnho"
        ten="'Stark Raving Mad' by Micahel Giacchino. https://www.youtube.com/watch?v=uVwsI5nDx3Q"
        eleven="'Barcode 01001001' by Frank IIfman. https://www.youtube.com/watch?v=9KRNezXQpfw"
        twelve="'The Civilian Executive' by Nick Cave. https://www.youtube.com/watch?v=w1cdy0K86hY"
        thirteen="'Bit of Dried Goat' by Trevor Morris. https://www.youtube.com/watch?v=9JqCdJlSq7E"
        fourteen="'Adagio for Tron' by Marc-Andre Gautier. https://www.youtube.com/watch?v=aFIXKXYfEy0"
        fifteen="'First Skype' by Andrew Lockington. https://www.youtube.com/watch?v=kenrOlqcnUo"
        sixteen="'The First Time' by Adam Taylor. https://www.youtube.com/watch?v=H7X-wG_Iyho"
        seventeen="'Love Lost' by Danny Elfman. https://www.youtube.com/watch?v=sZZCar6Tjgo"
        eighteen="'Dave McGillivray' by Jeff Beal. https://www.youtube.com/watch?v=SOXmOXDoURg"
        nineteen="'Signing' by David Arnold. https://www.youtube.com/watch?v=3Nl_V5jpzIo"
        twenty="'Love Never Felt So Good' by Justin Timberlake. https://www.youtube.com/watch?v=oG08ukJPtR8"
        twentyone="'Time (Inception)' by Hans Zimmer. https://www.youtube.com/watch?v=RxabLA7UQ9k"
        twentytwo="'We Forget Who We Are' by Trent Reznor. https://www.youtube.com/watch?v=p3GtREoEZwc"
        twentythree="'Beyond Football' by Gary Lionelli. https://www.youtube.com/watch?v=NH1fZV0YOYo"
        twentyfour="'Aurora' by Thomas Newman. https://www.youtube.com/watch?v=--S-zCJWCBg"
        twentyfive="'Gabriel's Trumpet' by Marcelo Zarvos. https://www.youtube.com/watch?v=hxf1QYxEFI0"
        twentysix="'Kite' by Coby Brown. https://www.youtube.com/watch?v=L4dLdxV0Loc"
        twentyseven="'Funeral Rites' by Rob Lane. https://www.youtube.com/watch?v=weIP7PbOYzU"
        twentyeight="'A Sepulchre' by George Fenton. https://www.youtube.com/watch?v=_yv-uKZQIio"
        twentynine="'The Lagoon' by Hans Zimmer. https://www.youtube.com/watch?v=1fBm6xJiCo4"
        thirty="'Destiny's Path' by John Williams. https://www.youtube.com/watch?v=IHafONzO3hw" 
        option=selectoption(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty)
        return 'Listen to ' + option
    else:
        return "error"

##############################################################################
##                            MAIN SCRIPT                                   ##
##############################################################################

hostdir=sys.argv[1]
musictype=sys.argv[2]

#make into integer for later use
if musictype in ["alternative", "alternativerock","alternattive"]:
    musictype=1
    count1=0
elif musictype in ["classical"]:
    musictype=2
    count2=0
elif musictype in ["country"]:
    musictype=3
    count3=0
elif musictype in ["dance","edm"]:
    musictype=4  
    count4=0
elif musictype in ["jazz","classicaljazz", "jpop"]:
    musictype=5
    count5=0
elif musictype in ["hiphop","rap"]:
    musictype=6
    count6=0
elif musictype in ["holiday"]:
    musictype=7
    count7=0
elif musictype in ["indie","indiepop"]:
    musictype=8
    count8=0
elif musictype in ["christian","gospel"]:
    musictype=9
    count9=0
elif musictype in ["latin"]:
    musictype=10
    count10=0
elif musictype in ["newage"]:
    musictype=11
    count11=0
elif musictype in ["pop"]:
    musictype=12
    count12=0
elif musictype in ["reggae"]:
    musictype=13
    count13=0
elif musictype in ["rock"]:
    musictype=14
    count14=0
elif musictype in ["folk"]:
    musictype=15
    count15=0
elif musictype in ["soundtrack"]:
    musictype=16
    count16=0
elif musictype in ["all", "everything", "allgenres", "random"]:
    musictype=17
    count17=0 

g=getmusic(musictype)
print("%s"%(g))

try:
    linkindex=g.index('https')
    link=g[linkindex:]
    speaktext(hostdir, g[0:linkindex])
    webbrowser.open_new(link)
       
except:
    print('no link')

# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('registration.json'))
action_log=database['action log']
name=database['name']
email=database['email']

message='Hey %s, \n\n Looks like you are stressed today. \n\n Perhaps take a quick break and listen to %s! \n\n Remember, be well! \n\n Cheers, \n\n -The NeuroLex Team'%(name.split()[0].title(), g[10:])
sendmail([email],'NeuroLex: Listen to this song!', message, os.environ['NEUROLEX_EMAIL'], os.environ['NEUROLEX_EMAIL_PASSWORD'], [])

action={
    'action': 'search.py',
    'date': get_date(),
    'meta': [musictype, link],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('registration.json','w')
json.dump(database,jsonfile)
jsonfile.close()

            
