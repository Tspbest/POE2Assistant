from database.db import Database


def test_database():

    db = Database()

    db.create_table()

    assert db.connection is not None

    db.close()