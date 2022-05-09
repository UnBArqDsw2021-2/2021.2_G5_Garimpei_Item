from typing import List
from pydantic import BaseModel

class CategorySchema(BaseModel):
    name: str
    description: str
    category_id: int

    class Config():
        orm_mode = True


class ItemSchema(BaseModel):
    title: str
    description: str
    status: str
    category_id: int

    class Config():
        orm_mode = True


class ShowCategorySchema(BaseModel):
    id: int
    name: str
    description: str
    items: List[ItemSchema] = []

    class Config():
        orm_mode = True


class ShowItemSchema(BaseModel):
    id: int
    title: str
    description: str
    status: str
    category_id: int
    category: ShowCategorySchema = None

    class Config():
        orm_mode = True
