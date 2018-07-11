'''
Useful sox commands.
'''
import os
# take in one.wav and two.wav to make three.wav 
os.system('sox one.wav two.wav three.wav')
# take first second of one.wav and output to output.wav  
os.system('sox one.wav output.wav trim 0 1')
# make volume 2x in one.wav and output to volup.wav 
os.system('sox -v 2.0 one.wav volup.wav')
# make volume ½ in one.wav and output to voldown.wav 
os.system('sox -v -0.5 one.wav volup.wav')
# reverse one.wav and output to reverse.wav 
os.system('sox one.wav reverse.wav reverse')
# change sample rate of one.wav to 16000 Hz
os.system('sox one.wav -r 16000 sr.wav')
# change audio file to 16 bit quality
os.system('sox -b 16 one.wav 16bit.wav')
# convert mono file to stereo by cloning channels
os.system('sox one.wav -c 2 stereo.wav')
# make stereo file mono by averaging out the channels
os.system('sox stereo.wav -c 1 mono.wav')
# double speed of file 
os.system('sox one.wav 2x.wav speed 2.0')
