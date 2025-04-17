import streamlit as st
import sys
import os

# Add the modules directory to the path so we can import the nav module
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modules'))
from nav import SideBarLinks

# Page configuration
st.set_page_config(
    page_title="Example UI 2 | MediTrack",
    page_icon="🏥",
    layout="wide"
)

# Authentication check
if 'is_authenticated' not in st.session_state or not st.session_state.is_authenticated:
    st.switch_page("Home.py")
elif 'role' not in st.session_state or st.session_state.role != "physician":
    st.warning("You don't have permission to access this page.")
    st.switch_page("Home.py")

# Display sidebar navigation
SideBarLinks(st.session_state.role)

# Page content
st.title("Example UI 2")
st.subheader("This is a placeholder for the second example UI")

# Placeholder content
st.info("This UI will be implemented in the next phase.")

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Example UI 2")
