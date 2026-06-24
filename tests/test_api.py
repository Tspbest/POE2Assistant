from collector.api_client import APIClient

def test_api_get():
    client = APIClient()

    response = client.get(
        "https://jsonplaceholder.typicode.com/todos/1"
    )

    assert response is not None
    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1