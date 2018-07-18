'''
unpack_files.py

This unpacks any .zip file that stored either .OPUS or .FLAC files.
Then, the files are converted back into .WAV format.

This should make it easier for you to analyze with python libraries,
as most python libraries prefer the .WAV format. 
'''
import zipfile, os, shutil

def unzip(file):
    filepath=os.getcwd()+'/'+file
    folderpath=os.getcwd()+'/'+file[0:-4]
    zip = zipfile.ZipFile(filepath)
    zip.extractall(path=folderpath)

def convert_wav(opusdir):
    curdir=os.getcwd()
    listdir=os.listdir()
    removedfiles=list()

    for i in range(len(listdir)):
        file=listdir[i]
        newfile=file[0:-5]+'.wav'
        if file[-5:] in ['.opus','.flac']:
            if file[-5:]=='.flac':
                os.system('ffmpeg -i %s %s'%(file, newfile))
                os.remove(file)
            elif file[-5:]=='.opus':
                # copy file to opus encoding folder 
                print(file)
                shutil.copy(curdir+'/'+file, opusdir+'/'+file)
                os.chdir(opusdir)
                # encode with opus codec 
                os.system('opusdec %s %s'%(file,newfile))
                shutil.copy(opusdir+'/'+newfile, curdir+'/'+newfile)
                # delete files in opus folder 
                os.remove(file)
                os.remove(newfile)
                # delete .wav file in original dir 
                os.chdir(curdir)
                os.remove(file)

# extract zip file into 'recordings' folder
unzip('recordings.zip')
# now cd into this folder and convert files to wav format
opusdir=os.getcwd()+'/opustools'
os.chdir('recordings')
print(os.listdir())
convert_wav(opusdir)


