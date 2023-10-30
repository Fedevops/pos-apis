from pydantic import BaseModel
from typing import List

class OrderBaseSchema(BaseModel):
    total_price: float

class OrderCreateSchema(OrderBaseSchema):
    pass

class OrderSchema(OrderBaseSchema):
    id: int
    timestamp: str  # ou datetime dependendo da serialização que você usar

    class Config:
        orm_mode = True
