from sqlalchemy import Column, Integer, String
from app.database import Base
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    field_1: str
    author: str
    description: str
    my_numeric_field: int
