'''
trim_silence.py

Trim leading and trailing silence from sample 
'''
import os

def trim_silence(filename):
	new_filename=filename[0:-4]+'_trimmed.wav'
	command='sox %s %s silence -l 1 0.1 1'%(filename, new_filename)+"% -1 2.0 1%"
	os.system(command)
	return new_filename

	# trim the leading and trailing silence => (test_trimmed.wav)
trim_silence('test.wav')