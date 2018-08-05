'''
setup_kafka.py

simple setup of kafka using virtuenv.
Following tutorial here:
https://scotch.io/tutorials/build-a-distributed-streaming-system-with-apache-kafka-and-python
'''
import os

# make directory and install dependencies
os.system('brew install kafka')
os.system('mkdir kafka && cd kafka')
os.system('virtualenv env && source env/bin/activate')
os.system('pip3 install kafka-python sounddevice soundfile')
