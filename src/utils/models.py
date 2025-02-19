from sqlalchemy import create_engine, Column, Date, Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, declarative_base

from src.database import get_database_url

Base: DeclarativeBase = declarative_base()


class SaleModel(Base):
    __tablename__ = 'sales'

    id = Column(Integer, autoincrement=True, index=True, primary_key=True)
    email = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    price = Column(Float, nullable=False)
    product = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    category = Column(String, nullable=False)

def create_models():
    url = get_database_url()
    engine = create_engine(url)

    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_models()