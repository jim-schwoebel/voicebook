# nlx-clean
This is the NeuroLex cleaning microservice. Once an audio file is collected from NLX-collect, it is sent here to assess the signal's quality. 

![](https://media.giphy.com/media/njF0UzDcz6PuM/giphy.gif)

There are a few quality checks that are made here including: 

1. checking if the file is under a certain file size.

2. classifying the incoming audio file as voice, music, silence, or noise. 

3. converting audio files to .wav format if in another format

4. converting audio files from stereo to mono format (if applicable) 

5. silence removal (for long pauses in a session) 

6. noise reduction 

These quality checks ensure that the audio collected from the end user is clean and can be subsequently processed by our server. 

## Dependencies

Here is a list of dependencies (in requirements.txt doc):

    pymongo
    importlib
    scipy
    ffmpy
    getpass
    wave
    pydub
    librosa
    matplotlib
    numpy
    
## How to run

Go to the command prompt and type:

    cd ~
    cd nlx-clean
    python3 nlx-clean.py 
    
You will now have 2 folders: nlx-clean-incoming and nlx-clean-outgoing. These are the two streaming folders that we will use.

Now place a audio file (any format - e.g. '.wav') in the nlx-clean-incoming folder. 

The file should then be cleaned and outputted to nlx-clean-outgoing folder as a .json file and a cleaned .wav file with the same name. Here is a sample output:

> {
>   "processing time": 22.206774950027466,
>   "cleaned file size": 1411244,
>   "error count": 0,
>   "file size": 1411244,
>   "filename": "test.wav",
>   "file duration": 19.992380952380952,
>   "file incoming location": "/Users/jim/nlx-clean/nlx-clean-incoming/",
>   "silence removed": 11.269002267573695,
>   "file process location": "/Users/jim/nlx-clean/nlx-clean-processed/",
>   "processed datetime": "2018-02-28 15:12:41.230024",
>   "cleaned dfile duration": 8.7233786848072565,
>   "process worker count": 2
> }

## References

Note that much of this documentation can be used to filter and enhance signals as well. For example, stretch a file that has an improper format. This could also be a good way to get introduced to this library by reading through the documentation of these other required dependencies:

### Audio file manipulation (I/O)

* [librosa - wav write](https://librosa.github.io/librosa/ioformats.html)
* [librosa - time stretch](https://librosa.github.io/librosa/generated/librosa.effects.time_stretch.html)
* [soundfile - wav write](https://pysoundfile.readthedocs.io/en/0.9.0/)

### File conversion

* [ffmpeg](https://www.ffmpeg.org/ffmpeg-all.html)

### Noise reduction 

Note we currently use sox for noise reduction, but we could explore other libraries:

* [audiosegment](https://media.readthedocs.org/pdf/audiosegment/latest/audiosegment.pdf)
* [pysox](https://media.readthedocs.org/pdf/pysox/latest/pysox.pdf) 
* [scipy](https://docs.scipy.org/doc/scipy/reference/signal.html) 
* [adaptfilt](https://pypi.python.org/pypi/adaptfilt)
* [ffmpeg normalize](https://pypi.python.org/pypi/ffmpeg-normalize/0.5.1)

### Silence Removal 

Note we currently use [vadrtc](https://github.com/wiseman/py-webrtcvad) to splice up voice files and detect voice activity and sox for silence removal but we can explore some other libraries:

* [pydub](https://github.com/jiaaro/pydub)
* [wave](https://stackoverflow.com/questions/875476/editing-a-wav-files-using-python)
* [soundfile](https://pypi.python.org/pypi/SoundFile/0.8.1)
* [pyaudioanalysis - segmentation](https://github.com/tyiannak/pyAudioAnalysis/wiki/5.-Segmentation)
* [librosa - silence removal](https://librosa.github.io/librosa/generated/librosa.effects.trim.html)
* [vadrtc](https://github.com/wiseman/py-webrtcvad)

### Other references

* [dsp in python](http://pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/)
* [python: computing with audio](http://www.cs.bu.edu/courses/cs101b1/slides/CS101.Lect28.Python.Audio.ppt.pdf)
* [using sox from cmd](https://stackoverflow.com/questions/48414889/how-do-i-convert-a-4-channel-stereo-file-to-mono-in-python)
* [stereo2mono conversion](https://stackoverflow.com/questions/30401042/stereo-to-mono-wav-in-python)
* [silence removal](https://stackoverflow.com/questions/29547218/remove-silence-at-the-beginning-and-at-the-end-of-wave-files-with-pydub)
* [processing files with fft](https://stackoverflow.com/questions/29544563/how-to-convert-complex-numbers-back-into-normal-numbers-after-performing-fft)
* [sound filtering tutorial](https://rsmith.home.xs4all.nl/miscellaneous/filtering-a-sound-recording.html)
* [computing signal-to-noise (SNR) ratio in python](https://m.garysieling.com/blog/compute-signal-noise-ratio-audio-files-python)
* [resampling and smoothing with python](http://urinieto.com/2011/05/audio-resampling-in-python/)
* [filtering with fft](http://exnumerus.blogspot.com/2011/12/how-to-remove-noise-from-signal-using.html?m=1)
