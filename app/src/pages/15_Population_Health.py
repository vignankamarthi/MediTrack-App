import streamlit as st
from modules.nav import SideBarLinks

# Set the page configuration
st.set_page_config(layout="wide", page_title="MediTrack - Population Health Dashboard")

# Show the navigation sidebar
SideBarLinks()

# Check if user is authenticated and has the physician role
if "authenticated" not in st.session_state or st.session_state["role"] != "pol_strat_advisor":
    st.warning("Please log in as a Physician to access this page.")
    st.stop()

# Create a header container
header_container = st.container()

# Create header section
with header_container:
    # Title and logo
    st.markdown("""
    <div style="display: flex; align-items: center; padding: 1rem 0;">
        <h2 style="margin: 0; color: #3366cc;">MediTrack</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Separator line
    st.markdown("<hr style='margin: 0.25rem 0 1rem 0;'>", unsafe_allow_html=True)
    
    # Dashboard title
    st.title("Population Health Dashboard")
    
    # Doctor info in top right (added via CSS)
    st.markdown(f"""
    <div style="position: absolute; top: 1rem; right: 1rem; display: flex; align-items: center;">
        <span style="margin-right: 0.5rem;">Dr. {st.session_state.get('first_name', 'James')} Wilson</span>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGXCZUhjdCSfXjq8IJmvbDPVfA7B-7HjZAWjgJCEaWhCvhDvr5SPS4s" 
             alt="user" style="width: 32px; height: 32px; border-radius: 50%;">
    </div>
    """, unsafe_allow_html=True)
    
    # Search bar and filters section
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.text_input("Search patients or conditions...", placeholder="Search...")
    
    with col2:
        st.button("Search", type="primary")
    
    # Filters section
    st.markdown("<div style='margin-top: 1rem;'><h4>Filters</h4></div>", unsafe_allow_html=True)
    
    filter_cols = st.columns(4)
    
    with filter_cols[0]:
        st.checkbox("All Conditions", value=True)
    
    with filter_cols[1]:
        st.checkbox("All Ages", value=True)
    
    with filter_cols[2]:
        st.checkbox("All Genders", value=True)
    
    with filter_cols[3]:
        st.checkbox("Last 3 Months", value=True)
    
    st.button("Apply Filters")
    
# Main content placeholder - not implementing full functionality as per request
st.info("This page would contain the full Population Health Dashboard functionality. Only the header has been implemented as requested.")
