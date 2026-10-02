import mysql.connector

# Connect to MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='new_username',
    password='vimbai@33',
    database='employee'
)
cursor = connection.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL
)
''')

# Insert data into the table
cursor.execute('INSERT INTO accounts (name, age) VALUES (%s, %s)', ('Naina', 26))
cursor.execute('INSERT INTO accounts (name, age) VALUES (%s, %s)', ('Akina', 30))

# Commit the changes
connection.commit()

# Retrieve data
cursor.execute('SELECT * FROM accounts')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
cursor.close()
connection.close()