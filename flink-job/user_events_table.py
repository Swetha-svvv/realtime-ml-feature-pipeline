def register_user_events_table(table_env):

    table_env.execute_sql("""
        CREATE TABLE user_events (

            user_id STRING,
            content_id STRING,
            event_type STRING,
            dwell_time_ms INT,
            `timestamp` STRING,

            event_time AS TO_TIMESTAMP(`timestamp`),

            WATERMARK FOR event_time AS event_time - INTERVAL '30' SECOND

        ) WITH (

            'connector' = 'kafka',
            'topic' = 'user-events',
            'properties.bootstrap.servers' = 'kafka:9092',
            'properties.group.id' = 'user-events-group',

            'format' = 'json',
            'scan.startup.mode' = 'earliest-offset'

        )
    """)