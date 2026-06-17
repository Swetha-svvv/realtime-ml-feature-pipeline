from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream.connectors.kafka import KafkaSink
from pyflink.datastream.connectors.kafka import KafkaRecordSerializationSchema


def create_feature_sink():

    sink = (
        KafkaSink.builder()
        .set_bootstrap_servers("kafka:9092")
        .set_record_serializer(
            KafkaRecordSerializationSchema.builder()
            .set_topic("feature-store")
            .set_value_serialization_schema(
                SimpleStringSchema()
            )
            .build()
        )
        .build()
    )

    return sink