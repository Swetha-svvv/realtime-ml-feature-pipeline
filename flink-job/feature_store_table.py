def register_feature_store_table(table_env):

    table_env.execute_sql("""
        CREATE TABLE feature_store (

            entity_id STRING,

            feature_name STRING,

            feature_value STRING,

            computed_at STRING

        ) WITH (

            'connector' = 'kafka',

            'topic' = 'feature-store',

            'properties.bootstrap.servers' = 'kafka:9092',

            'properties.group.id' = 'feature-store-group',

            'format' = 'json',

            'scan.startup.mode' = 'earliest-offset'

        )
    """)