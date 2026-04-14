# cleanup_tokens.py

import sqlite3
import time

DB_NAME = "tenders.db"


def cleanup_expired_tokens():
    """
    Remove tokens older than 24 hours.
    """

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    now = int(time.time())
    one_day = 86400

    c.execute(
        "DELETE FROM verification_tokens WHERE ? - created_at > ?",
        (now, one_day)
    )

    conn.commit()
    conn.close()

    print("Expired tokens removed.")


if __name__ == "__main__":
    cleanup_expired_tokens()