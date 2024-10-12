# Kafka Docker Python Example with Containerized Producer and Consumer

This project demonstrates a simple example of using Kafka with Docker and Python. It includes a producer that accepts HTTP requests to send messages to a Kafka topic and a consumer that reads these messages, performs a simple transformation, and logs the result. Both the producer and consumer run in Docker containers.

## Prerequisites

- Docker
- Docker Compose

## Project Structure

```
kafka-docker-python/
├── docker-compose.yml
├── Dockerfile.producer
├── Dockerfile.consumer
├── src/
│   ├── producer.py
│   └── consumer.py
└── requirements.txt
```

## Setup and Running

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/kafka-docker-python.git
   cd kafka-docker-python
   ```

2. Start all services using Docker Compose:
   ```
   docker-compose up --build
   ```

This command will build the Docker images for the producer and consumer, and start all services including Kafka and Zookeeper.

## How it works

1. Docker Compose starts Kafka, Zookeeper, producer, and consumer services.
2. The producer runs as a Flask server in a Docker container, exposing an HTTP endpoint.
3. When the producer receives a POST request, it sends the message to the Kafka topic.
4. The consumer runs in another Docker container, connecting to Kafka and continuously reading messages from the topic.
5. The consumer performs a simple transformation on the messages and logs the result.

## Using the HTTP Producer

You can use curl to send requests to the producer:

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

## Viewing logs

To view the logs of a specific service:

```
docker-compose logs -f [service_name]
```

Replace [service_name] with kafka, zookeeper, producer, or consumer.

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

To also remove the built images:
```
docker-compose down --rmi all
```