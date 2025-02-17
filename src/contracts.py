from datetime import date
from enum import Enum

from pydantic import BaseModel, EmailStr, Field, PositiveFloat, PositiveInt


class SaleCategory(str, Enum):
    RETAIL = 'retail'
    ONLINE = 'online'
    B2B = 'b2b'


class Sale(BaseModel):
    email: EmailStr
    date: date
    price: PositiveFloat
    product: str = Field(min_length=1)
    quantity: PositiveInt
    category: SaleCategory
