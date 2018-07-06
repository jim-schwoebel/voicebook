import sys
import pyttsx3 as pyttsx

def say(text):
    engine = pyttsx.init()
    engine.setProperty('voice','com.apple.speech.synthesis.voice.fiona')
    engine.say(text)
    engine.runAndWait()

say(str(sys.argv[1]))
