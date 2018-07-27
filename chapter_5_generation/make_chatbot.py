'''
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
    question=input('how can I help you? \n')
    response = chatbot.get_response(question)
    print(response)

