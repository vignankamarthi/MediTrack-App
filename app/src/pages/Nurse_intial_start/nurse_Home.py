# nurse_Home.py
import streamlit as st

# Page config
st.set_page_config(page_title="Nurse Dashboard", page_icon="🩺", layout="wide")
st.title("👩‍⚕️ Nurse Navigation Center")

# Initialize session state
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "care"

# Style buttons to look clean and blend in
st.markdown("""
    <style>
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
        .stButton>button {
            width: 100%;
            text-align: left;
            padding: 0.75rem 1rem;
            margin: 0.3rem 0;
            border: none;
            border-radius: 6px;
            background-color: transparent;
            font-size: 20px;
            font-weight: 500;
            color: inherit;
        }
        .stButton>button:hover {
            background-color: rgba(0,0,0,0.05);
        }
        .stButton>button.selected {
            background-color: rgba(0,100,200,0.1);
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# Mapping for button labels
label_map = {
    "care": "📝 Care Task Manager",
    "symptoms": "🩺 Patient Symptom Dashboard",
    "lab": "🔬 Lab Results Viewer"
}

# Sidebar layout
with st.sidebar:
    st.markdown("<div class='sidebar-title'>Nurse Tools</div>", unsafe_allow_html=True)

    # Real buttons that update selected page
    if st.button("Care Task Manager", key="btn_care"):
        st.session_state.selected_page = "care"
    if st.button("Patient Symptom Dashboard", key="btn_symptoms"):
        st.session_state.selected_page = "symptoms"
    if st.button("Lab Results Viewer", key="btn_lab"):
        st.session_state.selected_page = "lab"

    # Highlight selected one using JS
    selected_label = label_map[st.session_state.selected_page]
    st.markdown(f"""
        <script>
            const buttons = window.parent.document.querySelectorAll('.stButton>button');
            buttons.forEach(btn => {{
                if (btn.innerText.trim() === "{selected_label}") {{
                    btn.classList.add("selected");
                }}
            }});
        </script>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-caption">Made with Love in CS3200</div>', unsafe_allow_html=True)

# Route to pages
if st.session_state.selected_page == "care":
    from caretask_manager_dash_page2 import run as care_tasks_run
    care_tasks_run()

elif st.session_state.selected_page == "symptoms":
    from pat_symptom_dash_page1 import run as symptoms_run
    symptoms_run()

elif st.session_state.selected_page == "lab":
    from lab_viewer_dash_page3 import run as lab_run
    lab_run()
else:
    st.info("👈 Please select a tool from the sidebar to begin.")
