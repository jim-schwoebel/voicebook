'''
Read_write_audio.py

Read and write audio files with various libraries in python.
'''

from pydub import AudioSegment
data = AudioSegment.from_wav("test.wav")
data.export("new_test.wav")

import wave
data=wave.open('test.wav', mode='rb')
params=data.getparams()
# _wave_params(nchannels=1, sampwidth=2, framerate=16000, nframes=47104, comptype='NONE', compname='not compressed')

import librosa
y, sr = librosa.load('test.wav')
librosa.output.write_wav('new_test.wav', y, sr)

from scipy.io import wavfile
fs, data = wavfile.read('test.wav')
wavfile.write('new_test.wav',fs, data)

import soundfile as sf
data, fs = sf.read('test.wav')
sf.write('new_test.ogg', data, fs)
