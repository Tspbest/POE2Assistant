from models.item import Item
from services.inventory import Inventory


def test_inventory():

    items = [

        Item(
            "Helmet",
            "Armor",
            10,
            50,
            20
        ),

        Item(
            "Shield",
            "Armor",
            5,
            80,
            30
        )

    ]

    assert Inventory.total_price(items) == 50
    assert Inventory.total_defense(items) == 130