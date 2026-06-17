import json


def convert_to_json(feature):

    return json.dumps({

        "entity_id": feature["entity_id"],

        "feature_name": feature["feature_name"],

        "feature_value": feature["feature_value"],

        "computed_at": feature["computed_at"]

    })