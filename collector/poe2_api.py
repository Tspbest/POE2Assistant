from collector.api_client import APIClient


class POE2API:

    def __init__(self):

        self.client = APIClient()

    def get_build(self, url):

        response = self.client.get(url)

        if response is None:
            return None

        return response.json()