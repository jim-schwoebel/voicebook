*This section documents all the scripts in the Chapter_3_featurization folder.*

## Definitions 
| Term | Definition | 
| ------- | ------- |
| [features](https://en.wikipedia.org/wiki/Feature_(machine_learning)) | descriptive numerical representations to describe an object. | 
| tagging | the process of tagging features to an object. | 
| voice features |  any features that relate to any information contained within the original audio file format.|
| audio features | voice features that do not contain features derived from a transcript, or strings of text outputted from speech-to-text models. | 
| text features | any voice features that are derived from an output transcript from a speech-to-text model, or transcription model. | 
| mixed features | Mixed features relate audio features to text features through some relationship. This often takes the form of ratios (e.g. speaking rate = total word count : total time in seconds). | 
| meta features | features outputted from machine learning models that are trained on audio, text, or mixed features. | 
| [dimensionality reduction techniques (DRTs)](https://en.wikipedia.org/wiki/Dimensionality_reduction) | DRTs compress existing feature sets into smaller sizes without changing the data dramatically. | 
| [feature selection](https://en.wikipedia.org/wiki/Feature_selection) | helps to set priorities as to what features are most important for a given machine learning problem. | 

## Using [numpy](http://www.numpy.org/) arrays 
### convert a list into a numpy array 
```python3
import numpy as np
>>> g=[5,2,61,1]
>>> type(g)
<class 'list'>
>>> g=np.array(g)
>>> type(g)
<class 'numpy.ndarray'>
```
### indexing numpy arrays 
```python3 
>>> g[0]
5
```
### serializing numpy data to a database 
```python3
>>> import json
>>> data={
	'data':g.tolist(),
	}
>>> jsonfile=open('test.json','w')
>>> json.dump(data,jsonfile)
>>> jsonfile.close()
```
### loading numpy data from a database
```python3
>>> newdata=json.load(open('test.json'))
>>> numpydata=np.array(newdata['data'])
>>> type(numpydata)
<class 'numpy.ndarray'>
>>> numpydata
array([ 5,  2, 61,  1])
```
### Get basic data
```python3
>>> numpydata.shape
(4,)
>>> numpydata.size
4
```
### get statistical features from an array 
```python3
>>> np.mean(numpydata)
17.25
>>> np.std(numpydata)
25.301926804099327
>>> np.amin(numpydata)
1
>>> np.amax(numpydata)
61
```
### initialize an array with zeros 
```python3
>>> makezeros=np.zeros(5)
>>> makezeros
array([0., 0., 0., 0., 0.])
```
### array operations 
```python3
>>> A=np.zeros(4)
>>> A+numpydata
array([ 5.,  2., 61.,  1.])
>>> A-np.array([2,-1,5,8])
array([-2.,  1., -5., -8.])
>>> 5*numpydata
array([ 25,  10, 305,   5])
```
## Audio features 
Audio features are voice features that do not contain features derived from a transcript, or strings of text outputted from speech-to-text models.

| Audio Feature | Description | Use case |
| ------- | ------- | ------- | 
| [Mel spectrogram frequency coefficients (mfcc)](https://dsp.stackexchange.com/questions/12812/mfcc-calculation) | Frequency bands that narrow in on the human voice range (usually 13 types but can be more).| Classifying phonemes. | 
| [Mel spectrogram frequency delta coefficients (mfcc)](https://dsp.stackexchange.com/questions/12812/mfcc-calculation)| A variation of the mfcc coefficients above. | Classifying phonemes. |
| [Fundamental frequency](https://en.wikipedia.org/wiki/Fundamental_frequency) | The lowest frequency of a periodic voice waveform. | Useful for classifying genders. | 
| [Jitter](https://en.wikipedia.org/wiki/Jitter) | Cycle-to-cycle variations in fundamental frequency.| Useful for speaker recognition and pathological voice quality.| 
| [Shimmer](http://www.wevosys.com/knowledge/_data_knowledge/107.pdf) | Cycle-to-cycle variations in the amplitude.| Useful for speaker recognition and pathological voice quality.| 
| [Formant frequencies](http://clas.mq.edu.au/speech/acoustics/frequency/tubes.html) | Higher frequency resonances can be calculated by determining all odd multiples of the first formant (e.g. multiply by 1, 3, 5, 7, ...: Fz = F1 x (2z -1)). | Detecting intratracheal lengths. |
| [File duration](https://stackoverflow.com/questions/7833807/get-wav-file-length-or-duration) | Length of the audio file | Detecting speaking rates. | 
| [Root mean squared (RMS) energy](https://en.wikipedia.org/wiki/Root_mean_square) | The mean of the energy emitted into the microphone over the span of time. | Detecting stress or new environments.|
| [Spectral centroid](https://en.wikipedia.org/wiki/Spectral_centroid) | Center of mass of an audio spectrum, or the weighted mean of the frequencies present in the signal. where x(n) represents the weighted frequency value, or magnitude, of bin number n, and f(n) represents the center frequency of that bin.| Characterizes ‘brightness’ of sound (timbre). |
| [Spectral flux](https://en.wikipedia.org/wiki/Spectral_flux) | How quickly the power spectrum of an audio signal is changing from one frame to the next.| Characterizes environments.|
| [Onset strength](http://docs.twoears.eu/en/latest/afe/available-processors/onset-strength/) | A measurement of the power which a voice recording begins and stops. | Helps localize sound sources.|
| [Spectral contrast](https://pdfs.semanticscholar.org/ed54/e0250f106a208cb693d50dbfd13df2d9cd9e.pdf) | The decibel difference between peaks and valleys in the spectrum. | Helps to detect noise in samples.|
| [Spectral flatness](https://en.wikipedia.org/wiki/Spectral_flatness) | Entropy measure that helps assess self-similarity in an audio signal. |Useful for noise detection (1) compared to tone-signals (0). |
| [Spectral rolloff](https://www.sciencedirect.com/science/article/pii/S1051200412002473) | Frequency below which the total energy is typically concentrated. | Speech bandwidth characterization and segmentation (diarization).|
| [Zero-crossing rates](https://en.wikipedia.org/wiki/Zero-crossing_rate) | The rate of sign changes in a sample of audio (+/-) or (-/+). | Useful to measure periodicity and detect voices.|

### [librosa](https://librosa.github.io/librosa/core.html) features 
librosa_features.py
```python3
import librosa
import numpy as np 

# get statistical features in numpy
def stats(matrix):
    mean=np.mean(matrix)
    std=np.std(matrix)
    maxv=np.amax(matrix)
    minv=np.amin(matrix)
    median=np.median(matrix)

    output=np.array([mean,std,maxv,minv,median])
    
    return output

# featurize with librosa following documentation
# https://librosa.github.io/librosa/feature.html 
def librosa_featurize(filename, categorize):
    # if categorize == True, output feature categories 
    print('librosa featurizing: %s'%(filename))

    y, sr = librosa.load(filename)

    # FEATURE EXTRACTION
    ######################################################
    # extract major features using librosa
    mfcc=librosa.feature.mfcc(y)
    poly_features=librosa.feature.poly_features(y)
    chroma_cens=librosa.feature.chroma_cens(y)
    chroma_cqt=librosa.feature.chroma_cqt(y)
    chroma_stft=librosa.feature.chroma_stft(y)
    tempogram=librosa.feature.tempogram(y)

    spectral_centroid=librosa.feature.spectral_centroid(y)[0]
    spectral_bandwidth=librosa.feature.spectral_bandwidth(y)[0]
    spectral_contrast=librosa.feature.spectral_contrast(y)[0]
    spectral_flatness=librosa.feature.spectral_flatness(y)[0]
    spectral_rolloff=librosa.feature.spectral_rolloff(y)[0]
    onset=librosa.onset.onset_detect(y)
    onset=np.append(len(onset),stats(onset))
    tempo=librosa.beat.tempo(y)[0]
    onset_features=np.append(onset,tempo)
    onset_strength=librosa.onset.onset_strength(y)
    zero_crossings=librosa.feature.zero_crossing_rate(y)[0]
    rmse=librosa.feature.rmse(y)[0]

    # FEATURE CLEANING 
    ######################################################

    # onset detection features
    onset_features=np.append(onset_features,stats(onset_strength))

    # rhythm features (384) - take the first 13
    rhythm_features=np.concatenate(np.array([stats(tempogram[0]),
                                      stats(tempogram[1]),
                                      stats(tempogram[2]),
                                      stats(tempogram[3]),
                                      stats(tempogram[4]),
                                      stats(tempogram[5]),
                                      stats(tempogram[6]),
                                      stats(tempogram[7]),
                                      stats(tempogram[8]),
                                      stats(tempogram[9]),
                                      stats(tempogram[10]),
                                      stats(tempogram[11]),
                                      stats(tempogram[12])]))

    # spectral features (first 13 mfccs)
    spectral_features=np.concatenate(np.array([stats(mfcc[0]),
                                        stats(mfcc[1]),
                                        stats(mfcc[2]),
                                        stats(mfcc[3]),
                                        stats(mfcc[4]),
                                        stats(mfcc[5]),
                                        stats(mfcc[6]),
                                        stats(mfcc[7]),
                                        stats(mfcc[8]),
                                        stats(mfcc[9]),
                                        stats(mfcc[10]),
                                        stats(mfcc[11]),
                                        stats(mfcc[12]),
                                        stats(poly_features[0]),
                                        stats(poly_features[1]),
                                        stats(spectral_centroid),
                                        stats(spectral_bandwidth),
                                        stats(spectral_contrast),
                                        stats(spectral_flatness),
                                        stats(spectral_rolloff)])) 

    # power features
    power_features=np.concatenate(np.array([stats(zero_crossings),
                                         stats(rmse)])) 

    # you can also concatenate the features
    if categorize == True:
        # can output feature categories if true 
        features={'onset':onset_features,
                  'rhythm':rhythm_features,
                  'spectral':spectral_features,
                  'power':power_features}
    else:
        # can output numpy array of everything if we don't need categorizations 
        features = np.concatenate(np.array([onset_features,
                                       rhythm_features,
                                       spectral_features,
                                       power_features]))

    return features

features=librosa_featurize('test.wav', False)
```

### [pyaudioanalysis](https://github.com/tyiannak/pyAudioAnalysis) features
pyaudio_features.py
```python3
import os,json
import numpy as np

def stats(matrix):
    mean=np.mean(matrix)
    std=np.std(matrix)
    maxv=np.amax(matrix)
    minv=np.amin(matrix)
    median=np.median(matrix)
    output=np.array([mean,std,maxv,minv,median])
    return output

def pyaudio_featurize(file):
    # use pyaudioanalysis library to export features
    # exported as file[0:-4].json 
    os.system('python pyaudio_help.py %s'%(file))
    jsonfile=file[0:-4]+'.json'
    g=json.load(open(jsonfile))
    features=np.array(g['features'])
    # now go through all the features and get statistical features for array
    new_features=list()
    all_labels=['zero crossing rate','energy','entropy of energy','spectral centroid',
                'spectral spread', 'spectral entropy', 'spectral flux', 'spectral rolloff',
                'mfcc1','mfcc2','mfcc3','mfcc4',
                'mfcc5','mfcc6','mfcc7','mfcc8',
                'mfcc9','mfcc10','mfcc11','mfcc12',
                'mfcc13','chroma1','chroma2','chroma3',
                'chroma4','chroma5','chroma6','chroma7',
                'chroma8','chroma9','chroma10','chroma11',
                'chroma12','chroma deviation']
    labels=list()
                
    for i in range(len(features)):
        tfeature=stats(features[i])
        for j in range(len(tfeature)):
            new_features.append(tfeature[j])
            if j==0:
                labels.append('mean '+all_labels[i])
            elif j==1:
                labels.append('std '+all_labels[i])
            elif j==2:
                labels.append('max '+all_labels[i])
            elif j==3:
                labels.append('min '+all_labels[i])
            elif j==4:
                labels.append('median '+all_labels[i])
            
    new_features=np.array(new_features)
    os.remove(jsonfile)
    
    return new_features, labels
    
features, labels =pyaudio_featurize('test.wav')
```

### [SoX](http://sox.sourceforge.net/Docs/Features) features
sox_features.py
```python3 
import os
import numpy as np   

def clean_text(text):
    text=text.lower()
    chars=['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'o','p','q','r','s','t','u','v','w','x','y','z',' ',
           ':', '(',')','-','=',"'.'"]
    for i in range(len(chars)):
        text=text.replace(chars[i],'')

    text=text.split('\n')
    new_text=list()
    # now get new text
    for i in range(len(text)):
        try:
            new_text.append(float(text[i].replace('\n','').replace('n','')))
        except:
            pass
            #print(text[i].replace('\n','').replace('n',''))
                        
    return new_text

def sox_featurize(filename):
    # soxi and stats files 
    soxifile=filename[0:-4]+'_soxi.txt'
    statfile=filename[0:-4]+'_stats.txt'
    os.system('soxi %s > %s'%(filename, soxifile))
    os.system('sox %s -n stat > %s 2>&1'%(filename, statfile))
    # get basic info 
    s1=open(soxifile).read()
    s1_labels=['channels','samplerate','precision',
               'duration','filesize','bitrate','sample encoding']
    s1=clean_text(s1)
    
    s2=open(statfile).read()
    s2_labels=['samples read','length','scaled by','maximum amplitude',
               'minimum amplitude','midline amplitude','mean norm','mean amplitude',
               'rms amplitude','max delta','min delta','mean delta',
               'rms delta','rough freq','vol adj']
    
    s2=clean_text(s2)

    labels=s1_labels+s2_labels
    features=np.array(s1+s2)
    
    return features,labels

features, labels = sox_featurize('test.wav')
```

### [Audioset](https://research.google.com/audioset/index.html) features 
audioset_features.py
```python3
# ^^ ... (down to main script in audioset_features.py)
# get current directory 
curdir=os.getcwd()

# download audioset files if audioset not in current directory 
if 'audioset' not in os.listdir():
    try:
        setup_audioset(curdir)
    except:
        print('there was an error installing audioset')

# record a 10 second, mono 16k Hz audio file in the current directory
filename='test.wav'
sync_record(filename,10,16000,1)

# now let's featurize an audio sample in the current directory, test.wav 
features, new_features =audioset_featurize(filename)
# print('new features')   
# print(new_features)
# print(len(new_features))
```

## Text features
Text features are any voice features that are derived from an output transcript from a speech-to-text model, or transcription model. 

| Text Feature | Description | Use case |
| ------- | ------- | ------- | 
| [Keyword frequency](https://en.wikipedia.org/wiki/Reserved_word) | Count of word ‘basketball’ relative to the total number of words| Useful to determine topics. |
| [Character frequencies](https://en.wikipedia.org/wiki/Character_(symbol)) | Count of the letter ‘a’ relative to all characters | Letter frequencies represent phonemes in speech and sometimes enrich model accuracies. A standard list of phonemes in English is provided by the International Phonetic Alphabet. | 
| [Part-of-speech tags](https://en.wikipedia.org/wiki/Part_of_speech) | Number of nouns in the entire transcript. | Sometimes can be used to infer the type of speech production - for example, whether it’s descriptive, interjectory, or free speech.| 
| [Sentiment polarity](https://textblob.readthedocs.io/en/dev/) | Positive, negative, or neutral.| Can detect whether the content of the transcript is positive, negative, or neutral; helps to detect emotional content. |
| [Brunet’s index](https://www.cs.toronto.edu/~kfraser/Fraser15-JAD.pdf) | A measure of the richness of text; a complexity measure. | Can measure cognitive impairment associated with Alzheimer’s disease. | 
| [Morphological features](https://spacy.io/usage/linguistic-features) | Past, present, or future tense of a verb (lemma and surface forms). | Useful to see time-based content in a conversation. | 
| [Syntactic features](https://en.wikipedia.org/wiki/Syntax) | Dependencies between tokens and parts of speech (e.g. noun-verb-noun frequency throughout entire text).| Biometric identification - people have a very unique syntax which describes their interactions. Can be more computationally-intensive.| 
| [Named entity recognition](https://en.wikipedia.org/wiki/Named-entity_recognition) | The frequency of a specific person, Jim, being used in a transcript. | Useful to determine relevance of certain things in a conversation, or for topic labeling.|

### [nltk](https://www.nltk.org/) features
nltk_features.py
```python3
import nltk
from nltk import word_tokenize 
import speech_recognition as sr_audio 
import numpy as np
from textblob import TextBlob
import transcribe as ts

def nltk_featurize(file):
	# get transcript 
	transcript=ts.transcribe_sphinx('test.wav')
	#alphabetical features 
	a=transcript.count('a')
	b=transcript.count('b')
	c=transcript.count('c')
	d=transcript.count('d')
	e=transcript.count('e')
	f=transcript.count('f')
	g_=transcript.count('g')
	h=transcript.count('h')
	i=transcript.count('i')
	j=transcript.count('j')
	k=transcript.count('k')
	l=transcript.count('l')
	m=transcript.count('m')
	n=transcript.count('n')
	o=transcript.count('o')
	p=transcript.count('p')
	q=transcript.count('q')
	r=transcript.count('r')
	s=transcript.count('s')
	t=transcript.count('t')
	u=transcript.count('u')
	v=transcript.count('v')
	w=transcript.count('w')
	x=transcript.count('x')
	y=transcript.count('y')
	z=transcript.count('z')
	space=transcript.count(' ')

	#numerical features and capital letters 
	num1=transcript.count('0')+transcript.count('1')+transcript.count('2')+transcript.count('3')+transcript.count('4')+transcript.count('5')+transcript.count('6')+transcript.count('7')+transcript.count('8')+transcript.count('9')
	num2=transcript.count('zero')+transcript.count('one')+transcript.count('two')+transcript.count('three')+transcript.count('four')+transcript.count('five')+transcript.count('six')+transcript.count('seven')+transcript.count('eight')+transcript.count('nine')+transcript.count('ten')
	number=num1+num2
	capletter=sum(1 for c in transcript if c.isupper())

	#part of speech 
	text=word_tokenize(transcript)
	g=nltk.pos_tag(transcript)
	cc=0
	cd=0
	dt=0
	ex=0
	in_=0
	jj=0
	jjr=0
	jjs=0
	ls=0
	md=0
	nn=0
	nnp=0
	nns=0
	pdt=0
	pos=0
	prp=0
	prp2=0
	rb=0
	rbr=0
	rbs=0
	rp=0
	to=0
	uh=0
	vb=0
	vbd=0
	vbg=0
	vbn=0
	vbp=0
	vbp=0
	vbz=0
	wdt=0
	wp=0
	wrb=0

	for i in range(len(g)):
		if g[i][1] == 'CC':
			cc=cc+1
		elif g[i][1] == 'CD':
			cd=cd+1
		elif g[i][1] == 'DT':
			dt=dt+1
		elif g[i][1] == 'EX':
			ex=ex+1
		elif g[i][1] == 'IN':
			in_=in_+1
		elif g[i][1] == 'JJ':
			jj=jj+1
		elif g[i][1] == 'JJR':
			jjr=jjr+1                   
		elif g[i][1] == 'JJS':
			jjs=jjs+1
		elif g[i][1] == 'LS':
			ls=ls+1
		elif g[i][1] == 'MD':
			md=md+1
		elif g[i][1] == 'NN':
			nn=nn+1
		elif g[i][1] == 'NNP':
			nnp=nnp+1
		elif g[i][1] == 'NNS':
			nns=nns+1
		elif g[i][1] == 'PDT':
			pdt=pdt+1
		elif g[i][1] == 'POS':
			pos=pos+1
		elif g[i][1] == 'PRP':
			prp=prp+1
		elif g[i][1] == 'PRP$':
			prp2=prp2+1
		elif g[i][1] == 'RB':
			rb=rb+1
		elif g[i][1] == 'RBR':
			rbr=rbr+1
		elif g[i][1] == 'RBS':
			rbs=rbs+1
		elif g[i][1] == 'RP':
			rp=rp+1
		elif g[i][1] == 'TO':
			to=to+1
		elif g[i][1] == 'UH':
			uh=uh+1
		elif g[i][1] == 'VB':
			vb=vb+1
		elif g[i][1] == 'VBD':
			vbd=vbd+1
		elif g[i][1] == 'VBG':
			vbg=vbg+1
		elif g[i][1] == 'VBN':
			vbn=vbn+1
		elif g[i][1] == 'VBP':
			vbp=vbp+1
		elif g[i][1] == 'VBZ':
			vbz=vbz+1
		elif g[i][1] == 'WDT':
			wdt=wdt+1
		elif g[i][1] == 'WP':
			wp=wp+1
		elif g[i][1] == 'WRB':
			wrb=wrb+1		

	#sentiment
	tblob=TextBlob(transcript)
	polarity=float(tblob.sentiment[0])
	subjectivity=float(tblob.sentiment[1])

	#word repeats
	words=transcript.split()
	newlist=transcript.split()
	repeat=0
	for i in range(len(words)):
		newlist.remove(words[i])
		if words[i] in newlist:
			repeat=repeat+1 

	features=np.array([a,b,c,d,
	e,f,g_,h,
	i,j,k,l,
	m,n,o,p,
	q,r,s,t,
	u,v,w,x,
	y,z,space,number,
	capletter,cc,cd,dt,
	ex,in_,jj,jjr,
	jjs,ls,md,nn,
	nnp,nns,pdt,pos,
	prp,prp2,rbr,rbs,
	rp,to,uh,vb,
	vbd,vbg,vbn,vbp,
	vbz,wdt,wp,wrb,
	polarity,subjectivity,repeat])

	labels=['a', 'b', 'c', 'd',
			'e','f','g','h',
			'i', 'j', 'k', 'l',
			'm','n','o', 'p',
			'q','r','s','t',
			'u','v','w','x',
			'y','z','space', 'numbers',
			'capletters','cc','cd','dt',
			'ex','in','jj','jjr',
			'jjs','ls','md','nn',
			'nnp','nns','pdt','pos',
			'prp','prp2','rbr','rbs',
			'rp','to','uh','vb',
			'vbd','vbg','vbn','vbp',
			'vbz', 'wdt', 'wp','wrb',
			'polarity', 'subjectivity','repeat']

	return features, labels


# transcribe with pocketsphinx
features, labels = nltk_featurize('test.wav')
```

### [spacy](https://spacy.io/) features
spacy_features.py
```python3
import spacy_features

# Alice’s Adventures in Wonderland = text 
transcript=open('alice.txt').read()
features, labels = spacy_featurize(transcript)
# shows feature array with labels = 315 features total 
print(features)
print(labels)
print(len(features))
print(len(labels))
```

### [gensim](https://radimrehurek.com/gensim/) word2vec features 
gensim_features.py
```python3
import os
import numpy as np 
from gensim.models import Word2Vec

def w2v_train(textlist,size,modelname):
    sentences=list()
    
    #split into individual word embeddings
    for i in range(len(textlist)):
        if len(textlist[i].split())==0:
            pass
        else:
            sentences.append(textlist[i].split())

    #test (for small samples)
    #print(sentences)
    model = Word2Vec(sentences, size=size, window=5, min_count=1, workers=4)
    
    if modelname in os.listdir():
        #do not save if already file in folder with same name 
        pass
    else:
        print('saving %s to disk...'%(modelname))
        model.save(modelname)
        
    return model

def sentence_embedding(sentence,size,modelname):
    model=Word2Vec.load(modelname)

    sentences2=sentence.split()

    w2v_embed=list()
    for i in range(len(sentences2)):
        try:
            #print(sentences2[i])
            w2v_embed.append(model[sentences2[i]])
            #print(model[sentences2[i]])
        except:
            #pass if there is an error to not distort averages... :)
            pass

    out_embed=np.zeros(size)
    for j in range(len(w2v_embed)):
        out_embed=out_embed+w2v_embed[j]

    out_embed=(1/size)*out_embed

    return out_embed

# load alice and wonderland corpus and build w2v model
text=open('alice.txt').read()
transcript='I had a great time at the bar today.'
modelname='alice.pickle'
w2v_train(text,100,modelname)
features=sentence_embedding(transcript, 100,modelname)
print(features)
print(len(features))
```

## Mixed features 
Mixed features relate audio features to text features through some relationship. This often takes the form of ratios (e.g. speaking rate = total word count : total time in seconds). Since it’s not necessarily very intuitive, I prefer to make mixed features through random combinations of text features with audio features.

make_mixed_features.py
```python3
import pyaudio_features as pf 
import spacy_features as sf
import transcribe as ts
import random

# get features 
pyaudio_features, pyaudio_labels=pf.pyaudio_featurize('test.wav')
transcript=ts.transcribe_sphinx('test.wav')
spacy_features, spacy_labels=sf.spacy_featurize(transcript)

# relate some features to each other
# engineer 10 random features by dividing them and making new labels 
mixed_features=list()
mixed_labels=list()
for i in range(10):
    # get some random features from both text and audio 
    i1=random.randint(0,len(pyaudio_features)-1)
    label_1=pyaudio_labels[i1]
    feature_1=pyaudio_features[i1]
    i2=random.randint(0,len(spacy_features)-1)
    label_2=spacy_labels[i2]
    feature_2=spacy_features[i2]
    # make new label 
    mixed_label=label_2+' (spacy) ' + '| / | '+label_1 + ' (pyaudio)'
    print(mixed_label)
    mixed_labels.append(mixed_label)
    # make new feature from labels 
    mixed_feature=feature_2/feature_1
    print(mixed_feature)
    mixed_features.append(mixed_feature)
```
## Meta features 
Meta features are features outputted from machine learning models that are trained on audio, text, or mixed features.

| Meta feature (# features) | feature array (training data) | Accuracy range | output from model | 
|-------|-------|-------|-------| 
| Ages (7) | Modified librosa audio embedding  (Common Voice, N=1000+) | 70-77% (+/- 0.6%) (knn) | Teens, twenties, thirties, forties, fifties, sixties, and seventies. | 
| Gender (1) | Modified librosa audio embedding (Common Voice, N=1000+) | ~87-88% (+/- 6.0%) | Male or female. | 
| Ethnicity (1) | Modified librosa audio embedding (internal data, N= ~150) | 88.7% (+/- 5.2%) | African american or caucasian.|  
| Accents (19) | Modified librosa audio embedding (Kaggle, N=~35) | 51-82%(+/- 6-8%) (various) | French, japanese, cantonese, romanian, korean, turkish, macedonian, dutch, english, Italian, swedish, amharic, vietnamese, russian, mandarin, portuguese, polish, spanish, and german. | 
| Diseases (15) | Modified librosa audio embedding (YouTube, N=~30) | ~60-80% (+/-10-15%). | Addiction, adhd, als, anxiety, autism, cold, depression, dyslexia, glioblastoma, graves disease, multiple sclerosis, parkinson’s, postpartum depression, schizophrenia, and sleep apnea. | 
| Emotions (6) | Modified librosa audio embedding (YouTube, N=~100) | 55-80% (+/- 15%). | Happy, sad, neutral, disgust, angry, and surprised.| 
| Audio quality (1) | Modified librosa audio embedding (internal, manually tagged, N=~70)| 75.6% (+/- 8.2%). | Highquality or lowquality.| 
| Fatigue level (1) | Modified librosa audio embedding (internal, manually tagged, N=~80)| 77.2% (+/- 8.4%).| Fatigued or awake. | 
| Stress level (1) | Modified librosa embedding (internal, manually tagged, N=~80) | 78.9% (+/- 9.3%). | Stressed or calm.| 
| Speaking type (1) | Modified librosa audio embedding (internal, manually tagged, N=~60) | 79.6% (+/- 8.0%) | Natural or not natural (abnormal) speech. | 
| Music genres (15) | Modified librosa embedding (YouTube data, N=~30) | ~70-90% (+/- 10-12.0%). | Alternative, christian, country, edm, folk, holiday, indie, jazz, latin, newage, pop, rap, reggae, rock, soundtrack | 

### example output meta feature array
meta_features.py

All you need to do is run the script one time and it will create a folder, load_dir, in the current directory. Then, place any audio files you’d like to process in this load_dir directory (e.g. 20 sec .wav files). If you run the script again (e.g. python3 meta_features.py), all the audio files will then be featurized with the script and put into a .JSON file (e.g. ‘test.wav’ → ‘test.json’). In this way, all you need are the model files (.PICKLE format) in the meta_models folder and new features will be loaded into the array.

```
META FEATURES 


[1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


 META CLASSES: 


['controls', 'adhd', 'africanamerican', 'controls', 'alternativecontrolbalanced', 'amharic_controls', 'angry_controls', 'anxiety', 'controls', 'controls', 'controls', 'cantonese', 'christian', 'controls', 'country', 'depression', 'disgust_controls', 'dutch_controls', 'controls', 'edmcontrolbalanced', 'english', 'awake', 'fear_controls', 'fifties_controls', 'folkcontrolbalanced', 'fourties_controls', 'french_controls', 'male', 'german', 'controls', 'controls', 'happy_controls', 'holiday', 'indiecontrolbalanced', 'italian', 'japanese', 'jazzcontrolbalanced', 'korean', 'latin', 'macedonian_controls', 'mandarin_controls', 'multiple_sclerosis', 'natural', 'neutral_controls', 'newagecontrolbalanced', 'controls', 'polish', 'popcontrolbalanced', 'portuguese_controls', 'controls', 'badquality', 'rapcontrolbalanced', 'reggae', 'rock', 'romanian', 'russian_controls', 'sad', 'controls', 'seventies_controls', 'sixties', 'controls', 'soundtrackcontrolbalanced', 'spanish_controls', 'stressed', 'surprise_controls', 'swedish', 'teens', 'thirties', 'turkish', 'twenties', 'vietnamese_controls']
```

## Dimensionality reduction 
List of automated ways to reduce dimensionality of large feature arrays. 

| Technique | Supervised or unsupervised? | Pros | Cons | 
|-------|-------|-------|-------| 
| [Principal Component Analysis (PCA)](https://en.wikipedia.org/wiki/Principal_component_analysis) | Unsupervised  | Easy to execute in scikit-learn library, Can be used as a pre-processing step in many machine learning pipelines. | Highly sensitive to outliers in the dataset. Does not scale well to large datasets. Does not capture local structures. | 
| [Independent component analysis (ICA)](https://en.wikipedia.org/wiki/Independent_component_analysis) | Unsupervised  | Works for non-Gaussian signals and that they are statistically independent from each other.  | Does not work for Gaussian signals very well; for these cases use PCA. | 
| [K-means clustering (vector quantization)](https://en.wikipedia.org/wiki/K-means_clustering)   | Unsupervised  | Low computational cost burden. | Does not take into account temporal evolution of signals. | 
| [Canonical correlation analysis](https://en.wikipedia.org/wiki/Canonical_correlation) | Unsupervised | Good for datasets with high correlation. | Not very robust in datasets with high variance. | 
| [Partial least squares regression](https://en.wikipedia.org/wiki/Partial_least_squares_regression) | Unsupervised | Good for linear datasets.| Not good for nonlinear datasets.| 
| [Manifold learning](https://en.wikipedia.org/wiki/Nonlinear_dimensionality_reduction#Manifold_learning_algorithms)| Unsupervised | No good framework for handling missing data.| Few people know how to actually implement these techniques. More generalizable to nonlinear datasets (representative of real-world data). Computationally-intensive. | 
| [Supervised dictionary learning (SDL)](https://en.wikipedia.org/wiki/Sparse_dictionary_learning) | Supervised  | Simple representation as weighted sum of features. | n/a | 
| [Linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis) or [Correspondence analysis](https://en.wikipedia.org/wiki/Correspondence_analysis) | Supervised (continuous data) | Good for when the class means and variances are known. | Not robust when class centroids coincide or class covariances vary. Sensitive to sampling rates (e.g. undersampling). | 
| [Variational Autoencoders (VA)](https://en.wikipedia.org/wiki/Autoencoder) | Supervised  |  Neural network. Powerful and accurate. | Prone to overfitting. Doesn’t work well on small datasets. CPU/GPU intensive. | 
### unsupervised techniques 
dimensionality_reduction.py
```python3
import numpy as np
import json, os 

# load data (149 in each class)
data = json.load(open(os.getcwd()+'/data/africanamerican_controls.json'))
X= np.array(data['africanamerican'])
Y= np.array(data['controls']) 


################################################################
##                 UNSUPERVISED TECHNIQUES                    ##
################################################################
# Principal Component Analysis 
from sklearn.decomposition import PCA

# calculate PCA for 50 components 
pca = PCA(n_components=50)
pca.fit(X)
X_pca = pca.transform(X)

# Independent component analysis 
from sklearn.decomposition import FastICA

ica = FastICA(n_components=50)
S_ = ica.fit_transform(X)  # Reconstruct signals

# K-means clustering
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=50, random_state=0).fit_transform(X)

# Canonical correlation analysis
from sklearn.cross_decomposition import CCA
cca = CCA(n_components=50).fit(X, Y).transform(X, Y)
new_X=cca[0]
new_Y=cca[1]

# PLS regression
from sklearn.cross_decomposition import PLSRegression
pls = PLSRegression(n_components=50).fit(X, Y).transform(X, Y)
pls_X=pls[0]
pls_Y=pls[1]

# manifold learning 
from sklearn import manifold
manifold_X = manifold.Isomap(10, 50).fit_transform(X)
manifold_Y = manifold.Isomap(10,50).fit_transform(Y)
```

### supervised techniques 
dimensionality_reduction.py
```python3
mport numpy as np
import json, os 

# load data (149 in each class)
data = json.load(open(os.getcwd()+'/data/africanamerican_controls.json'))
X= np.array(data['africanamerican'])
Y= np.array(data['controls']) 


################################################################
##                  SUPERVISED TECHNIQUES                     ##
################################################################
# supervised dictionary learning
from sklearn.decomposition import MiniBatchDictionaryLearning
dico_X = MiniBatchDictionaryLearning(n_components=50, alpha=1, n_iter=500).fit_transform(X)
dico_Y = MiniBatchDictionaryLearning(n_components=50, alpha=1, n_iter=500).fit_transform(Y)

# linear discriminant analysis
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA 
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis as QDA
from sklearn.model_selection import train_test_split

# make a train set and train labels 
Z=np.array(list(X)+list(Y))
newlabels=list()
for i in range(len(X)):
	newlabels.append('1')
for i in range(len(Y)):
	newlabels.append('0')

X_train, X_test, y_train, y_test = train_test_split(Z, newlabels, test_size=0.33, random_state=42)

lda = LDA(n_components=50).fit(X_train, y_train).transform(X)
```

## Feature selection 

Feature selection helps to set priorities as to what features are most important for a given machine learning problem.  

| Method | Description | Examples | 
|-------|-------|-------|
| Filter method | The features are ranked by the score and either selected to be kept or removed from the dataset. | Chi squared test, information gain, and correlation coefficient scores. | 
| Wrapper method| Wrapper methods consider the selection of a set of features as a search problem, where different combinations are prepared, evaluated and compared to other combinations. | Recursive feature elimination algorithm.| 
| Embedded methods| “Embedded methods learn which features best contribute to the accuracy of the model while the model is being created. | LASSO, elastic net, and ridge regression.|

### select_features.py
```python3
import os, json
import numpy as np

# load data 
data = json.load(open('africanamerican_controls.json'))
X=np.array(data['africanamerican'])
Y=np.array(data['controls'])
training=list()
for i in range(len(X)):
	training.append(X[i])
for i in range(len(Y)):
	training.append(Y[i])

# get labels (as binary class outputs)
labels=list()
for i in range(len(X)):
    labels.append(1)
for i in range(len(Y)):
    labels.append(0)

#########################################################
##                  Chi Square test                    ##
#########################################################
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(training, labels, test_size=0.20, random_state=42)
X_train=np.array(X_train)
X_test=np.array(X_test)
y_train=np.array(y_train).astype(int)
y_test=np.array(y_test).astype(int)

# normalize features so they are non-negative [0,1], or chi squared test will fail
# it assumes all values are positive 
min_max_scaler = preprocessing.MinMaxScaler()
chi_train = min_max_scaler.fit_transform(X_train)
chi_labels = y_train 

# Select 50 features with highest chi-squared statistics
chi2_selector = SelectKBest(chi2, k=50)
X_kbest = chi2_selector.fit_transform(chi_train, chi_labels)


#########################################################
##           Recursive feature elimination             ##
#########################################################
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.svm import SVR

model = LogisticRegression() 
rfe = RFE(model, 50)
fit = rfe.fit(X_train, y_train)

# list out number of features and selected features 
print("Num Features: %d"% fit.n_features_) 
print("Selected Features: %s"% fit.support_) 
print("Feature Ranking: %s"% fit.ranking_)

#########################################################
##                   LASSO technique                   ##
#########################################################
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel

lsvc = LinearSVC(C=0.01, penalty="l1", dual=False).fit(X_train, y_train)
model = SelectFromModel(lsvc, prefit=True)
X_new = model.transform(X_train)
print(X_new.shape)
# (238, 208) --> (238, 22), dramatic reduction of features using LASSO
```
## References
If you are interested to read more on any of these topics, check out the documentation below.

**Audio features**
* [Librosa](https://librosa.github.io/librosa/core.html)
* [PyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis)
* [SoX](http://sox.sourceforge.net/)
* [OpenSMILE](https://audeering.com/technology/opensmile/)
* [AudioSet VGGish model](https://github.com/tensorflow/models/tree/master/research/audioset)

**Text features**
* [NLTK](https://www.nltk.org/)
* [Spacy](https://spacy.io/)
* [Gensim](https://radimrehurek.com/gensim/)
* [Textblob](https://textblob.readthedocs.io/en/dev/)

**Mixed features**
* [PyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis)
* [Spacy](https://spacy.io/)

**Meta features** 
* [Scikit-learn](http://scikit-learn.org/stable/auto_examples/index.html#general-examples)
* [Keras](https://keras.io/)
* [Tensorflow](https://www.tensorflow.org/)

**Dimensionality reduction**
* [Scikit-learn](http://scikit-learn.org/stable/auto_examples/index.html#general-examples)
* [Megaman (nonlinear manifold learning)](https://github.com/mmp2/megaman)
* [Tensorflow](https://www.tensorflow.org/)

**Feature selection**
* [Scikit-learn](http://scikit-learn.org/stable/)
* [MLpy](http://mlpy.sourceforge.net/)
* [Scikit-feature](http://featureselection.asu.edu/)
* [Yellowbrick](http://www.scikit-yb.org/en/latest/) 
