import streamlit as st
from modules.nav import SideBarLinks

# Set the page configuration
st.set_page_config(layout="wide", page_title="MediTrack - System Dashboard")

# Show the navigation sidebar
SideBarLinks()

# Check if user is authenticated and has the administrator role
if "authenticated" not in st.session_state or st.session_state["role"] != "administrator":
    st.warning("Please log in as a System Administrator to access this page.")
    st.stop()

# Create a header container
header_container = st.container()

# Create header section
with header_container:
    col1, col2 = st.columns([4, 1])
    
    with col1:
        # Logo and title
        st.markdown("<div style='display: flex; align-items: center;'>", unsafe_allow_html=True)
        st.image("/Users/vkamarthi24/Desktop/MediTrack-App/app/src/assets/logo.png", width=50)
        st.markdown("<h2 style='margin-left: 10px; margin-bottom: 0; color: #6550e6;'>MediTrack Admin</h2>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Display admin information
        st.markdown(f"""
        <div style='margin-top: 0.5rem;'>
            <span style='font-weight: bold;'>{st.session_state.get('first_name', 'Brennan')} Johnson</span>
            <span style='color: #666; margin-left: 1rem;'>System Administrator</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Current date and time
        st.markdown(f"""
        <div style='text-align: right; color: #666;'>
            <span>Sun, Apr 13, 2025 at 10:29:39 PM</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Add a separator line
    st.markdown("<hr style='margin: 0.5rem 0 1rem 0;'>", unsafe_allow_html=True)

# Main content placeholder - not implementing full functionality as per request
st.title("System Dashboard")
st.info("This page would contain the system administration dashboard. Only the header has been implemented as requested.")
