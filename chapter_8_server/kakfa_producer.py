'''
kafka_producer.py

Simple kafka producer to send messages on port 9092 
on topic 'test'
'''
from kafka import KafkaProducer
import time 

producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic='test'

for i in range(30):
	print('sending message...%s'%(str(i)))
	producer.send(topic, b'test2')
	time.sleep(1)

print(producer.metrics())
