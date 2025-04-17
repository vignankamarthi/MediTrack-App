import streamlit as st
import sys
import os

# Add the modules directory to the path so we can import the nav module
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modules'))
from nav import SideBarLinks

# Page configuration
st.set_page_config(
    page_title="Treatment Outcomes | MediTrack",
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
st.title("Treatment Outcomes")
st.subheader("View and analyze treatment effectiveness")

# Placeholder for treatment outcomes content
st.markdown("This page would display treatment outcomes data from the physician_routes.py API endpoint `/treatment-outcomes`.")
st.code("GET /dr/treatment-outcomes", language="http")

# Create placeholder data
st.markdown("### Sample Treatment Outcomes Data")
data = {
    "outcome_id": [1, 2, 3, 4, 5],
    "treatment_name": ["ACE Inhibitor Therapy", "Insulin Therapy", "Inhaled Corticosteroids", "Coronary Angioplasty", "Bronchodilator Therapy"],
    "outcome_name": ["Reduced Blood Pressure", "Dizziness", "Stabilized Blood Glucose", "Hypoglycemia", "Improved Breathing"],
    "description": ["Patient blood pressure decreased to normal range", "Patient experienced mild dizziness as side effect", "Patient blood sugar levels stabilized", "Patient experienced low blood sugar episodes", "Patient reported easier breathing and fewer asthma attacks"],
    "is_positive": [True, False, True, False, True]
}

st.dataframe(data, use_container_width=True)

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Treatment Outcomes Dashboard")
