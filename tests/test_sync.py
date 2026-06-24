import os

def test_sync_files():

    assert os.path.exists("data/leagues.json")
    assert os.path.exists("data/items.json")
    