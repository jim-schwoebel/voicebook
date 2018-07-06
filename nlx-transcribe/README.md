# nlx-transcribe

Transcribe audio with the opensource [DeepSpeech model](https://github.com/mozilla/DeepSpeech). This is currently the best opensource library to transcribe voice samples (beats PocketSphinx and others by a long shot).

This repository creates two folders - incoming_samples and processed_samples. All .wav files are converted to 16 bit 16,000 HZ files for processing (this is required). 

Note that all the required model files, etc. are automatically downloaded and executed here to make it easier for you to process data. All you need to do to start is to type this into the terminal:

    cd deepspeech
    git clone 
    python3 nlx-transcribe.py


Reach out if you have any questions!

-JS 

# references
* [DeepSpeech Repository](https://github.com/mozilla/DeepSpeech)
* [PocketSphinx](https://github.com/cmusphinx/pocketsphinx)
