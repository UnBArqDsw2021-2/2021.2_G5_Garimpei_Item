from common.models import BaseModel
from sqlalchemy import Column, String


class Item(BaseModel):
    __tablename__ = "item"

    title = Column(String)
    description = Column(String)
    status = Column(String)
