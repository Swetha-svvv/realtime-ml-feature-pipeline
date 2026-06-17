import json
import pandas as pd
import streamlit as st
from kafka import KafkaConsumer

st.set_page_config(
    page_title="Real-Time ML Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Real-Time ML Dashboard")
st.write("Live User Events from Kafka")

consumer = KafkaConsumer(
    "user-events",
    bootstrap_servers="kafka:9092",
    group_id=None,                      # Don't commit offsets
    auto_offset_reset="earliest",       # Read available events
    enable_auto_commit=False,
    consumer_timeout_ms=3000,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

events = []

try:
    for message in consumer:
        events.append(message.value)

        # Show only the latest 50 events
        if len(events) >= 50:
            break
finally:
    consumer.close()

if events:
    df = pd.DataFrame(events)

    st.success(f"Loaded {len(df)} events from Kafka")

    st.dataframe(
        df.tail(50),
        use_container_width=True
    )
else:
    st.warning("No events found.")