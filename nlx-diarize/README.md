# nlx-diarize

Welcome to the nlx-diarize! 

![](https://media.giphy.com/media/3o6MbmvhgNSyHIu7oA/giphy.gif)

Insert an audio or video file (any format), diarize output into 2 speakers with snipped segments and stitched files (as .zip file). Note that this script is intended to be used for streaming applications, locally or in the cloud.

## Dependencies 

These are the dependencies (in requirements.txt document):

    kafka-python
    pymongo
    importlib
    scipy
    ffmpy
    getpass
    pydub
    numpy

## How to run the script locally

Go to the terminal and type in:

    cd ~
    git clone git@github.com:NeuroLexDiagnostics/nlx-diarize.git
    cd nlx-diarize 
    python3 setup.py 
    git clone git@github.com:NeuroLexDiagnostics/pyAudioAnalysis3.git
    python3 nlx-diarize.py

Once you run this, you should see two new folders in the nlx-diarize directory: nlx-diarize-incoming and nlx-diarize-processed.

In order to diarize a new file (say from like a zoom meeting), put the audio or video file into the nlx-diarize-incoming folder.

The scipt will now process this video or audio file and diarize it into 2 speakers. 

The output will be put into nlx-diarize-processed folder in the form of a .zip file. The .zip file contains folders with speaker 1 and speaker 2 segments, as well as all the stitched segments in each of those folders (that is, all the segments combined into one segment of each speaker), like this: 

![](http://models.neurolexapi.com/uploads/diarizefold.png)

Also, .json file with an output like this: 

![](http://models.neurolexapi.com/uploads/diarize.png)

That was easy! :) 

## References

This script relies on these libraries:

* [pyaudioanalysis3](https://github.com/tyiannak/pyAudioAnalysis/wiki/5.-Segmentation)
* [pydub](https://github.com/jiaaro/pydub)
* [ffmpy](https://pypi.python.org/pypi/ffmpy)
* [sidekit](https://pypi.python.org/pypi/SIDEKIT)

Some research papers on the topic of speaker diarization:

* [LDA for speaker diarization](http://ieeexplore.ieee.org/document/6171836/?arnumber=6171836&abstractAccess=no&userType=inst)
