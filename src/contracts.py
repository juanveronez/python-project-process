from datetime import date
from enum import Enum

from pydantic import BaseModel, EmailStr, Field, PositiveFloat, PositiveInt


class SaleCategory(str, Enum):
    RETAIL = 'retail'
    ONLINE = 'online'
    B2B = 'b2b'


class Sale(BaseModel):
    """
    Modelo de dados para as vendas.

    Args:
        email (str): email do comprador
        data (datetime): data da compra
        valor (int): valor da compra
        produto (str): nome do produto
        quantidade (int): quantidade de produtos
        categoria (str): categoria do produto

    """
    email: EmailStr
    date: date
    price: PositiveFloat
    product: str = Field(min_length=1)
    quantity: PositiveInt
    category: SaleCategory
