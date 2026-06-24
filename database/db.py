import sqlite3


class Database:

    def __init__(self):

        self.connection = sqlite3.connect(
            "data/poe2.db"
        )

        self.cursor = self.connection.cursor()

    def create_table(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS builds(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT,

            level INTEGER,

            job TEXT,

            damage INTEGER,

            defense INTEGER

        )

        """)

        self.connection.commit()

    def close(self):

        self.connection.close()