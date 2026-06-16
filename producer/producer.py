import json
import time

from kafka import KafkaProducer

from config import (
    KAFKA_BOOTSTRAP_SERVERS,
    USER_EVENTS_TOPIC,
    CONTENT_METADATA_TOPIC,
)
from data_generator import generate_metadata, generate_event


producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)


def publish_metadata():
    metadata_list = generate_metadata()

    for metadata in metadata_list:
        producer.send(CONTENT_METADATA_TOPIC, metadata)
        print(f"Metadata sent: {metadata}")

    producer.flush()


def publish_events():
    while True:
        event = generate_event()

        producer.send(USER_EVENTS_TOPIC, event)

        print(f"Event sent: {event}")

        producer.flush()

        time.sleep(1)


def main():
    print("Starting Producer...")

    publish_metadata()

    print("Metadata publishing completed.")

    print("Starting event generation...")

    publish_events()


if __name__ == "__main__":
    main()