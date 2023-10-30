from pydantic import BaseModel

class ItemBaseSchema(BaseModel):
    name: str
    price: float
    quantity: int

class ItemCreateSchema(ItemBaseSchema):
    pass

class ItemSchema(ItemBaseSchema):
    id: int

    class Config:
        orm_mode = True
