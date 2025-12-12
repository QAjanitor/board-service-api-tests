import requests

from urls import BASE_URL


class SignUp:
    def __init__(self):
        self.base_url = BASE_URL

    def create_user(self, payload):
        return requests.post(f"{self.base_url}/api/signup", json=payload)