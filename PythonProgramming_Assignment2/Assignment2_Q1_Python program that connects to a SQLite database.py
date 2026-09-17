#Q1. Python program that connects to a SQLite database,
#creates a table, inserts some data, and retrieves the data from the table.
import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect("company.db")

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          age INTEGER,
          department TEXT
)
""")

# Insert sample data
employees = [
           ("Alice", 30, "HR"),
           ("Bob", 25, "IT"),
           ("Charlie", 35, "Finance")
]

cursor.executemany("""
INSERT INTO employees (name, age, department)
VALUES (?, ?, ?)
""", employees)

# Save changes
conn.commit()

# Retrieve data from the table
cursor.execute("SELECT * FROM employees")

# Fetch all rows
rows = cursor.fetchall()

# Display the data
print("Employees:")

for row in rows:
     print(row)

# Close the connection
conn.close()
