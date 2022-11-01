from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers="localhost:9092")

while True:

    message = b'oi'

    producer.send("quickstart", key=b"python-message", value=message)
    print(message)
    time.sleep(2)
