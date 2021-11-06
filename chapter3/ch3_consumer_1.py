from confluent_kafka import Consumer


conf = {'bootstrap.servers': 'kafka-1:9092', 'group.id': 'ch3_consumer_group'}

consumer = Consumer(conf)
consumer.subscribe(['ch3_topic_1'])
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        elif msg.error():
            print('error: {}'.format(msg.error()))
        else:
            record_key = msg.key()
            record_value = msg.value()
            print(record_key, record_value)

except KeyboardInterrupt:
    pass
finally:
    consumer.close()


