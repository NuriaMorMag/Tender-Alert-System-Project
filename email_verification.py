# email_verification.py

import uuid
import time
from database_helper import get_connection


def create_verification_token(email):
    token = str(uuid.uuid4())

    conn = get_connection()
    c = conn.cursor()

    c.execute(
        "INSERT INTO verification_tokens (email, token, created_at) VALUES (%s, %s, %s)",
        (email, token, int(time.time()))
    )

    conn.commit()
    conn.close()

    return token


def verify_token(token):
    conn = get_connection()
    c = conn.cursor()

    c.execute(
        "SELECT email FROM verification_tokens WHERE token = %s",
        (token,)
    )

    result = c.fetchone()
    conn.close()

    if result:
        return result[0]
    return None


def delete_token(token):
    conn = get_connection()
    c = conn.cursor()

    c.execute(
        "DELETE FROM verification_tokens WHERE token = %s",
        (token,)
    )

    conn.commit()
    conn.close()