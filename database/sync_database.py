import sqlite3


class SyncDatabase:

    @staticmethod
    def save_items(items):

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

        cursor.execute("DELETE FROM items")

        for item in items:

            cursor.execute(
                """
                INSERT INTO items
                (name,item_type,value,defense,price)
                VALUES(?,?,?,?,?)
                """,
                (
                    item.get("name", ""),
                    item.get("item_type", ""),
                    item.get("value", 0),
                    item.get("defense", 0),
                    item.get("price", 0),
                ),
            )

        conn.commit()
        conn.close()

        return True