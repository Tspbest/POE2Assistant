import sqlite3

conn = sqlite3.connect("poe2.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT,
    price INTEGER,
    chaos_price INTEGER,
    divine_price INTEGER
)
""")

cursor.execute("""
INSERT INTO items
(name, category, price, chaos_price, divine_price)
VALUES
('Astramentis', 'Amulet', 15, 0, 100),
('Gold Ring', 'Ring', 10, 0, 20)
""")

conn.commit()
conn.close()

print("Items table created")