#!/usr/bin/env python3

from ast import List
import json
import sys
from random import choice
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from time import time
from confluent_kafka import Producer

def streamTable(recordList:List):
    t1 = time()
    # Parse the command line.
    # parser = ArgumentParser()
    # parser.add_argument('config_file', type=FileType('r'))
    # args = parser.parse_args()

    # # Parse the configuration.
    # # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    # config_parser = ConfigParser()
    # config_parser.read_file(args.config_file)
    # config = dict(config_parser['default'])

    conf = {'bootstrap.servers': 'broker:9092',
        'client.id': 'mssql-to-kafka-producer'}

    # Create Producer instance
    producer = Producer(conf)

    # Optional per-message delivery callback (triggered by poll() or flush())
    # when a message has been successfully delivered or permanently
    # failed delivery (after retries).
    def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            # head = msg.header()
            print("Produced event to topic {topic}: key = {key} value = {value}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))

    # Produce data by selecting random values from these lists.
    topic = "purchases"
    # user_ids = ['eabara', 'jsmith', 'sgarcia', 'jbernard', 'htanaka', 'awalther']
    # products = ['book', 'alarm clock', 't-shirts', 'gift card', 'batteries']

    count = 0
    for r in recordList:
        msg = {
        'sku': str(r['rowguid']),
        'WarehouseId': r['PasswordHash'],
        'BackorderQuantity': r['BusinessEntityID']}

        # user_id = choice(user_ids)
        # product = choice(products)
        producer.produce(topic, key=msg['skq'], value=json.dumps(msg), callback=delivery_callback)
        #count += 1

    # Block until the messages are sent.
    producer.poll(10000)
    producer.flush()
    # producer.close()

    t2 = time()
    print(f'Function executed in {(t2-t1):.4f}s')
