'''
Make_vchatbot.py

Makes a voice-enabled chatbot.

Scrape a Drupal FAQ page, then build a chatbot that can be used
to answer all the questions from a given query.

Following tutorial of http://chatterbot.readthedocs.io/en/stable/training.html

Trains using a list trainer.

More advance types of Q&A pairing are to come.
'''
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os, requests
from bs4 import BeautifulSoup
import speech_recognition as sr_audio
import sounddevice as sd
import soundfile as sf 
import pyttsx3, time 

# define some helper functions 
def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

def transcribe_sphinx(file):
    r=sr_audio.Recognizer()
    with sr_audio.AudioFile(file) as source:
        audio = r.record(source) 
    transcript=r.recognize_sphinx(audio)
    print('sphinx transcript: '+transcript)
    
    return transcript 

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# works on Drupal FAQ forms
page=requests.get('http://cyberlaunch.vc/faq-page')
soup=BeautifulSoup(page.content, 'lxml')
g=soup.find_all(class_="faq-question-answer")
y=list()

# initialize chatbot parameters 
chatbot = ChatBot("CyberLaunch")
chatbot.set_trainer(ListTrainer)

# parse through soup and get Q&A 
for i in range(len(g)):
    entry=g[i].get_text().replace('\xa0','').split('  \n\n')
    newentry=list()
    for j in range(len(entry)):
        if j==0:
            qa=entry[j].replace('\n','')
            newentry.append(qa)
        else:
            qa=entry[j].replace('\n',' ').replace('   ','')
            newentry.append(qa)
        
    y.append(newentry)

# train chatbot with Q&A training corpus 
for i in range(len(y)):
    question=y[i][0]
    answer=y[i][1]
    print(question)
    print(answer)

    chatbot.train([
        question,
        answer,
        ])
    
# now ask the user 2 sample questions to get response.
for i in range(2):
    speak_text('how can I help you?')
    # record a voice sample 
    sync_record('sample.wav', 5, 16000, 1)
    # transcribe this voice sample and remove the audio 
    question=transcribe_sphinx('sample.wav')
    os.remove('sample.wav')
    # speak_text('okay, processing...')
    response = chatbot.get_response(question)
    # speak the response instead of playing it on screen
    print(str(response))
    speak_text(str(response))

