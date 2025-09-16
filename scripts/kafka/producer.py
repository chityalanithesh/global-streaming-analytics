from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for i in range(10):
    data = {'id': i, 'message': f'event-{i}'}
    producer.send('event_topic', value=data)
    print(f"Sent: {data}")
    time.sleep(1)

producer.flush()
