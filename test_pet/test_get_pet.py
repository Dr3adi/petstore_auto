import pytest
import requests
from src.baseclasses.response import Response
from config import BASE_URL
from src.baseclasses.api_client import ApiClient
from src.schemas.pet.pet import Pet
from src.enums.pet_enums import Statuses


api_client = ApiClient(BASE_URL)


def test_get_pet():
    response = api_client.send_request('GET', '/v2/pet/1')
    response.assert_status_code(200).validate(Pet)


@pytest.mark.parametrize('status', [status.value for status in Statuses])
def test_pet_find_by_status(status):
    response = api_client.send_request('GET', '/v2/pet/findByStatus', params={'status': status})
    response.assert_status_code(200).assert_status(status).validate(Pet)


@pytest.mark.parametrize('status', [status.value for status in Statuses])
def test_create_pet(get_pet_generator, status):
    body = (get_pet_generator
            .pet_status(status)
            # .pet_category({"id": 1, "name": "NewCategory"})
            # .pet_tags([{"id": 10, "name": "NewTag"}, {"id": 11, "name": "ExtraTag"}])
            .pet_name()
            .pet_photo_urls()
            .build_pet())
    response = api_client.send_request('POST', '/v2/pet', json=body)
    data = response.response_json
    response.assert_status_code(200).validate(Pet)
    print(data)