'''
================================================ 
##            VOICEBOOK REPOSITORY            ##      
================================================ 

repository name: voicebook 
repository version: 1.0 
repository link: https://github.com/jim-schwoebel/voicebook 
author: Jim Schwoebel 
author contact: js@neurolex.co 
description: a book and repo to get you started programming voice applications in Python - 10 chapters and 200+ scripts. 
license category: opensource 
license: Apache 2.0 license 
organization name: NeuroLex Laboratories, Inc. 
location: Seattle, WA 
website: https://neurolex.ai 
release date: 2018-09-28 

This code (voicebook) is hereby released under a Apache 2.0 license license. 

For more information, check out the license terms below. 

================================================ 
##               LICENSE TERMS                ##      
================================================ 

Copyright 2018 NeuroLex Laboratories, Inc. 

Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 

     http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License. 

================================================ 
##               SERVICE STATEMENT            ##        
================================================ 

If you are using the code written for a larger project, we are 
happy to consult with you and help you with deployment. Our team 
has >10 world experts in Kafka distributed architectures, microservices 
built on top of Node.js / Python / Docker, and applying machine learning to 
model speech and text data. 

We have helped a wide variety of enterprises - small businesses, 
researchers, enterprises, and/or independent developers. 

If you would like to work with us let us know @ js@neurolex.co. 

================================================ 
##             GENERATE_SUMMARY.PY            ##    
================================================ 

Generate a summary from a URL link or link to text file locally.
'''
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import os, nltk

# modify 
LANGUAGE = "english"
SENTENCES_COUNT = 10

# read the data 
os.chdir(os.getcwd()+'/data')

# input file type
ftype=input('what file type is this (t) for text, (w) for website. \n').lower().replace(' ','')
while ftype not in ['t','w']:
    ftype=input('what file type is this (t) for text, (w) for website. \n').lower().replace(' ','')

if ftype in 't':
    textfile=input('what is the name of the text file (e.g. poetry.txt) in the ./data directory? \n')
    g=open(textfile).read()
    parser = PlaintextParser.from_file(textfile, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    # now summarize: output as [txtfile]_summary.txt
    g=open(textfile[0:-4]+'_summary.txt','w')
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
        g.write(str(sentence))
    g.close()
    os.system('open %s'%(textfile[0:-4]+'_summary.txt'))
elif ftype in ['w']:
    # for URLS
    url=input('what link would you like to summarize on Wikipedia? \n')
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # for plaintext
    #parser = PlaintextParser.from_file("poetry.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    # now summarize: output as [txtfile]_summary.txt
    g=open('web_summary.txt','w')
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
        g.write(str(sentence))
    g.close()
    os.system('open web_summary.txt')



