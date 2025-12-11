import requests
from urls import BASE_URL


class CreateAd:
    def __init__(self):
        self.base_url = BASE_URL

    def create_ad(self, token, data=None, files=None):
        headers = {
            'Authorization': f'Bearer {token}'
        }
        return requests.post(f"{self.base_url}/api/create-listing", headers=headers, data=data, files=files)