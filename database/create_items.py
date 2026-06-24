import sqlite3

conn = sqlite3.connect("poe2.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    item_type TEXT,
    value INTEGER,
    defense INTEGER,
    price INTEGER
)
""")

conn.commit()
conn.close()

print("items table created")