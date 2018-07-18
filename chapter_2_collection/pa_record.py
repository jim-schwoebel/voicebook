'''
ps_record.py

quick example illustrating passive-synchronous mode (PS mode).

Record a 2 second audio sample in background every 10 seconds. 

Do this for 10 iterations. 

It's a blocking example, meaning no other code can run when 
the code is recording a sample.
'''
import sounddevice as sd
import soundfile as sf 
import time, os, shutil, psutil 

# define synchronous recording function (did this is Chapter 1)
def get_battery():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    return percent 

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    print('battery is currently at %s'%get_battery())
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

# make a folder to put recordings in 
try:
    os.mkdir('recordings')
    os.chdir(os.getcwd()+'/recordings')
except:
    shutil.rmtree('recordings')
    os.mkdir('recordings')
    os.chdir(os.getcwd()+'/recordings')
    
i=0

# loop through 10 times recoridng a 2 second sample 
# can change to infinite loop ==> while i > -1: 
while i<10:
    # record a mono file synchronously
    filename=str(i+1)+'.wav'
    print('recording %s'%(filename))
    sync_record(filename, 2, 16000, 1)
    time.sleep(10)
    i=i+1

    
    
