import sqlite3
import os
import colorama


def setup_database(db_path):
    # Ensure the directory exists
    db_dir = os.path.dirname(db_path)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir)

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS calls (
        id INTEGER PRIMARY KEY,
        username TEXT,
        duration TEXT,
        duration_minutes INTEGER,
        timestamp TEXT
    )
    ''')
    conn.commit()
    print(colorama.Fore.YELLOW + f"Connected to detabase at: {db_path}" + colorama.Fore.RESET)
    return conn

def store_call_in_db(conn, call):
    cursor = conn.cursor()
    duration_minutes = 0
    cursor.execute('''
    INSERT INTO calls (username, duration, duration_minutes, timestamp)
    VALUES (?, ?, ?, ?)
    ''', (
        call["username"],
        call["duration"],
        duration_minutes,
        call["timestamp"]
    ))
    conn.commit()