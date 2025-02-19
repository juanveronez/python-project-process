from backend import process_excel, save_df_on_sql
from frontend import ExcelValidationUI

from logging import error, info

from logs import sentry_sdk

def main():
    ui = ExcelValidationUI()
    ui.display_header()

    uploaded_file = ui.upload_file()
    if uploaded_file:
        errors, df = process_excel(uploaded_file)
        ui.display_result(errors)
        
        if df is None:
            error("Error in sheet format")
            sentry_sdk.capture_message("Error in sheet format")
        elif ui.display_save_db():
            rows_affected = save_df_on_sql(df)
            if rows_affected and rows_affected > 0:
                ui.display_success()
                info("Database updated with success!")
                sentry_sdk.capture_message("Database updated with success!")


if __name__ == '__main__':
    main()