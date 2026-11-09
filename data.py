
import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()


cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table';
""")

tables = cursor.fetchall()

print("Tables in the database:")

for table in tables:
    print(table[0])

connection.close()


import sqlite3

# Connect to the database
connection = sqlite3.connect("database.db")

cursor = connection.cursor()


cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table';
""")

tables = cursor.fetchall()

print("Tables in the database:")

if tables:
    for table in tables:
        print(table[0])
else:
    print("No tables found in the database.")

connection.close()

