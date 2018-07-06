from kafka import KafkaConsumer, KafkaProducer

#dependency modules 
import json, os, sys, shutil, getpass, time, requests, getpass, time, requests, random
import numpy as np
from ftplib import FTP

#get incoming and outgoing topic, create producer on server
incoming_topic = 'incoming_samples'
outgoing_topic = 'outgoing_samples'
bootstrap_servers = ['localhost:9092']

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

#testmode - put True if testing, False if production
testmode=True 

#define some functions 
def internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
        return False

def getclass(inputlist):
    #for later, get the results of models 
    array=inputlist[1].tolist()
    maxval=np.max(array)
    index=array.index(maxval)
    choices=inputlist[2]
    #output choice
    return choices[index]

#get current directory listing in /usr/app/lib folder 
listdir=os.listdir(os.getcwd())

#create folders for incoming and outgoing samples 
if 'nlx-model-incoming_samples' not in listdir:
    os.mkdir('nlx-model-incoming_samples')

if 'nlx-model-processed_samples' not in listdir:
    os.mkdir('nlx-model-processed_samples')

#sleep until internet connection is established if it does not exist (so code does not crash if somehow server goes offline)
if internet()==False:
    while internet()==False:
        print('internet connection does not exist')
        time.sleep(1)

#now go to this directory (/usr/app/pyAudioAnalysis3 folder)
os.chdir(os.getcwd()[0:-3]+'/pyAudioAnalysis3')
sys.path.append(os.getcwd())
modeldir=os.getcwd()+'/models/audiomodels'
            
#now load the right module from pyAudioAnalysis3 
import audioTrainTest as aT

#now move these test transcripts and test audio files into the right folder
if testmode==True:
    #obtain test audio file (test.wav) and transcript (test.txt)
    audiofile='test.wav'
    textfile='test.txt'
    transcript=open('test.txt','w')
    transcript.write('this is a dummy test transcript. It really does not matter what goes in here.')
    transcrit.close()
    try:
        shuil.copy(listdir[0:-3]+'/pyAudioAnalysis3/models/audiomodels/test.wav',listdir+'/nlx-model-incoming_samples/test.wav')
        shuil.copy(listdir[0:-3]+'/pyAudioAnalysis3/test.txt',listdir+'/nlx-model-incoming_samples/test.txt')
        #move to process
        testmode==False
    except:
        print('error moving test samples, looking for files in nlx-model-incoming_samples folder...')
        #move to process
        testmode==False
        
elif testmode==False:
    try:
        os.chdir(listdir+'lib/nlx-model-incoming_samples/')
        dirlist=os.listdir(os.getcwd())
        if len(dirlist)>3:
            random.shuffle(dirlist)
            while dirlist[0][-4:] not in ['.wav','.txt']:
                random.shuffle(dirlist)

            #get audio and text file 
            audiofile=dirlist[0][0:-4]+'.wav'
            textfile=dirlist[0][0:-4]+'.txt'

            #error handling for later 
            if audiofile not in dirlist and textfile in dirlist:
                print('text file found but no audio file found')
                #fetch audio file from db and download 
            if textfile not in dirlist and audiofile in dirlist:
                print('no transcript found')
                #send audio file to NLX-transcribe and get transcript
        else:
            print('no files in queue')

    except:
        print('error getting sample to process')
        
#Ensure in the directory that can run the files 
os.chdir(listdir+'/nlx-model-incoming_samples/')

#AUDIO models
print('fingerprinting %s with audio machine learning models.'%(audiofile))

try:
    gender=aT.fileClassification(audiofile,modeldir+"/genderymodel","svm")
    gender=getclass(gender.lower())
    print(gender)
except:
    gender='n/a'
    print('error applying gender model')

try:
    age=aT.fileClassification(audiofile, modeldir+'/childrenvscontrol2model","svm")
    age=getclass(age)
    if age=='control2':
        age='adult'
    print(age)
except:
    age='n/a'
    print('error applying age model')

try:
    sampletype=aT.fileClassification(audiofile, modeldir+'/ambilexmodel',"svm")
    sampletype=getclass(sampletype)
    print(sampletype)
except:
    sampletype='n/a'
    print('error applying sampletype model')

try:
    speaktype=aT.fileClassification(audiofile, modeldir+'/speaktypelex',"svm")
    speaktype=getclass(speaktype)
    print(speaktype)
except:
    speaktype='n/a'
    print('error applying speaktype model')

try:
    silence=aT.fileClassification(audiofile, modeldir+'/voicevssilencemodel',"svm")
    silence=getclass(silence)
    print(silence)
except:
    silence='n/a'
    print('error applying silence model')
 
try:
    race=aT.fileClassification(audiofile, modeldir+'/aajamesmodel',"svm")
    race=getclass(race)
    if race=='controls':
      race='caucasian'
    print(race)
except:
    race='n/a'
    print('error applying race model')

try:
    dialect=aT.fileClassification(audiofile, modeldir+'/britishvsamericanmodel',"svm")
    dialect=getclass(dialect)
    print(dialect)
except:
    dialect='n/a'
    print('error applying dialect model')

try:
    happysad=aT.fileClassification(audiofile, modeldir+'/happyvssad',"svm")
    happysad=getclass(happysad)
    print(happysad)
except:
    happysad='n/a'
    print('error applying happy-sad model')

try:
    stress=aT.fileClassification(audiofile, modeldir+'/stresslex',"svm")
    stress=getclass(stress)
    print(stress)
except:
    stress='n/a'
    print('error applying stress model')

try:
    fatigue=aT.fileClassification(audiofile, modeldir+'/fatiguelex',"svm")
    fatigue=getclass(fatigue)
    print(fatigue)
except:
    fatigue='n/a'
    print('error applying fatigue model')

#TEXT models
print('fingerprinting %s with text machine learning models.'%(textfile))
#n/a - will be here in future 

#DELETE FILES FROM QUEUE - (in the while loop it would be the files processed with same name)
os.remove(audiofile)
os.remove(textfile)

#now run CMD to classify all the samples and
try:
    os.chdir(listdir+'/nlx-model-processed_samples')
    
    data={
        'survey name':'test',
        #name of survey as created on website 
        'sample id':'test', 
        #id # from survey, in chronological order
        'sampletype':sampletype,
        #music, mouse click, keyboard, music, noise
        'speaktype':speaktype,
        #natural or non-natural
        'silence':silence,
        #silence vs. voice 
        'age':age,
        #child or adult (ML model, audio)
        'gender':gender,
        #male or female (ML model, audio)
        'language':'n/a',
        #english vs. foreign (ML model, audio)
        'education level':'n/a',
        #Ph.D.,BSE, etc. 
        'dialect':dialect,
        #british vs. american
        'ethnicity':race,
        #african american vs. caucasian (ML model, audio)
        'mood': happysad,
        #happy | sad (ML model, audio)
        'stress level': stress,
        #stressed vs. not stressed
        'fatigue level':fatigue,
        #fatigued vs. non-fatigued 
        'noise':'n/a',
        #indoor vs. outdoor (ML model, audio)
        'location': 'n/a',
        #location from IP address
        'transcript':transcript,
        #from NLX-transcribe
        }

    jsonfile=open(audiofile[0:-4]+'_models.json','w')
    json.dump(data,jsonfile)
    jsonfile.close()
    
    # Convert the image to bytes and send to kafka (finished)
    producer.send(incoming_topic, b'nlx-1')
    # To reduce CPU usage create sleep time of 0.2sec
    time.sleep(0.2)

except:
    print('error writing json file')
    # Convert the image to bytes and send to kafka (error)
    producer.send(incoming_topic, b'error, nlx-1')
    
