'''
Splice.py

From 1 folder of .wav files, create another with snipped 20 sec splices.

Useful to then use the second folder for remixing. 
'''

import soundfile as sf 
import os, ffmpy, random, getpass

fold=input('what folder do you want to create 20 sec splices for?')
splice_length=input('how long (in secs) do you want the splices')

dir1=os.getcwd()+'/'+fold
dir2=os.getcwd()+'/'+fold+'_snipped'

os.chdir(dir1)
os.mkdir(dir2)

listdir=os.listdir()

for i in range(len(listdir)):
    try:
        os.chdir(dir1)
        file=listdir[i]
        data, samplerate = sf.read(file)
        totalframes=len(data)
        totalseconds=int(totalframes/samplerate)
        startsec=random.randint(0,totalseconds-(splice_length+1))
        endsec=startsec+splice_length
        startframe=samplerate*startsec
        endframe=samplerate*endsec
        
        #write file to resave wave file at those frames
        os.chdir(dir2)
        sf.write('snipped_'+file, data[int(startframe):int(endframe)], samplerate)
    except:
        print('error, skipping...')
