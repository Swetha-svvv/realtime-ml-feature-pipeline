from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream.connectors.kafka import (
    KafkaSource,
    KafkaOffsetsInitializer
)


def create_kafka_source():

    source = (
        KafkaSource.builder()
        .set_bootstrap_servers("kafka:9092")
        .set_topics("user-events")
        .set_group_id("feature-engineering-group")
        .set_starting_offsets(
            KafkaOffsetsInitializer.earliest()
        )
        .set_value_only_deserializer(
            SimpleStringSchema()
        )
        .build()
    )

    return source