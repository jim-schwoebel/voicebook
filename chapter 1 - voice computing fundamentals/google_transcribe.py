import speech_recognition as sr_audio
import sounddevice as sd
import soundfile as sf
import os, json, datetime

def transcribe_audio_google(filename):
    # transcribe the audio (note this is only done if a voice sample)
    r=sr_audio.Recognizer()
    with sr_audio.AudioFile(filename) as source:
        audio = r.record(source) 
    text=r.recognize_google_cloud(audio)

    return text    

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

def store_transcript(filename, transcript):
    jsonfilename=filename[0:-4]+'.json'
    print('saving %s to current directory'%(jsonfilename))
    data = {
        'date': str(datetime.datetime.now()),
        'filename':filename,
        'transcript':transcript,
        }
    print(data)
    jsonfile=open(jsonfilename,'w')
    json.dump(data,jsonfile)
    jsonfile.close()

# record file and print transcript
filename='google_record.wav'
sync_record(filename, 10, 16000, 1)
transcript=transcribe_audio_google(filename)

# now write the transcript into a .json file
# e.g. sync_record.wav transcript will be stored in sync_record.json
store_transcript(filename, transcript)
