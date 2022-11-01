from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "quickstart", bootstrap_servers='localhost:9092', group_id='kafka-topics')

for msg in consumer:
    print(msg)
