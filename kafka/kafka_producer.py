from kafka import KafkaProducer
import json
import random

# Initialize the Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Define a function to send messages
def send_message(topic, message):
    producer.send(topic, value=message)
    producer.flush()
    print(f"Message sent to topic {topic}:{message}")

# Example usage
if __name__ == '__main__':
    topic_name = 'hello_world'
    
    for i in range(100):
        message_data = {i: random.randint(1, 1000)}
        send_message(topic_name, message_data)
