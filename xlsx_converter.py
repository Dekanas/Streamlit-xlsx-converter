import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Excel Transformer", page_icon=":guardsman:", layout="wide")

st.title("Excel Transformer")

uploaded_file = st.file_uploader("Choose a CSV file", type=["xls", "xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)

    # Transforming data
    df["new_column"] = df["old_column"] + 1

    # Download transformed data
    buffer = BytesIO()
    export_file = df.to_excel(buffer, index = None, header=True)
    buffer.seek(0)
    st.write("Transform Done!")
    st.markdown("### Download transformed data:")
    st.markdown("[Download Excel File](http://localhost:8501" + 
                st.set_page_config(page_title="Download", page_icon=":guardsman:", layout="wide") + 
                f"/files/transformed_data.xlsx)")
    st.set_page_config(page_title="Excel Transformer", page_icon=":guardsman:", layout="wide")
