import requests


class ExtenalAPICleint:
    BASE_URL = "url api"

    @staticmethod
    def get_data():
        response = requests.get(f"{ExtenalAPICleint}/data", timeout=5)

        response.raise_for_status()

        return response.json()
