import sqlite3

conn = sqlite3.connect("poe2.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS leagues")

conn.commit()
conn.close()

print("Table dropped")