import sqlite3

conn = sqlite3.connect("poe2.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM items LIMIT 10")

for row in cursor.fetchall():
    print(row)

conn.close()