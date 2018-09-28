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
##                Y_SCRAPE.PY                 ##    
================================================ 

This script takes in a template excel sheet and downloads videos from youtube.

After this, the videos are clipped to the desired ranges as annoted by the end user.

This is all done in the current directory that the script is executed. 

In this way, we can quickly build custom curated datasets around specific 
use cases based on self-reported video bloggers.

Also, labels each output audio file with date, url, length, clipped points, 
label, age, gender, accent, and environment (if available in excel sheet).
'''
import os, json, pafy, time, wave, ffmpy, shutil, getpass, taglib, datetime 
import pandas as pd
import soundfile as sf

filename=input('what is the file name? \n')
desktop=os.getcwd()+'/'
foldername=filename[0:-5]
destfolder=desktop+foldername+'/'
try:
    os.mkdir(foldername)
    os.chdir(destfolder)
except:
    os.chdir(destfolder)

#move file to destfolder 
shutil.move(desktop+filename,destfolder+filename)

#load xls sheet (and get labels)
loadfile=pd.read_excel(filename)

link=loadfile.iloc[:,0]
length=loadfile.iloc[:,1]
times=loadfile.iloc[:,2]
label=loadfile.iloc[:,3]
age=loadfile.iloc[:,4]
gender=loadfile.iloc[:,5]
accent=loadfile.iloc[:,6]
quality=loadfile.iloc[:,7]
environment=loadfile.iloc[:,8]

#initialize lists 
links=list()
lengths=list()
start_times=list()
end_times=list()
labels=list()

#only make links that are in youtube processable 
for i in range(len(link)):
    if str(link[i]).find('youtube.com/watch') != -1:
        links.append(str(link[i]))
        lengths.append(str(length[i]))
        #find the dash for start/stop times
        time=str(times[i])
        index=time.find('-')
        start_time=time[0:index]
        #get start time in seconds 
        start_minutes=int(start_time[0])
        start_seconds=int(start_time[-2:])
        start_total=start_minutes*60+start_seconds
        #get end time in seconds 
        end_time=time[index+1:]
        end_minutes=int(end_time[0])
        end_seconds=int(end_time[-2:])
        end_total=end_minutes*60+end_seconds
        #update lists 
        start_times.append(start_total)
        end_times.append(end_total)
        #labels
        labels.append(str(label[i]))

files=list()
for i in range(len(links)):
    try: 
        video=pafy.new(links[i])
        bestaudio=video.getbestaudio()
        filename=bestaudio.download()
        start=start_times[i]
        end=end_times[i]
        extension=bestaudio.extension
        #get file extension and convert to .wav for processing later 
        os.rename(filename,'%s_start_%s_end_%s%s'%(str(i),start,end,extension))
        filename='%s_start_%s_end_%s%s'%(str(i),start,end,extension)
        if extension not in ['.wav']:
            xindex=filename.find(extension)
            filename=filename[0:xindex]
            ff=ffmpy.FFmpeg(
                inputs={filename+extension:None},
                outputs={filename+'.wav':None}
                )
            ff.run()
            os.remove(filename+extension)
        
        file=filename+'.wav'
        data,samplerate=sf.read(file)
        totalframes=len(data)
        totalseconds=totalframes/samplerate
        startsec=int(start_times[i])
        startframe=samplerate*startsec
        endsec=int(end_times[i])
        endframe=samplerate*endsec
        sf.write('snipped'+file, data[startframe:endframe], samplerate)
        newfilename='snipped'+file
        
        #can write json too 
        nfile= dict()
        nfile["Date"] = str(datetime.datetime.now())
        nfile["URL"] = str(links[i])
        nfile["Length"] = str(length[i])
        nfile["Clipped points"] = str(times[i])
        nfile["Label"] = str(label[i])
        nfile["Age"] = str(age[i])
        nfile["Gender"] = str(gender[i])
        nfile["Accent"] = str(accent[i])
        nfile["Environment"] = str(environment[i])
        jsonfile=open(newfilename[0:-4]+'.json','w')
        json.dump(nfile, jsonfile)
        jsonfile.close()

        os.remove(file)

    except:
        print('no urls')
