import sqlite3

conn = sqlite3.connect("poe2.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM leagues")

rows = cursor.fetchall()

print(f"Total: {len(rows)}")

for row in rows:
    print(row)

conn.close()