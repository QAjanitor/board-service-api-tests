import requests

from urls import BASE_URL


class SignIn:
    def __init__(self):
        self.base_url = BASE_URL

    def login_user(self, payload):
        return requests.post(f"{self.base_url}/api/signin", json=payload)