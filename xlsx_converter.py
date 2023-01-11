import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Excel Transformer", page_icon=":guardsman:", layout="wide")

st.title("Excel Transformer")

uploaded_file = st.file_uploader("Choose a CSV file", type=["xls", "xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, sheet_name = 'Claims')
    st.dataframe(df)

    # Transforming data
    new_excel = df[['Reference No.', 'Claim No.', 'Country', 'Claim type', 'Became a claim?', 'Claim status (closed/open)', 'Claim open date', 'Claim close date', 'Total claim cost so far (EUR with VAT)', 'Repair cost (EUR with VAT)', 'Parts cost (with VAT)', 'Shipping paid by the service (EUR/with VAT)', 'Shiping cost (EUR with VAT)', 'Disposal cost (EUR with VAT)']]
    st.dataframe(new_excel)
    # Download transformed data
    st.write("Transform Done!")
    st.markdown("### Download transformed data:")
    st.download_button('Download XLSX', new_excel, 'new_excel.xlsx', 'text/csv')
