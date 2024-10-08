import streamlit as st
from streamlit import session_state as state

# Define individual pages for homework 1 and homework 2
lab2_page = st.Page("lab2.py", title="lab2")
lab1_page = st.Page("lab1.py", title="lab1")

# Initialize navigation with the pages
pg = st.navigation([lab2_page,lab1_page])

# Set page configuration (optional but helps with page title and icon)
st.set_page_config(page_title="Homework Manager", page_icon=":memo:")

# Run the navigation system
pg.run()
