import random

class GenerateCategory:
    def __init__(self):
        self.result = {'id': random.randint(100, 200)}
        self.reset()


    def category_name(self, name='myanimal'):
        self.result['name'] = name
        return self

    def reset(self):
        self.category_name()
        return self


    def build_category(self):
        return self.result