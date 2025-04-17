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

# Function to handle role selection
def select_role(role, name):
    st.session_state.role = role
    st.session_state.is_authenticated = True
    st.session_state.user_name = name
    
    # Redirect to appropriate role page
    if role == "physician":
        st.switch_page("pages/01_Physician_Home.py")
    elif role == "nurse":
        st.switch_page("pages/11_Nurse_Home.py")
    elif role == "pharmacist":
        st.switch_page("pages/21_Pharmacist_Home.py")
    elif role == "admin":
        st.switch_page("pages/31_Admin_Home.py")

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
    
    st.button("🧑‍⚕️ Physician (Dr. James Wilson)", 
              on_click=select_role, 
              args=("physician", "James Wilson"),
              use_container_width=True)
    
    st.button("👩‍⚕️ Nurse (Maria Rodriguez)", 
              on_click=select_role, 
              args=("nurse", "Maria Rodriguez"),
              use_container_width=True)

with col2:
    st.markdown("### Support Staff")
    
    st.button("💊 Pharmacist (Sarah Chen)", 
              on_click=select_role, 
              args=("pharmacist", "Sarah Chen"),
              use_container_width=True)
    
    st.button("🔧 System Administrator (Brennan)", 
              on_click=select_role, 
              args=("admin", "Brennan"),
              use_container_width=True)

# Footer
st.markdown("---")
st.markdown("© 2025 MediTrack - Developed for CS 3200")
