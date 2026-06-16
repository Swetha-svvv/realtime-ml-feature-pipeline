#!/bin/bash

echo "Waiting for Kafka..."

sleep 30

echo "Creating user-events topic..."

kafka-topics \
--bootstrap-server kafka:9092 \
--create \
--if-not-exists \
--topic user-events \
--partitions 3 \
--replication-factor 1

echo "Creating content-metadata topic..."

kafka-topics \
--bootstrap-server kafka:9092 \
--create \
--if-not-exists \
--topic content-metadata \
--partitions 1 \
--replication-factor 1 \
--config cleanup.policy=compact

echo "Creating feature-store topic..."

kafka-topics \
--bootstrap-server kafka:9092 \
--create \
--if-not-exists \
--topic feature-store \
--partitions 1 \
--replication-factor 1 \
--config cleanup.policy=compact

echo "Topics created successfully."