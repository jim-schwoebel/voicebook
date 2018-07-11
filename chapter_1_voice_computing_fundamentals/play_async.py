'''
play_async.py

Play audio files back asynchronously.

'''
import sounddevice as sd
import soundfile as sf
import time 

def async_playback(filename):
    data, fs = sf.read(filename)
    sd.play(data, fs)
    return data, fs 

# playback file 
data, fs = async_playback('play.wav')

# can execute commands 
print('able to execute this before finishing')
print('hi, this is cool!')

# can stop after 1 second playing back
time.sleep(1)
sd.stop()
print('stopped')
