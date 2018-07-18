'''
convert_flac.py

Quick script to collect some audio files in .wav format, 
then transcode these audio files into .FLAC format, and then
compress all the files in the folder into a .zip file. 

Compressing to .FLAC format is lossless and takes up about
1/2 as much file space as do .wav files. I recommend using 
this format if storing a large volume of data on a server. 
'''
import shutil, os, ffmpy 

def zipdir(folder, delete):
    # ziph is zipfile handle
    shutil.make_archive(folder, 'zip', folder)
    if delete == True:
        shutil.rmtree(folder)

def convert_opus(opusdir):
    curdir=os.getcwd()
    listdir=os.listdir()
    removedfiles=list()
    for i in range(len(listdir)):
        if listdir[i][-4:]!='opus':
            # get new file names 
            file=listdir[i]
            newfile=file[0:-4]+'.opus'
            # copy file to opus encoding folder 
            shutil.copy(curdir+'/'+file, opusdir+'/'+file)
            os.chdir(opusdir)
            # encode with opus codec 
            os.system('opusenc %s %s'%(file,newfile))
            shutil.copy(opusdir+'/'+newfile, curdir+'/'+newfile)
            # delete files in opus folder 
            os.remove(file)
            os.remove(newfile)
            # delete .wav file in original dir 
            os.chdir(curdir)
            os.remove(file)
            removedfiles.append(file)
    return removedfiles 

# get 10 files recorded in 'recordings' folder in current directory
# record them if the folder doesn't exist 
hostdir=os.getcwd()
opusdir=hostdir+'/opustools'
if 'recordings' not in os.listdir():
    os.system('python3 ps_record.py')

# change to directory of recordings to compress all files in directory 
os.chdir(hostdir+'/recordings')
convert_opus(opusdir)

# change back to main directory and compress files, delete main folder 
os.chdir(hostdir)
zipdir('recordings', True)
