import json

from pyflink.common import Duration
from pyflink.common.watermark_strategy import WatermarkStrategy
from pyflink.datastream import StreamExecutionEnvironment

from kafka_source import create_kafka_source


def parse_event(event):

    try:
        data = json.loads(event)

        return {
            "user_id": data["user_id"],
            "content_id": data["content_id"],
            "event_type": data["event_type"],
            "dwell_time_ms": int(data["dwell_time_ms"]),
            "timestamp": data["timestamp"]
        }

    except Exception as e:

        print("Invalid Event:", e)

        return None


def main():

    env = StreamExecutionEnvironment.get_execution_environment()

    env.set_parallelism(1)

    source = create_kafka_source()

    watermark = (
        WatermarkStrategy
        .for_bounded_out_of_orderness(
            Duration.of_seconds(30)
        )
    )

    stream = env.from_source(
        source,
        watermark,
        "User Events"
    )

    parsed_stream = (
        stream
        .map(parse_event)
        .filter(lambda x: x is not None)
    )

    parsed_stream.print()

    env.execute("Real-Time ML Feature Pipeline")


if __name__ == "__main__":
    main()