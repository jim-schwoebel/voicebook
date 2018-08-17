*This section documents all the scripts in the Chapter_7_design folder.*
 
## Definitions 
| Term | Definition | 
| ------- | ------- |
| voice computer | any computerized system that can process voice inputs. | 
| voice computing software | examples include Alexa Voice Service (AVS), the Google Assistant SDK, the Cortana skills kit, the Jovo software framework, Jasper software, Mycroft AI, and Nala. | 
| voice computing hardware | examples include desktop personal computers (PCs), laptops, raspberry pis, arduinos, cell phones, and various smart speakers (e.g. Amazon echo) to name a few. | 

## Hardware
### Bluetooth connections 
bluetooth.py
```python3
import bluetooth
from bluetooth.ble import DiscoveryService

# The MAC address of a Bluetooth adapter on the server.
# The server might have multiple Bluetooth adapters.
hostMACAddress = '00:1f:e1:dd:08:3d'
serverMACAddress = hostMACAddress
# 3 is an arbitrary choice. However, it must match the port used by the client.
port = 3
    
def get_devices():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("found %d devices" % len(nearby_devices))
    for addr, name in nearby_devices:
        print("  %s - %s" % (addr, name))
    
    return nearby_devices 

def bluetooth_send(serverMACAddress, port, data):
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((serverMACAddress, port))
    s.send(data)
    sock.close()

def bluetooth_receive(hostMACAddress, port):
    # receive data 
    backlog = 1
    size = 1024
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.bind((hostMACAddress, port))
    s.listen(backlog)
    try:
        client, clientInfo = s.accept()
        while 1:
            data = client.recv(size)
            if data:
                print(data)
                client.send(data) # Echo back to client
    except:	
        print("Closing socket")
        client.close()
        s.close()
```
### Wifi connections 
wifi.py
```python3
from wireless import Wireless

# connect to wireless network 
wireless=Wireless()
ssid='I_am_cool'
password='password'
wireless.connect(ssid='ssid', password='password')

# various things you can get 
print(wireless.current())
print(wireless.interfaces())
print(wireless.interface())
print(wireless.power())
print(wireless.driver())
```
### serial connections 
pyserial.py
```python3
import serial

# simple example of opening serial port and closing it 
ser = serial.Serial()
ser.baudrate = 19200
ser.port = 'COM1'
print(ser)
ser.open()
print(ser.is_open) 
# write some data 
ser.write(b'hello')
ser.close()
print(ser.is_open) # False
```

## Software 
### wakewords with pocketsphinx 
wake_pocket.py
```python3
import os, pyaudio, pyttsx3 
from pocketsphinx import *

def speak():
    engine = pyttsx3.init()
    engine.say("hello!!")
    engine.runAndWait() 

def pocket_detect(key_phrase):

    modeldir = os.path.dirname(pocketsphinx.__file__)+'/model'



    # Create a decoder with certain model
    config = pocketsphinx.Decoder.default_config()
    # config.set_string('-hmm', os.path.join(modeldir, 'en-us/en-us'))
    config.set_string('-dict', modeldir+'/cmudict-en-us.dict')
    config.set_string('-hmm', os.path.join(modeldir, 'en-us'))
    config.set_string('-keyphrase', key_phrase)
    config.set_float('-kws_threshold', 1)

    # Start a pyaudio instance
    p = pyaudio.PyAudio()
    # Create an input stream with pyaudio
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    # Start the stream
    stream.start_stream()

    # Process audio chunk by chunk.
    decoder = pocketsphinx.Decoder(config)
    decoder.start_utt()
    # Loop forever
    while True:
        # Read 1024 samples from the buffer
        buf = stream.read(1024)
        # If data in the buffer, process using the sphinx decoder
        if buf:
            decoder.process_raw(buf, False, False)
        else:
            break
        # If the hypothesis is not none, the key phrase was recognized
        if decoder.hyp() is not None:
            keyphrase_function(keyword)
            # Stop and reinitialize the decoder
            decoder.end_utt()
            decoder.start_utt()
            speak()
            break 

def keyphrase_function(keyword):
    print("Keyword %s detected!"%(keyword))

keyword='test'
pocket_detect(keyword)
```
### wakewords with snowboy (using CLI)
wake_snow.py
```
cd ~
cd voicebook/chapter_7_design/snowboy
python3 hey_nala.pmdl
```
### wakewords with porcupine
training models
```
cd ~
git clone https://github.com/Picovoice/Porcupine.git
cd porcupine 
tools/optimizer/mac/x86_64/pv_porcupine_optimizer -r resources -w "hey test" -p mac -o ~/voicebook/chapter_7_design/porcupine/
```
run model 
```
cd ~
cd voicebook/chapter_7_design/porcupine
python3 porcupine_demo.py --keyword_file_paths “hey test.ppn”
```

### loading custom PocketSphinx language models
transcribe_custom.py
```python3
import os, sys
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
import sounddevice as sd
import soundfile as sf

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

# Get all the directories right
def transcribe(sample):

    modeldir=os.getcwd()+'/data'
    # Create a decoder with certain model
    config = Decoder.default_config()
    config.set_string('-hmm', modeldir+'/en-us')
    config.set_string('-lm', modeldir+'/TAR4311/4311.lm')
    config.set_string('-dict', modeldir+'/TAR4311/4311.dic')
    decoder = Decoder(config)

    # Decode streaming data.
    decoder = Decoder(config)
    decoder.start_utt()
    stream = open(sample, 'rb')
    while True:
      buf = stream.read(1024)
      if buf:
        decoder.process_raw(buf, False, False)
      else:
        break
    decoder.end_utt()

    #print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])
    output=[seg.word for seg in decoder.seg()]
    try:
        output.remove('<s>')
        output.remove('</s>')

        transcript = ''
        for i in range(len(output)):
            if output[i] == '<sil>':
                pass 
            elif i == 0:
                transcript=transcript+output[i]
            else:
                transcript=transcript+' '+output[i]

        transcript=transcript.lower()
        print('transcript: '+transcript)
    except:
        transcript=''

    return transcript

t=1
i=0



while t>0:
    sync_record('test.wav',3,16000,1)
    transcribe('test.wav')
``` 

## Nala: a voice assistant 
See [Nala's documentation](https://github.com/jim-schwoebel/nala).

![](https://media.giphy.com/media/VDzVG8lvNRufu/giphy.gif)

## Resources
If you are interested to read more on any of these topics, check out the documentation below.

**Bluetooth**
* [Pybluez](https://github.com/pybluez/pybluez)

**Wifi**
* [Wireless](https://github.com/joshvillbrandt/wireless)
* [Wifi](https://pypi.org/project/python-wifi/)

**Serial connections**
* [Pyserial](https://github.com/pyserial/pyserial)
* [PyVISA](https://pyvisa.readthedocs.io/en/stable/getting.html)

**Wakeword detectors** 
* [PocketSphinx](https://cmusphinx.github.io/wiki/) 
* [Snowboy](http://docs.kitt.ai/snowboy/) 
* [Porcupine](https://github.com/Picovoice/Porcupine)

**Transcription models** 
* [PocketSphinx Language models](https://cmusphinx.github.io/wiki/tutoriallm/) 
* [PyKaldi](https://github.com/pykaldi/pykaldi) 
* [LIUM diarization models](http://www-lium.univ-lemans.fr/diarization/doku.php/related_projects) 

**Nala: building voice assistants** 
* [Sys](https://docs.python.org/2/library/sys.html)
* [Os](https://docs.python.org/3/library/os.html)
* [Porcupine](https://github.com/Picovoice/Porcupine)
* [Pyttsx3](https://pyttsx3.readthedocs.io/en/latest/) 
* [PocketSphinx](https://cmusphinx.github.io/wiki/tutoriallm/)
