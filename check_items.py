import sqlite3

conn = sqlite3.connect("poe2.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM items")

for row in cursor.fetchall():
    print(row)

conn.close()