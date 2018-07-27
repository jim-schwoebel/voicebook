'''
plotspectrogram.py

import library to make 
audio_spectrogram look better for book :)

Simple function to plot a spectrogram
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

