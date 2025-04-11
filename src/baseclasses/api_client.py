import requests
from src.baseclasses.response import Response


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url


    def send_request(self, method, endpoint, **kwargs):
        url = f'{self.base_url}{endpoint}'
        response = requests.request(method, url, **kwargs)
        return Response(response)