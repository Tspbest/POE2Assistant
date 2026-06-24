import sqlite3

conn = sqlite3.connect("poe2.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO items
(name, item_type, value, defense, price)
VALUES
('Astramentis', 'Amulet', 15, 0, 100),
('Gold Ring', 'Ring', 10, 0, 20)
""")

conn.commit()
conn.close()

print("seed complete")
