'''
Transcribe.py

Simple script to transcribe audio using PocketSphinx and Speech Recognition.

Note that we can use free transcription engines for free accounts, limiting
the first 3 samples to be google and rest crappier transcriptions :)

To call the program, all you need to do in the terminal:

python3 transcribe.py /usr/src/app/tests/ test_mono_16000.wav

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
    
        transcript=r.recognize_sphinx(audio)
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
transcript=transcribe_audio(wavfile)

data = {
    'transcript':transcript
    }

jsonfile=open(sampleid,'w')
json.dump(data,jsonfile)
jsonfile.close()

#print(time.time()-start)
#print(transcript)
#print(os.listdir())

# this transcript can now be read by other programs. As a good practice,
# remove this transcript after you read it into the kafka queue 
