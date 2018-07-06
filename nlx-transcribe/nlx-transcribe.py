import os, json, time, shutil

#directory listings
host_dir=os.getcwd()
incoming_dir=os.getcwd()+'/incoming_samples'
processed_dir=os.getcwd()+'/processed_samples'

#folder for audio files 
try:
    os.mkdir(incoming_dir)
except:
    pass

#folder for processed transcripts
try:
    os.mkdir(processed_dir)
except:
    pass

# run featurizer in current directory (assumes these commands are run)
os.chdir(incoming_dir)
if 'models' not in os.listdir():
    os.system('brew install wget')
    os.system('brew install ffmpeg')
    os.system('pip3 install deepspeech')
    os.system('wget https://github.com/mozilla/DeepSpeech/releases/download/v0.1.1/deepspeech-0.1.1-models.tar.gz')
    os.system('tar -xvzf deepspeech-0.1.1-models.tar.gz')

#now run while loop to transcribe samples
t=1
processed_files=list()
processed_files.append('models')
processed_files.append('.DS_Store')
processed_files.append('deepspeech-0.1.1-models.tar.gz')
processcount=0
errorcount=0

while t>0:
    try:
        os.chdir(incoming_dir)
        g=os.listdir()
        for i in range(len(g)):
            file=g[i]
            if file not in '.DS_Store' and file not in processed_files:
                # convert to .wav with proper bitrate
                start=time.time()
                filename='mono_'+file[0:-4]+'.wav'
                textfilename='text_file_%s.txt'%(str(processcount))
                command='ffmpeg -i %s -acodec pcm_s16le -ac 1 -ar 16000 %s'%(file,filename)
                os.system(command)
                os.remove(file)

                # convert deepspeech model
                command='deepspeech models/output_graph.pb %s models/alphabet.txt models/lm.binary models/trie >> %s'%(filename,textfilename)
                os.system(command)

                # now read text file
                transcript=open(textfilename).read()

                end=time.time()
                processtime=end-start
                
                # get transcript 
                os.chdir(processed_dir)
                data={
                    'name':file,
                    'processtime':processtime,
                    'transcript':transcript,
                    'processcount':processcount,
                    'errorcount':errorcount,
                    }
                
                jsonfilename=file[0:-4]+'.json'
                jsonfile=open(jsonfilename,'w')
                json.dump(data,jsonfile)
                jsonfile.close()

                # append file to list
                shutil.move(incoming_dir+'/'+filename,processed_dir+'/'+filename)
                shutil.move(incoming_dir+'/'+textfilename,processed_dir+'/'+textfilename)
                
                processed_files.append(file)
                processcount=processcount+1

    except:
        print('error')
        errorcount=errorcount+1 
        
    time.sleep(1)
