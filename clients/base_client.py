import requests

class BaseClient:
    def __init__(self, auth=None):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': auth
        }
        self.request = requests

