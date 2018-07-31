'''
wake_transcribe.py

Use asynchronous transcription as a wakeword detector.
'''
import soundfile as sf
import sounddevice as sd
import speech_recognition as sr_audio
import pyttsx3 
import os, time

# transcribe with pocketsphinx (open-source)
def speak():
    engine = pyttsx3.init()
    engine.say("hello!!")
    engine.runAndWait() 

def find_wake(transcript, hotwords):
    for i in range(len(hotwords)):
##        print(transcript)
##        print(transcript.lower().find(hotwords[i]))
        if transcript.lower().find(hotwords[i])>=0:
            print('%s wakeword found!!'%(hotwords[i].upper()))
            speak()
            break 
        
def transcribe_sphinx(file):
    try:
        r=sr_audio.Recognizer()
        with sr_audio.AudioFile(file) as source:
            audio = r.record(source) 
        transcript=r.recognize_sphinx(audio)
        print('sphinx transcript: '+transcript)
    except:
        transcript=''
        print(transcript)
        
    return transcript 

def async_record(hotwords, filename, filename2, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    transcript=transcribe_sphinx(filename2)
    find_wake(transcript, hotwords)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

# initial parameters
hotwords=['test', 'testing']
i=0
t=1
filename2='n/a'
# create infinite loop
while t>0:
    # record a mono file asynchronous, transcribe, and fine wakeword 
    filename=str(i+1)+'.wav'
    async_record(hotwords, filename, filename2, 3, 16000, 1)
    filename2=filename 
    i=i+1
    try:
        os.remove(str(i-2)+'.wav')
    except:
        pass
