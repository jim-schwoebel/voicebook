# import required modules 
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import sys,json, os 
import numpy as np

def convert_mono(filename):
    mono=filename[0:-4]+'_mono.wav'
    os.system('ffmpeg -i %s -ac 1 %s'%(filename,mono))
    return mono

filename=sys.argv[1];
print(filename)
mono=convert_mono(filename)
[Fs, x] = audioBasicIO.readAudioFile(mono);
F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs);
os.remove(mono)

data={
    'features': F.tolist()
    }

jsonfile=open(filename[0:-4]+'.json','w')
json.dump(data,jsonfile)
jsonfile.close() 

