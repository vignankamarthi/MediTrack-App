import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="MediTrack - Healthcare Management System",
    page_icon="🏥",
    layout="wide"
)

# Initialize session state for user role if it doesn't exist
if 'role' not in st.session_state:
    st.session_state.role = None
    
if 'is_authenticated' not in st.session_state:
    st.session_state.is_authenticated = False
    
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# Page header
st.title("Welcome to MediTrack")
st.subheader("Healthcare Management System")

# Introduction
st.markdown("""
MediTrack is a comprehensive healthcare management system designed to streamline
patient care, medication management, and administrative tasks.

Please select your role to continue:
""")

# Create two columns for the role selection buttons
col1, col2 = st.columns(2)

# Role selection buttons
with col1:
    st.markdown("### Medical Staff")
    
    physician_clicked = st.button("🧑‍⚕️ Physician (Dr. James Wilson)", use_container_width=True)
    nurse_clicked = st.button("👩‍⚕️ Nurse (Maria Rodriguez)", use_container_width=True)

with col2:
    st.markdown("### Support Staff")
    
    pharmacist_clicked = st.button("💊 Pharmacist (Sarah Chen)", use_container_width=True)
    admin_clicked = st.button("🔧 System Administrator (Brennan)", use_container_width=True)

# Handle button clicks without callbacks
if physician_clicked:
    st.session_state.role = "physician"
    st.session_state.is_authenticated = True
    st.session_state.user_name = "James Wilson"
    st.switch_page("pages/01_Physician_Home.py")

elif nurse_clicked:
    st.session_state.role = "nurse"
    st.session_state.is_authenticated = True
    st.session_state.user_name = "Maria Rodriguez"
    st.switch_page("pages/11_Nurse_Home.py")

elif pharmacist_clicked:
    st.session_state.role = "pharmacist"
    st.session_state.is_authenticated = True
    st.session_state.user_name = "Sarah Chen"
    st.switch_page("pages/21_Pharmacist_Home.py")

elif admin_clicked:
    st.session_state.role = "admin"
    st.session_state.is_authenticated = True
    st.session_state.user_name = "Brennan"
    st.switch_page("pages/31_Admin_Home.py")

# Footer
st.markdown("---")
st.markdown("© 2025 MediTrack - Developed for CS 3200")
