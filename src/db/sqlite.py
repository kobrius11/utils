import sqlite3
import databases


DATABASE_URL = "sqlite:///./sqlite.db"
db = databases.Database(DATABASE_URL)


def init_db():
    conn = sqlite3.connect("sqlite.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        is_done BOOLEAN NOT NULL CHECK (is_done IN (0, 1)),
        due_date TEXT
    )
    """)
    conn.commit()
    conn.close()

