import streamlit as st
import sys
import os

# Add the modules directory to the path so we can import the nav module
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modules'))
from nav import SideBarLinks

# Page configuration
st.set_page_config(
    page_title="Clinical Protocols | MediTrack",
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
st.title("Clinical Protocols")
st.subheader("Manage standardized care protocols")

# Protocol management
st.markdown("### Clinical Protocol Management")
col1, col2 = st.columns([3, 1])
with col1:
    protocol_search = st.text_input("Search protocols", placeholder="Enter protocol name or keyword")
with col2:
    create_button = st.button("Create New Protocol", use_container_width=True)

# Protocol list (placeholder)
st.markdown("### Active Protocols")
protocols = {
    "protocol_id": [1, 2, 3, 4, 5],
    "protocol_name": ["Hypertension Management Protocol", "Type 2 Diabetes Care Protocol", "Asthma Treatment Protocol", "Coronary Artery Disease Protocol", "COPD Management Protocol"],
    "version": ["1.2", "2.0", "1.5", "1.3", "1.8"],
    "effective_date": ["2023-01-01", "2023-03-15", "2022-06-01", "2023-02-01", "2022-09-01"],
    "expiration_date": ["2025-12-31", "2026-03-14", "2025-05-31", "2025-12-31", "2025-08-31"],
    "is_active": [True, True, True, True, True]
}
st.dataframe(protocols, use_container_width=True)

# Protocol details (placeholder)
st.markdown("### Protocol Details")
st.info("Select a protocol from the list above to view and edit details.")

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Clinical Protocols Dashboard")
