import requests

url = "https://www.pathofexile.com/api/trade2/data/leagues"

response = requests.get(
    url,
    headers={
        "User-Agent": "POE2Assistant/1.0"
    },
    timeout=10
)

print("Status:", response.status_code)
print(response.text[:500])