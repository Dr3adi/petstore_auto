from pydantic import BaseModel


class Tag(BaseModel):
    id: int = None
    name: str = None