'''
Author: Jim Schwoebel
summarize_poems.py

Short script that takes in all the poems I've written and summarizes them
based on keyword frequencies. 
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



