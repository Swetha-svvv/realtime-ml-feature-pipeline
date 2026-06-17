import json

from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.window import (
    TumblingEventTimeWindows,
    SlidingEventTimeWindows
)
from pyflink.common.time import Time
from pyflink.common.watermark_strategy import WatermarkStrategy
from pyflink.table import (
    EnvironmentSettings,
    StreamTableEnvironment
)
from stream_join import create_category_affinity

from metadata_table import register_metadata_table
from user_events_table import register_user_events_table

from kafka_source import create_kafka_source
from watermark import create_watermark

from user_features import UserFeatureAggregator
from user_window import UserFeatureWindow

from content_features import ContentFeatureAggregator
from content_window import ContentFeatureWindow

from kafka_sink import create_feature_sink
from feature_mapper import convert_to_json

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

    # -----------------------------
    # Table Environment
    # -----------------------------
    settings = EnvironmentSettings.in_streaming_mode()

    table_env = StreamTableEnvironment.create(
        env,
        environment_settings=settings
    )
    
    register_metadata_table(table_env)
    register_user_events_table(table_env)

    source = create_kafka_source()

    stream = env.from_source(
        source,
        WatermarkStrategy.no_watermarks(),
        "User Events"
    )

    parsed_stream = (
        stream
        .map(parse_event)
        .filter(lambda x: x is not None)
        .assign_timestamps_and_watermarks(
            create_watermark()
        )
    )

    # ------------------------------------
    # User Features (1 Hour Tumbling Window)
    # ------------------------------------

    user_features = (
        parsed_stream
        .key_by(lambda event: event["user_id"])
        .window(
            TumblingEventTimeWindows.of(
                Time.hours(1)
            )
        )
        .aggregate(
            UserFeatureAggregator(),
            UserFeatureWindow()
        )
    )

    # ------------------------------------
    # Content Features (15 Min Sliding Window)
    # ------------------------------------

    content_features = (
        parsed_stream
        .key_by(lambda event: event["content_id"])
        .window(
            SlidingEventTimeWindows.of(
                Time.minutes(15),
                Time.minutes(5)
            )
        )
        .aggregate(
            ContentFeatureAggregator(),
            ContentFeatureWindow()
        )
    )

    user_features.print()

    content_features.print()

    

    env.execute("Real-Time ML Feature Pipeline")


if __name__ == "__main__":
    main()