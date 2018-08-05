import sounddevice as sd
import soundfile as sf
import time 

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

# playback file 
sync_record('sync_record.wav', 10, 16000, 1)
