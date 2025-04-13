

class GenerateCategory:
    def __init__(self):
        self.result = {'id': 44}


    def category_name(self, name='myanimal'):
        self.result['name'] = name
        return self

    def build_category(self):
        return self.result