from models.item import Item


def test_item():

    item = Item(
        "Astramentis",
        "Amulet",
        15
    )

    data = item.to_dict()

    assert data["name"] == "Astramentis"
    assert data["type"] == "Amulet"
    assert data["price"] == 15