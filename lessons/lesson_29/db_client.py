import os

import psycopg


def get_connection():

    return psycopg.connect(
        host=os.getenv("DB_HOST", "postgres-db"),
        port=5432,
        dbname="qa_db",
        user="qa_user",
        password=os.environ["DB_PASSWORD"]
    )