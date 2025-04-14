import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout="wide", page_title="MediTrack - Medication Reconciliation Tool")

SideBarLinks()

if "authenticated" not in st.session_state or st.session_state["role"] != "usaid_worker":
    st.warning("Please log in as a Pharmacist to access this page.")
    st.stop()


header_container = st.container()

with header_container:
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.markdown("<div style='display: flex; align-items: center;'>", unsafe_allow_html=True)
        st.markdown("<h2 style='margin-bottom: 0; color: #3366cc;'>MediTrack</h2>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='margin-top: 0.5rem;'>
            <span style='font-weight: bold;'>Pharmacist {st.session_state.get('first_name', 'Sarah')} Chen, PharmD</span>
            <span style='color: #666; margin-left: 1rem;'>User ID: SC-{st.session_state.get('user_id', '12345')}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr style='margin: 0.5rem 0 1rem 0;'>", unsafe_allow_html=True)

st.title("Medication Reconciliation Tool")
st.info("This page will generate comprehensive reconciliation reports. Functionality not implemented in this header-only version.")
