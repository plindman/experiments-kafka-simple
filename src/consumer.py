import os
import sys
import time
from kafka import KafkaConsumer
import json

print("Consumer starting up...", flush=True)
KAFKA_BROKER = os.environ['KAFKA_BROKER']
print(f"Connecting to Kafka broker: {KAFKA_BROKER}", flush=True)

max_retries = 5
retry_delay = 5

for attempt in range(max_retries):
    try:
        consumer = KafkaConsumer(
            'sensor_data',
            bootstrap_servers=[KAFKA_BROKER],
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            auto_offset_reset='earliest',
            group_id='my-group',
            enable_auto_commit=True
        )
        print("Successfully connected to Kafka", flush=True)
        break
    except Exception as e:
        print(f"Attempt {attempt + 1} failed to connect to Kafka: {str(e)}", flush=True)
        if attempt < max_retries - 1:
            print(f"Retrying in {retry_delay} seconds...", flush=True)
            time.sleep(retry_delay)
        else:
            print("Max retries reached. Exiting.", flush=True)
            sys.exit(1)

def process_message(message):
    return {k: v.upper() if isinstance(v, str) else v for k, v in message.items()}

print("Waiting for messages...", flush=True)
for message in consumer:
    print(f"Received message: {message}", flush=True)
    data = message.value
    processed_data = process_message(data)
    print(f"Processed: {processed_data}", flush=True)
    print("---", flush=True)

print("Consumer shutting down...", flush=True)