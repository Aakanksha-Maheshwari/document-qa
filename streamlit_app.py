import streamlit as st

# Set up the page configuration to ensure the sidebar starts expanded and uses the 'wide' layout
st.set_page_config(page_title="Homework Manager", page_icon=":memo:", layout="wide", initial_sidebar_state="expanded")

# Define a function to load the page
def load_page(page_name):
    if page_name == "Lab 1":
        st.title("Lab 1")
        st.write("This is the content of Lab 1.")
    elif page_name == "Lab 2":
        st.title("Lab 2")
        st.write("This is the content of Lab 2.")

# Initialize a default page 
if 'page' not in st.session_state:
    st.session_state.page = 'Lab 2'  # Default page is Lab 2

# Sidebar with buttons for navigation
st.sidebar.title("Navigation")
lab1_button = st.sidebar.button("Lab 1")
lab2_button = st.sidebar.button("Lab 2")

# Update session 
if lab1_button:
    st.session_state.page = 'Lab 1'
elif lab2_button:
    st.session_state.page = 'Lab 2'

# Load the correct page 
load_page(st.session_state.page)
