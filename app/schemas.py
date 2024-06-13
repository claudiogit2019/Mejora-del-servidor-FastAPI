from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None
    price: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

