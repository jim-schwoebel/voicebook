'''
speak.py

This is a short script to playback text in python
in a TTS system.

It's super simple and pyttx3 has great documentation.
You should check it out here:

https://github.com/nateshmbhat/pyttsx3
'''
import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# change text as necessary
# e.g. 'the weather is currently 90 degrees outside.'
text=input('type text to speak here: \n')

# speak output text 
spoken_time=speak_text(text)
    
