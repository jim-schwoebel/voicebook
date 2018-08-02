'''
transcribe.py

Transcribes speech through different vendors:
Google speech and/or a custom engine. 
'''
import os 
import speech_recognition as sr_audio
from nala.data.models import ps_transcribe as pst 

def transcribe_audio(filename,hostdir,transcript_type):
    # transcribe the audio according to transcript type 
    # google or sphinx (custom model) 
    #try:
    if transcript_type == 'sphinx':
        transcript=pst.transcribe(hostdir,filename)
        print('pocket: '+transcript)

    elif transcript_type == 'google':
        try:
            # try google if you can, otherwise use sphinx 
            r=sr_audio.Recognizer()
            with sr_audio.AudioFile(filename) as source:
                audio = r.record(source) 
            transcript=r.recognize_google_cloud(audio)
            print('google: '+transcript)
        except:
            print('error using google transcription, need to put API key in environment vars')
            print('defaulting to pocketsphinx...')
            r=sr_audio.Recognizer()
            with sr_audio.AudioFile(filename) as source:
                audio = r.record(source) 
            transcript=r.recognize_sphinx(audio)
            print('sphinx (failed google): '+transcript)

    else:
        # default to sphinx if not sphinx or google inputs 
        transcript=pst.transcribe(hostdir,filename)
        print('pocket: '+transcript)

    #except:
        #transcript=''


    return transcript
