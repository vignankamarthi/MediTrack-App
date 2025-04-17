import streamlit as st
import sys
import os

# Add the modules directory to the path so we can import the nav module
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modules'))
from nav import SideBarLinks

# Page configuration
st.set_page_config(
    page_title="Patient Records | MediTrack",
    page_icon="🏥",
    layout="wide"
)

# Authentication check - simplified without callbacks
if 'is_authenticated' not in st.session_state or not st.session_state.is_authenticated:
    st.switch_page("Home.py")
elif 'role' not in st.session_state or st.session_state.role != "physician":
    st.warning("You don't have permission to access this page.")
    st.switch_page("Home.py")

# Display sidebar navigation
SideBarLinks(st.session_state.role)

# Page content
st.title("Patient Records")
st.subheader("Access and manage patient medical information")

# Search section
st.markdown("### Patient Search")
col1, col2, col3 = st.columns([2, 2, 1])
with col1:
    patient_search = st.text_input("Search by name or ID", placeholder="Enter patient name or ID")
with col2:
    condition_filter = st.selectbox("Filter by condition", ["All Conditions", "Hypertension", "Diabetes", "Asthma", "COPD", "Heart Failure"])
with col3:
    search_button = st.button("Search", use_container_width=True)

# Patient list (placeholder)
st.markdown("### Patient List")
patients = {
    "patient_id": [101, 102, 103, 104, 105],
    "first_name": ["John", "Sarah", "Michael", "Emily", "William"],
    "last_name": ["Doe", "Smith", "Brown", "Davis", "Johnson"],
    "DOB": ["1980-05-15", "1992-08-22", "1975-03-10", "1988-11-30", "1965-07-19"],
    "condition": ["Hypertension", "Diabetes", "COPD", "Asthma", "Heart Failure"],
    "last_visit": ["2025-04-10", "2025-04-05", "2025-03-28", "2025-04-12", "2025-04-01"]
}
st.dataframe(patients, use_container_width=True)

# Placeholder for patient details section
st.markdown("### Patient Details")
st.info("Select a patient from the list above to view their details.")

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Patient Records Dashboard")
