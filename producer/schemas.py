USER_EVENT_SCHEMA = {
    "user_id": str,
    "content_id": str,
    "event_type": str,
    "dwell_time_ms": int,
    "timestamp": str
}

CONTENT_METADATA_SCHEMA = {
    "content_id": str,
    "category": str,
    "creator_id": str,
    "publish_timestamp": str
}

FEATURE_STORE_SCHEMA = {
    "entity_id": str,
    "feature_name": str,
    "feature_value": object,
    "computed_at": str
}