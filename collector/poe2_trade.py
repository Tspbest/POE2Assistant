import requests


class POE2TradeClient:

    BASE_URL = "https://www.pathofexile.com/api/trade2/data"

    def fetch(self, endpoint):

        response = requests.get(
            f"{self.BASE_URL}/{endpoint}",
            headers={
                "User-Agent": "POE2Assistant/1.0"
            },
            timeout=10
        )

        response.raise_for_status()

        return response.json()