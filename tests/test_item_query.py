from services.item_query import ItemQuery


def test_item_query():

    data = ItemQuery.all()

    assert data is not None