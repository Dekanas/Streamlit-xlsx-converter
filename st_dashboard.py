import streamlit as st
import streamlit_elements as st_elements
import streamlit_dnd as dnd

st.set_page_config(page_title="My Dashboard", page_icon=":guardsman:", layout="wide", initial_sidebar_state="auto")

st.title("My Dashboard")

# Use the Drag and Drop component to create a draggable element
draggable_element = dnd.dnd_container(
    children=[
        st.text_area("Enter some code")
    ],
    style={'background': '#f2f2f2', 'padding': '20px'}
)

st.write(draggable_element)
# Use the Resizable component to create a resizable element
resizable_element = st_elements.resizable.resizable_container(
    children=[
        st_elements.select_box(label="Select a data set", options=["Data Set 1", "Data Set 2", "Data Set 3"], key="data_set")
    ],
    key="resizable_element",
    style={'background': '#f2f2f2', 'padding': '20px'}
)

# Use the Grid component to create a grid layout
grid_layout = st_elements.grid.grid_container(
    children=[
        resizable_element,
        draggable_element
    ],
    key="grid_layout",
    style={'background': '#f2f2f2', 'padding': '20px'}
)

st_elements.render_element(grid_layout)

# Get the data from the draggable and resizable elements
code = st_elements.get_state("code")
data_set = st_elements.get_state("data_set")

# Use the Chart component to create a chart
chart_element = st_elements.chart.chart_container(
    chart_type='bar',
    data=data_set,
    key="chart_element",
    style={'background': '#f2f2f2', 'padding': '20px'}
)
st_elements.render_element(chart_element)
