from pyflink.datastream.functions import ProcessWindowFunction


class UserFeatureWindow(ProcessWindowFunction):

    def process(
        self,
        key,
        context,
        aggregates
    ):

        result = next(iter(aggregates))

        yield {
            "entity_id": key,
            "feature_name": "user_features",
            "feature_value": result,
            "computed_at": str(
                context.window().end
            )
        }