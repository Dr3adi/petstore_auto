from pydantic import BaseModel, field_validator
from src.enums.pet_enums import Statuses
from pydantic.types import List
from src.schemas.pet.tag import Tag
from src.schemas.pet.category import Category
from typing import Optional, List
from src.enums.global_emums import GlobalErrorMessanges


class Pet(BaseModel):
    id: int = None
    category: Category = None
    name: str = None
    photoUrls: Optional[List[Optional[str]]] = None
    tags: List[Tag] = None
    status: Statuses = None


    @field_validator('status', mode='before')
    def validate_status(cls, value):
        if isinstance(value, Statuses):
            value = value.value
        status_list = [status.value for status in Statuses]
        if value not in status_list:
            raise ValueError(f'{GlobalErrorMessanges.WRONG_STATUS.value}, был получен статус: {value}')
        return value