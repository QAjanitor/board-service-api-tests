import requests

from urls import BASE_URL


class DeleteAd:
    def __init__(self):
        self.base_url = BASE_URL

    def delete_ad(self, token, id_ad):
        headers = {
            'Authorization': f'Bearer {token}'
        }
        return requests.delete(f"{self.base_url}/api/listings/{id_ad}", headers=headers)