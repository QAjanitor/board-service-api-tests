import requests

from urls import BASE_URL


class UpdateAd:
    def __init__(self):
        self.base_url = BASE_URL

    def update_ad(self, token, id_ad, data):
        headers = {
            'Authorization': f'Bearer {token}'
        }
        return requests.patch(f"{self.base_url}/api/update-offer/{id_ad}", headers=headers, data=data)