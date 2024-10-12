from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def generate_message():
    return {
        "id": random.randint(1, 1000),
        "temperature": round(random.uniform(0, 40), 2),
        "humidity": round(random.uniform(20, 80), 2)
    }

while True:
    message = generate_message()
    producer.send('sensor_data', message)
    print(f"Produced message: {message}")
    time.sleep(5)
