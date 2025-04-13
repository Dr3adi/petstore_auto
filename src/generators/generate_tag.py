

class GenerateTag:
    def __init__(self):
        self.result = {'id': 66}


    def tag_name(self, name='animal'):
        self.result['name'] = name
        return self


    def build_tag(self):
        return self.result