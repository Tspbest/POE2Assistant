import sqlite3


class ItemRepository:

    @staticmethod
    def get_all():
        conn = sqlite3.connect("poe2.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM items")
        data = cursor.fetchall()

        conn.close()

        return data

    @staticmethod
    def get_by_id(item_id):
        conn = sqlite3.connect("poe2.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM items WHERE id = ?",
            (item_id,)
        )

        data = cursor.fetchone()

        conn.close()

        return data

    @staticmethod
    def search(name):
        conn = sqlite3.connect("poe2.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM items WHERE name LIKE ?",
            (f"%{name}%",)
        )

        data = cursor.fetchall()

        conn.close()

        return data