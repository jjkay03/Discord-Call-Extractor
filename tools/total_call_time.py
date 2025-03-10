import sqlite3

# Connect to the SQLite database
db_path = 'data/database/put_data_base_name' # UPDATE WITH DATABSE PATH
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Query
cursor.execute("SELECT SUM(duration_minutes) FROM calls")
total_call_time_minutes = cursor.fetchone()[0]
conn.close()

# Maths
total_call_time_hours = total_call_time_minutes // 60
remaining_minutes = total_call_time_minutes % 60
total_call_time_days = total_call_time_minutes // (60 * 24)
remaining_minutes_after_days = total_call_time_minutes % (60 * 24)
hours_after_days = remaining_minutes_after_days // 60
minutes_after_hours = remaining_minutes_after_days % 60

print(f"Total call time: {total_call_time_minutes} minutes")
print(f"Total call time: {total_call_time_hours} hours and {remaining_minutes} minutes")
print(f"Total call time: {total_call_time_days} days, {hours_after_days} hours, and {minutes_after_hours} minutes")