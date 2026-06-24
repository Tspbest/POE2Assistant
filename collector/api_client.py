import requests

class APIClient:

    def get(self, url):
        try:
            response = requests.get(url, timeout=10)
            return response

        except requests.RequestException:
            return None