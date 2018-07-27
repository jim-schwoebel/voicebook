'''
text_wordcloud.py

Plot the most frequent words from highest to lowest in a session
in the form of a wordcloud.

Done with wordcloud module here:
https://github.com/amueller/word_cloud

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
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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
    print(text)
    
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
wordcloud = WordCloud().generate(transcript)
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("wordcloud.png")
plt.show()
