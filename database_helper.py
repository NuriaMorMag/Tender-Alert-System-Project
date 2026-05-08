# database_helper.py

import pymysql
from datetime import datetime

# MySQL connection config
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "tender_alerts"
}


def get_connection():
    """
    Create a new database connection.
    """
    return pymysql.connect(**DB_CONFIG)


def save_user(email):
    """
    Save a user email (ignore duplicates).
    """
    conn = get_connection()
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users (email) VALUES (%s)", (email,))
        conn.commit()
    except:
        pass
    finally:
        conn.close()


def get_users():
    """
    Return all user emails.
    """
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT email FROM users")
    users = c.fetchall()

    conn.close()

    return [u[0] for u in users]


def remove_user(email):
    """
    Delete a user.
    """
    conn = get_connection()
    c = conn.cursor()

    c.execute("DELETE FROM users WHERE email = %s", (email,))
    conn.commit()

    conn.close()


# -------------------------------
# DATE HANDLING (IMPORTANT FIX)
# -------------------------------

def parse_any_date(date_text):
    """
    Convert API / scraped date into datetime safely.
    Supports ISO format: 2026-05-18T12:00:00
    """
    if not date_text:
        return None

    try:
        return datetime.fromisoformat(date_text)
    except:
        return None


def save_tender_if_new(tender_text, date_text):
    """
    Save tender only if it's new.
    Uses safe ISO date parsing.
    """
    conn = get_connection()
    c = conn.cursor()

    try:
        parsed_date = parse_any_date(date_text)

        if not parsed_date:
            return False

        c.execute(
            "INSERT INTO sent_tenders (text, published_date) VALUES (%s, %s)",
            (tender_text, parsed_date)
        )
        conn.commit()
        return True

    except Exception as e:
        print("DB error:", e)
        return False

    finally:
        conn.close()


def get_tender_first_seen(tender_text):
    """
    (Optional legacy function - not used in new logic)
    """
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT first_seen FROM sent_tenders WHERE text = %s", (tender_text,))
    result = c.fetchone()

    conn.close()

    if result:
        return result[0]

    return None