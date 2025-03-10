import sqlite3

# Connect to the SQLite database
db_path = 'data/database/put_data_base_name' # UPDATE WITH DATABSE PATH
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Debugging: List all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:", tables)

# Function to convert duration to minutes
def convert_to_minutes(duration):
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

# Fetch all rows where duration_minutes is 0
cursor.execute("SELECT id, duration FROM calls WHERE duration_minutes = 0")
rows = cursor.fetchall()

# Update duration_minutes for each row
for row in rows:
    id, duration = row
    duration_minutes = convert_to_minutes(duration)
    cursor.execute("UPDATE calls SET duration_minutes = ? WHERE id = ?", (duration_minutes, id))

# Commit the transaction
conn.commit()

# Close the connection
conn.close()