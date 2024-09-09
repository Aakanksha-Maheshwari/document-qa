import streamlit as st
import importlib

# Set up the page configuration to ensure the sidebar starts expanded and uses the 'wide' layout
st.set_page_config(page_title="Homework Manager", page_icon=":memo:", layout="wide", initial_sidebar_state="expanded")

# Sidebar with buttons for navigation
st.sidebar.title("Navigation")
lab1_button = st.sidebar.button("Lab 1")
lab2_button = st.sidebar.button("Lab 2")

# Initialize a default page (Lab 2)
if 'page' not in st.session_state:
    st.session_state.page = 'Lab 2'

# Update session state based on button clicks
if lab1_button:
    st.session_state.page = 'Lab 1'
elif lab2_button:
    st.session_state.page = 'Lab 2'

# Function to dynamically load the page from .py files
def load_page(page_name):
    try:
        if page_name == "Lab 1":
            lab_module = importlib.import_module('Lab 1')  # Import Lab 1.py dynamically
        elif page_name == "Lab 2":
            lab_module = importlib.import_module('Lab 2')  # Import Lab 2.py dynamically
        else:
            st.error("Page not found!")
    except ModuleNotFoundError as e:
        st.error(f"Error loading the page: {e}")

# Load the correct page based on session state
load_page(st.session_state.page)

