#!/bin/bash

# Create src directory
mkdir -p src

# Create files
touch docker-compose.yml
touch src/producer.py
touch src/consumer.py
touch requirements.txt

echo "Project structure created successfully!"
