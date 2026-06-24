from collector.api_client import APIClient

client = APIClient()

url = "https://httpbin.org/json"

data = client.get(url)

print(data)