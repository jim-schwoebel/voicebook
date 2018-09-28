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
##               LABEL_SAMPLES.PY             ##    
================================================ 

Have you listen to an audio file and then type in the appropriate
information for labeling.

It outputs a .json file [filename]_label.json with all the associated information.

You can then create a master set of labels by running the script
make_labels.py

'''
import json, xlsxwriter, os 
import pandas as pd

url ='labeling url'
master_label=input('what is the master label (e.g. stressed)? \n')
master_label_description='is this person %s? 1 for yes, 0 for no'%(master_label)
sample_number=0
dataset=list()

while url not in ['','n']:
    print('sample number: %s'%(str(sample_number)))
    url = input('what is the URL of the video? \n').replace(' ','')
    if url in ['', 'n']:
        # break loop if no url description 
        break 
    clip_length=input('how long is the audio sample in seconds? (e.g. 20) \n').replace(' ','')
    start_stop=input('what are the stop and start times of the video (e.g. 0:13-0:33)\n').replace(' ','')
    label=input(master_label_description + '\n')
    age=input('is this person a child (c, <13) or adolescent (d, 13-18) or adult  (a, >18 <70) or elderly (e, >70)? \n').lower().replace(' ','')
    if age == 'c':
        age='child (<13 years old)'
    elif age  == 'd':
        age='adolescent (13-18 years old)'
    elif age  == 'a':
        age='adult (>18 years old)'
    elif age == 'e':
        age='elderly (>70 years old)'

    gender=input('is this person male (m) or female (f)? \n').lower().replace(' ','')
    if gender == 'm':
        gender='male'
    elif gender == 'f':
        gender='female'
    accent=input('does this person have an American (a) or foreign (f) accent? \n').lower().replace(' ','')
    if accent =='a':
        accent='american'
    elif accent =='f':
        accent='foreign'
    audioquality=input('what is the audio quality? (1 - poor, 2 - moderate, 3 - good quality, 4 - high quality)').replace(' ','')
    while audioquality not in ['1','2','3','4']:
        print('input not recognized')
        audioquality=input('what is the audio quality? (1 - poor, 2 - moderate, 3 - good quality, 4 - high quality)').replace(' ','')
    environment=input('is the environment indoors (i) or outdoors (o)?').lower().replace(' ','')
    if environment == 'i':
        environment='indoors'
    elif environment == 'o':
        environment='outdoors'

    data={
        'sample number':sample_number,
        'url':url,
        'clip_length':clip_length,
        'start_stop':start_stop,
        'master_label':master_label,
        'master_label_description':master_label_description,
        'label':label,
        'age':age,
        'gender':gender,
        'accent':accent,
        'audioquality': audioquality,
        'environment': environment,
        }

    dataset.append(data)
          
    sample_number=sample_number+1 

#  dump everything into a .json file 
jsonfilename=master_label+'_'+str(sample_number)+'.json'
jsonfile=open(jsonfilename,'w')
data={
    'labeled data':dataset
    }
json.dump(data,jsonfile)
jsonfile.close()
        
# write all data to excelsheet (in desired label format later)
filename=master_label+'_'+str(sample_number)+'.xlsx'
workbook = xlsxwriter.Workbook(filename)
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'URL')
worksheet.write('B1', 'Clip Length (seconds)')
worksheet.write('C1', 'Start and stop points')
worksheet.write('D1', 'Label: %s'%(master_label_description))
worksheet.write('E1', 'Age')
worksheet.write('F1', 'Gender')
worksheet.write('G1', 'Accent')
worksheet.write('H1', 'Audio quality: (1 - poor, 2 - moderate, 3 - good quality, 4 - high quality)')
worksheet.write('I1', 'Environment')
                
for i in range(len(dataset)):
    worksheet.write('A'+str(i+2),dataset[i]['url'])
    worksheet.write('B'+str(i+2),dataset[i]['clip_length'])
    worksheet.write('C'+str(i+2),dataset[i]['start_stop'])
    worksheet.write('D'+str(i+2),dataset[i]['label'])
    worksheet.write('E'+str(i+2),dataset[i]['age'])
    worksheet.write('F'+str(i+2),dataset[i]['gender'])
    worksheet.write('G'+str(i+2),dataset[i]['accent'])
    worksheet.write('H'+str(i+2),dataset[i]['audioquality'])
    worksheet.write('I'+str(i+2),dataset[i]['environment'])
          
workbook.close()
os.system('open %s'%(filename))
        
    
