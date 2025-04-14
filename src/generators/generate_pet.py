from faker import Faker
from src.generators.generate_category import GenerateCategory
from src.generators.generate_tag import GenerateTag
import random


class GeneratePet:

    def __init__(self):
        self.result = {'id': random.randint(100, 200)}
        self.reset()


    def pet_name(self, name='Trump'):
        self.result['name'] = name
        return self


    def pet_photo_urls(self, count=2):
        fake = Faker()
        self.result['photoUrls'] = [fake.url() for _ in range(count)]
        return self


    def pet_status(self, status='sold'):
        self.result['status'] = status
        return self


    def reset(self):
        self.result['category'] = GenerateCategory().build_category()
        self.pet_name()
        self.pet_photo_urls()
        self.result['tags'] = [GenerateTag().build_tag()]
        self.pet_status()
        return self


    def build_pet(self):
        return self.result