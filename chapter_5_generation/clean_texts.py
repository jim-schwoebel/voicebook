'''
clean_texts.py

Takes in the SMS text corpus dataset and cleans it,
outputting the texts as a .txt file that can be loaded
in and processed with textgenrnn library.

'''
import os, json

# get 55,835 messages
os.chdir('data')
data=json.load(open('smsCorpus_en_2015.03.09_all.json'))
t_messages=data['smsCorpus']['message']
messages=list()
for i in range(len(t_messages)):
    messages.append(t_messages[i]['text']['$'])

# write them to a text file for training purposes (if file doesn't exist)
if 'textmessages.txt' not in os.listdir():
    textfile=open('textmessages.txt','w')
    for i in range(len(messages)):
        # every new line is a new entry
        # skip ones that have odd characters by adding error handling 
        try:
            textfile.write(messages[i])
            textfile.write('\n')
        except:
            pass 
    textfile.close()
