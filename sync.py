import sqlite3

from collector.poe2_trade import POE2TradeClient

client = POE2TradeClient()
data = client.fetch("leagues")

conn = sqlite3.connect("poe2.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leagues(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    league_id TEXT UNIQUE,
    name TEXT,
    realm TEXT
)
""")

for league in data["result"]:
    cursor.execute(
        """
        INSERT OR REPLACE INTO leagues
        (league_id, name, realm)
        VALUES (?, ?, ?)
        """,
        (
            league["id"],
            league["text"],
            league["realm"]
        )
    )

conn.commit()
conn.close()

print("Sync Complete")