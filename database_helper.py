# database_helper.py
import sqlite3
from datetime import datetime, timedelta
import secrets

DB_NAME = "tender_alerts.db"


def get_connection():
    """Create and return a new database connection."""
    return sqlite3.connect(DB_NAME)


def init_db():
    """Create database tables if they do not exist."""
    conn = get_connection()
    cur = conn.cursor()

    # Table for companies
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS companies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            website TEXT,
            description TEXT,
            keywords TEXT,
            verified INTEGER DEFAULT 0,
            unsubscribed INTEGER DEFAULT 0,
            created_at TEXT
        )
        """
    )

    # Table for email verification tokens
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS verification_tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_id INTEGER,
            token TEXT UNIQUE,
            expires_at TEXT,
            FOREIGN KEY(company_id) REFERENCES companies(id)
        )
        """
    )

    conn.commit()
    conn.close()


def create_company(name, email, description, website, keywords):
    """
    Insert a new company and create a verification token.
    Returns (company_id, token).
    """
    conn = get_connection()
    cur = conn.cursor()

    now = datetime.utcnow().isoformat()

    cur.execute(
        """
        INSERT INTO companies (name, email, website, description, keywords, verified, unsubscribed, created_at)
        VALUES (?, ?, ?, ?, ?, 0, 0, ?)
        """,
        (name, email, website, description, keywords, now),
    )

    company_id = cur.lastrowid

    # Create a random token valid for 24 hours
    token = secrets.token_urlsafe(32)
    expires_at = (datetime.utcnow() + timedelta(hours=24)).isoformat()

    cur.execute(
        """
        INSERT INTO verification_tokens (company_id, token, expires_at)
        VALUES (?, ?, ?)
        """,
        (company_id, token, expires_at),
    )

    conn.commit()
    conn.close()

    return company_id, token


def get_company_by_token(token):
    """Return company row (as dict) for a given verification token, if not expired."""
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute(
        """
        SELECT c.*
        FROM companies c
        JOIN verification_tokens vt ON vt.company_id = c.id
        WHERE vt.token = ?
        """,
        (token,),
    )

    row = cur.fetchone()
    conn.close()

    if not row:
        return None

    return dict(row)


def verify_company_email(company_id):
    """Mark company as verified."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE companies SET verified = 1 WHERE id = ?",
        (company_id,),
    )

    conn.commit()
    conn.close()


def unsubscribe_company(email):
    """Mark company as unsubscribed so they no longer receive alerts."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE companies SET unsubscribed = 1 WHERE email = ?",
        (email,),
    )

    conn.commit()
    conn.close()


def get_active_companies():
    """
    Return all companies that:
    - are verified
    - are not unsubscribed
    """
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute(
        """
        SELECT * FROM companies
        WHERE verified = 1 AND unsubscribed = 0
        """
    )

    rows = cur.fetchall()
    conn.close()

    return [dict(r) for r in rows]


def delete_expired_tokens():
    """Delete verification tokens that are expired."""
    conn = get_connection()
    cur = conn.cursor()

    now = datetime.utcnow().isoformat()
    cur.execute(
        "DELETE FROM verification_tokens WHERE expires_at < ?",
        (now,),
    )

    conn.commit()
    conn.close()