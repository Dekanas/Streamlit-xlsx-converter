import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Excel Transformer", page_icon=":guardsman:", layout="wide")
st.title("Excel Transformer")

uploaded_file = st.file_uploader("Choose an Excel file", type=["xls", "xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)

    # Transforming data
    df = df[['Reference No.', 'Claim No.', 'Country', 'Claim type', 'Became a claim?', 'Claim status (closed/open)', 'Claim open date', 'Claim close date', 'Total claim cost so far (EUR with VAT)', 'Repair cost (EUR with VAT)', 'Parts cost (with VAT)', 'Shipping paid by the service (EUR/with VAT)', 'Shiping cost (EUR with VAT)', 'Disposal cost (EUR with VAT)']]

    # Create a function that returns the transformed data as an Excel file
    def get_excel():
        buffer = BytesIO()
        export_file = df.to_excel(buffer, index = None, header=True)
        buffer.seek(0)
        return buffer.getvalue()

    # Add a button that, when clicked, triggers a download of the transformed data
    if st.button("Download transformed data"):
        st.markdown("Transform Done!")
        st.markdown("### Download transformed data:")
        st.download_button("Download Excel File", get_excel, "transformed_data.xlsx")   
