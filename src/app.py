from frontend import ExcelValidationUI

def main():
    ui = ExcelValidationUI()
    ui.display_header()

    upload_file = ui.upload_file()

if __name__ == "__main__":
    main()