from pyflink.datastream.functions import AggregateFunction


class UserFeatureAggregator(AggregateFunction):

    def create_accumulator(self):
        return {
            "total": 0,
            "clicks": 0,
            "dwell": 0
        }

    def add(self, value, accumulator):

        accumulator["total"] += 1

        if value["event_type"] == "click":
            accumulator["clicks"] += 1

        accumulator["dwell"] += value["dwell_time_ms"]

        return accumulator

    def get_result(self, accumulator):

        if accumulator["total"] == 0:
            return {
                "click_rate": 0,
                "avg_dwell_time": 0
            }

        return {
            "click_rate":
                accumulator["clicks"] / accumulator["total"],

            "avg_dwell_time":
                accumulator["dwell"] / accumulator["total"]
        }

    def merge(self, a, b):

        a["total"] += b["total"]
        a["clicks"] += b["clicks"]
        a["dwell"] += b["dwell"]

        return a