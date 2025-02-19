import pandas as pd

from src.contracts import Sale
from src.database import get_database_url


def process_excel(uploaded_file) -> tuple[list[str], pd.DataFrame | None]:
    errors: list[str] = []
    try:
        df = pd.read_excel(uploaded_file)

        extra_columns = set(df.columns) - set(Sale.model_fields.keys())
        if extra_columns:
            errors.append(
                f'Extra columns in your file: {', '.join(extra_columns)}'
            )
            return errors, None

        for index, row in df.iterrows():
            try:
                Sale(**row.to_dict())
            except Exception as e:
                errors.append(f'Error in line {index + 1}: {e}')

        return errors, df if len(errors) == 0 else None
    except Exception as e:
        errors.append(f'Unexpected error: {str(e)}')
        return errors, None

def save_df_on_sql(df: pd.DataFrame):
    db_url = get_database_url()
    return df.to_sql('sales', con=db_url, if_exists="append", index=False)