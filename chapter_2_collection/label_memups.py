'''
label_memups.py

Label a voice file with metadata:
1) Microphone
2) Environment
3) Mode
4) User (distance)
5) Processing
6) Storage 
'''
import os, taglib, json
import sounddevice as sd
import soundfile as sf 

def get_defaults():
    if 'label.json' in os.listdir():
        data=json.load('label.json')
    else:
        mic=input('what is the microphone?')
        env=input('what is the environment?')
        mode=input('what is the mode?')
        sampletype=input('sample type? (e.g. voice)')
        distance=input('what is the distance from mic?')
        process=input('do you use any processing (e.g. SoX noisefloor, .wav--> .opus --> .wav)? if so what?')
        storage=input('where are you storing files?')
        data={
            'microphone':mic,
            'environment':env,
            'mode':mode,
            'sample type': sampletype,
            'distance':distance,
            'processing':process,
            'storage':storage,
        }
            
        jsonfile=open('label.json','w')
        json.dump(data,jsonfile)
        jsonfile.close()
    return data 

def label_sample(file):
    data=get_defaults()    
    audio=taglib.File(os.getcwd()+'/'+file)
    print(audio)
    audio.tags['microphone']=data['microphone']
    audio.tags['environment']=data['environment']
    audio.tags['mode']=data['mode']
    audio.tags['sample type']=data['sample type']
    audio.tags['distance']=data['distance']
    audio.tags['processing']=data['processing']
    audio.tags['storage']=data['storage']
    audio.save()

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')
    label_sample(filename)

file='test.wav'
sync_record(file,10,18000,1)
