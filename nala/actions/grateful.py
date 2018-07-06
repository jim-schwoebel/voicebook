
##############################################################################
##                         STRESSLEX - GRATEFUL.PY                          ##
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

The grateful.py action module prompts the user to be grateful. Gratitude
has shown to improve well-being. There are two types of gratitude - 
Name 5 things that you're most grateful for today and also what are you 
most grateful for today. After you give a spoken response, it is emailed
to you as a reminder of what you should be thankful for.

In this way, you can remain healthy and keep thinking about all that you
have. :-)

'''

##############################################################################
##                           IMPORT STATEMENTS                              ##
##############################################################################

import pygame, random, datetime, time, pyaudio, ftplib, getpass, shutil, wave
import webbrowser, smtplib, os, platform, json, sys
from sys import byteorder
from array import array
from struct import pack
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
        
def playbackaudio(question,filename):
#takes in a question and a filename to open and plays back the audio file and prints on the screen the question for the user
    print(question)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(5)
    return "playback completed"
        
def record_to_file(path,filename,typefile):

    os.chdir(path)

    if typefile == 'mostgrateful':
        CHUNK = 1024 
        FORMAT = pyaudio.paInt16 #paInt8
        CHANNELS = 1 
        RATE = 44100 #sample rate
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = filename

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK) #buffer

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data) # 2 bytes(16 bits) per channel

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        
    elif typefile =='5mostgrateful':
        CHUNK = 1024 
        FORMAT = pyaudio.paInt16 #paInt8
        CHANNELS = 1 
        RATE = 44100 #sample rate
        RECORD_SECONDS = 20
        WAVE_OUTPUT_FILENAME = filename

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK) #buffer

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data) # 2 bytes(16 bits) per channel

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        

def pleasebegrateful(randomint):
    hostdir=os.getcwd()
    os.chdir(hostdir+'/actions')
    #speak into mic
    if randomint==1:
        playbackaudio("what are you most grateful for today?", "mostgrateful.mp3")
        today=datetime.datetime.today()
        record_to_file(hostdir+'/data/actions',"%s-mostgrateful.mp3"%(str(today)[0:9]),"mostgrateful")
    elif randomint==2:
        playbackaudio("what are 5 things are you are grateful for today?", "grateful5.mp3")
        today=datetime.datetime.today()
        record_to_file(hostdir+'/data/actions',"%s-grateful5.mp3"%(str(today)[0:9]),"5mostgrateful")
    
    #gratitute journal
    return "grateful completed"

def get_date():
    return str(datetime.datetime.now())

##############################################################################
##                            MAIN SCRIPT                                   ##
##############################################################################

print("Prepare to be grateful.")
time.sleep(1)

# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('registration.json'))
action_log=database['action log']
name=database['name']
email=database['email']

#import name, email from before 
webbrowser.open("http://actions.neurolex.co/uploads/grateful.m4a")
time.sleep(2)
webbrowser.open('http://actions.neurolex.co/uploads/grateful.png')
time.sleep(6)
today=datetime.datetime.now()
webbrowser.open('http://actions.neurolex.co/uploads/grateful2.png')
time.sleep(2)

randomint=random.randint(1,2)
pleasebegrateful(randomint)

today=get_date()

if randomint==1:
    message='Hey %s, \n\n Perhaps be more thankful! Gratitude journals are known to help reduce your stress. \n\n The attached .wav file is what you are grateful for today. Listen to and reflect upon this file. \n\n Is this all you are thankful for, or is there more? \n\n Remember, be well! \n\n Cheers, \n\n -The NeuroLex Team'%(name.split()[0].title())
    sendmail([email],'NeuroLex: Be more thankful!', message, os.environ['NEUROLEX_EMAIL'], os.environ['NEUROLEX_EMAIL_PASSWORD'], ["%s-mostgrateful.mp3"%(str(today)[0:9])])
    
elif randomint==2:
    message='Hey %s, \n\n Perhaps be more thankful! Gratitude journals are known to help reduce your stress. \n\n The attached .wav file is what you are grateful for today. Listen to and reflect upon this file. \n\n Is this all you are thankful for, or is there more? \n\n Remember, be well! \n\n Cheers, \n\n -The NeuroLex Team'%(name.split()[0].title())
    sendmail([email],'NeuroLex: Be more thankful!', message, os.environ['NEUROLEX_EMAIL'], os.environ['NEUROLEX_EMAIL_PASSWORD'], ["%s-grateful5.mp3"%(str(today)[0:9])])

webbrowser.open('http://actions.neurolex.co/uploads/exit2.png')

os.chdir(hostdir)
action={
    'action': 'grateful.py',
    'date': get_date(),
    'meta': [message],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('registration.json','w')
json.dump(database,jsonfile)
jsonfile.close()

