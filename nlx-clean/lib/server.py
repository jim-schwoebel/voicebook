'''
NLX-clean (kafka version)

This microservice takes in a speech sample and cleans it to be processed further along the pipeline.

Specifically, there are a few checks:

    -check if speech sample is provided with a speech sample classifier (speech vs. other)
    -if not .wav format, convert to .wav using ffmpeg (can be a video or any sample) 
    -if not mono signal, convert to mono signal using stereo2mono()

To test this we use a sample bucket in GCP (collect-). This is for sample purposes only.
'''
from __future__ import print_function, division, unicode_literals
import os, json, shutil, time, sys, datetime, pickle
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials 
from kafka import KafkaConsumer, KafkaProducer
import importlib, scipy, ffmpy, getpass, wave, pydub, collections, contextlib, sys, webrtcvad 
import soundfile as sf
import librosa 
from scipy import signal
import scipy.io.wavfile as wav
from scipy.fftpack import fftfreq
import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
from nlx-clean import nlx-clean-kafka as nc

# STEP 2: INSTALL EVERYTHING FOR CRYPTO-CLI
#########################################################
# go to the right directory (docker should have already cloned repository to this location)
os.chdir('/usr/src/app/crypto-cli')
# install the library 
os.system('npm install')

# STEP 3: INSTALL SOX FOR PROCESSING IN CLI 
#########################################################
os.system('brew install sox')

# STEP 4: INITIALIZE GCP AND KAFKA 
#########################################################

# CONNECT TO GCP + RIGHT PROJECT
credentials_dict = {
    'type': 'service_account',
    'client_id': os.environ['BACKUP_CLIENT_ID'],
    'client_email': os.environ['BACKUP_CLIENT_EMAIL'],
    'private_key_id': os.environ['BACKUP_PRIVATE_KEY_ID'],
    'private_key': os.environ['BACKUP_PRIVATE_KEY'],
}
credentials = ServiceAccountCredentials.from_json_keyfile_dict(
    credentials_dict
)

client = storage.Client(credentials=credentials, project='NLX-infrastructure')

#INITIALIZE KAFKA

incoming_topic = 'CREATED_SAMPLE'
outgoing_topic = 'CREATED_CLEANSAMPLE'
bootstrap_servers = ['localhost:29092']

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
consumer = KafkaConsumer(incoming_topic, bootstrap_servers=bootstrap_servers)

print(f'Microservice listening to topic: %s...')

# STEP 5: INITIALIZE LISTS AND VARIABLES 
#########################################################

# gcloud bucket to listen into here
bucketid='nlx-collect-test'
bucketproject="NLX-infrastructure'
bucket_type='gcp'

# create incoming and processed directory
crypto_dir='/usr/src/app/crypto-cli/'
incoming_dir='/usr/src/app/incoming_samples/'
processed_dir='/usr/src/app/processed_samples/'
try:
  os.mkdir(incoming_dir)
except:
  pass 
try:
  os.mkdir(processed_dir)
except:
  pass 
#initialize sleep time for worker (default is 1 second)
sleeptime=1
# now initialize process list with files already in the directory
processlist=list()
convertformat_list=list()
messagelist=list()
#error counts will help us debug later
errorcount=0
processcount=0
#initialize t for infinite loop
t=1

# LOOP THROUGH SAMPLES GENERATED ON TOPIC (COLLECT TOPIC)
#########################################################

#infinite loop for worker now begins with while loop...
while t>0:
  #try statement to reduce errors
  try:
  
    #look for messages / initialize producer for later 
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    consumer = KafkaConsumer(incoming_topic, bootstrap_servers=bootstrap_servers)

    for msg in consumer:
        # download message
        [decrypted_files, encrypted_files]=nc.msgdownload(msg,crypto_dir)
        # download all files in the previous payload message
        nc.download(bucketid,encrypted_files)
        # decrypt uncleaned files
        nc.decrypt(encrypted_files,decrypted_files,crypto_dir, incoming_dir)
        # now loop through and clean all files that are in the folder
        [cleaned_filenames, durations, processtimes, durations2,sizes,sizes2]=nc.clean(decrypted_files, processlist, incoming_dir, hostdir,incoming_dir, processed_dir)
        # encrypt clean files
        cleaned_filenames_encrypted=nc.encrypt(cleaned_filenames, processed_dir, crypto_dir)
        # Upload the local files to Cloud Storage.
        nc.upload(cleaned_filenames_encrypted, bucket)
        # update messages
        metrics=producer.metrics()
        message = nc.clean_msg(cleaned_filenames_encrypted,sizes,durations,durations2,silences,processtimes,sizes2,processcount,errorcount, metrics)
        # send message (to kafka / zookeper, for other microservices to consume)
        producer.send(outgoing_topic,message)
        # update process count (number of times this worker has looped)
        processcount=processcount+1
        #sleep to reduce cpu load
        time.sleep(sleeptime)
      
  except:
      print('error')
      errorcount=errorcount+1
      time.sleep(sleeptime)

    
  
