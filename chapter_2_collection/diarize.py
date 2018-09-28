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
##               DIARIZE.PY                   ##    
================================================ 

This function takes in a speech sample and diarizes it for 2 speakers.

The output files are stored in a folder structure with Speaker A and Speaker B.

It is assumed to be a 2 speaker diarization problem.

The output .zip file is named filename[0:-4]+'diarization.zip' and contains:

--->filename[0:-4]+'.json'
--> speaker 1 folder
    --> speaker 1 sections (multiple .wav files)
    --> speaker 1 stiched togetehr (single .wav file)
--> speaker 2 folder
    --> speaker 2 sections (multiple .wav files)
    --> speaker 2 stich (single .wav file)

Diarization is done with the pyaudioanalysis3 library.
'''

import os, json, importlib, scipy, shutil, ffmpy, time, sys, getpass, zipfile
import speech_recognition as sr_audio
from pydub import AudioSegment
import numpy as np 

if 'pyAudioAnalysis3' not in os.listdir():
    os.system("git clone git@github.com:NeuroLexDiagnostics/pyAudioAnalysis3.git")
    
sys.path.append(os.getcwd()+'/pyAudioAnalysis3')

import audioTrainTest as aT
import audioBasicIO 
import audioFeatureExtraction as aF
import audioSegmentation as aS

##INITIALIZE FUNCTIONS FOR DIARIZATION
####################################################################################

def exportfile(newAudio,time1,time2,filename,i,speaknum):
    #Exports to a wav file in the current path.
    newAudio2 = newAudio[time1:time2]
    print('making '+filename[0:-4]+'_'+str(speaknum)+'_'+str(i)+'_'+str(time1/1000)+'_'+str(time2/1000)+'.wav')
    newAudio2.export(filename[0:-4]+'_'+str(speaknum)+'_'+str(i)+'_'+str(time1/1000)+'_'+str(time2/1000)+'.wav', format="wav")

    return filename[0:-4]+'_'+str(speaknum)+'_'+str(i)+'_'+str(time1/1000)+'_'+str(time2/1000)+'.wav'

def stitchtogether(dirlist,dirloc,filename):
    try:
        #assumes already in proper directory 
        for i in range(len(dirlist)):
            if i ==0:
                sound=AudioSegment.from_wav(dirloc+'/'+str(dirlist[i]))
            else:
                sound=sound+AudioSegment.from_wav(dirloc+'/'+str(dirlist[i]))
        sound.export(dirloc+'/'+filename, format="wav")

    except:
        print('error stitching...')

def stereo2mono(audiodata,filename):
    newaudiodata = list()
    
    for i in range(len(audiodata)):
        d = audiodata[i][0]/2 + audiodata[i][1]/2
        newaudiodata.append(d)
    
    return np.array(newaudiodata, dtype='int16')
    #to apply this function, SR=sample rate usually 44100
    #wavfile.write(newfilename, sr, newaudiodata)

def convertformat(filename):
    newfilename=filename[0:-4]+'.wav'
    ff = ffmpy.FFmpeg(
        inputs={filename:None},
        outputs={newfilename: None}
        )
    ff.run()

    return newfilename

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def transcribe_audio_google(filename):
    # transcribe the audio (note this is only done if a voice sample)
    r=sr_audio.Recognizer()
    with sr_audio.AudioFile(filename) as source:
        audio = r.record(source) 
    text=r.recognize_google_cloud(audio)

    return text    

def transcribe_audio_sphinx(filename):
    # transcribe the audio (note this is only done if a voice sample)
    r=sr_audio.Recognizer()
    with sr_audio.AudioFile(filename) as source:
        audio = r.record(source) 
    text=r.recognize_sphinx(audio)
    print('transcript: '+text)
    
    return text

##GO TO HOST DIRECTORY AND BEGIN BULK PROCESSING 
####################################################################################

#host directory in app is likely /usr/app/...
hostdir=os.getcwd()
curdir=os.listdir()

#now create some folders if they have not already been created 
incoming_dir=hostdir+'/diarize-incoming/'
processed_dir=hostdir+'/diarize-processed/'

try:
    os.chdir(incoming_dir)
    curdir=os.listdir()
    if 'data' not in curdir:
        #this is necessary for diarnization
        shutil.copytree(hostdir+'/pyaudioanalysis3/data/',os.getcwd()+'/data/')
except:
    os.mkdir(incoming_dir)
    os.chdir(incoming_dir)
    curdir=os.listdir()
    if 'data' not in curdir:
        #this is necessary for diarization 
        shutil.copytree(hostdir+'/pyaudioanalysis3/data/',os.getcwd()+'/data/')

try:
    os.chdir(processed_dir)
except:
    os.mkdir(processed_dir)

#change to incoming directory to look for samples
os.chdir(incoming_dir)

#initialize sleep time for worker (default is 1 second)
sleeptime=1

# now initialize process list with files already in the directory
processlist=os.listdir()
convertformat_list=list()

#error counts will help us debug later
errorcount=0
processcount=0

#initialize t for infinite loop
t=1

#infinite loop for worker now begins with while loop...

while t>0:

    #go to incoming directory
    os.chdir(incoming_dir)
    listdir=os.listdir()
    print(listdir)

    #try statement to avoid errors
    try:
        if listdir==['.DS_Store'] or listdir == ['data'] or listdir==['data','.DS_Store'] or listdir==[]:
            #pass if no files are processible
            print('no files found...')
        
        else:
            #look for any files that have not been previously in the directory
            for i in range(len(listdir)):
                if listdir[i]=='.DS_Store' or listdir[i]=='data':
                    pass
                
                else:
                    #convert format if not .wav
                    if listdir[i][-4:] != '.wav':
                        filename=convertformat(listdir[i])
                        os.remove(listdir[i])
                    else:
                        filename=listdir[i]
                    
                    #log start time for later 
                    start_time=time.time()
                    
                    if filename not in processlist:
                        print('processing '+filename)
                        processlist.append(listdir[i])
                        filesize=os.path.getsize(filename)
                    
                        if filesize > int(500):
                            #if over 20 minute of audio collected (10.580MB), assume 2 speakers 

                            shutil.copy(incoming_dir+filename,hostdir+'/pyaudioanalysis3/data/'+filename)
                        
                            g=aS.speakerDiarization(filename,2,mtSize=2.0,mtStep=0.2,stWin=0.05,LDAdim=35, PLOT=False)

                            s0seg=list()
                            s1seg=list()
                            allseg=list()

                            for i in range(len(g)-1):
                                if i==0:
                                    start=i/5.0
                                else:
                                    if g[i]==g[i+1]:
                                        pass
                                        #continue where left off to find start length, 20 milliseconds 
                                    else:
                                        if g[i+1]==0:
                                            end=i/5.0
                                            s1seg.append([start,end])
                                            allseg.append([0,[start,end]])
                                            start=(i+1)/5.0
                                            
                                        elif g[i+1]==1:
                                            end=i/5.0
                                            s0seg.append([start,end])
                                            allseg.append([1, [start,end]])
                                            start=(i+1)/5.0
                                                
                                        else:
                                            print('error')

                            #now save this data in individual segments
                            newAudio = AudioSegment.from_wav(filename)
                            diarizedir=os.getcwd()+'/'+filename[0:-4]+'_diarization'

                            try:
                                os.mkdir(diarizedir)
                                os.chdir(diarizedir)
                            except:
                                os.chdir(diarizedir)

                            #copy file to this directory and delete from other directory
                            shutil.move(incoming_dir+filename,os.getcwd()+'/'+filename)

                            #diarize speaker 1 
                            print('diarizing speaker 1')
                            curdir=os.getcwd()
                            newdir1=curdir+'/1'

                            try:
                                os.mkdir(newdir1)
                                os.chdir(newdir1)
                            except:
                                os.chdir(newdir1)
                                
                            for i in range(len(s0seg)):
                                filename2=filename[0:-4]+'_speaker_1'+str(i)+'.wav'
                                print(('making file @ %s to %s')%(str(s0seg[i][0]),str(s0seg[i][1])))
                                exportfile(newAudio,s0seg[i][0]*1000,s0seg[i][1]*1000,filename,i,1)

                            curdir=os.getcwd()
                            listdir=os.listdir(curdir)
                            removedfilelist1=list()
                            keptfilelist1=list()

                            for i in range(len(listdir)):
                                if os.path.getsize(listdir[i]) < 300000:
                                    removedfile=[listdir[i], os.path.getsize(listdir[i])]
                                    removedfilelist1.append(removedfile)
                                    os.remove(listdir[i])
                                else:
                                    keptfile=[listdir[i],os.path.getsize(listdir[i])]
                                    keptfilelist1.append(keptfile)

                            #speaker 1 stitched size
                            s1stitchedsize=0
                            for i in range(len(keptfilelist1)):
                                s1stitchedsize=s1stitchedsize+int(keptfilelist1[i][1])
                                
                            #speaker 2 
                            os.chdir(diarizedir)
                            curdir=os.getcwd()
                            newdir2=curdir+'/2'

                            try:
                                os.mkdir(newdir2)
                                os.chdir(newdir2)
                            except:
                                os.chdir(newdir2)
                                
                            print('diarizing speaker 2')
                            for i in range(len(s1seg)):
                                filename2=filename[0:-4]+'_speaker_2'+str(i)+'.wav'
                                print(('making file @ %s to %s')%(str(s1seg[i][0]),str(s1seg[i][1])))
                                exportfile(newAudio,s1seg[i][0]*1000,s1seg[i][1]*1000,filename,i,2)

                            curdir=os.getcwd()
                            listdir=os.listdir(curdir)
                            removedfilelist2=list()
                            keptfilelist2=list()

                            ##now delete files that are less than 300 KB 
                            for i in range(len(listdir)):
                                if os.path.getsize(listdir[i]) < 300000:
                                    removedfile=[listdir[i], os.path.getsize(listdir[i])]
                                    removedfilelist2.append(removedfile)
                                    os.remove(listdir[i])
                                else:
                                    keptfile=[listdir[i],os.path.getsize(listdir[i])]
                                    keptfilelist2.append(keptfile)

                            #speaker 2 stitched size
                            s2stitchedsize=0
                            for i in range(len(keptfilelist2)):
                                s2stitchedsize=s2stitchedsize+int(keptfilelist2[i][1])

                            # all segments 
                            os.chdir(diarizedir)
                            curdir=os.getcwd()
                            newdir3=curdir+'/all'

                            try:
                                os.mkdir(newdir3)
                                os.chdir(newdir3)
                            except:
                                os.chdir(newdir3)

                            print('transcribing session')
                            master_transcript=open('transcript.txt','w')

                            for i in range(len(allseg)):
                                print(('making file @ %s to %s')%(str(allseg[i][1][0]),str(allseg[i][1][1])))
                                filename2=str(i)+'_'+str(allseg[i][0])+'.wav'
                                filename2=exportfile(newAudio,allseg[i][1][0]*1000,allseg[i][1][1]*1000,filename,i,2)
                                new_filename=str(i)+'_'+str(allseg[i][0])+'.wav'
                                os.rename(filename2,new_filename)
                                os.system('ffmpeg -i %s -ac 1 -acodec pcm_s16le -ar 16000 %s -y'%(new_filename,new_filename))

                                if i == 0:
                                    speaker='102334'

                                try:
                                    try:
                                        transcript=transcribe_audio_google(new_filename)
                                    except:
                                        transcript=transcribe_audio_sphinx(new_filename)

                                    if str(allseg[i][0]) != speaker:
                                        speaker=str(allseg[i][0])
                                        master_transcript.write('\n\nspeaker %s: %s '%(str(allseg[i][0]), transcript))
                                        print('\n\nspeaker %s: %s '%(str(allseg[i][0]), transcript))
                                    else:
                                        speaker=str(allseg[i][0])
                                        master_transcript.write('%s'%(transcript))
                                        print(transcript)
                                        
                                except:
                                    print('failed transcript')

                            master_transcript.close()
                            transcript=open('transcript.txt').read()

                            #calculate processing time
                            end_time=time.time()
                            processtime=end_time-start_time 

                            #this is the .json serializable diarization
                            os.chdir(diarizedir)
                            
                            data={
                                'filename':filename,
                                'file location':diarizedir,
                                'file size':filesize,
                                'processing time':processtime,
                                'processcount':processcount,
                                'errorcount':errorcount,
                                'data':list(g),
                                'master transcript': transcript,
                                'allseg': allseg,
                                'speaker 1':s0seg,
                                'speaker 2':s1seg,
                                'speaker 1 kept segments':keptfilelist1,
                                'speaker 1 stitched size':s1stitchedsize,
                                'speaker 1 folder location':newdir1,
                                'speaker 2 kept segments':keptfilelist2,
                                'speaker 2 stitched size':s2stitchedsize,
                                'speaker 2 folder location':newdir2,
                                'speaker 1 deleted segments':removedfilelist1,
                                'speaker 2 deleted segments':removedfilelist2,
                                }

                            #write to json 
                            os.chdir(diarizedir)
                            with open(filename[0:-4]+'.json', 'w') as f:
                                json.dump(data, f)
                            f.close()

                            #read the db
                            g=json.loads(open(filename[0:-4]+'.json').read())
                            keptlist1=g['speaker 1 kept segments']
                            keptloc1=g['speaker 1 folder location']
                            filelist1=list()
                            for i in range(len(keptlist1)):
                                filelist1.append(str(keptlist1[i][0]))

                            keptlist2=g['speaker 2 kept segments']
                            keptloc2=g['speaker 2 folder location']
                            filelist2=list()
                            for i in range(len(keptlist2)):
                                filelist2.append(str(keptlist2[i][0]))

                            #save stitch to locations where segments are 
                            os.chdir(keptloc1)
                            try:
                                print('stitching to location 1: ' + keptloc1)
                                print(filelist1)
                                stitchtogether(filelist1,keptloc1,'stitched_1.wav')
                            except:
                                print('error stitching 1')

                            #save stitch to locations where segments are
                            os.chdir(keptloc2)
                            try:
                                print('stiching to location 2: ' + keptloc2)
                                print(filelist2)
                                stitchtogether(filelist2,keptloc2,'stitched_2.wav')
                            except:
                                print('error stitching 2')
                                
                            #go back to the incoming dir folder for further processing 
                            os.chdir(incoming_dir)

                            #zip the entire directory into a .zip file and move to processed_dir folder
                            shutil.make_archive(filename[0:-4]+'_diarization','zip',filename[0:-4]+'_diarization/')                            
                            shutil.move(incoming_dir+filename[0:-4]+'_diarization.zip',processed_dir+filename[0:-4]+'_diarization.zip')

                            #delete the directory using shutil
                            shutil.rmtree(filename[0:-4]+'_diarization')

                            #update processcount
                            processcount=processcount+1

                        else:
                            errorcount=errorcount+1
                            os.remove(filename)
                            print('skipping file, need to resample (too small size)')
                            
            #sleep to avoid server overhead
            print('sleeping...')
            time.sleep(sleeptime)
    except:
        print('error')
        print('sleeping...')
        errorcount=errorcount+1
        time.sleep(sleeptime)
