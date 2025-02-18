import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models import Base


def get_database_url():
    load_dotenv()

    db_user = os.getenv('POSTGRES_USER')
    db_password = os.getenv('POSTGRES_PASSWORD')
    db_name = os.getenv('POSTGRES_DB')
    db_host = os.getenv('POSTGRES_HOST')
    db_port = os.getenv('POSTGRES_PORT')

    url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    return url


def create_session():
    url = get_database_url()
    engine = create_engine(url)

    Base.metadata.create_all(bind=engine)
    LocalSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)

    return LocalSession()
