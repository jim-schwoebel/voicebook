'''
================================================ 
##            VOICEBOOK REPOSITORY            ##      
================================================ 

repository name: voicebook 
repository version: 1.0 
repository link: https://github.com/jim-schwoebel/voicebook 
author: Jim Schwoebel 
author contact: js@neurolex.co 
description: a book and repo to get you started programming voice applications in Python - 10 chapters and 200+ scripts. 
license category: opensource 
license: Apache 2.0 license 
organization name: NeuroLex Laboratories, Inc. 
location: Seattle, WA 
website: https://neurolex.ai 
release date: 2018-09-28 

This code (voicebook) is hereby released under a Apache 2.0 license license. 

For more information, check out the license terms below. 

================================================ 
##               LICENSE TERMS                ##      
================================================ 

Copyright 2018 NeuroLex Laboratories, Inc. 

Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 

     http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License. 

================================================ 
##               SERVICE STATEMENT            ##        
================================================ 

If you are using the code written for a larger project, we are 
happy to consult with you and help you with deployment. Our team 
has >10 world experts in Kafka distributed architectures, microservices 
built on top of Node.js / Python / Docker, and applying machine learning to 
model speech and text data. 

We have helped a wide variety of enterprises - small businesses, 
researchers, enterprises, and/or independent developers. 

If you would like to work with us let us know @ js@neurolex.co. 

================================================ 
##                 AUDIO_PLOT.PY              ##    
================================================ 

A simple function to plot a spectrogram with librosa.
'''
import librosa, os
import matplotlib.pyplot as plt
import numpy as np
import librosa.display

# now begin plotting linear-frequency power spectrum 
def plot_spectrogram(filename):
	y, sr = librosa.load(filename)
	plt.figure(figsize=(12, 8))
	D = librosa.amplitude_to_db(librosa.stft(y), ref=np.max)
	plt.subplot(4, 2, 1)
	librosa.display.specshow(D, y_axis='linear')
	plt.colorbar(format='%+2.0f dB')
	plt.title('Linear-frequency power spectrogram')

	# on logarithmic scale 
	plt.subplot(4, 2, 2)
	librosa.display.specshow(D, y_axis='log')
	plt.colorbar(format='%+2.0f dB')
	plt.title('Log-frequency power spectrogram')

	# Or use a CQT scale
	CQT = librosa.amplitude_to_db(librosa.cqt(y, sr=sr), ref=np.max)
	plt.subplot(4, 2, 3)
	librosa.display.specshow(CQT, y_axis='cqt_note')
	plt.colorbar(format='%+2.0f dB')
	plt.title('Constant-Q power spectrogram (note)')
	plt.subplot(4, 2, 4)
	librosa.display.specshow(CQT, y_axis='cqt_hz')
	plt.colorbar(format='%+2.0f dB')
	plt.title('Constant-Q power spectrogram (Hz)')

	# Draw a chromagram with pitch classes
	C = librosa.feature.chroma_cqt(y=y, sr=sr)
	plt.subplot(4, 2, 5)
	librosa.display.specshow(C, y_axis='chroma')
	plt.colorbar()
	plt.title('Chromagram')

	# Force a grayscale colormap (white -> black)
	plt.subplot(4, 2, 6)
	librosa.display.specshow(D, cmap='gray_r', y_axis='linear')
	plt.colorbar(format='%+2.0f dB')
	plt.title('Linear power spectrogram (grayscale)')

	# Draw time markers automatically
	plt.subplot(4, 2, 7)
	librosa.display.specshow(D, x_axis='time', y_axis='log')
	plt.colorbar(format='%+2.0f dB')
	plt.title('Log power spectrogram')

	# Draw a tempogram with BPM markers
	plt.subplot(4, 2, 8)
	Tgram = librosa.feature.tempogram(y=y, sr=sr)
	librosa.display.specshow(Tgram, x_axis='time', y_axis='tempo')
	plt.colorbar()
	plt.title('Tempogram')
	plt.tight_layout()

	# # Draw beat-synchronous chroma in natural time
	# plt.figure()
	# tempo, beat_f = librosa.beat.beat_track(y=y, sr=sr, trim=False)
	# beat_f = librosa.util.fix_frames(beat_f, x_max=C.shape[1])
	# Csync = librosa.util.sync(C, beat_f, aggregate=np.median)
	# beat_t = librosa.frames_to_time(beat_f, sr=sr)
	# ax1 = plt.subplot(2,1,1)
	# librosa.display.specshow(C, y_axis='chroma', x_axis='time')
	# plt.title('Chroma (linear time)')
	# ax2 = plt.subplot(2,1,2, sharex=ax1)
	# librosa.display.specshow(Csync, y_axis='chroma', x_axis='time',
	#                           x_coords=beat_t)
	# plt.title('Chroma (beat time)')
	# plt.tight_layout()

	# image file save
	imgfile=filename[0:-4]+'.png'
	plt.savefig(imgfile)
	os.system('open %s'%(imgfile))

	return imgfile 

