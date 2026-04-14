# database_helper.py

import pymysql

# MySQL connection config
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
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


def save_tender_if_new(tender_text):
    """
    Save tender if not already stored.
    """
    conn = get_connection()
    c = conn.cursor()

    try:
        c.execute("INSERT INTO sent_tenders (text) VALUES (%s)", (tender_text,))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()