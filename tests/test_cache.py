from services.cache import Cache


def test_cache():

    Cache.clear()

    Cache.set(
        "league",
        ["Standard", "Hardcore"]
    )

    data = Cache.get("league")

    assert data[0] == "Standard"
    assert len(data) == 2