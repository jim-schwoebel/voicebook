'''
Author: Jim Schwoebel
Script: generate_poem.py

Use natural language processing techniques to generate
a poem in the format ABQBA.

This was trained on my own poetry (59 poems) over the years.

Feel free to add in other texts as you see fit. 
'''
import nltk, os, re, random 
from collections import Counter
import numpy as np 
from textblob import TextBlob
from nltk.corpus import genesis

def randselect(stringlist):
    length=len(stringlist)-1
    randnum=random.randint(0,length)
    return stringlist[randnum]

# ask user if they'd like a random poem 
randompoem=input('would you like a random poem? \n')
os.chdir(os.getcwd()+'/data')
poetry=open('poetry.txt', encoding="utf8").read()
tokens=poetry.split()
text=nltk.Text(tokens)
tags=nltk.pos_tag(text)

# get POS lists 
verbs=list()
nouns=list()
adjectives=list()
adverbs=list()
vbed=list()
ned=list()
eadj=list()
nounend=list()

if randompoem in ['y','yes']:

    for i in range(len(tags)):
        if tags[i][1] in ['VB','VBD']:
            verbs.append(tags[i][0])
            if tags[i][0].endswith('ed')==True:
                vbed.append(tags[i][0])
        elif tags[i][1] in ['NN','NNS']:
            nouns.append(tags[i][0])
            if tags[i][0].endswith('ed')==True:
                ned.append(tags[i][0])   
        elif tags[i][1] in ['JJ','JJS']:
            adjectives.append(tags[i][0])
            if tags[i][0].endswith('e')==True:
                eadj.append(tags[i][0])
        elif tags[i][1] in ['RB','RBS']:
            adverbs.append(tags[i][0])
        else:
            pass
    poemname=randselect(nouns)
    #random selection of a noun
    description='I feel %s and %s and %s toward %s'%(randselect(adjectives),randselect(adjectives),randselect(adjectives),poemname)
    #I feel [adjective] and [adjective] and [adjective] towards [poemname].
    tokens2=description.split()
    text2=nltk.Text(tokens)
    tags2=nltk.pos_tag(text)
    name=poemname.title()

    for i in range(len(tags)):
        if tags[i][1] in ['NN','NNS']:
          if tags[i][0].endswith(name[len(name)-1])==True:
                nounend.append(tags[i][0])     

    #make a poem - funny 
    poem=open(name+'3.txt','w')
    poem.write(name)
    for i in range(5):
        poem.write('\n\n')
        #X5 stanzas
        poem.write("I seek a %s %s \n"%(randselect(adjectives),name))
        poem.write("The %s is %s \n"%(randselect(nouns),randselect(eadj)))
        poem.write("Why is it %s to %s? \n"%(randselect(adverbs),randselect(verbs)))
        poem.write("The %s is %s \n"%(randselect(nouns),randselect(eadj)))
        poem.write("The %s is a %s %s \n"%(randselect(nouns),randselect(adjectives),randselect(nounend)))

    poem.close()
               
elif randompoem in ['n','no']:
    poemname=input('what is the name of the poem? (noun) \n')
    description=input('what is the description? \n')
    tokens2=description.split()
    text2=nltk.Text(tokens)
    tags2=nltk.pos_tag(text)
    name=poemname.title()

    for i in range(len(tags)):
        if tags[i][1] in ['VB','VBD']:
            verbs.append(tags[i][0])
            if tags[i][0].endswith('ed')==True:
                vbed.append(tags[i][0])
        elif tags[i][1] in ['NN','NNS']:
            nouns.append(tags[i][0])
            if tags[i][0].endswith('ed')==True:
                ned.append(tags[i][0])
            if tags[i][0].endswith(name[len(name)-1])==True:
                nounend.append(tags[i][0])        
        elif tags[i][1] in ['JJ','JJS']:
            adjectives.append(tags[i][0])
            if tags[i][0].endswith('e')==True:
                eadj.append(tags[i][0])
        elif tags[i][1] in ['RB','RBS']:
            adverbs.append(tags[i][0])
        else:
            pass

    #make a poem - funny 
    poem=open(name+'.txt','w')
    poem.write(name)
    for i in range(5):
        poem.write('\n\n')
        #X5 stanzas
        poem.write("I seek a %s %s \n"%(randselect(adjectives),name))
        poem.write("The %s is %s \n"%(randselect(nouns),randselect(eadj)))
        poem.write("Why is it %s to %s? \n"%(randselect(adverbs),randselect(verbs)))
        poem.write("The %s is %s \n"%(randselect(nouns),randselect(eadj)))
        poem.write("The %s is a %s %s \n"%(randselect(nouns),randselect(adjectives),randselect(nounend)))

    poem.close()
