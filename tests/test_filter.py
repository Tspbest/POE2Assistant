from models.item import Item
from services.filter import Filter


def test_filter():

    items = [

        Item("A", "Ring", 5),
        Item("B", "Ring", 20),
        Item("C", "Ring", 15),

    ]

    result = Filter.expensive(items)

    assert len(result) == 2