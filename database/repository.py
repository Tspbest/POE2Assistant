class BuildRepository:

    def __init__(self, database):

        self.database = database

    def insert(self, build):

        self.database.cursor.execute(

            """

            INSERT INTO builds(

                name,
                level,
                job,
                damage,
                defense

            )

            VALUES(

                ?,
                ?,
                ?,
                ?,
                ?

            )

            """,

            (

                build.name,
                build.level,
                build.job,
                build.damage,
                build.defense

            )

        )

        self.database.connection.commit()

    def all(self):

        self.database.cursor.execute(

            "SELECT * FROM builds"

        )

        return self.database.cursor.fetchall()