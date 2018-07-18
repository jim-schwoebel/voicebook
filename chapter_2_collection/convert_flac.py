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

def convert_flac():
    listdir=os.listdir()
    removedfiles=list()
    for i in range(len(listdir)):
        if listdir[i][-4:]!='flac':
            file=listdir[i]
            newfile=file[0:-4]+'.flac'
            os.system('ffmpeg -i %s %s'%(file,newfile))
            os.remove(file)
            removedfiles.append(file)
    return removedfiles 

# get 10 files recorded in 'recordings' folder in current directory
# record them if the folder doesn't exist 
hostdir=os.getcwd()
if 'recordings' not in os.listdir():
    os.system('python3 ps_record.py')

# change to directory of recordings to compress all files in directory 
os.chdir(hostdir+'/recordings')
convert_flac()

# change back to main directory and compress files, delete main folder 
os.chdir(hostdir)
zipdir('recordings', True)
