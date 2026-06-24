import requests


class APIClient:

    def get(self, url):

        try:
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                return response.json()

            print(f"HTTP Error : {response.status_code}")
            return None

        except Exception as error:
            print("Error :", error)
            return None
        