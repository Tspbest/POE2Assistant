from services.json_loader import JSONLoader


def test_json_loader():

    data = JSONLoader.load(
        "data/leagues.json"
    )

    assert data is not None
    