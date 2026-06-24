from services.item_query import ItemQuery


def test_search():

    data = ItemQuery.search("Astra")

    assert len(data) >= 1