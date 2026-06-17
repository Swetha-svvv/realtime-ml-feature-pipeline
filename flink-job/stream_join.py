def create_category_affinity(table_env):

    result = table_env.sql_query("""

        SELECT
            u.user_id,
            m.category,
            COUNT(*) AS affinity_score

        FROM user_events AS u

        JOIN content_metadata AS m

        ON u.content_id = m.content_id

        GROUP BY
            u.user_id,
            m.category

    """)

    return result