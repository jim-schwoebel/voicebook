'''
kafka_consumer.py

consumer to consumer messages on topic 'test'
on port 9092.


'''
from kafka import KafkaConsumer

topic='test'
consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092')

# creates a running loop to listen for messages 
for msg in consumer:
	print(msg)