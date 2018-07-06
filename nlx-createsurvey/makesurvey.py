'''
Author: @Jim Schwoebel
Last edit: 03/04/2018 

This script takes in a list of questions and outputs a .html survey to be done in offline-related applications.

Surveys can be uploaded online using the Site 5 backstage shared server. New surveys will have new survey IDs and 
can track responses.

(C) 2018, NeuroLex Laboratories
'''

import webbrowser
import os
import pygame 
import time
import ftplib
import pyttsx3 as pyttsx
import speech_recognition as sr
import shutil
from sys import byteorder
from array import array
from struct import pack
import pyaudio
import wave

def playbackaudio(filename):
#takes in a question and a filename to open and plays back the audio file and prints on the screen the question for the user 
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(0.5)
    return "playback completed"

def transcribe(question):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(question)
        audio = r.listen(source)
        transcript=r.recognize_sphinx(audio)
    return transcript

def record_to_file(path,filename,time):
    CHUNK = 1024 
    FORMAT = pyaudio.paInt16 #paInt8
    CHANNELS = 2 
    RATE = 44100 #sample rate
    RECORD_SECONDS = time
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
    return filename

def transcribe2(question,filename,time):
    #https://pypi.python.org/pypi/SpeechRecognition/2.1.3
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(question)
        audio1 = record_to_file(os.getcwd(),filename,time)
        with sr.WavFile(audio1) as source:              # use "test.wav" as the audio source
            audio = r.record(source)  
        transcript=r.recognize_sphinx(audio)
    return transcript

def surveytemplate(var,question,speakprompt,timelength):
    if speakprompt=='yes':
        #usually done the first time in the survey
        #defaults to 200 words per minute len(g.split())/200=minutes (start after this) 
        file=open(var+'.html','w')
        file.write(logo)
        file.write('</br>')
        file.write('<h2><center><strong>After the tone, please answer this question:</strong></center></h2>')
        file.write('</br>')
        file.write("<font size='+1'><center>")
        file.write(question)
        file.write("</font></center>")
        file.close()
        webbrowser.open(os.getcwd()+'/'+var+'.html')
        engine.say('After the tone, please answer this question.')
        engine.runAndWait()
        time.sleep(1)
        engine.say(question)
        engine.runAndWait()
        playbackaudio('logo.wav')
        time.sleep(1)
        record_to_file(path,str(userid2)+'_'+var+'.wav',int(timelength))
    elif speakprompt=='no':
        file=open(var+'.html','w')
        file.write(logo)
        file.write('</br>')
        file.write('<h2><center><strong>After the tone, please answer this question:</strong></center></h2>')
        file.write('</br>')
        file.write("<font size='+1'><center>")
        file.write(question)
        file.write("</font></center>")
        file.close()
        webbrowser.open(os.getcwd()+'/'+var+'.html')
        engine.say(question)
        engine.runAndWait()
        playbackaudio('logo.wav')
        time.sleep(1)
        record_to_file(path,str(userid2)+'_'+var+'.wav',int(timelength))

#change to desktop
try:
    os.mkdir('/Users/jim/Desktop/surveyaudio')
    os.chdir('/Users/jim/Desktop/surveyaudio')
except:
    os.chdir('/Users/jim/Desktop/surveyaudio')
path=os.getcwd()
engine = pyttsx.init()

#surveyaudio directory
#get username and password + open up the proper directory 
session=ftplib.FTP('neurolex.co','neurolex','jschwoebel3')
session.cwd('/public_html/surveyaudio/surveys')
lf=open('logo.wav','wb')
session.retrbinary('RETR '+'logo.wav',lf.write,8*1024)
lf.close()
lf=open('id.txt','wb')
session.retrbinary('RETR '+'id.txt',lf.write,8*1024)
lf.close()
userid=open('id.txt').read() 
userid2=int(userid)+1
userid=open('id.txt','w')
userid.write(str(userid2))
userid.close() 
lf=open('id.txt','rb')
session.storbinary('STOR '+'id.txt',lf)
lf.close()
try:
    session.mkd('/public_html/surveyaudio/surveys/'+str(userid2))
    session.cwd('/public_html/surveyaudio/surveys/'+str(userid2))
except:
    session.cwd('/public_html/surveyaudio/surveys/'+str(userid2))

company=input('what is your company name?')
purpose=input('what is the purpose of the survey? (e.g. to improve future events)')
questions=input('how many open-ended (20 second) questions do you want for your survey?')
questionlist=list()
timelist=list()
totaltime=0
for i in range(int(questions)):
    question=input('what is the open-ended question number %s?'%(str(i+1)))
    timelength=input('how long do you want as a response (in seconds)? (30 sec max)')
    while timelength not in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']:
        print('input not recognized')
        timelength=input('how long do you want as a response (in seconds)? (30 sec max)')
    totaltime=totaltime+int(timelength)
    questionlist.append(question)
    timelist.append(timelength)
logopath='http://baseline.neurolex.co/uploads/stresslexlogo.png'
logo="<center><img src='"+logopath+"'></center>"

#startup baseline script 
#consent / license document
startup=open('startup.html','w')
startup.write(logo)
startup.write("</br>")
startup.write("<font size='+1'><center>")
startup.write('<h2><center><strong>Disclaimer</strong></center></h2>')
startup.write('</br>')
startup.write("By continuing, you are agreeing to take a short voice-enabled survey for <a href='http://neurolex.ai'> %s </a> %s."%(company,purpose))
startup.write("</br></br>")
startup.write("Please follow the following voice prompts. The whole process should take roughly %s minutes."%(str(int(totaltime/60+10/60*len(questionlist)))))
startup.write("</br></br>")
startup.write("Thanks so much!")
startup.write("</br></br>")
startup.write("-the %s team"%(company))
startup.write("</br></br>")
startup.write("To agree to these terms, say 'yes' after the tone.")
startup.write("</font></center>")
startup.close()
webbrowser.open(os.getcwd()+'/startup.html')
question="By continuing, you are agreeing to take a short voice-enabled survey for %s %s."%(company,purpose)
engine.say(question)
engine.runAndWait()
time.sleep(1)
question='To agree to these terms, say yes after the tone'
engine.say(question)
engine.runAndWait()
playbackaudio('logo.wav')
time.sleep(1)
terms=transcribe2(question,'terms.wav',3)
##while terms.lower() not in ['yes','no']:
##    question='Sorry, input not recognized. Do you agree to these terms? Yes or no.'
##    engine.say(question)
##    engine.runAndWait()
##    playbackaudio('logo.wav')
##    time.sleep(1)
##    terms=transcribe2(question,'terms.wav',4)                           

#Get started by baselining you
baseline=open('baseline.html','w')
baseline.write(logo)
baseline.write("</br>")
baseline.write('<h2><center><strong>Baseline questions.</strong></center></h2>')
baseline.write("<font size='+1'><center>")
baseline.write("To continue, we need you to answer a few questions.")
baseline.write("</br></br>")
baseline.write("Please respond after the tone to each of these questions.")
baseline.write("</br></br>")
baseline.close()
webbrowser.open(os.getcwd()+'/baseline.html')
question="To continue, we need you to answer a few questions."
engine.say(question)
engine.runAndWait()

baseline2=open('baseline2.html','w')
baseline2.write(logo)
baseline2.write("</br>")
baseline2.write('<h2><center><strong>Baseline questions.</strong></center></h2>')
baseline2.write("<font size='+1'><center>")
baseline2.write("Are you male or female?")
baseline2.write("</br></br>")
baseline2.write("What is your age?")
baseline2.write("</br></br>")
baseline2.write("What is your ethnicity?")
baseline2.write("</br></br>")
baseline2.close() 
webbrowser.open(os.getcwd()+'/baseline2.html')
question='Are you male or female?'
engine.say(question)
engine.runAndWait()
playbackaudio('logo.wav')
time.sleep(1)
gender=transcribe2(question,'gender.wav',4) 
##while terms.lower() not in ['male','female']:
##    question='Sorry, input not recognized. Are you male or female?'
##    engine.say(question)
##    engine.runAndWait()
##    playbackaudio('logo.wav')
##    time.sleep(1)
##    terms=transcribe(question)
question='What is your age?'
engine.say(question)
engine.runAndWait()
playbackaudio('logo.wav')
time.sleep(1)
age=transcribe2(question,'age.wav',4)
question='What is your ethnicity?'
engine.say(question)
engine.runAndWait()
playbackaudio('logo.wav')
time.sleep(1)
ethnicity=transcribe2(question,'ethnicity.wav',4)
baselinedata=open('baseline.txt','w')
baselinedata.write('gender: '+gender)
baselinedata.write('\n')
baselinedata.write('age: '+age)
baselinedata.write('\n')
baselinedata.write('ethnicity: '+ethnicity)
baselinedata.write('\n')
baselinedata.close()
lf3=open('baseline.txt','rb')
session.storbinary('STOR '+'baseline.txt',lf3)
lf3.close()

#now do all the surveys
for i in range(len(questionlist)):
    if i==0:
        surveytemplate(str(i),questionlist[i],'yes',timelist[i])
    else:
        surveytemplate(str(i),questionlist[i],'no',timelist[i])

finish=open('finish.html','w')
finish.write(logo)
finish.write('</br>')
finish.write('<h2><center><strong>You are finished. Thank you!</strong></center></h2>')
finish.close()
webbrowser.open(os.getcwd()+'/finish.html')
question='You are finished. Thank you!'
engine.say(question)
engine.runAndWait()
    
g=os.listdir()
for i in range(len(g)):
    if g[i][-4:]=='.wav' or g[i][-5:]=='.html':
        print("uploading file to server.")
        file=open(g[i],'rb')
        session.storbinary('STOR '+g[i],file)
        file.close()

#delete directory 
#shutil.rmtree('C:/Users/Jim Schwoebel/Desktop/neurolex-baseline')
        
session.close()

#transcript each part to produce a report with features and reference ranges 

