from frontend import ExcelValidationUI
from backend import process_excel

def main():
    ui = ExcelValidationUI()
    ui.display_header()

    uploaded_file = ui.upload_file()
    if uploaded_file:
        errors = process_excel(uploaded_file)
        ui.display_result(errors)

if __name__ == "__main__":
    main()