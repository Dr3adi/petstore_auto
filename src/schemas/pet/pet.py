from pydantic import BaseModel
from src.enums.pet_enums import Statuses
from pydantic.types import List
from src.schemas.pet.tag import Tag
from src.schemas.pet.category import Category


class Pet(BaseModel):
    id: int = None
    category: Category = None
    name: str = None
    photoUrls: List[str] = None
    tags: List[Tag] = None
    status: Statuses = None