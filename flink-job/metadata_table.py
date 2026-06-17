def register_metadata_table(table_env):

    table_env.execute_sql("""
        CREATE TABLE content_metadata (

            content_id STRING,
            category STRING,
            creator_id STRING,
            publish_timestamp STRING

        ) WITH (

            'connector' = 'kafka',
            'topic' = 'content-metadata',
            'properties.bootstrap.servers' = 'kafka:9092',
            'properties.group.id' = 'metadata-group',

            'format' = 'json',
            'scan.startup.mode' = 'earliest-offset'

        )
    """)