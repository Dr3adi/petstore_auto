from pydantic import BaseModel
from src.enums.pet_enums import Statuses
from pydantic.types import List
from src.schemas.pet.tag import Tag
from src.schemas.pet.category import Category


class Pet(BaseModel):
    id: int
    category: Category = None
    name: str
    photoUrls: List[str]
    tags: List[Tag] = None
    status: Statuses = None