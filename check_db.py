import sqlite3

conn = sqlite3.connect("poe2.db")
cursor = conn.cursor()

for row in cursor.execute(
    "SELECT * FROM leagues"
):
    print(row)

conn.close()