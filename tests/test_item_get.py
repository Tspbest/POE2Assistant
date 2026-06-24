from services.item_query import ItemQuery


def test_get():

    data = ItemQuery.get(1)

    assert data is not None