import sounddevice as sd
import soundfile as sf
import time 

def printstuff(number):
    for i in range(number):
         print(i)

def async_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    # can execute commands 
    print('able to execute this before finishing')
    printstuff(30)
    # now wait until done before writing to file 
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

# playback file 
async_record('async_record.wav', 10, 16000, 1)
