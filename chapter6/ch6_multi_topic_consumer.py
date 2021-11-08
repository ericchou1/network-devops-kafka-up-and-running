import csv
from confluent_kafka import Consumer, Producer
import json 
from datetime import datetime

def invenotry_information(csv_file):
    hardware_addresses = {}
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # first line is header information
            if line_count == 0:
                pass
                line_count += 1
            else:
                hardware_addresses[row[0]] = {'street': row[1],
                                                'city': row[2], 
                                                'zip_code': row[3]
                                            }
                line_count += 1
    return hardware_addresses

# Provides call back for Kafka delivery response
delivered_records = 0
def acked(err, msg):
    global delivered_records
    """Delivery report handler called on
    successful or failed delivery of message
    """
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        delivered_records += 1
        print("Produced record to topic {} partition [{}] @ offset {}"
            .format(msg.topic(), msg.partition(), msg.offset()))


if __name__ == "__main__":
    hardware_addresses = invenotry_information('ch6_hardware_data.csv')

    producer_conf = {'bootstrap.servers': "kafka-1:9092", 'client.id': '1'}
    producer = Producer(producer_conf)

    consumer_conf = {'bootstrap.servers': 'kafka-1:9092', 'group.id': 'ch6_consumer_group_1'}
    consumer = Consumer(consumer_conf)
    consumer.subscribe(['ch6_topic_show_inventory'])
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
                # print(f'Device: {record_key}, Version:', json.loads(record_value)['Output'])

                # construc new record
                # enhance with address record
                try: 
                    address = hardware_addresses[record_key]
                except: 
                    address = {}
                
                new_record_key = record_key.encode("utf-16")
                new_record_value = json.dumps({
                    'Time': str(datetime.now()),
                    'Address': address,
                    'Hardware': json.loads(record_value)['Output']
                })

                # produce to Kafka
                producer.produce("ch6_topic_datacenter_hardware", key=new_record_key, value=new_record_value, on_delivery=acked)
                producer.poll(0)

            producer.flush()

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
