'''
text_freqplot.py

Plot the most frequent words from highest to lowest in a session.

This is best done using NLTK.

Transcriptions can happen with pocketsphinx 
'''

####################################################
##              IMPORT STATEMENTS                 ## 
####################################################
import os, json, shutil
from nltk import FreqDist
import speech_recognition as sr_audio
import sounddevice as sd
import soundfile as sf 

####################################################
#           HELPER FUNCTIONS                      ##
####################################################
def transcribe_pocket(filename):
    # transcribe the audio (note this is only done if a voice sample)
    try:
        r=sr_audio.Recognizer()
        with sr_audio.AudioFile(filename) as source:
            audio = r.record(source) 
        text=r.recognize_sphinx(audio)
    except:
        text=''
        
    return text

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

# record a 30 second sample and receive a plot 
if 'freqplot.wav' not in os.listdir():
    sync_record('freqplot.wav',30, 44100, 1)
    
transcript=transcribe_pocket('freqplot.wav')
g=transcript.split()
fd=FreqDist(g)
fd.plot()
