*This section documents all the scripts in the chapter_4_modeling folder.*

## Machine learning definitions 
| Term | Definition | 
| ------- | ------- |
| [features](https://en.wikipedia.org/wiki/Feature_(machine_learning)) | descriptive numerical representations to describe an object. | 
| [machine learning](https://en.wikipedia.org/wiki/Machine_learning) |  the process of teaching a machine something that is useful. | 
| [classification model](https://en.wikipedia.org/wiki/Statistical_classification) | If the goal is to separate out into classes (e.g. male or female), then this is known as a classification problem. | 
| [regression model](https://en.wikipedia.org/wiki/Regression_analysis) | if the end goal is to measure some correlation with a variable and the output is more a numerical range (e.g. often between 0 and 1), then this is more of a regression problem. | 
| [deep learning models](https://en.wikipedia.org/wiki/Deep_learning) | models that are trained using a neural network. |
| [unsupervised learning](https://en.wikipedia.org/wiki/Unsupervised_learning) | if machines do not require labels (e.g. just need features), this is known as a unsupervised learning problem. | 
| [supervised learning](https://en.wikipedia.org/wiki/Supervised_learning) | if machines require labels (e.g. male or female as separate feature arrays), this is known as a supervised learning problem. | 
| [training set](https://en.wikipedia.org/wiki/Training,_test,_and_validation_sets#training_set) | Machines are fed training data in the form of feature arrays and compress patterns in these feature arrays into models through algorithms.| 
| [testing set](https://en.wikipedia.org/wiki/Training,_test,_and_validation_sets) | data that is left out during training so that the accuracy can be calculated using cross-validation techniques. | 
| [validation set](https://en.wikipedia.org/wiki/Training,_test,_and_validation_sets#Validation_set) | data that is left out during training to tune hyperparameters (often used in deep learning modeling. | 
| [label](https://stackoverflow.com/questions/40898019/what-is-the-difference-between-a-feature-and-a-label/40899529) | a tag of an featurized audio sample (e.g. male or female) to aid in supervised learning.| 
| [cross-validation](https://en.wikipedia.org/wiki/Cross-validation_(statistics)) | how the performance of ML models are assessed (in terms of accuracy).| 

## Obtaining training data 
make_playlist.py (from CLI)
```
cd ~
cd voicebook/chapter_4_modeling/youtube_scrape
python3 make_playlist.py 
what is the name of this playlist?
what is the playlist id or URL?
… [‘n’ to stop making playlist]
```
download_playlist.py (from CLI)
```
python3 download_playlist.py 
what is the name of the playlist to download?
… downloads playlist to /playlist folder 
```
## Labeling training data 
label_samples.py (from CLI)
### labeling YouTube data in spreadsheets 
label_samples.py (from CLI)
```
python3 label_samples.py
what is the master label (e.g. stressed)? 
stressed
sample number: 0
what is the URL of the video? 
https://www.youtube.com/watch?v=47HLiAxHgdo
how long is the audio sample in seconds? (e.g. 20) 
20
what are the stop and start times of the video (e.g. 0:13-0:33)
0:05-0:25            
is this person stressed? 1 for yes, 0 for no
1
is this person a child (c, <13) or adolescent (d, 13-18) or adult  (a, >18 <70) or elderly (e, >70)? 
a
is this person male (m) or female (f)? 
m
does this person have an American (a) or foreign (f) accent? 
a
what is the audio quality? (1 - poor, 2 - moderate, 3 - good quality, 4 - high quality)3
is the environment indoors (i) or outdoors (o)?i
sample number: 1
what is the URL of the video?
...After entering [‘’] here, it ends the script and outputs excel sheet below.
```
### downloading YouTube data from spreadsheets
y_scrape.py (from CLI)
```
Run script in terminal...
python3 y_scrape.py
Get file name to parse 
what is the file name? 
Stressed_1.xlsx
```
All the files are then downloaded (Pafy module) and converted to .wav format with FFmpeg ...

## Classification models 
### building optimized classification models
train_audioclassify.py (from CLI)
```
cd ~
cd voicebook/chapter_4_modeling
python3 train_audioclassify.py 
# insert number of classes and class names 
how many classes are you training?2
what is the folder name for class 1?schizophrenia
what is the folder name for class 2?controls
# now all the classes will featurize 
SCHIZOPHRENIA - featurizing snipped38_start_2_end_22.wav
making 0.wav
[-4.51487917e+02  1.32250653e+02 -6.48964827e+02 -2.16927909e+02...
  9.57062705e-04  4.54699943e-02 -5.85259705e-02  5.74577384e-02]
...
Decision tree accuracy (+/-) 0.20779263167344933
0.5733333333333334
Gaussian NB accuracy (+/-) 0.1305543735171076
0.7866666666666667
SKlearn classifier accuracy (+/-) 0.039999999999999994
0.48
Adaboost classifier accuracy (+/-) 0.22666666666666668
0.6366666666666667
Gradient boosting accuracy (+/-) 0.1319090595827292
0.6599999999999999
Logistic regression accuracy (+/-) 0.07557189365836424
0.7366666666666667
Hard voting accuracy (+/-) 0.2341889076033373
0.6766666666666666
K Nearest Neighbors accuracy (+/-) 0.12666666666666668
0.5633333333333332
Random forest accuracy (+/-) 0.2758824226207808
0.7333333333333333
svm accuracy (+/-) 0.13556466271775172
0.7533333333333333

most accurate classifier is Gaussian NB with audio features (mfcc coefficients).
saving classifier to disk. 

Summarizing session…
GaussianNB(priors=None)

['gaussian-nb', 0.7866666666666667, 0.1305543735171076]
```
### loading classification models 
load_audioclassify.py (from CLI)
```
python3 load_audioclassify.py
```
This results in an output:
```
{"filename": "348.wav", "filetype": "audio file", "class": ["controls"], "model": ["schizophrenia_controls_sc_audio.pickle"], "model accuracies": [0.7866666666666667], "model deviations": [0.1305543735171076], "model types": ["gaussian-nb"], "features": [[-322.9664360980726, 59.53868288968913, -462.5294083924505, -166.3993076206564, 131.38738649438437, 52.44671783868567, -33.74398658437562, 227.8102207133376, 9.52738149362727, 28.505927165579884, -90.65927286414657, 71.52976680142815, 9.73530102063688, 25.62432182324615, -66.02663398503707, 73.87513246074612, -1.596002360610912, 22.81632350096357, -87.30807566263049, 41.72876898633217, 0.8865486997595385, 17.735652130525168, -65.99456073539176, 52.43567091641821, -14.286216477070838, 14.128449781073533, -59.836804831757654, 18.175026917411316, -9.131276510645463, 13.701302570519355, -57.44541029310883, 25.74622598177111, -4.545971824836885, 10.899138142787697, -42.116927063121395, 29.536967420470695, -3.4558647963609186, 10.31513522815575, -36.17230935229129, 26.551369428146693, -3.6667095757279236, 10.079488079876286, -33.78123311320836, 26.14112294381864, 5.366060779304841, 8.570956061981061, -19.248854886451802, 38.20513572569962, -5.458667628428172, 7.490745204714798, -31.338790159786562, 12.539046082339311, 0.024288590342538358, 10.584946850085212, -34.52340818393254, 38.15078289969128, -0.156898762979172, 11.158828455811786, -34.10403400345244, 30.973152153233336, 0.020648845552068328, 5.827064754672902, -22.052042500906857, 16.81872640844321, -0.06170338085832314, 5.229174923928, -14.518978383592026, 14.845857302315114, -0.04962607796690964, 4.5211806494022735, -14.998074177634704, 12.378100326632655, 0.07415513595268168, 3.724070455888158, -9.939566189661432, 10.85577098792062, -0.017072005372266726, 2.7463908847692204, -6.600475000502117, 6.524786791283427, -0.02310274039018664, 2.7092557498939636, -7.467322311111723, 7.481090337383571, 0.04464197716713606, 2.198722832501255, -6.88438775831641, 7.844106037059699, 0.045382707259550105, 2.0580935158253872, -6.638462605186588, 5.991186816663746, -0.013702557713332408, 1.9496130791163644, -6.458246324901151, 5.7716202748695, -0.007340250450717803, 1.6409103586116958, -5.380714141939734, 5.539025057788075, 0.011411587050311969, 1.3949062816882583, -4.390308824019425, 4.13132941219398, -291.2947346432915, 49.04737058565422, -381.6816501283554, -222.9638855557117, 158.3460978309033, 23.15415034729552, 99.62697329203677, 189.70121020164896, 7.287058326977949, 30.77474443760493, -38.71222832828984, 56.208286170618955, -1.0950341842073796, 21.3498811006992, -34.41685805740065, 31.926254848624147, -9.172025861857653, 11.511454213511039, -29.874153138705573, 8.203596981294625, 2.6663941698626865, 6.753684660513026, -5.9061357505887955, 19.305474480034082, -14.088225581455214, 17.47630600064678, -49.8886801840349, 8.935818425975743, -13.521963272886959, 8.25999525518404, -24.851695100203774, -0.11752456737790722, -12.762992506945213, 8.598616338770906, -29.72115313687536, 0.05275012294025435, -4.531403069755177, 11.8713757531457, -24.376936764599744, 12.207624665298002, -2.6914750628989266, 14.673164819510685, -22.308447521294887, 17.767626038347583, 11.80700932417913, 10.516802160193405, -13.092759032892214, 24.963056992755536, -10.390953114902164, 6.1887066403103965, -20.39253124562046, 2.7941268719402848, -4.41480192601625, 7.0550461587501, -15.045545852884578, 5.8468320221431656, 0.22555437964894862, 4.881477566532211, -4.990490269946867, 8.519079155558249, 3.4745028409138827, 2.7045163211953187, 0.5391937155699558, 8.988399905874912, 0.45051536549204274, 4.824805683998831, -4.424922867740668, 9.67554223394205, -0.8502687288362012, 3.1351941328536777, -4.844124443962841, 4.754766492721427, 0.870140923131266, 1.1137966493666094, -1.4131441258277446, 2.418345086057676, 2.4254793474500635, 1.2058772715931956, 0.5825294849801214, 4.536777131050609, 0.10251353649615984, 1.51146113365032, -1.4592806547585204, 3.291502702928505, -1.075428938064348, 1.0559521971759946, -2.4408814841825865, 1.12308565480587, -0.3002420005778045, 2.4751693616737347, -3.6333810904861688, 3.34737386167248, 0.17805269515377548, 3.7250267108754236, -5.189309157660288, 5.579262003298437, 0.24091712079378458, 2.451817967640338, -5.215650064568107, 2.3865116769275567, 0.003640041240486553, 1.4235044885102617, -2.379919268715038, 1.5581599658532437]], "count": 0, "errorcount": 0}
```

## Regression models
### training regression models 
train_audioregression.py (from CLI)
```
cd ~
cd voicebook/chapter_4_modeling/
python3 train_audioregression.py
what is the name of the file in /data directory you would like to analyze? 
africanamerican_controls.json
RESULTS: 
+-------------------------------------------+-----------+----------------------+
|                model type                 | R^2 score | Mean Absolute Errors |
+-------------------------------------------+-----------+----------------------+
|             linear regression             |  -1.672   |        0.656         |
+-------------------------------------------+-----------+----------------------+
|             ridge regression              |   0.047   |        0.367         |
+-------------------------------------------+-----------+----------------------+
|                   LASSO                   |   0.426   |        0.273         |
+-------------------------------------------+-----------+----------------------+
|                elastic net                |   0.483   |        0.255         |
+-------------------------------------------+-----------+----------------------+
|       Least angle regression (LARS)       |   0.065   |        0.478         |
+-------------------------------------------+-----------+----------------------+
|                LARS lasso                 |  -0.025   |        0.502         |
+-------------------------------------------+-----------+----------------------+
|     orthogonal matching pursuit (OMP)     |  -0.032   |         0.39         |
+-------------------------------------------+-----------+----------------------+
|            logistic regression            |  -0.019   |        0.253         |
+-------------------------------------------+-----------+----------------------+
|     stochastic gradient descent (SGD)     |  -0.153   |         0.41         |
+-------------------------------------------+-----------+----------------------+
|                perceptron                 |  -7.297   |        1.131         |
+-------------------------------------------+-----------+----------------------+
|        passive-agressive algorithm        |   0.316   |        0.329         |
+-------------------------------------------+-----------+----------------------+
|                  RANSAC                   |   0.316   |        0.329         |
+-------------------------------------------+-----------+----------------------+
|                 Theil-Sen                 |  -1.672   |        0.674         |
+-------------------------------------------+-----------+----------------------+
|             huber regression              |  -0.582   |         0.49         |
+-------------------------------------------+-----------+----------------------+
|      polynomial (linear regression)       |  -0.582   |         0.49         |
+-------------------------------------------+-----------+----------------------+
logistic regression has the lowest mean absolute error (0.25252525252525254)
saving file to disk (africanamerican_controls_regression.pickle)...
```

### loading regression models 
load_audioregression.py
```
python3 load_audioregression.py 
1.0
controls
```
## Deep learning models 
keras_mlp.py
```python3 
from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Generate dummy data
import numpy as np
data = np.random.random((1000, 100))
labels = np.random.randint(2, size=(1000, 1))

# Train the model, iterating on the data in batches of 32 samples
model.fit(data, labels, epochs=10, batch_size=32)
```
### from CLI 
train_audiokeras.py
```
cd ~
cd voicebook/chapter_4_modeling 
python3 train_audiokeras.py
folder name 1 
africanamerican     
folder name 2 
controls
...
[[1.]]
Epoch 1/20
149/149 [==============================] - 0s 2ms/step - loss: 3.8728 - acc: 0.3423
Epoch 2/20
149/149 [==============================] - 0s 29us/step - loss: 0.3178 - acc: 0.3624
Epoch 3/20
149/149 [==============================] - 0s 26us/step - loss: -0.0068 - acc: 0.4228

...
 final acc: 50.34% 
...
 Saved africanamerican_controls_dl_audio.json model to disk
summarizing data...
testing loaded model

'Loaded model from disk'

[[1.]]
```

## AutoML approaches 
### using TPOT for classification 
train_audioTPOT.py
```
cd ~
cd voicebook/chapter_4_modeling/
python3 train_audioTPOT.py
classification (c) or regression (r) problem?
c
what is the name of class 1? 
africanamerican
what is the name of class 2? 
controls
Generation 1 - Current best internal CV score: 0.9056433904259992               
Generation 2 - Current best internal CV score: 0.9100878348704435               
Generation 3 - Current best internal CV score: 0.9100878348704435               
Generation 4 - Current best internal CV score: 0.9100878348704435               
Generation 5 - Current best internal CV score: 0.9191787439613526               
                                                                                
Best pipeline: LogisticRegression(LogisticRegression(MinMaxScaler(StandardScaler(input_matrix)), C=1.0, dual=False, penalty=l1), C=5.0, dual=True, penalty=l2)
saving classifier to disk
```
Loading TPOT classification models: load_audioTPOT.py
```
Jims-MBP:~ jimschwoebel$ cd voicebook/chapter_4_modeling
Jims-MBP:chapter_4_modeling jimschwoebel$ python3 load_audiotpot.py
making 0.wav
making 1.wav
making 2.wav
...
making 36.wav
making 37.wav
making 38.wav
controls
```
### Using TPOT for regression
train_audioTPOT.py (from CLI)
```
cd ~
cd voicebook/chapter_4_modeling/
python3 train_audioTPOT.py

classification (c) or regression (r) problem?
r
what is the name of class 1? 
africanamerican
what is the name of class 2? 
Controls
Generation 1 - Current best internal CV score: -0.06707070707070706             
Generation 2 - Current best internal CV score: -0.06707070707070706             
Generation 3 - Current best internal CV score: -0.06707070707070706             
Generation 4 - Current best internal CV score: -0.062207740346188735            
Generation 5 - Current best internal CV score: -0.062207740346188735            
                                                                                
Best pipeline: KNeighborsRegressor(input_matrix, n_neighbors=4, p=1, weights=distance)
saving classifier to disk
```
Loading TPOT regression models: load_audioTPOT.py
```
Jims-MBP:~ jimschwoebel$ cd voicebook/chapter_4_modeling
Jims-MBP:chapter_4_modeling jimschwoebel$ python3 load_audiotpot.py
making 0.wav
making 1.wav
making 2.wav
...
making 36.wav
making 37.wav
making 38.wav
controls
controls
```

## Resources
If you are interested to read more on any of these topics, check out the documentation below.

**Datasets**
* [Common Voice Dataset](https://www.kaggle.com/mozillaorg/common-voice)
* [Google Audioset](https://research.google.com/audioset/)
* [NeuroLex Disease Dataset](https://github.com/neurolexdiagnostics/train-diseases)

**Data labeling**
* [Pandas](http://pandas.pydata.org)
* [Xlsxwriter](https://xlsxwriter.readthedocs.io/)
* [Pytube](https://github.com/nficano/pytube)

**Featurization**
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* [Librosa](https://librosa.github.io)
* [PyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis)
* [Spacy](https://spacy.io)
* [NLTK](http://www.nltk.org)
* [Gensim](https://radimrehurek.com/gensim/)

**Classification models** 
* [Numpy](http://www.numpy.org)
* [Scikit-learn](https://youtu.be/2kT6QOVSgSg)

**Regression models**
* [Statsmodels](https://www.statsmodels.org/stable/index.html)
* [Scikit-learn](https://youtu.be/2kT6QOVSgSg) 

**Deep learning** 
* [Keras](https://keras.io)
* [Tensorflow](https://www.youtube.com/watch?time_continue=1202&v=t1A3NTttvBA)
* [Deep learning book](http://neuralnetworksanddeeplearning.com/index.html)
* [Udacity class](https://www.udacity.com/course/deep-learning--ud730)

**AutoML** 
* [Autokeras](https://autokeras.com/)
* [TPOT](https://github.com/EpistasisLab/tpot)
* [Devol](https://github.com/joeddav/devol)
* [Clarifai](https://clarifai.com/)
* [H20.ai](https://www.h2o.ai/)
* [DataRobot](https://www.datarobot.com/)
* [Google Cloud ML engine](https://cloud.google.com/ml-engine/)
* [Microsoft Azure ML](https://azure.microsoft.com/en-us/services/machine-learning-studio/)
