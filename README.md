# Voicebook

This is an assortment of all the scripts associated with [Intro to Voice Computing Book](). These scripts should give you a jumpstart in learning how to write python code for voice-related applications. 

## Getting started: setting up environment (mac)

First, clone the repository in the terminal application and 

    cd ~
    git clone git@github.com:jim-schwoebel/voicebook.git

Now you need to run the setup.py script to make sure you have all the required dependencies for all the chapters of the book. To do this, run:

    cd ~
    cd voicebook
    python3 setup.py

Now you have all the dependencies necessary to follow along with the chapters in the book. You don’t need to worry about any other installations. Also, the entire book is available in the voicebook folder for you to read :-) 

## Frequently asked questions (FAQs)

### Why are you writing this book?

I’m creating this book because when I first was learning how to program voice applications there was really no one central place to go and learn how to program in voice. I learned by doing, and in doing I struggled through the fragmentation of all the different voice tools and technologies. Python seemed like the best language to get started, as it was simple, had a rich set of libraries for audio processing and manipulation, and had a thriving community. 

Throughout the past 6 months, I have had repeated requests (mostly by the TRIBE members in NeuroLex) for resources on where to look to get started with voice computing. There were a few great places to start - like sharing the librosa library documentation, but this didn’t seem like enough to get through the activation energy necessary to thrive in this space. I would find myself taking some breakout sessions with TRIBE members to hack code together to model voice files. Soon, my time became limited (as a CEO of a company), and I needed a way to scale this knowledge in a more repeatable way.

Moreover, I felt like this knowledge I had could be useful for anyone who wants to get involved programming in voice. Many of the scripts I have open-sourced under an Apache 2.0 license. This will give you flexibility for using these scripts for commercial applications. We need more startups in this space! :-) 

### Who is the target audience?

Anyone who is interested to begin learning how to program voice interfaces in python. It helps to know some python, though it is not necessary. 

If you’re looking for another book to start learning python before you read this book, I would recommend Automating the Boring Stuff or the NLTK book; both are quite well-written and freely accessible.

### How do I provide feedback?

I welcome any feedback on this book. The best way to give feedback is through adding an issue on the github repository. If you could follow these best practices for providing feedback, it would greatly help with resolving any issues:

Go to ‘issues tab’ of the repository at this link.
Select ‘new issue’ to provide feedback, assign this to ‘jim-schwoebel’ (my github username), label the issue as an enhancement, and assign it to the project ‘Book feedback.’ 

Add in the page number that you’re commenting about in the title and the issue (e.g. Page 35 - Table 1.1.1 mis-labeled). 
In the description, add in what you think should be fixed (e.g. The table is not labeled properly. The proper label should be Table 1.3.4. Also, the description is a bit unclear. You may want to eliminate the last sentence). 

## References 
* [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis)
* [librosa](https://github.com/librosa/librosa)
* [speechrecognition](https://pypi.org/project/SpeechRecognition/)
