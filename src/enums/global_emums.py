from enum import Enum


class GlobalErrorMessanges(Enum):
    WRONG_STATUS_CODE = 'Полученный статус-код отличается от ожидаемого'
    WRONG_STATUS = 'Полученный статус отличатся от ожидаемого'