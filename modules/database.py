import sqlite3
import os
import colorama

# Function to create and setup db
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

# Function to store call in db
def store_call_in_db(conn, call):
    cursor = conn.cursor()
    duration_minutes = convert_duration_to_minutes(call["duration"])
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

# Function to convert duration to minutes
def convert_duration_to_minutes(duration):
    if duration == '"':
        return 0
    if duration == "an hour":
        return 60
    if duration == "a minute":
        return 1
    if 'hour' in duration:
        hours = int(duration.split()[0])
        return hours * 60
    if 'minute' in duration:
        return int(duration.split()[0])
    if 'seconds' in duration:
        return 0
    return 0