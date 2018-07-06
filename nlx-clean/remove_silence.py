import soundfile as sf
import scipy.signal
import numpy as np 
import getpass,os,time

curdir=os.getcwd()+'/'
filename='test235.wav'
outfilename='new_file.wav'
#threshold determined from experimental testing 
threshold=0.0001
#input('what is the filename?')

data, samplerate = sf.read(filename)

datalist=list()
for i in range(len(data)):
    framemean=np.mean([abs(data[i][0]),abs(data[i][1])])
    if framemean>=threshold:
        datalist.append(np.array([data[i][0],data[i][1]]))
    else:
        pass

#TESTING
#########################################################
#this if for testing what should be cut, etc. 
for i in range(0,len(data),samplerate):
    print(np.mean([abs(data[i][0]),abs(data[i][1])]))
    time.sleep(0.5)
#########################################################

#seconds cleaned
    
datalist=np.array(datalist)

sampledelta=len(data)-len(datalist)
time=sampledelta/samplerate

print('cut off %s seconds'%(str(time)))

try:
    sf.write(outfilename, datalist, samplerate)
    #can remove original file too...
except:
    print('error writing file')

if os.path.getsize(outfilename)<1000:
    print('silence file detected, deleting file...')
    os.remove(outfilename)

###delete silence segment
##type(data)
##len(data)
##type(samplerate)

#write data
