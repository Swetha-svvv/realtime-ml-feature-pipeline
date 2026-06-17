from datetime import datetime

from pyflink.common import Duration
from pyflink.common.watermark_strategy import (
    TimestampAssigner,
    WatermarkStrategy
)


class EventTimestampAssigner(TimestampAssigner):

    def extract_timestamp(self, value, record_timestamp):

        dt = datetime.fromisoformat(
            value["timestamp"].replace("Z", "+00:00")
        )

        return int(dt.timestamp() * 1000)


def create_watermark():

    return (
        WatermarkStrategy
        .for_bounded_out_of_orderness(
            Duration.of_seconds(30)
        )
        .with_timestamp_assigner(
            EventTimestampAssigner()
        )
    )