from database_helper import get_connection
import time

def cleanup_expired_tokens():
    conn = get_connection()
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