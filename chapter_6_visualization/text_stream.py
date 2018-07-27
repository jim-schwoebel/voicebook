'''
text_stream.py

Transcribe an audio file every 1 second and then propagate it on the screen.

Do this in an asyncronous manner, as transcription can take some time.
'''
####################################################
##              IMPORT STATEMENTS                 ## 
####################################################
import os, json, shutil
import speech_recognition as sr_audio
import sounddevice as sd
import soundfile as sf 

####################################################
#           HELPER FUNCTIONS                      ##
####################################################
def transcribe_pocket(filename):
    # transcribe the audio (note this is only done if a voice sample)
    r=sr_audio.Recognizer()
    with sr_audio.AudioFile(filename) as source:
        audio = r.record(source) 
    text=r.recognize_sphinx(audio)
    
    return text

def sync_record(filename, duration, fs, channels):
    #print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    #print('done recording')

####################################################
##              MAIN SCRIPT                       ## 
####################################################

# set recording params 
duration=1
fs=44100
channels=1

try:
    os.mkdir('recordings')
    os.chdir(os.getcwd()+'/recordings')
except:
    shutil.rmtree('recordings')
    os.mkdir('recordings')
    os.chdir(os.getcwd()+'/recordings')

filenames=list()
transcripts=list()
for i in range(30):
    filename='%s.wav'%(str(i))
    sync_record(filename, duration, fs, channels)
    transcript=transcribe_pocket(filename)
    # print transcript on screen 
    print(transcript)
    filenames.append(filename)
    transcripts.append(transcript)

data={
    'filenames':filenames,
    'transcripts':transcripts
    }

jsonfile=open('recordings.json','w')
json.dump(data,jsonfile)
jsonfile.close()
    
