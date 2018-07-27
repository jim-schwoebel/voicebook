'''
text_entity.py

Plot entities using spacy.


'''
import spacy

# read a transcript 
transcript=open('./data/entity.txt').read()
nlp = spacy.load('en_core_web_sm')
doc = nlp(u"%s"%(transcript))
spacy.displacy.serve(doc, style='ent', port=3003)
