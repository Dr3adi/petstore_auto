import pytest
import requests
from src.baseclasses.response import Response
from config import BASE_URL
from src.baseclasses.api_client import ApiClient
from src.schemas.pet.pet import Pet
from src.enums.pet_enums import Statuses
import allure


api_client = ApiClient(BASE_URL)

@allure.title('Получение питомца по id')
def test_get_pet(create_pet):
    with allure.step('Получение id'):
        petId = create_pet['id']
    with allure.step('Отправка GET-запроса с полученным id'):
        response = api_client.send_request('GET', f'/v2/pet/{petId}')
    with allure.step('Проверка статус-кода'):
        response.assert_status_code(200)
    with allure.step('Валидация json-схемы'):
        response.validate(Pet)


@pytest.mark.parametrize('status', [status.value for status in Statuses])
def test_pet_find_by_status(status):
    response = api_client.send_request('GET', '/v2/pet/findByStatus', params={'status': status})
    response.assert_status_code(200).assert_value('status', status).validate(Pet)


@pytest.mark.parametrize('status', [status.value for status in Statuses])
def test_create_pet(get_pet_generator, status):
    body = (get_pet_generator
            .pet_status(status)
            # .pet_category({"id": 1, "name": "NewCategory"})
            # .pet_tags([{"id": 10, "name": "NewTag"}, {"id": 11, "name": "ExtraTag"}])
            .pet_photo_urls()
            .build_pet())
    response = api_client.send_request('POST', '/v2/pet', json=body)
    data = response.response_json
    response.assert_status_code(200).validate(Pet).assert_value('status', status)
    print(data)


def test_update_pet(create_pet):
    pet = create_pet
    pet['name'] = 'newName'
    response = api_client.send_request('PUT', '/v2/pet', json=pet)
    response.assert_status_code(200).validate(Pet)


def test_delete_pet(create_pet):
    petId = create_pet['id']
    response = api_client.send_request('DELETE', f'/v2/pet/{petId}')
    response.assert_status_code(200)