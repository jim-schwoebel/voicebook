'''
trim_audio.py

Trim an audio file in seconds from start and stop point.
'''
import os

def trim_audio(filename, start, end):
	clip_duration=end-start 
	new_filename=filename[0:-4]+'_trimmed_'+str(start)+'_'+str(end)+'.wav'
	command='sox %s %s trim %s %s'%(filename,new_filename,str(start),str(clip_duration))
	os.system(command)
	return new_filename

# trim the first 10 seconds of clip => (test_trimmed_0_10.wav)
trim_audio('test.wav', 0, 10)
# trim from second 30 to 40 => (test_trimmed_30_40.wav)
trim_audio('test.wav', 30, 40)

