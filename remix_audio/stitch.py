'''
Stitch.py

Stitches together all the audio and normalizes them in current directory.

Assumes segments have been cut appropriately and are the same length (e.g. 5 secs).
'''

from pydub import AudioSegment
import os, getpass, random

os.chdir(os.getcwd())
listdir=os.listdir()
random.shuffle(listdir)
t=0
for i in range(len(listdir)):
    if listdir[i][-4:]=='.wav':
        if t==0:
            soundt=AudioSegment.from_wav(os.getcwd()+'/'+listdir[i])
            sound=soundt
            t=t+1
        else:
            soundt=AudioSegment.from_wav(os.getcwd()+'/'+listdir[i])
            sound=sound+soundt
        
sound.export('remix.wav', format="wav")
os.system('ffmpeg-normalize remix.wav -o remix-normalized.wav')
