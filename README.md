# AWS Playground

## Kafka
### Run ZooKeeper:
`bin/zookeeper-server-start.sh config/zookeeper.properties`

### Run Kafka Server:
`bin/kafka-server-start.sh config/server.properties`

### Create Topic:
`bin/kafka-topics.sh --create --topic topic-name --bootstrap-server localhost:9092 --partitions 2`

### List Topics:
`./bin/kafka-topics.sh --list --bootstrap-server localhost:9092`

### Publish Messages:
`python kafka_producer.py`

### Consume Messages:
`python kafka_consumer.py`