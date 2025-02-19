from pandas import read_sql_table
from database import get_database_url

db_url = get_database_url()

def test_db_schema():
    df = read_sql_table("sales", con=db_url)

    df_types = df.dtypes.to_dict()

    expected_types = {
        'id': 'int64',
        'email': 'object',  # object em Pandas corresponde a string em SQL
        'date': 'datetime64[ns]',
        'price': 'float64',
        'quantity': 'int64',
        'product': 'object',
        'category': 'object'
    }

    assert df_types == expected_types, "The schema of the DataFrame does not match the expected one."

def test_db_not_empty():
    df = read_sql_table("sales", con=db_url)

    assert not df.empty, "DataFrame is empty."