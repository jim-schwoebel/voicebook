'''
transcribe_custom.py

Record a short sample and get back a transcription in a loop.

This is to just show how to load a custom transcription model
inside of pocketsphinx. 
'''
import os, sys
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
import sounddevice as sd
import soundfile as sf

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

# Get all the directories right
def transcribe(sample):

    modeldir=os.getcwd()+'/data'
    # Create a decoder with certain model
    config = Decoder.default_config()
    config.set_string('-hmm', modeldir+'/en-us')
    config.set_string('-lm', modeldir+'/TAR4311/4311.lm')
    config.set_string('-dict', modeldir+'/TAR4311/4311.dic')
    decoder = Decoder(config)

    # Decode streaming data.
    decoder = Decoder(config)
    decoder.start_utt()
    stream = open(sample, 'rb')
    while True:
      buf = stream.read(1024)
      if buf:
        decoder.process_raw(buf, False, False)
      else:
        break
    decoder.end_utt()

    #print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])
    output=[seg.word for seg in decoder.seg()]
    try:
        output.remove('<s>')
        output.remove('</s>')

        transcript = ''
        for i in range(len(output)):
            if output[i] == '<sil>':
                pass 
            elif i == 0:
                transcript=transcript+output[i]
            else:
                transcript=transcript+' '+output[i]

        transcript=transcript.lower()
        print('transcript: '+transcript)
    except:
        transcript=''

    return transcript

t=1
i=0

while t>0:
    sync_record('test.wav',3,16000,1)
    transcribe('test.wav')
