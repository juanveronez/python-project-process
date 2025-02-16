import streamlit as st

class ExcelValidationUI:
    title = "Excel Schema Validator"

    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title=self.title
        )
    
    def display_header(self):
        st.title(self.title)

    def upload_file(self):
        return st.file_uploader("Load your Excel file here", type="xlsx")