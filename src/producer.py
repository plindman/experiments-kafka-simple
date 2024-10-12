import os
from kafka import KafkaProducer
import json
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

KAFKA_BROKER = os.environ.get('KAFKA_BROKER', 'localhost:9092')
producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def generate_message(data):
    return {
        "id": data.get("id", random.randint(1, 1000)),
        "temperature": data.get("temperature", round(random.uniform(0, 40), 2)),
        "humidity": data.get("humidity", round(random.uniform(20, 80), 2))
    }

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    message = generate_message(data)
    producer.send('sensor_data', message)
    return jsonify({"status": "success", "message": message}), 200

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)