import random
from datetime import datetime, timedelta, timezone

from config import USERS, CONTENT, EVENT_TYPES


def current_time():
    return datetime.now(timezone.utc)


def generate_metadata():
    metadata = []

    publish_time = current_time().isoformat().replace("+00:00", "Z")

    for item in CONTENT:
        metadata.append({
            "content_id": item["content_id"],
            "category": item["category"],
            "creator_id": item["creator_id"],
            "publish_timestamp": publish_time
        })

    return metadata


def generate_event():
    content = random.choice(CONTENT)

    event_time = current_time()

    # 5% late events (35-90 seconds old)
    if random.random() < 0.05:
        delay = random.randint(35, 90)
        event_time = event_time - timedelta(seconds=delay)

    return {
        "user_id": random.choice(USERS),
        "content_id": content["content_id"],
        "event_type": random.choice(EVENT_TYPES),
        "dwell_time_ms": random.randint(1000, 10000),
        "timestamp": event_time.isoformat().replace("+00:00", "Z")
    }