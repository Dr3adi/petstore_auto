import requests
from src.baseclasses.response import Response
from config import BASE_URL
from src.baseclasses.api_client import ApiClient
from src.schemas.pet.pet import Pet


api_client = ApiClient(BASE_URL)


def test_get_pet():
    response = api_client.sed_request('GET', '/v2/pet/1')
    response.assert_status_code(200).validate(Pet)