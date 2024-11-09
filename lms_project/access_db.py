import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Fetch all data from a specific table
cursor.execute("SELECT * FROM examination_features_exam")  # Replace with your table name
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()
