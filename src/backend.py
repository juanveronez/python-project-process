import pandas as pd

from contracts import Sale


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

        return errors, df
    except Exception as e:
        errors.append(f'Unexpected error: {str(e)}')
        return errors, None
