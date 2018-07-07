'''

Transcribe google

Very simple script to transcribe using google transcription.

Assumes environment variables exist:

export GOOGLE_APPLICATION_CREDENTIALS='/Users/jimschwoebel/Desktop/appcreds/NLX-infrastructure-b9201d884ea5.json'

'''

import json, sys, os, time
import speech_recognition as sr_audio

def transcribe_audio(wavfile):
    try:
        r = sr_audio.Recognizer()
        # use wavfile as the audio source (must be .wav file)
        with sr_audio.AudioFile(wavfile) as source:
            # extract audio data from the file
            audio = r.record(source)                    
    
        transcript=r.recognize_google_cloud(audio)
    except:
        print('error')
        transcript=''

    return transcript 

start=time.time()
# arguments passed through program
# so you should pass through the directory and wavfile name
directory = sys.argv[1]
wavfile = sys.argv[2]
sampleid = wavfile[0:-4]+'.json'

print(directory)
print(wavfile)

# go to designated directory
os.chdir(directory) 

# remove transcribe.json if it exists in the current directory 
try:
    os.remove(sampleid)
except:
    pass

# now transcribe the file and dump to transcript
os.system('ffmpeg -i %s -ac 1 -acodec pcm_s16le -ar 16000 %s_mono.wav'%(wavfile, wavfile[0:-4]))
transcript=transcribe_audio(wavfile[0:-4]+'_mono.wav')

data = {
    'transcript':transcript
    }

jsonfile=open(sampleid,'w')
json.dump(data,jsonfile)
os.remove(wavfile[0:-4]+'_mono.wav')