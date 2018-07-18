'''
change_channels.py

Functions for some audio manipulation 
'''
import os

def stereo2mono(filename):
    #Change stereo to mono 
    new_filename=filename[0:-4]+'_mono.wav'
    os.system('sox %s %s remix 1-2'%(filename,new_filename))
    return new_filename

def separate_channels(filename):
    #Change stereo to two mono files (mix-down)
    channel_1=filename[0:-4]+'_1.wav'
    channel_2=filename[0:-4]+'_2.wav'
    os.system('sox %s %s remix 1'%(filename, channel_1))
    os.system('sox %s %s remix 2'%(filename, channel_2))
    return channel_1, channel_2
    
def multiplex(channel_1, channel_2):
    #Convert two mono files into one stereo file (multiplexing)
    output=channel_1[0:-4]+'_'+channel_2[0:-4]+'.wav'
    os.system('sox -M %s %s %s'%(channel_1,channel_2,output))
    return output

stereo2mono('stereo.wav')
separate_channels('stereo.wav')
multiplex('stereo_1.wav','stereo_2.wav')
