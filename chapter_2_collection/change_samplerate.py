'''
change_samplerate.py

Use SoX to change samplerate of an audio file
'''
import os

def change_samplerate(filename, samplerate):
    new_filename=filename[0:-4]+'_sr'+str(samplerate)+'.wav
    new_samplerate=str(int(samplerate/1000))
    os.system('sox %s -r %sk %s'%(filename, new_samplerate, new_filename))
    return new_filename

change_samplerate('test.wav',48000)
