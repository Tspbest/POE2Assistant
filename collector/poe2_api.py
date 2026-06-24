from collector.api_client import APIClient


class POE2API:

    def __init__(self):
        self.client = APIClient()

    def get_build(self, url):

        return self.client.get(url)