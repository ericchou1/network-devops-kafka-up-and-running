from confluent_kafka import Producer
import json
from datetime import datetime


conf = {'bootstrap.servers': "kafka-1:9092", 'client.id': '1'}
producer = Producer(conf)

for n in range(5):
    # new in ch3_producer_2.py
    record_key = "100"
    record_value = json.dumps(
              {
                  "Time": str(datetime.now())
              }
            )
    topic = "ch3_topic_1"
    producer.produce(topic, key=record_key, value=record_value)


producer.flush()


