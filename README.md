# Voicebook
[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Are%20you%20a%20developer%20looking%20to%20learn%20how%20to%20program%20voice%20applications%20in%20Python?%20Check%20out%20the%20Voicebook%20@%20http://voicebook.neurolex.co.%20&hashtags=voicecomputing,hackvoice,voicebook)

This is an assortment of all the scripts associated with [Intro to Voice Computing Book](http://voicebook.neurolex.co). These scripts should give you a jumpstart in learning how to write Python code for voice-related applications. 

[![Voicebook video](https://github.com/jim-schwoebel/voicebook/blob/master/references/Screen%20Shot%202018-09-30%20at%207.15.03%20AM.png)](https://www.youtube.com/watch?v=7QV-Vlqq2GE "Voicebook intro video")

## Getting started: setting up environment (mac)

*Note that these are the instructions for Mac computers; you may need some custom setup of [FFmpeg](https://www.ffmpeg.org/) and/or [SoX](http://sox.sourceforge.net/) if you're using a Windows and/or Linux computer.* 

First, clone the repository and submodules:

    cd ~
    git clone --recurse-submodules -j8 https://github.com/jim-schwoebel/voicebook

Now you need to run the setup.py script to make sure you have all the required dependencies for all the chapters of the book. To do this, run:

    cd ~
    cd voicebook
    python3 setup.py

Now you have all the dependencies necessary to follow along with the chapters in the book. You don’t need to worry about any other installations. 

## Wiki for additional docs 
Check out the [wiki](https://github.com/jim-schwoebel/voicebook/wiki) for additional documentation around each chapter. These are also included in each folder here in the readmes of each chapter. In this way, you can get quickly up to speed with the 200+ scripts included in this repository. 
* [Chapter 1: Fundamentals](https://github.com/jim-schwoebel/voicebook/wiki/0.1.-Fundamentals)
* [Chapter 2: Collection](https://github.com/jim-schwoebel/voicebook/wiki/0.2.---Collection)
* [Chapter 3: Featurization](https://github.com/jim-schwoebel/voicebook/wiki/0.3.-Featurization)
* [Chapter 4: Data Modeling](https://github.com/jim-schwoebel/voicebook/wiki/0.4.-Data-modeling)
* [Chapter 5: Generation](https://github.com/jim-schwoebel/voicebook/wiki/0.5.-Generation)
* [Chapter 6: Visualization](https://github.com/jim-schwoebel/voicebook/wiki/0.6.-Visualization)
* [Chapter 7: Designing Voice Computers](https://github.com/jim-schwoebel/voicebook/wiki/0.7.-Designing-Voice-Computers)
* [Chapter 8: Designing Server Architectures](https://github.com/jim-schwoebel/voicebook/wiki/0.8.-Designing-server-architectures)
* [Chapter 9: Legal, Security, and Ethical Considerations](https://github.com/jim-schwoebel/voicebook/wiki/0.9.-Legal,-Ethical,-and-Security-Considerations)
* [Chapter 10: Getting involved](https://github.com/jim-schwoebel/voicebook/wiki/1.0.-Getting-involved)
