*This section documents all the scripts in the Chapter_6_visualization folder.*

## Visualizing audio features 
### audio streams 
audio_stream.py
```python3
import sounddevice as sd
import soundfile as sf
import random, time, librosa, os 
import numpy as np

def visualize_data(sample, minimum, maximum):
    difference=maximum-minimum
    delta=difference/10
    bar='==.==.'
    if sample <= minimum:
        # 1 bar
        output=bar
    elif minimum+delta >= sample > minimum:
        # 1 bar
        output=bar
    elif minimum+delta*2 >= sample > minimum+delta:
        # 2 bars
        output=bar*2
    elif minimum+delta*3 >= sample >= minimum+delta*2:
        # 3 bars
        output=bar*3
    elif minimum+delta*4 >= sample > minimum+delta*3:
        # 4 bars
        output=bar*4
    elif minimum+delta*5 >= sample > minimum+delta*4:
        # 5 bars
        output=bar*5
    elif minimum+delta*6 >= sample > minimum+delta*5:
        # 6 bars
        output=bar*6
    elif minimum+delta*7 >= sample > minimum+delta*6:
        # 7 bars
        output=bar*7
    elif minimum+delta*8 >= sample > minimum+delta*7:
        # 8 bards
        output=bar*8
    elif minimum+delta*9 >= sample > minimum+delta*8:
        # 9 bars
        output=bar*9
    elif maximum > sample >= minimum+delta*9:
        # 10 bars
        output=bar*10
    elif sample >= maximum:
        # 10 bars
        output=bar*10
    else:
        print(sample)
        output='error'

    # plot bars based on a min and max 
    return output[0:-1]

def record_data(filename, duration, fs, channels):
    # synchronous recording 
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    y, sr = librosa.load(filename)
    rmse=np.mean(librosa.feature.rmse(y)[0])
    os.remove(filename)
    
    return rmse*1000

# take a streaming sample and then put that data as it is being recorded
minimum=0
maximum=70
samples=list()

for i in range(100):    
    # record 20ms of data 
    sample=record_data('sample.wav',0.02, 44100, 1)
    if sample > maximum:
        maximum=sample 
        print('new max is %s'%(maximum))
    samples.append(sample)
    #print(sample)
    print(visualize_data(sample,minimum,maximum))

    # other stuff - if you'd like to sleep or generate random samples 
    # keep going streaming
    # randomize data 
    # sample=random.randint(0,30)
    #time.sleep(0.2)
samples=np.array(samples)
minval=np.amin(samples)
maxval=np.amax(samples)
print('minimum val: %s'%(str(minval)))
print('max val: %s'%(str(maxval)))
```
results in a stream like this:
```
new max is 157.97308087348938
==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==
==.==.==.==
==.==
==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==
==.==.==.==
==.==
==.==
==.==
==.==
==.==
==.==
==.==
==.==
==.==
==.==
==.==
==.==
==.==
==.==
==.==
==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==.==.==.==.==.==.==.==.==.==.==
==.==.==.==.==.==
==.==.==.==.==.==
==.==.==.==
==.==.==.==.==.==
==.==.==.==
==.==.==.==
==.==
==.==
==.==
==.==
==.==
==.==
==.==
==.==.==.==.==.==.==.==
==.==
==.==
==.==
==.==
==.==
==.==.==.==.==.==.==.==
==.==
==.==.==.==.==.==
==.==.==.==
==.==
==.==
==.==.==.==.==.==
minimum val: 0.057202301832148805
max val: 157.97308087348938
```
### audio path plots 
audio_path.py
```python3
import sounddevice as sd
import soundfile as sf
import random, time, librosa, os 
import numpy as np
import matplotlib.pyplot as plt
from drawnow import drawnow

def make_fig():
    plt.scatter(x, y)  
def record_data(filename, duration, fs, channels):
    # synchronous recording 
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    y, sr = librosa.load(filename)
    rmse=np.mean(librosa.feature.rmse(y)[0])
    os.remove(filename)
    
    return rmse*1000
# initialize plot 
plt.ion()  # enable interactivity
fig = plt.figure()  # make a figure
x = list()
y = list()
for i in range(100):    
    # record 20ms of data 
    sample=record_data('sample.wav',0.02, 44100, 1)
    x.append(i)
    y.append(sample)
    drawnow(make_fig)
plt.savefig('stream.png')
os.system('open stream.png')
```
results in an image like this:
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/stream.png)

### spectrograms 
audio_spectrograms.py
```
import librosa, os
import matplotlib.pyplot as plt
import numpy as np
import librosa.display
import audio_plot as ap 

# load file 
data_dir=os.getcwd()+'/data'
os.chdir(data_dir)
filename='Voice.wav'
imgfile=ap.plot_spectrogram(filename)
```
results in an image like this:
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/Voice.png)

### Frequency spectrums and oscillograms 
audio_plotmany.py 

results in an image like this:
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/plotmany.png)

### Spectral power density 
audio_plotspd.py 

results in an image like this:
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/plotspd.png)
### as KNN clusters 
audio_cluster.py
```python3
import os, librosa 
import scipy.io.wavfile as wav
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np 
########################################################################
##     MAIN CODE BASE    					       ##
########################################################################
os.chdir('data/samples')
listdir=os.listdir()
wavfiles=list()
for i in range(len(listdir)):
    if listdir[i][-4:]=='.wav':
        wavfiles.append(listdir[i])
wavfiles=sorted(wavfiles)
samples=list()
for i in range(len(wavfiles)):
    y, sr = librosa.core.load(wavfiles[i])
    rmse=np.mean(librosa.feature.rmse(y)[0])
    mfcc=np.mean(librosa.feature.mfcc(y)[0])
    samples.append(np.array([rmse, mfcc]))
        
kmeans = KMeans(3, max_iter = 1000, n_init = 100)
kmeans.fit_transform(samples)
predictions = kmeans.predict(samples)

x=list()
y=list()
for i in range(len(predictions)):
    x.append(i)
    y.append(predictions[i])


x0=list()
x1=list()
x2=list()
y0=list()
y1=list()
y2=list()

for i in range(len(y)):
    if y[i] == 0:
        x0.append(x[i])
        y0.append(y[i])
    elif y[i] == 1:
        x1.append(x[i])
        y1.append(y[i])
    elif y[i] == 2:
        x2.append(x[i])
        y2.append(y[i])

plt.scatter(x0, y0, marker='o', c='black')
plt.scatter(x1, y1, marker='o', c='blue')
plt.scatter(x2, y2, marker='o', c='red')
plt.xlabel('sample number')
plt.ylabel('k means class')
plt.savefig('kmeans.png')
```
results in an image like this:
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/kmeans.png)

## Visualizing text features 
### text streams 
text_stream.py
```python3
import os, json, shutil
import speech_recognition as sr_audio
import sounddevice as sd
import soundfile as sf 

def transcribe_pocket(filename):
    # transcribe the audio (note this is only done if a voice sample)
    r=sr_audio.Recognizer()
    with sr_audio.AudioFile(filename) as source:
        audio = r.record(source) 
    text=r.recognize_sphinx(audio)
    
    return text

def sync_record(filename, duration, fs, channels):
    #print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    #print('done recording')

# set recording params 
duration=1
fs=44100
channels=1

try:
    os.mkdir('recordings')
    os.chdir(os.getcwd()+'/recordings')
except:
    shutil.rmtree('recordings')
    os.mkdir('recordings')
    os.chdir(os.getcwd()+'/recordings')

filenames=list()
transcripts=list()
for i in range(30):
    filename='%s.wav'%(str(i))
    sync_record(filename, duration, fs, channels)
    transcript=transcribe_pocket(filename)
    # print transcript on screen 
    print(transcript)
    filenames.append(filename)
    transcripts.append(transcript)

data={
    'filenames':filenames,
    'transcripts':transcripts
    }

jsonfile=open('recordings.json','w')
json.dump(data,jsonfile)
jsonfile.close()
```
results in a .JSON output like this:
```
1 lines (1 sloc)  672 Bytes
{"filenames": ["0.wav", "1.wav", "2.wav", "3.wav", "4.wav", "5.wav", "6.wav", "7.wav", "8.wav", "9.wav", "10.wav", "11.wav", "12.wav", "13.wav", "14.wav", "15.wav", "16.wav", "17.wav", "18.wav", "19.wav", "20.wav", "21.wav", "22.wav", "23.wav", "24.wav", "25.wav", "26.wav", "27.wav", "28.wav", "29.wav"], "transcripts": ["oh", "it is gorgeous", "testing on this", "return to go", "oh good and it's", "", "", "where", "it can be", "", "", "runny nose", "", "", "the", "oh", "the", "we're then were", "so good", "", "", "", "resting to", "testing testing", "asking because too", "testing testing", "interesting times", "testing testing", "deemed resting", "talking to us"]}
```

### text path 
text_path.py

results an image like this:
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/wordstream.png)

### frequency distribution plots 
text_freqplot.py

results in an image like this:
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/freqplot.png)
### wordclouds
text_wordcloud.py

results in an image like this:
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/wordcloud.png)
### parsed tree plots 
text_tree.py 

results in an image like this:
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/tree.png)
### named entity visualiations 
text_entity.py 

results in an image like this (in browser):
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/namedentity.png) 

### network plots
text_network.py 
### tSNE plots 
text_tsne.py 

results in an image like this: 
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/tsne_word.png)

text_tsne_many.py 

results in an image like this:
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/plotmany_tsne.png)

## Visualizing mixed features 
### mixed streams 
mixed_stream.py (sample output) 
```
==.==.==.==.==.==.==.==.==.== as things were
==.== 
==.==.==.==.==.==.==.==.==.== not sure who
==.==.==.==.==.== and it's all gone
==.== 
==.== 
==.== good
==.==.==.==.==.==.==.==.==.== exactly what
==.== air
==.== oh
==.== 
==.== 
==.==.==.==.==.==.==.==.==.==.==.== i was too good at all
==.== 
==.== 
==.==.==.==.==.==.==.==.==.== uh huh
==.==.==.==.==.==.==.==.==.==.==.== in the mud
==.==.==.==.==.==.==.==.==.== aren't you
==.== 
==.==.==.==.==.==.==.==.==.==.==.== so
==.== mm
==.== 
==.== 
==.== 
==.==.==.==.==.== this is
==.== oh
==.== 
==.==.==.==.==.== oh
==.== 
==.== 
minimum val: 0.05180590960662812
max val: 39.191748946905136
transcripts: 
['as things were', '', 'not sure who', "and it's all gone", '', '', 'good', 'exactly what', 'air', 'oh', '', '', 'i was too good at all', '', '', 'uh huh', 'in the mud', "aren't you", '', 'so', 'mm', '', '', '', 'this is', 'oh', '', 'oh', '', '']
```
### mixed path plat 
mixed_path.py 

results in an image like this:
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/mixedstream.png)

mixed_video.py 

results in a video as shown [here](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/mixed_video.avi)

Looks like this:
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/mixedstream.png)

## Visualizing meta features 
### streaming meta features 
meta_stream.py 

Looks like this: 
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/meta_stream.png)

### multiple streaming meta features 
meta_multi.py

Looks like this:
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/meta_multi.png)
### non-streaming meta features 
meta_nonstream.py

Looks like this:
![](https://github.com/jim-schwoebel/voicebook/blob/master/chapter_6_visualization/data/meta_nonstream.png)

## Resources
If you are interested to read more on any of these topics, check out the documentation below.

**Visualization libraries** 
* [Matplotlib](https://matplotlib.org/tutorials/introductory/sample_plots.html)
* [Seaborn](https://seaborn.pydata.org/)
* [Ggplot](http://ggplot.yhathq.com/)
* [Bokeh](https://bokeh.pydata.org/en/latest/)
* [Pygal](http://pygal.org/en/stable/)
* [Plotly Dash](https://plot.ly/)
* [Geoplotlib](https://github.com/andrea-cuttone/geoplotlib)
* [Gleam](https://github.com/dgrtwo/gleam) 
* [Missingno](https://github.com/ResidentMario/missingno)
* [Leather](https://leather.readthedocs.io/en/0.3.3/)

**Audio data**
* [Librosa](https://librosa.github.io/librosa/core.html) 
* [Soundfile](https://github.com/bastibe/SoundFile)
* [Sounddevice](https://python-sounddevice.readthedocs.io/en/0.3.11/)

**Text data** 
* [Sounddevice](https://python-sounddevice.readthedocs.io/en/0.3.11/)
* [NLTK](https://www.nltk.org/)
* [Spacy](https://spacy.io/)
* [NetworkX](https://networkx.github.io/) 

**Mixed data** 
* [Sounddevice](https://python-sounddevice.readthedocs.io/en/0.3.11/)
* [OpenCV](https://opencv.org/)

**Meta data** 
* [Keras](https://keras.io/) 
* [Scikit-learn](http://scikit-learn.org/stable/index.html) 
