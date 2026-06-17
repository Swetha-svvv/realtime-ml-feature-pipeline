from pyflink.datastream.functions import AggregateFunction


class ContentFeatureAggregator(AggregateFunction):

    def create_accumulator(self):
        return {
            "views": 0,
            "likes": 0,
            "shares": 0
        }

    def add(self, value, acc):

        if value["event_type"] == "view":
            acc["views"] += 1

        elif value["event_type"] == "like":
            acc["likes"] += 1

        elif value["event_type"] == "share":
            acc["shares"] += 1

        return acc

    def get_result(self, acc):

        if acc["views"] == 0:
            engagement_rate = 0

        else:
            engagement_rate = (
                acc["likes"] + acc["shares"]
            ) / acc["views"]

        return {
            "engagement_rate": engagement_rate
        }

    def merge(self, a, b):

        a["views"] += b["views"]
        a["likes"] += b["likes"]
        a["shares"] += b["shares"]

        return a