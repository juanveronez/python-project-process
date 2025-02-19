import os

from dotenv import load_dotenv


def get_database_url():
    load_dotenv()

    db_user = os.getenv('POSTGRES_USER')
    db_password = os.getenv('POSTGRES_PASSWORD')
    db_name = os.getenv('POSTGRES_DB')
    db_host = os.getenv('POSTGRES_HOST')
    db_port = os.getenv('POSTGRES_PORT')

    url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    return url
