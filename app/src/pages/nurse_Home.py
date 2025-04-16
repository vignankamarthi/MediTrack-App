# nurse_Home.py
import streamlit as st

# Configure Streamlit page
st.set_page_config(page_title="Nurse Dashboard", page_icon="🩺", layout="wide")

# Initialize session state for selected page
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "care"

# Sidebar configurations 
st.markdown("""
    <style>
        .sidebar-button {
            display: block;
            width: 100%;
            padding: 0.75rem 1rem;
            margin: 0.2rem 0;
            border: none;
            border-radius: 6px;
            background-color: transparent;
            font-size: 16px;
            text-align: left;
            color: inherit;
            font-weight: 500;
            cursor: pointer;
        }

        .sidebar-button:hover {
            background-color: rgba(0, 0, 0, 0.05);
        }

        .sidebar-button.selected {
            background-color: rgba(0, 100, 200, 0.1);
            font-weight: 600;
        }

        .sidebar-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .sidebar-caption {
            font-size: 12px;
            margin-top: 20px;
            color: gray;
        }
    </style>
""", unsafe_allow_html=True)

# Overall Sidebar navigation
with st.sidebar:
    st.markdown('<div class="sidebar-title"> Nurse Tools</div>', unsafe_allow_html=True)

    def nav_button(label, key, page_id):
        if st.button(label, key=key):
            st.session_state.selected_page = page_id

        
        

    nav_button("Care Task Manager", "btn_care", "care")
    nav_button("Patient Symptom Dashboard", "btn_symptoms", "symptoms")
    nav_button("Lab Results Viewer", "btn_lab", "lab")

    # Chooise which patient to select 
    st.markdown("### 👤 Select Patient")
    st.session_state.current_patient_id = st.selectbox(
        "Choose Patient ID", options=[1, 2, 3], index=0
    )

    st.markdown('<div class="sidebar-caption">Built With Love in CS3200</div>', unsafe_allow_html=True)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages', 'Nurse_final_implementation')))
# Nav Page routing
if st.session_state.selected_page == "care":
    from caretask_manager_dash_page2 import run as care_run
    care_run()

elif st.session_state.selected_page == "symptoms":
    from pat_symptom_dash_page1 import run as symptoms_run
    symptoms_run()

elif st.session_state.selected_page == "lab":
    from lab_viewer_dash_page3 import run as lab_run
    lab_run()

else:
    st.info(" Please select a tool from the sidebar. ")
