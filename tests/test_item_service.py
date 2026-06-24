from services.item_service import ItemService


def test_leagues():

    service = ItemService()

    data = service.leagues()

    assert data is not None
