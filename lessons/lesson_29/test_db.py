
import pytest

from db_client import get_connection


@pytest.fixture
def db():
    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL
            )
        """)
    connection.commit()

    yield connection

    connection.rollback()
    connection.close()


def test_db_connection(db):
    with db.cursor() as cursor:
        cursor.execute("SELECT 1")
        assert cursor.fetchone() == (1,)


def test_insert_user(db):
    with db.cursor() as cursor:
        cursor.execute(
            "INSERT INTO users (name) VALUES (%s) RETURNING id",
            ("Alex",)
        )
        user_id = cursor.fetchone()[0]

        assert user_id > 0


def test_select_user(db):
    with db.cursor() as cursor:
        cursor.execute(
            "INSERT INTO users (name) VALUES (%s) RETURNING id",
            ("Maria",)
        )
        user_id = cursor.fetchone()[0]

        cursor.execute(
            "SELECT name FROM users WHERE id = %s",
            (user_id,)
        )
        assert cursor.fetchone() == ("Maria",)


def test_update_user(db):
    with db.cursor() as cursor:
        cursor.execute(
            "INSERT INTO users (name) VALUES (%s) RETURNING id",
            ("Alex",)
        )
        user_id = cursor.fetchone()[0]

        cursor.execute(
            "UPDATE users SET name = %s WHERE id = %s",
            ("John", user_id)
        )

        cursor.execute(
            "SELECT name FROM users WHERE id = %s",
            (user_id,)
        )
        assert cursor.fetchone() == ("John",)


def test_delete_user(db):
    with db.cursor() as cursor:
        cursor.execute(
            "INSERT INTO users (name) VALUES (%s) RETURNING id",
            ("Alex",)
        )
        user_id = cursor.fetchone()[0]

        cursor.execute(
            "DELETE FROM users WHERE id = %s",
            (user_id,)
        )

        cursor.execute(
            "SELECT id FROM users WHERE id = %s",
            (user_id,)
        )
        assert cursor.fetchone() is None
