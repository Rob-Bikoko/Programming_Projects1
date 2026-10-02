#Question 5b Connecting Python to SQLite
#Explain the steps required to connect to SQLite and the purpose of each step.
"""
   Step by step explanation
   Step	Python action	Purpose
   1	import sqlite3	Loads Python's built-in SQLite interface.
   2	sqlite3.connect("school.db")	Opens the database file or creates it if it does not yet exist.
   3	connection.cursor()	Creates a cursor that can execute SQL statements. connection.execute() may also be used directly.
   4	execute(...) / executemany(...)	Runs SQL such as CREATE TABLE, INSERT, UPDATE, DELETE or SELECT.
   5	Use ? placeholders	Keeps data separate from SQL and helps prevent SQL-injection errors.
   6	connection.commit()	Permanently saves INSERT, UPDATE and DELETE changes. A successful with block commits automatically.
   7	fetchone() / fetchall()	Retrieves rows produced by a SELECT query.
   8	connection.close()	Releases the database resource. A with statement manages the transaction, after which close should occur or a direct context strategy may be used.

   A robust program uses parameterised SQL, handles sqlite3.Error where appropriate,
   commits intentional changes, and ensures the connection is closed.
   SQLite is serverless: the database is stored in a local file and no separate database
   server needs to be installed.

"""
#Question 5c Create insert and retrieve SQLite data
#Connect to SQLite, create a table, insert data and retrieve the stored rows.
"""
   Step by step method
   Step 1. Open school.db with sqlite3.connect().
   Step 2. Create a students table if it does not already exist.
   Step 3. Prepare sample rows as tuples.
   Step 4. Use executemany() with ? placeholders to insert or update the rows safely.
   Step 5. Execute SELECT and call fetchall() to bring the result rows into Python.
   Step 6. Display each row. The successful with block commits changes; finally closes the connection explicitly.

"""
import sqlite3

connection = None

try:
    connection = sqlite3.connect("school.db")

    with connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                mark REAL NOT NULL
            )
            """
        )

        student_rows = [
            (1, "Tendai", 78),
            (2, "Rudo", 85),
            (3, "Nyasha", 92),
        ]

        connection.executemany(
            """
            INSERT OR REPLACE INTO students (id, name, mark)
            VALUES (?, ?, ?)
            """,
            student_rows,
        )

        cursor = connection.execute(
            "SELECT id, name, mark FROM students ORDER BY id"
        )
        results = cursor.fetchall()

    for student_id, name, mark in results:
        print(student_id, name, mark)

except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()
