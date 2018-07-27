'''
generate_filtered.py

Quickly manipulate the audio file to create machine-generated audio with
filters.

Librosa has some handy filters for this that makes it quite easy for mono
audio.
'''
import librosa, os 
import soundfile as sf
import numpy as np 

os.chdir(os.getcwd()+'/data/')
curdir=os.getcwd()
wavfile=input('what is the name of the wav file (in ./data/ dir) you would like to manipulate?\n')

# load noise file and make 10 seconds 
y1, sr1 = librosa.load('beep.wav')
y1=np.append(y1,y1)
y1=np.append(y1,y1)
y1=np.append(y1,y1)
y1=np.append(y1,y1)
y1=np.append(y1,y1)

# load file 
y, sr = librosa.load(wavfile)
  
# time stretch (1/4 speed)
y_slow = librosa.effects.time_stretch(y, 0.50)

# pitch down very deep
y_low = librosa.effects.pitch_shift(y, sr, n_steps=-6)

# add noise to first 10 seconds
for i in range(len(y1)):
    y[i]=y[i]+y1[i]

y_noise=y

librosa.output.write_wav(curdir+'/'+wavfile[0:-4]+'_slow.wav',y_slow, sr)
librosa.output.write_wav(curdir+'/'+wavfile[0:-4]+'_lowpitch.wav',y_low, sr)
librosa.output.write_wav(curdir+'/'+wavfile[0:-4]+'_noise.wav',y_noise, sr)
