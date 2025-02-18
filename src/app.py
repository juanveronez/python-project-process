from backend import process_excel

# from models import SaleModel
from database import create_session
from frontend import ExcelValidationUI


def main():
    ui = ExcelValidationUI()
    ui.display_header()

    uploaded_file = ui.upload_file()
    if uploaded_file:
        errors, _ = process_excel(uploaded_file)
        ui.display_result(errors)


if __name__ == '__main__':
    # main()
    session = create_session()
    # print(session.query(SaleModel).all())
