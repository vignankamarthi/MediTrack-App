import streamlit as st
import sys
import os

# Add the modules directory to the path so we can import the nav module
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "modules"))
from nav import SideBarLinks

# Page configuration
st.set_page_config(
    page_title="Physician Dashboard | MediTrack", page_icon="🏥", layout="wide"
)

# Authentication check
if "is_authenticated" not in st.session_state or not st.session_state.is_authenticated:
    st.switch_page("Home.py")
elif "role" not in st.session_state or st.session_state.role != "physician":
    st.warning("You don't have permission to access this page.")
    st.switch_page("Home.py")

# Display sidebar navigation
SideBarLinks(st.session_state.role)

# Page content
st.title(f"Welcome, Dr. {st.session_state.user_name.split()[1]}")
st.subheader("Physician Dashboard")

# Create dashboard layout with cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Patients Under Care", value="27", delta="2 new")
    st.markdown("---")
    st.subheader("Recent Alerts")
    st.info("Patient #121 has missed medication doses")
    st.info("New lab results available for Patient #135")

with col2:
    st.metric(label="Pending Treatments", value="8", delta="-3")
    st.markdown("---")
    st.subheader("Upcoming Appointments")
    st.markdown("**Today**")
    st.markdown("• 10:30 AM - John Doe (Follow-up)")
    st.markdown("• 11:45 AM - Sarah Smith (New Patient)")
    st.markdown("• 2:15 PM - Michael Brown (Test Results)")

with col3:
    st.metric(label="Treatment Success Rate", value="94%", delta="2%")
    st.markdown("---")
    st.subheader("Quick Links")

    st.markdown("### Available Tools")
    col3a, col3b = st.columns(2)

    with col3a:
        st.page_link("pages/02_ExampleUI1.py", label="Provider Comparison", icon="📊")
        st.page_link(
            "pages/04_Treatment_Outcomes.py", label="Treatment Outcomes", icon="💊"
        )

    with col3b:
        st.page_link("pages/05_Patient_Records.py", label="Patient Records", icon="👤")
        st.page_link(
            "pages/06_Clinical_Protocols.py", label="Clinical Protocols", icon="📝"
        )

# Recent activity section
st.markdown("---")
st.subheader("Recent Activity")

# Create a table of recent activities
data = {
    "Date": ["2025-04-16", "2025-04-15", "2025-04-15", "2025-04-14", "2025-04-14"],
    "Patient": [
        "John Doe",
        "Emily Davis",
        "Sarah Smith",
        "Michael Brown",
        "David Johnson",
    ],
    "Activity": [
        "Prescription Update",
        "Treatment Completed",
        "Test Results Review",
        "New Treatment Plan",
        "Medication Change",
    ],
    "Status": ["Completed", "Completed", "Pending", "Completed", "Pending"],
}

# Display the table
st.dataframe(data, use_container_width=True)

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Physician Dashboard")
