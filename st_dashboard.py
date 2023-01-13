import streamlit as st
from streamlit_material_components import st_theme
from streamlit_material_components import st_text
from streamlit_material_components import st_card
from streamlit_material_components import st_selectbox
from streamlit_monaco_editor import st_monaco_code_editor
import streamlit_nivo

st.beta_set_page_config(page_title="My Dashboard", page_icon=":guardsman:", layout="wide", initial_sidebar_state="auto")

st_theme.set_theme("dark")

st.title("My Dashboard")

st_text("Select a data set:")
data_set = st_selectbox(["Data Set 1", "Data Set 2", "Data Set 3"])

st_text("Enter some code:")
code = st_monaco_code_editor(language="python", theme="vs-dark")

st_card("Results:")
st_nivo.bar_chart(data_set)
