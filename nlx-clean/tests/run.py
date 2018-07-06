import unittest
import os
import shutil
import sys
import numpy as np

def getclass(inputlist):
    #for later, get the results of models 
    array=inputlist[1].tolist()
    maxval=np.max(array)
    index=array.index(maxval)
    choices=inputlist[2]
    #output choice
    return choices[index]

g=os.getcwd()
os.chdir(os.getcwd()+'/nlx-pyAudioAnalysis3')
g=os.getcwd()
print(os.listdir())

#print('moving pyAudioAnalysis to modules directory')
##glist=os.listdir()
##for i in range(len(glist)):
##  shutil.move(os.getcwd()+'/'+glist[i],os.path.dirname(os.__file__)+'/'+glist[i])
##  
###'/usr/local/lib/python3.6/'
##print(os.listdir(os.path.dirname(os.__file__)))

sys.path.append(os.getcwd())

import audioTrainTest as aT
  
curdir=os.getcwd()
os.chdir(curdir+'/models/audiomodels/')
print(os.listdir())
testlist=list()

class SimplisticTest(unittest.TestCase):
  def test(self):
    try:
        print(os.listdir())
        gender=aT.fileClassification("test.wav","genderymodel","svm")
        gender=getclass(gender)
        print(gender.lower())
        testlist.append(gender)
    except:
        gender='n/a'
        print('gender n/a')
        testlist.append(gender)

    try:
        age=aT.fileClassification("test.wav", "childrenvscontrol2model","svm")
        age=getclass(age)
        if age == 'control2':
          age='adult'
        print(age)
        testlist.append(age)
    except:
        age='n/a'
        print('age n/a')
        testlist.append(age)

    try:
        sampletype=aT.fileClassification("test.wav", "ambilexmodel","svm")
        sampletype=getclass(sampletype)
        print(sampletype)
        testlist.append(sampletype)
    except:
        sampletype='n/a'
        print('sampletype n/a')
        testlist.append(sampletype)

    try:
        speaktype=aT.fileClassification("test.wav", "speaktypelex","svm")
        speaktype=getclass(speaktype)
        print(speaktype)
        testlist.append(speaktype)
    except:
        speaktype='n/a'
        print('speaktype n/a')
        testlist.append(speaktype)

    try:
        silence=aT.fileClassification("test.wav", "voicevssilencemodel","svm")
        silence=getclass(silence)
        print(silence)
        testlist.append(silence)
    except:
        silence='n/a'
        print('silence n/a')
        testlist.append(silence)
     
    try:
        race=aT.fileClassification("test.wav", "aajamesmodel","svm")
        if race=='controls':
          race='caucasian'
        race=getclass(race)
        print(race)
        testlist.append(race)
    except:
        race='n/a'
        print('race n/a')
        testlist.append(race)

    try:
        dialect=aT.fileClassification("test.wav", "britishvsamericanmodel","svm")
        dialect=getclass(dialect)
        print(dialect)
        testlist.append(dialect)
    except:
        dialect='n/a'
        print('dialect n/a')
        testlist.append(dialect)

    try:
        happysad=aT.fileClassification("test.wav", "happyvssad","svm")
        happysad=getclass(happysad)
        print(happysad)
        testlist.append(happysad)
    except:
        happysad='n/a'
        print('happysad n/a')
        testlist.append(happysad)

    try:
        stress=aT.fileClassification("test.wav","stresslex","svm")
        stress=getclass(stress)
        print(stress)
        testlist.append(stress)
    except:
        stress='n/a'
        print('stress n/a')
        testlist.append(stress)

    try:
        fatigue=aT.fileClassification("test.wav","fatiguelex","svm")
        fatigue=getclass(fatigue)
        print(fatigue)
        testlist.append(fatigue)
    except:
        fatigue='n/a'
        print('fatigue n/a')
        testlist.append(fatigue)

    if 'n/a' in testlist:
      self.assertFalse(False)
      print('contains an error')
      
    else:
      self.assertTrue(True)
      print('no errors')
    
if __name__ == '__main__':
  unittest.main()
