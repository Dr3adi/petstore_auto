import pytest
import requests
from src.baseclasses.response import Response
from config import BASE_URL
from src.baseclasses.api_client import ApiClient
from src.schemas.pet.pet import Pet


api_client = ApiClient(BASE_URL)


def test_get_pet():
    response = api_client.send_request('GET', '/v2/pet/1')
    response.assert_status_code(200).validate(Pet)


@pytest.mark.parametrize('status', ['available', 'pending', 'sold'])
def test_pet_find_by_status(status):
    response = api_client.send_request('GET', '/v2/pet/findByStatus', params={'status': f'{status}'})
    response.assert_status_code(200).validate(Pet)


def test_create_pet():
    body = {"id": 357,
            "category": {"id": 10, "name": "frog"},
            "name": "doggie",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available"}
    response = api_client.send_request('POST', '/v2/pet', json=body)
    # data = response.response_json['id']
    response.assert_status_code(200).validate(Pet)
    # print(data)