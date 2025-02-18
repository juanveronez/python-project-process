from sqlalchemy import Column, Date, Enum, Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, declarative_base

from contracts import SaleCategory

Base: DeclarativeBase = declarative_base()


class SaleModel(Base):
    __tablename__ = 'sales'

    id = Column(Integer, autoincrement=True, index=True, primary_key=True)
    email = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    price = Column(Float, nullable=False)
    product = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    category = Column(Enum(SaleCategory), nullable=False)
