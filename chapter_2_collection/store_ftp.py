'''
save_ftp.py

Collect a speech file and them upload it to a FTP server.

Note that this requires two environment variables:
os.environ['DOMAIN_USER']
os.environ['DOMAIN_PASSWORD']

These can be setup going to 
cd~
open .bash_profile

Then insert the domain user and password here like:
export DOMAIN_NAME='domainname'
export DOMAIN_USER='user'
export DOMAIN_PASSWORD='password'
'''
import sounddevice as sd
import soundfile as sf 
import time, os, shutil 
from ftplib import FTP

def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')
    return filename 

def upload_file(file, session)
    uploadfile = open(file,'rb')
    session.storbinary('STOR %s'%(file),uploadfile,1024)
    uploadfile.close() 

# get environment variables 
domain=os.environ['DOMAIN_NAME']
username=os.environ['DOMAIN_USER']
password=os.environ['DOMAIN_PASSWORD']

# log into session
session = ftplib.FTP(domain,username,password)

# record sample (note, could loop through and record samples with while loop)
file = sync_record('test.wav',10,16000,1)

# upload to server
upload_file(file, session)

# log off server 
session.quit() 
