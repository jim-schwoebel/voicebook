'''
kafka_producer.py

simple producer on localhost port 9092

'''
import time, sounddevice, soundfile
import numpy as np 
from kafka import SimpleProducer, KafkaClient

#  connect to Kafka
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)
# Assign a topic
topic = 'RECORDED_AUDIOFILE'

def audio_emitter(file, duration, fs, channels):
    # Make 1 second audio file 
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    message=myrecording.tobytes()
    producer.send_messages(topic, message) 
    print('done emitting')

if __name__ == '__main__':
    audio_emitter('test.wav',1,16000, 1)
