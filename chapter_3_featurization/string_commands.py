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
##             STRING_COMMANDS.PY             ##    
================================================ 

this script guides you on how to manipulate strings.

Originally, this was intended to be run in the python interpreter.
The red sections below represent the outputs in the python interpreter. 
'''
# GET SAMPLE TRANSCRIPT 
transcript='I am having a happy jolly day today writing this chapter. I ran across Boston this morning and just had my morning coffee shipped from Heart Coffee in portland, Oregon.'

# BREAK UP SENTENCE INTO TOKENS
transcript.split()
# -> ['I', 'am', 'having', 'a', 'happy', 'jolly', 'day', 'today', 'writing', 'this', 'chapter.', 'I', 'ran', 'across', 'Boston', 'this', 'morning', 'and', 'just', 'had', 'my', 'morning', 'coffee', 'shipped', 'from', 'Heart', 'Coffee', 'in', 'portland,', 'Oregon.']

# BREAK UP INTO SENTENCES 
transcript.split('.')
# -> ['I am having a happy jolly day today writing this chapter', ' I ran across Boston this morning and just had my morning coffee shipped from Heart Coffee in portland, Oregon', '']
sentences=transcript.split('.')
len(sentences)
# -> 3
sentences[0]
# -> 'I am having a happy jolly day today writing this chapter'
sentences[1]
# -> ' I ran across Boston this morning and just had my morning coffee shipped from Heart Coffee in portland, Oregon'
sentences[2]
# -> ''

# REPLACING CERTAIN ELEMENTS IN STRING 
transcript.replace('Oregon','OR')
# -> 'I am having a happy jolly day today writing this chapter. I ran across Boston this morning and just had my morning coffee shipped from Heart Coffee in portland, OR.'

# FIND CERTAIN ELEMENT INDICES IN STRING 
transcript.find('I')
#-> 0
transcript.find('jolly')
#-> 20

# SLICING A STRING 
transcript[0:20]
#-> 'I am having a happy '

# COUNT NUMBER OF OCCURENCES OF WORD OR LETTER 
transcript.count('I')
#-> 2
transcript.count('hello')
#-> 0
transcript.count('a')
#-> 13

# CONCATENATE STRINGS 
transcript+' This is additional stuff...'
# -> 'I am having a happy jolly day today writing this chapter. I ran across Boston this morning and just had my morning coffee shipped from Heart Coffee in portland, Oregon. This is additional stuff...'

# REPEATING STRINGS
transcript*2
'I am having a happy jolly day today writing this chapter. I ran across Boston this morning and just had my morning coffee shipped from Heart Coffee in portland, Oregon.I am having a happy jolly day today writing this chapter. I ran across Boston this morning and just had my morning coffee shipped from Heart Coffee in portland, Oregon.'

# CHANGING CASES
transcript.upper()
# -> 'I AM HAVING A HAPPY JOLLY DAY TODAY WRITING THIS CHAPTER. I RAN ACROSS BOSTON THIS MORNING AND JUST HAD MY MORNING COFFEE SHIPPED FROM HEART COFFEE IN PORTLAND, OREGON.'
transcript.lower()
#-> 'i am having a happy jolly day today writing this chapter. i ran across boston this morning and just had my morning coffee shipped from heart coffee in portland, oregon.'
transcript.title()
#-> 'I Am Having A Happy Jolly Day Today Writing This Chapter. I Ran Across Boston This Morning And Just Had My Morning Coffee Shipped From Heart Coffee In Portland, Oregon.'
