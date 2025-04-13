from src.generators.generate_pet import GeneratePet
import pytest


@pytest.fixture()
def get_pet_generator():
    return GeneratePet()