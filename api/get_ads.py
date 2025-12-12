import requests

from urls import BASE_URL


class GetAds:
    def __init__(self):
        self.base_url = BASE_URL

    def get_ads(self, token, page):
        headers = {
            'Authorization': f'Bearer {token}'
        }
        return requests.get(f"{self.base_url}/api/listings/{page}", headers=headers)