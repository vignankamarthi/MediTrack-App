##################################################
# This is the main/entry-point file for the 
# Nurse Persona Streamlit App
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# import the main streamlit library
import streamlit as st

# If you have a custom sidebar module, import it here
# from modules.nav import SideBarLinks

# Set the layout to wide (better for dashboards)
st.set_page_config(layout='wide')

# Set session state defaults
st.session_state['authenticated'] = False

# Optional: Custom sidebar links (if implemented)
# SideBarLinks(show_home=True)

# Main Content
logger.info("Loading the Home page for the Nurse Persona")
st.title('CS 3200 Sample Semester Project App')
st.write("### Hi! Select a user to log in as:")

# Nurse Maria
if st.button("Act as Maria, a Nurse", 
             type='primary', 
             use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'nurse'
    st.session_state['first_name'] = 'Maria'
    logger.info("Logged in as Nurse Maria")
    st.switch_page('pages/nurse_Home.py')  




