from pyflink.datastream.functions import ProcessWindowFunction


class ContentFeatureWindow(ProcessWindowFunction):

    def process(
        self,
        key,
        context,
        aggregates
    ):

        result = next(iter(aggregates))

        yield {
            "entity_id": key,
            "feature_name": "engagement_rate",
            "feature_value": result["engagement_rate"],
            "computed_at": str(context.window().end)
        }