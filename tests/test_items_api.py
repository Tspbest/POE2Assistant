from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)


def test_items():

    response = client.get("/items")

    assert response.status_code == 200

    data = response.json()

    assert "count" in data
    assert "items" in data


def test_search():

    response = client.get(
        "/items/search?name=Astra"
    )

    assert response.status_code == 200

    data = response.json()

    assert "items" in data