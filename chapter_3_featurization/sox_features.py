'''
sox_features.py

Get features using SoX library

Workaround by outputting CLI in txt file and
use function to extract these features.
'''
import os
import numpy as np   

def clean_text(text):
    text=text.lower()
    chars=['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'o','p','q','r','s','t','u','v','w','x','y','z',' ',
           ':', '(',')','-','=',"'.'"]
    for i in range(len(chars)):
        text=text.replace(chars[i],'')

    text=text.split('\n')
    new_text=list()
    # now get new text
    for i in range(len(text)):
        try:
            new_text.append(float(text[i].replace('\n','').replace('n','')))
        except:
            pass
            #print(text[i].replace('\n','').replace('n',''))
                        
    return new_text

def sox_featurize(filename):
    # soxi and stats files 
    soxifile=filename[0:-4]+'_soxi.txt'
    statfile=filename[0:-4]+'_stats.txt'
    os.system('soxi %s > %s'%(filename, soxifile))
    os.system('sox %s -n stat > %s 2>&1'%(filename, statfile))
    # get basic info 
    s1=open(soxifile).read()
    s1_labels=['channels','samplerate','precision',
               'duration','filesize','bitrate','sample encoding']
    s1=clean_text(s1)
    
    s2=open(statfile).read()
    s2_labels=['samples read','length','scaled by','maximum amplitude',
               'minimum amplitude','midline amplitude','mean norm','mean amplitude',
               'rms amplitude','max delta','min delta','mean delta',
               'rms delta','rough freq','vol adj']
    
    s2=clean_text(s2)

    labels=s1_labels+s2_labels
    features=np.array(s1+s2)
    
    return features,labels

features, labels = sox_featurize('test.wav')
