import os
from kafka import KafkaConsumer
import json

KAFKA_BROKER = os.environ.get('KAFKA_BROKER', 'localhost:9092')
consumer = KafkaConsumer('sensor_data',
                         bootstrap_servers=[KAFKA_BROKER],
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

def process_message(message):
    # Simple transformation: convert all string values to uppercase
    return {k: v.upper() if isinstance(v, str) else v for k, v in message.items()}

for message in consumer:
    data = message.value
    processed_data = process_message(data)
    print(f"Received: {data}")
    print(f"Processed: {processed_data}")
    print("---")

# In a more advanced version, you would add code here to store the processed data in a database