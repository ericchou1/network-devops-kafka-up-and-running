from confluent_kafka import Consumer
import json 

conf = {'bootstrap.servers': 'kafka-1:9092', 'group.id': 'ch6_consumer_group_1'}

consumer = Consumer(conf)
consumer.subscribe(['ch6_topic_show_ver'])
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        elif msg.error():
            print('error: {}'.format(msg.error()))
        else:
            record_key = msg.key().decode('utf-16')
            record_value = msg.value()
            print(f'Device: {record_key}, Version:', json.loads(record_value)['Output']['sys_ver_str'])

except KeyboardInterrupt:
    pass
finally:
    consumer.close()


