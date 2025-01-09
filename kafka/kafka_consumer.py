from confluent_kafka import Consumer, KafkaException, KafkaError

# Configuration for the Kafka consumer
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'
}

# Create a Kafka consumer
consumer = Consumer(conf)

# Subscribe to the topic
consumer.subscribe(['hello_world'])

try:
    while True:
        # Poll for new messages
        msg = consumer.poll(timeout=1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print('%% %s [%d] reached end at offset %d\n' %
                      (msg.topic(), msg.partition(), msg.offset()))
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            # Proper message
            print('Received message: %s' % msg.value().decode('utf-8'))
            
            # Manually commit the message offset
            consumer.commit(msg)

except KeyboardInterrupt:
    pass
finally:
    # Close down the consumer to commit final offsets
    consumer.close()
