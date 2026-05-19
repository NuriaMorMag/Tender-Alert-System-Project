# database_helper.py

import pymysql

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "tender_alerts"
}


def get_connection():

    return pymysql.connect(**DB_CONFIG)


def save_user(email):

    conn = get_connection()

    c = conn.cursor()

    try:

        c.execute(
            "INSERT INTO users (email) VALUES (%s)",
            (email,)
        )

        conn.commit()

    except:

        pass

    finally:

        conn.close()


def remove_user(email):

    conn = get_connection()

    c = conn.cursor()

    c.execute(
        "DELETE FROM users WHERE email=%s",
        (email,)
    )

    conn.commit()

    conn.close()


def get_users():

    conn = get_connection()

    c = conn.cursor()

    c.execute("SELECT email FROM users")

    users = c.fetchall()

    conn.close()

    return [u[0] for u in users]


def save_tender_if_new(tender):

    conn = get_connection()
    c = conn.cursor()

    try:

        c.execute("""
            INSERT INTO sent_tenders
            (text, published_at)
            VALUES (%s, %s)
        """, (
            tender["procurement_name"],
            tender["publication_date"]
        ))

        conn.commit()

        return True

    except:
        return False

    finally:
        conn.close()