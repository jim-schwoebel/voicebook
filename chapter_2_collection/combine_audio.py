'''
combine_audio.py

Combine audio in series or in parallel using SoX CLI.
'''
import os

def combine_series(one, two):
	three=one[0:-4]+'_'+two[0:-4]+'_series.wav'
	command='sox --combine concatenate %s %s %s'%(one, two, three)
	print(command)
	os.system(command)
	return three

def combine_channels(left, right):
	mixed=left[0:-4]+'_'+right[0:-4]+'_mixed.wav'
	command='sox --combine merge %s %s %s'%(left,right,mixed)
	print(command)
	os.system(command)
	return mixed

# combine two wav files in series => (1_2_series.wav)
combine_series('1.wav', '2.wav')

# combine two wav files together in same channel (1_2_mixed.wav)
combine_channels('1.wav', '2.wav')