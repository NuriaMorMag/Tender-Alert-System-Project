import sqlite3

# Database file name
DB_NAME = "users.db"

# Create database and table (run once)
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Create users table if it does not exist
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        description TEXT,
        verified INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()


# Save a new user in the database
def save_user(email, description):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Insert user data
    c.execute("INSERT INTO users (email, description) VALUES (?, ?)",
              (email, description))

    conn.commit()
    conn.close()