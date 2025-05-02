import requests
from src.enums.global_emums import GlobalErrorMessanges


class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code
        self.parsed_object = None


    def assert_status_code(self, status_code):
        assert status_code == self.response_status, f'{GlobalErrorMessanges.WRONG_STATUS_CODE.value} {status_code} != {self.response_status}'
        return self


    # def assert_status(self, status):
    #     if isinstance(self.response_json, list):
    #         for item in self.response_json:
    #             assert item['status'] == status, f'{GlobalErrorMessanges.WRONG_STATUS.value} {status}'
    #     return self


    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                parsed_object = schema.model_validate(item)
                self.parsed_object = parsed_object
        else:
            parsed_object = schema.model_validate(self.response_json)
            self.parsed_object = parsed_object
        return self


    def assert_value(self, key, value):
        if isinstance(self.response_json,list):
            for item in self.response_json:
                get_item = item[key]
                assert item[key] == value, f'{key} != {value} был получен {get_item}'
        else:
            get_item = self.response_json[key]
            assert self.response_json[key] == value, f'{key} != {value} был получен {get_item}'
        return self