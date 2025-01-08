import sqlite3

# Step 1: Connect to SQLite (or create the database file)
connection = sqlite3.connect("example.db")

# Step 2: Create a cursor object
cursor = connection.cursor()

# Step 3: Write an SQL command to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
);
"""

# Step 4: Execute the SQL command
cursor.execute(create_table_query)

# Step 5: Commit changes and close the connection
connection.commit()

print("Database and table created successfully!")

# Query to select all rows from the table
cursor.execute('SELECT * FROM users')

# Fetch all rows from the executed query
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close the connection
connection.close()