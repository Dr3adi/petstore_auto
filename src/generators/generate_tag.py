import random


class GenerateTag:
    def __init__(self):
        self.result = {'id': random.randint(100, 200)}
        self.reset()


    def tag_name(self, name='animal'):
        self.result['name'] = name
        return self


    def reset(self):
        self.tag_name()
        return self


    def build_tag(self):
        return self.result