import sqlite3

# Connect to SQLite database (it will create the file if it doesn't exist)
connection = sqlite3.connect('database.db')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# Commit changes and close the connection
connection.commit()
connection.close()
