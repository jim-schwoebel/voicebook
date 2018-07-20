'''
string_commands.py

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
