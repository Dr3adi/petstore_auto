from src.generators.generate_pet import GeneratePet
import pytest
from config import BASE_URL
from src.baseclasses.api_client import ApiClient
from src.schemas.pet.pet import Pet


api_client = ApiClient(BASE_URL)


@pytest.fixture()
def get_pet_generator():
    return GeneratePet()


@pytest.fixture()
def create_pet(get_pet_generator):
    body = get_pet_generator.build_pet()
    response = api_client.send_request('POST', '/v2/pet', json=body)
    data = response.response_json
    return data


