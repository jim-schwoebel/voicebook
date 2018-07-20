'''
record_transcribe.py
'''
import transcribe as ts
import sounddevice as sd
import soundfile as sf

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

# record a test file 
sync_record('test.wav', 10, 44100, 2)

# fetch a google transcript (note: you need environment vars setup)
try:
    google_transcript=ts.transcribe_google('test.wav')
except:
    print('do not have proper environment variables setup') 

# transcribe with pocketsphinx
sphinx_transcript=ts.transcribe_sphinx('test.wav')

# transcribe with deepspeech (can be CPU intensive)
deepspeech_transcript=ts.transcribe_deepspeech('test.wav')

# record a sample file and transcribe using all transcription methods
# then, output all the transcripts into a jsonfile ('test.json') 
jsonfile=ts.transcribe_all('test.wav')
