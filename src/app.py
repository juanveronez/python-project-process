from backend import process_excel, save_df_on_sql
from frontend import ExcelValidationUI

def main():
    ui = ExcelValidationUI()
    ui.display_header()

    uploaded_file = ui.upload_file()
    if uploaded_file:
        errors, df = process_excel(uploaded_file)
        ui.display_result(errors)
        
        if not df is None and ui.display_save_db():
            rows_affected = save_df_on_sql(df)
            if rows_affected and rows_affected > 0:
                ui.display_success()

if __name__ == '__main__':
    main()