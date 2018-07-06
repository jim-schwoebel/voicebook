import pip, os

os.system("brew install portaudio")

try:
    import pymongo
except:
    pip.main(["install","pymongo"])

try:
    import kafka-python
except:
    pip.main(["install","kafka-python"])

try:
    import webbrowser
except:
    pip.main(["install","webbrowser"])

try:
    import pygame
except:
    pip.main(["install","pygame"])

try:
    import pymongo
except:
    pip.main(["install","pymongo"])
    
try:
    import ftplib
except:
    pip.main(["install","ftplib"])
    
try:
    import pyttsx3 
except:
    pip.main(["install","pyttsx3 "])
    
try:
    import pyttsx3 
except:
    pip.main(["install","pyttsx3 "])
    
try:
    import pyttsx3 
except:
    pip.main(["install","pyttsx3 "])

try:
    import speech_recognition
except:
    pip.main(["install","SpeechRecognition"])
 
try:
    import pyaudio
except:
    pip.main(["install","pyaudio"])

try:
    import wave
except:
    pip.main(["install","wave"])
