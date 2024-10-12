# Kafka Docker Python Example with HTTP Producer

This project demonstrates a simple example of using Kafka with Docker and Python. It includes a producer that accepts HTTP requests to send messages to a Kafka topic and a consumer that reads these messages, performs a simple transformation, and logs the result.

## Prerequisites

- Docker
- Docker Compose
- Python 3.7+

## Project Structure

```
kafka-docker-python/
├── docker-compose.yml
├── src/
│   ├── producer.py
│   └── consumer.py
└── requirements.txt
```

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/kafka-docker-python.git
   cd kafka-docker-python
   ```

2. Create a virtual environment and install the requirements:
   ```
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Start the Kafka and Zookeeper containers:
   ```
   docker-compose up -d
   ```

4. Run the producer:
   ```
   python src/producer.py
   ```

5. In a new terminal, run the consumer:
   ```
   python src/consumer.py
   ```

## Using the HTTP Producer

The producer now exposes an HTTP endpoint to send messages to Kafka. You can use curl to send requests:

1. Send a message with custom data:
   ```
   curl -X POST -H "Content-Type: application/json" -d '{"id": 123, "temperature": 25.5, "humidity": 60.0}' http://localhost:5000/send
   ```

2. Send a message with partial data (missing fields will be randomly generated):
   ```
   curl -X POST -H "Content-Type: application/json" -d '{"temperature": 30.0}' http://localhost:5000/send
   ```

3. Send a message without any data (all fields will be randomly generated):
   ```
   curl -X POST -H "Content-Type: application/json" -d '{}' http://localhost:5000/send
   ```

4. Check the health of the producer:
   ```
   curl http://localhost:5000/health
   ```

## How it works

1. The producer exposes an HTTP endpoint that accepts POST requests with JSON data.
2. When a request is received, the producer sends the message to a Kafka topic.
3. The consumer reads messages from the topic, performs a simple transformation (uppercase conversion), and logs the result.

## VSCode Development

To set up the project for development in VSCode:

1. Open the project folder in VSCode.
2. Ensure you have the Python extension installed.
3. Select the Python interpreter from the virtual environment:
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS)
   - Type "Python: Select Interpreter"
   - Choose the interpreter from the `.venv` folder

This setup will provide better IntelliSense and linting in VSCode.

## Next steps

To extend this example:
1. Modify the consumer to store the transformed data in a database.
2. Add more complex data processing logic in the consumer.
3. Implement error handling and retry mechanisms.

## Cleaning up

To stop and remove the Docker containers:
```
docker-compose down
```