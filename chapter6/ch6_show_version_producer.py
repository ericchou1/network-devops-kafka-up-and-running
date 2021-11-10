#!/usr/bin/env python3

from confluent_kafka import Producer
import requests
import json
from datetime import datetime

devices = {
    'lax-cor-r1': {'ip': '192.168.2.50'},
    'nyc-cor-r1': {'ip': '192.168.2.60'}
}

def show_version(host, username, password):
    url = f"http://{host}/ins"
    myheaders={'content-type':'application/json-rpc'}
    payload=[
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
        "cmd": "show version",
        "version": 1.2
        },
        "id": 1
    }
    ]
    response = requests.post(url,data=json.dumps(payload), headers=myheaders, auth=(username, password)).json()

    return response['result']['body']


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
    conf = {'bootstrap.servers': "kafka-1:9092", 'client.id': '1'}
    producer = Producer(conf)
    # query_results = []
    for device in devices: 
        # Query for Device Information
        print(f"Querying Information on {device}")
        ip = devices[device]['ip']
        result = show_version(ip, 'cisco', 'cisco')

        # construct record 
        record_key = device.encode("utf-16")
        record_value = json.dumps({
            'Time': str(datetime.now()),
            'Output': result
        })

        # produce to Kafka
        producer.produce("ch6_topic_show_ver", key=record_key, value=record_value, on_delivery=acked)
        producer.poll(0)

    producer.flush()

