'''
combine_files.py

Combine two audio files using SoX software.
'''
import os

def combine_files(one,two):
    three=one[0:-4]+'_'+two[0:-4]+'.wav'
    os.system('sox %s %s %s'%(one,two,three))
    return three

combine_files('test1.wav','test2.wav')
