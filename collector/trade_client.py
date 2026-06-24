import requests


class TradeClient:

    BASE_URL = "https://www.pathofexile.com/api/trade2"

    def search(self, league, query):

        url = f"{self.BASE_URL}/search/{league}"

        response = requests.post(
            url,
            json=query,
            timeout=10
        )

        response.raise_for_status()

        return response.json()