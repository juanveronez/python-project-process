from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, Field
from datetime import date
from enum import Enum

class SaleCategory(str, Enum):
    RETAIL = "retail"
    ONLINE = "online"
    B2B = "b2b"

class Sale(BaseModel):
    email: EmailStr
    date: date
    price: PositiveFloat
    product: str = Field(min_length=1)
    quantity: PositiveInt
    category: SaleCategory