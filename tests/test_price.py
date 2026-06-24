from models.item import Item
from services.price_service import PriceService


def test_average():

    items = [

        Item("A", "Rare", 100, 20, 10),
        Item("B", "Rare", 80, 40, 20)

    ]

    assert PriceService.average(items) == 15