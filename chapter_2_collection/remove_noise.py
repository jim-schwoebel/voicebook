'''
remove_noise.py

Given an audio file, remove the noise from the first 100 milliseconds of audio.

This is good at removing things such as air conditioning noise from
the raw audio.
'''
import soundfile as sf
import os

def remove_noise(filename):
    #now use sox to denoise using the noise profile
    data, samplerate =sf.read(filename)
    duration=data/samplerate
    first_data=samplerate/10
    filter_data=list()
    for i in range(int(first_data)):
        filter_data.append(data[i])
    noisefile='noiseprof.wav'
    sf.write(noisefile, filter_data, samplerate)
    os.system('sox %s -n noiseprof noise.prof'%(noisefile))
    filename2='tempfile.wav'
    filename3='tempfile2.wav'
    noisereduction="sox %s %s noisered noise.prof 0.21 "%(filename,filename2)
    command=noisereduction
    #run command 
    os.system(command)
    print(command)
    #reduce silence again
    #os.system(silenceremove)
    #print(silenceremove)
    #rename and remove files 
    os.remove(filename)
    os.rename(filename2,filename)
    #os.remove(filename2)
    os.remove(noisefile)
    os.remove('noise.prof')

    return filename

remove_noise('test.wav')
