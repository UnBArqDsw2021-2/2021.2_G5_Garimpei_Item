from unicodedata import name
from common.models import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Item(BaseModel):
    __tablename__ = "item"

    title = Column(String)
    description = Column(String)
    status = Column(String)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category", back_populates="items")


class Category(BaseModel):
    __tablename__ = "category"

    name = Column(String)
    description = Column(String)
    items = relationship("Item", back_populates="category")
