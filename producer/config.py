KAFKA_BOOTSTRAP_SERVERS = "kafka:9092"

USER_EVENTS_TOPIC = "user-events"
CONTENT_METADATA_TOPIC = "content-metadata"

USERS = [
    "user_1",
    "user_2",
    "user_3",
    "user_4",
    "user_5"
]

CONTENT = [
    {
        "content_id": "movie_1",
        "category": "SciFi",
        "creator_id": "creator_1"
    },
    {
        "content_id": "movie_2",
        "category": "News",
        "creator_id": "creator_2"
    },
    {
        "content_id": "movie_3",
        "category": "Sports",
        "creator_id": "creator_3"
    },
    {
        "content_id": "movie_4",
        "category": "Music",
        "creator_id": "creator_4"
    },
    {
        "content_id": "movie_5",
        "category": "Education",
        "creator_id": "creator_5"
    }
]

EVENT_TYPES = [
    "view",
    "click",
    "like",
    "share"
]