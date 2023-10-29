from kafka import KafkaProducer
import time
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
    message = {'key': 'value'}  # Replace this with your desired message content (can be a string or JSON object)
    producer.send('test-topic', json.dumps(message).encode('utf-8'))
    print('Message sent:', message)
    time.sleep(1)  # Sends a message every second
