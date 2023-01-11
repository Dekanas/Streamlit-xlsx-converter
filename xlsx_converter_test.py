import streamlit as st
import pandas as pd
import openpyxl
from io import BytesIO

@st.cache
def main():
    st.set_page_config(page_title="Excel File Processing App", page_icon=":guardsman:", layout="wide")
    st.title("Upload Excel File")

    # Allow user to upload an Excel file with multiple sheets
    excel_file = st.file_uploader("Choose a spreadsheet", type=["xlsx", "xls"])

    if excel_file is not None:
        # Open the workbook and display a summary of each sheet's columns
        workbook = openpyxl.load_workbook(excel_file)
        sheet_names = workbook.sheetnames
        for sheet_name in sheet_names:
            sheet = workbook[sheet_name]
            st.write(f"Sheet: {sheet_name}")
            st.write("Columns:")
            st.write([cell.value for cell in sheet[1]])

        # Ask the user which sheets and columns they would like to keep
        selected_sheets = st.multiselect("Select the sheets to keep", options=sheet_names)
        selected_columns = {}
        for sheet_name in selected_sheets:
            selected_columns[sheet_name] = st.multiselect(f"Select the columns to keep from {sheet_name}", options=[cell.value for cell in workbook[sheet_name][1]])
        
        # Filter the dataframe and allow to download the modified data.
        transformed_df = {}
        for sheet_name in selected_sheets:
            sheet_df = pd.DataFrame(workbook[sheet_name].values)
            sheet_df.columns = [cell.value for cell in workbook[sheet_name][1]]
            sheet_df = sheet_df[selected_columns[sheet_name]]
            transformed_df[sheet_name] = sheet_df
        
        
            # Create a buffer to save the transformed data as a binary stream
            buffer = BytesIO()
            writer = pd.ExcelWriter(buffer, engine='xlsxwriter')
            for sheet_name in transformed_df.keys():
                transformed_df[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
            writer.save()
            buffer.seek(0)
            
    
    
    def get_data():
        return buffer
    
    file_data = get_data()
    
    if st.download_button("Download transformed data", file_data, "transformed_data.xlsx"):
        st.write("Download complete")

if __name__ == "__main__":
    main()
