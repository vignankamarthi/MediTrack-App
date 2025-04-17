import streamlit as st
import sys
import os
import pandas as pd
import requests
from datetime import datetime, timedelta

# Add the modules directory to the path so we can import the nav module
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "modules"))
from nav import SideBarLinks

# Page configuration
st.set_page_config(
    page_title="Care Pathway Management | MediTrack", 
    page_icon="🏥", 
    layout="wide"
)

# Authentication check
if 'is_authenticated' not in st.session_state or not st.session_state.is_authenticated:
    st.switch_page("Home.py")
elif 'role' not in st.session_state or st.session_state.role != "nurse":
    st.warning("You don't have permission to access this page.")
    st.switch_page("Home.py")

# Display sidebar navigation
SideBarLinks(st.session_state.role)

# Page title
st.title("Care Pathway Management")
st.subheader("Create and manage patient care pathways")

# Custom CSS for styling
st.markdown("""
<style>
    /* General Layout Styles */
    .container {
        max-width: 1400px;
        margin: 0 auto;
    }

    /* Patient Header Styles */
    .patient-header {
        background-color: white;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .patient-info {
        display: flex;
        gap: 20px;
        align-items: center;
    }

    .patient-avatar {
        width: 60px;
        height: 60px;
        border-radius: 8px;
        background-color: #95aac9;
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 24px;
        font-weight: bold;
    }

    .patient-details h3 {
        margin-bottom: 5px;
        color: #12263f;
    }

    .patient-details p {
        color: #95aac9;
        margin-bottom: 3px;
    }

    /* Panel Layout Styles */
    .pathway-container {
        display: grid;
        grid-template-columns: 1fr 2fr 1fr;
        gap: 20px;
    }

    /* Responsive adjustments */
    @media (max-width: 1200px) {
        .pathway-container {
            grid-template-columns: 1fr 1fr;
        }
    }

    @media (max-width: 768px) {
        .pathway-container {
            grid-template-columns: 1fr;
        }
    }

    /* Panel Styles */
    .panel {
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }

    .panel-header {
        padding: 15px;
        border-bottom: 1px solid #edf2f9;
        background-color: #f9fbfd;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .panel-header h3 {
        font-size: 16px;
        font-weight: 600;
        color: #12263f;
        margin: 0;
    }

    .panel-body {
        padding: 15px;
    }

    /* Template Panel Styles */
    .category-list {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-bottom: 15px;
    }

    .template-list {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    .template-item {
        display: flex;
        align-items: center;
        gap: 15px;
        padding: 12px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.2s;
        border-left: 3px solid transparent;
    }

    .template-item:hover {
        background-color: #f9fbfd;
    }

    .template-item.active {
        background-color: rgba(44, 123, 229, 0.1);
        border-left: 3px solid #2c7be5;
    }

    .template-icon {
        width: 40px;
        height: 40px;
        background-color: #f9fbfd;
        border-radius: 5px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #2c7be5;
        font-size: 18px;
    }

    /* Pathway Steps Styles */
    .customization-tabs {
        display: flex;
        border-bottom: 1px solid #edf2f9;
        margin-bottom: 15px;
    }

    .tab {
        padding: 10px 15px;
        cursor: pointer;
        border-bottom: 2px solid transparent;
        color: #95aac9;
    }

    .tab.active {
        border-bottom-color: #2c7be5;
        font-weight: 600;
        color: #2c7be5;
    }

    .section-title {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
    }

    .pathway-steps {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    .pathway-step {
        border: 1px solid #edf2f9;
        border-radius: 5px;
        overflow: hidden;
    }

    .step-header {
        display: flex;
        align-items: center;
        padding: 12px 15px;
        background-color: #f9fbfd;
        gap: 10px;
    }

    .step-number {
        width: 24px;
        height: 24px;
        border-radius: 50%;
        background-color: #2c7be5;
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 14px;
        font-weight: bold;
    }

    .step-title {
        flex: 1;
        font-weight: 600;
        color: #12263f;
    }

    .step-status {
        font-size: 12px;
        padding: 3px 8px;
        border-radius: 20px;
        color: white;
    }

    .step-status.complete {
        background-color: #00d97e;
    }

    .step-status.in-progress {
        background-color: #f6c343;
    }

    .step-status.not-started {
        background-color: #95aac9;
    }

    .step-details {
        padding: 15px;
    }

    .step-details p {
        color: #12263f;
        font-size: 14px;
        margin-bottom: 10px;
    }

    .step-customizations {
        display: flex;
        flex-direction: column;
        gap: 5px;
    }

    .custom-item {
        font-size: 12px;
        color: #2c7be5;
        background-color: rgba(44, 123, 229, 0.1);
        padding: 5px 10px;
        border-radius: 3px;
    }

    /* Progress and Social Determinants Styles */
    .progress-bar-container {
        height: 20px;
        background-color: #edf2f9;
        border-radius: 10px;
        overflow: hidden;
        margin-bottom: 10px;
    }

    .progress-bar {
        height: 100%;
        background-color: #2c7be5;
        border-radius: 10px;
        color: white;
        font-size: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .progress-stats {
        display: flex;
        justify-content: space-between;
    }

    .stat-item {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .stat-value {
        font-size: 18px;
        font-weight: bold;
        color: #12263f;
    }

    .stat-label {
        font-size: 12px;
        color: #95aac9;
    }

    .determinant-list {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    .determinant-item {
        border: 1px solid #edf2f9;
        border-radius: 5px;
        overflow: hidden;
    }

    .determinant-header {
        display: flex;
        align-items: center;
        padding: 12px 15px;
        background-color: #f9fbfd;
        gap: 10px;
    }

    .determinant-icon {
        width: 12px;
        height: 12px;
        border-radius: 50%;
    }

    .determinant-icon.warning {
        background-color: #f6c343;
    }

    .determinant-icon.caution {
        background-color: #f5803e;
    }

    .determinant-title {
        flex: 1;
        font-weight: 600;
        color: #12263f;
    }

    .determinant-details {
        padding: 15px;
    }

    .determinant-details p {
        color: #12263f;
        font-size: 14px;
        margin-bottom: 10px;
    }

    .determinant-intervention {
        font-size: 12px;
        background-color: #f9fbfd;
        padding: 8px;
        border-radius: 5px;
        color: #12263f;
    }

    /* Notes Styles */
    .notes-list {
        display: flex;
        flex-direction: column;
        gap: 15px;
        margin-bottom: 15px;
    }

    .note-item {
        padding: 12px;
        background-color: #f9fbfd;
        border-radius: 5px;
    }

    .note-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 8px;
    }

    .note-author {
        font-weight: 600;
        color: #12263f;
        font-size: 14px;
    }

    .note-time {
        font-size: 12px;
        color: #95aac9;
    }

    .note-content {
        font-size: 14px;
        color: #12263f;
    }

    /* Buttons and indicators */
    .mini-badge {
        display: inline-block;
        padding: 2px 6px;
        border-radius: 12px;
        font-size: 10px;
        font-weight: 600;
        margin-left: 5px;
    }

    .mini-badge.active {
        background-color: #00d97e;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Mock API functions for demo purposes (these would be replaced with actual API calls)
def get_care_pathways():
    """Simulate an API call to /n/care-pathways endpoint"""
    # In a real app, this would call the Flask API:
    # response = requests.get("http://web-api:4000/n/care-pathways")
    # return response.json()
    
    # Return simulated data
    return [
        {"pathway_id": 1, "pathway_name": "Heart Failure Management", "description": "Standard pathway for CHF patients", "standard_duration": 90, "is_active": True},
        {"pathway_id": 2, "pathway_name": "Diabetes Care Plan", "description": "Comprehensive diabetes management", "standard_duration": 180, "is_active": True},
        {"pathway_id": 3, "pathway_name": "Post-Surgical Recovery", "description": "General post-op care pathway", "standard_duration": 45, "is_active": True},
        {"pathway_id": 4, "pathway_name": "COPD Management", "description": "Exacerbation prevention pathway", "standard_duration": 120, "is_active": True},
        {"pathway_id": 5, "pathway_name": "Stroke Recovery Protocol", "description": "Rehabilitation following stroke", "standard_duration": 90, "is_active": True},
        {"pathway_id": 6, "pathway_name": "Hypertension Management", "description": "Blood pressure monitoring and control", "standard_duration": 180, "is_active": True},
        {"pathway_id": 7, "pathway_name": "Pain Management", "description": "Chronic pain therapy protocol", "standard_duration": 60, "is_active": True},
        {"pathway_id": 8, "pathway_name": "Wound Care Protocol", "description": "Advanced wound healing pathway", "standard_duration": 30, "is_active": True},
    ]

def get_patient_pathway_steps(pathway_id=1):
    """Return the steps in a care pathway"""
    # For demo, we'll return fixed data for Heart Failure Management
    return [
        {
            "step_id": 1, 
            "step_name": "Initial Assessment", 
            "description": "Comprehensive baseline evaluation including vital signs, weight, edema assessment, and symptom evaluation.",
            "status": "complete",
            "customizations": [
                "Added: Pulmonary function test",
                "Modified: Include sleep quality assessment"
            ]
        },
        {
            "step_id": 2, 
            "step_name": "Medication Reconciliation", 
            "description": "Review and adjust medications based on current status and symptoms. Ensure compliance with heart failure regimen.",
            "status": "in-progress",
            "customizations": [
                "Added: Follow up for medication adherence barriers"
            ]
        },
        {
            "step_id": 3, 
            "step_name": "Dietary Counseling", 
            "description": "Sodium restriction education and fluid management guidance. Referral to nutritionist if needed.",
            "status": "not-started",
            "customizations": []
        },
        {
            "step_id": 4, 
            "step_name": "Activity Planning", 
            "description": "Establish appropriate exercise regimen based on capacity. Refer to cardiac rehabilitation if appropriate.",
            "status": "not-started",
            "customizations": []
        }
    ]

def get_patient_social_determinants(patient_id=101):
    """Simulate an API call to /n/patient-social-records endpoint"""
    # In a real app:
    # response = requests.get(f"http://web-api:4000/n/patient-social-records?patient_id={patient_id}")
    # return response.json()
    
    # Return simulated data
    return [
        {
            "determinant_id": 1,
            "determinant_name": "Transportation",
            "category": "Access to Care",
            "description": "Patient reports difficulty attending follow-up appointments due to lack of reliable transportation.",
            "impact_level": "MODERATE",
            "intervention": "Referral to community transportation service"
        },
        {
            "determinant_id": 2,
            "determinant_name": "Medication Access",
            "category": "Economic Stability",
            "description": "Patient expresses concern about cost of heart medications.",
            "impact_level": "MODERATE",
            "intervention": "Application for medication assistance program submitted"
        }
    ]

def get_pathway_notes():
    """Return care team communication notes for this pathway"""
    return [
        {
            "author": "Dr. James Wilson",
            "time": "Yesterday, 3:45 PM",
            "content": "Patient showing improved ejection fraction on latest echo. Continue current medication regimen but monitor for orthostatic hypotension."
        },
        {
            "author": "Sarah Chen, PharmD",
            "time": "Mar 21, 2025, 10:15 AM",
            "content": "Adjusted furosemide dosing based on renal function. Please monitor daily weights closely for next 3 days."
        }
    ]

def get_patients():
    """Return a list of patients"""
    return [
        {"patient_id": 101, "first_name": "John", "last_name": "Doe", "dob": "1968-05-15", "gender": "Male", "admission_date": "2025-03-20", "primary_provider": "Dr. James Wilson"},
        {"patient_id": 102, "first_name": "Sarah", "last_name": "Smith", "dob": "1992-08-22", "gender": "Female", "admission_date": "2025-03-25", "primary_provider": "Dr. James Wilson"},
        {"patient_id": 103, "first_name": "Michael", "last_name": "Brown", "dob": "1975-03-10", "gender": "Male", "admission_date": "2025-03-28", "primary_provider": "Dr. Michael Chen"},
        {"patient_id": 104, "first_name": "Emily", "last_name": "Davis", "dob": "1988-11-30", "gender": "Female", "admission_date": "2025-04-01", "primary_provider": "Dr. James Wilson"},
        {"patient_id": 105, "first_name": "William", "last_name": "Johnson", "dob": "1965-07-19", "gender": "Male", "admission_date": "2025-04-05", "primary_provider": "Dr. Michael Chen"}
    ]

def create_care_pathway(data):
    """Simulate an API call to POST /n/care-pathways endpoint"""
    # In real implementation:
    # response = requests.post("http://web-api:4000/n/care-pathways", json=data)
    # return response.json()
    
    # For demo purposes:
    return {"message": "New Care Pathway created successfully!", "pathway_id": 9}

def assign_pathway_to_patient(data):
    """Simulate an API call to POST /n/patient-pathway-records endpoint"""
    # In real implementation:
    # response = requests.post("http://web-api:4000/n/patient-pathway-records", json=data)
    # return response.json()
    
    # For demo purposes:
    return {"message": "Care Pathway successfully assigned to patient!"}

def add_social_determinant(data):
    """Simulate an API call to POST /n/patient-social-records endpoint"""
    # In real implementation:
    # response = requests.post("http://web-api:4000/n/patient-social-records", json=data)
    # return response.json()
    
    # For demo purposes:
    return {"message": "Social determinant successfully added to patient!"}

# Main layout
def main():
    # Initialize session state for the current patient, selected pathway, etc.
    if 'current_patient' not in st.session_state:
        st.session_state.current_patient = get_patients()[0]  # Default to first patient
    
    if 'selected_pathway' not in st.session_state:
        st.session_state.selected_pathway = get_care_pathways()[0]  # Default to first pathway
    
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = "Overview"  # Default tab
    
    if 'note_text' not in st.session_state:
        st.session_state.note_text = ""
    
    # Patient selection
    patients = get_patients()
    patient_options = [f"{p['first_name']} {p['last_name']} (#{p['patient_id']})" for p in patients]
    selected_patient_display = st.selectbox("Select Patient", patient_options)
    
    # Extract patient ID and find current patient data
    patient_id = int(selected_patient_display.split("(#")[1].split(")")[0])
    for p in patients:
        if p["patient_id"] == patient_id:
            st.session_state.current_patient = p
            break
    
    # Display patient header
    patient_first_name = st.session_state.current_patient["first_name"]
    patient_last_name = st.session_state.current_patient["last_name"]
    patient_id = st.session_state.current_patient["patient_id"]
    patient_age = 2025 - int(st.session_state.current_patient["dob"].split("-")[0])  # Rough calculation
    patient_admission = st.session_state.current_patient["admission_date"]
    patient_provider = st.session_state.current_patient["primary_provider"]
    
    st.markdown(f"""
    <div class="patient-header">
        <div class="patient-info">
            <div class="patient-avatar">{patient_first_name[0]}{patient_last_name[0]}</div>
            <div class="patient-details">
                <h3>{patient_first_name} {patient_last_name}</h3>
                <p>ID: {patient_id} • {patient_age} years • {st.session_state.current_patient["gender"]}</p>
                <p>Admitted: {patient_admission} • Primary: {patient_provider}</p>
            </div>
        </div>
        <div class="action-buttons">
            <button class="stButton">Save Pathway</button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Create the 3-column layout
    main_container = st.container()
    col1, col2, col3 = main_container.columns([1, 2, 1])
    
    # Column 1: Pathway Templates
    with col1:
        st.markdown("""
        <div class="panel">
            <div class="panel-header">
                <h3>Pathway Templates</h3>
            </div>
            <div class="panel-body">
        """, unsafe_allow_html=True)
        
        # Search box
        search_term = st.text_input("Search templates...", placeholder="Enter template name...")
        
        # Template categories
        categories = ["All Templates", "Chronic Disease", "Post-Surgical", "Preventive Care", "Transitions of Care"]
        st.markdown('<div class="category-list">', unsafe_allow_html=True)
        selected_category = st.radio("Category", categories, horizontal=True, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Template list
        pathways = get_care_pathways()
        
        # Apply search filter
        if search_term:
            pathways = [p for p in pathways if search_term.lower() in p["pathway_name"].lower() or search_term.lower() in p["description"].lower()]
        
        # Display templates
        st.markdown('<div class="template-list">', unsafe_allow_html=True)
        for i, pathway in enumerate(pathways):
            selected = st.session_state.selected_pathway["pathway_id"] == pathway["pathway_id"]
            template_class = "template-item active" if selected else "template-item"
            
            # Use a button to simulate clicking on the template
            if st.button(f"Select {i}", key=f"select_{pathway['pathway_id']}"):
                st.session_state.selected_pathway = pathway
                st.experimental_rerun()
            
            st.markdown(f"""
            <div class="{template_class}">
                <div class="template-info">
                    <h4>{pathway["pathway_name"]}</h4>
                    <p>{pathway["description"]}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div></div>', unsafe_allow_html=True)
    
    # Column 2: Pathway Customization
    with col2:
        st.markdown("""
        <div class="panel">
            <div class="panel-header">
                <h3>Pathway Customization</h3>
            </div>
            <div class="panel-body">
        """, unsafe_allow_html=True)
        
        # Display pathway details
        pathway_name = st.session_state.selected_pathway["pathway_name"]
        
        st.markdown(f"""
        <h4 style="margin: 0;">{pathway_name} <span class="mini-badge active">Active</span></h4>
        <p style="color: #95aac9; margin: 0;">Standard Duration: {st.session_state.selected_pathway["standard_duration"]} days</p>
        """, unsafe_allow_html=True)
        
        if st.button("Assign to Patient", use_container_width=True):
            # This would actually call assign_pathway_to_patient() with patient and pathway IDs
            st.success(f"Pathway '{pathway_name}' successfully assigned to {patient_first_name} {patient_last_name}")
        
        # Create tab buttons at the top
        st.markdown("<hr>", unsafe_allow_html=True)
        tab_names = ["Overview", "Interventions", "Medications", "Education"]
        
        # Create buttons for the tabs
        tab_cols = st.columns(len(tab_names))
        for i, tab_name in enumerate(tab_names):
            with tab_cols[i]:
                if st.button(tab_name, key=f"tab_{tab_name}", use_container_width=True):
                    st.session_state.current_tab = tab_name
                    st.experimental_rerun()
        
        st.markdown("<hr>", unsafe_allow_html=True)
        
        # Tab content - Overview is shown by default
        if st.session_state.current_tab == "Overview":
            st.subheader("Customize Pathway Steps")
            
            if st.button("Add Step", use_container_width=True):
                st.session_state.show_add_step = True
            
            # Add step form
            if 'show_add_step' in st.session_state and st.session_state.show_add_step:
                with st.form("add_step_form"):
                    st.subheader("Add New Pathway Step")
                    new_step_name = st.text_input("Step Name")
                    new_step_description = st.text_area("Description")
                    new_step_status = st.selectbox("Status", ["not-started", "in-progress", "complete"])
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        submit = st.form_submit_button("Add Step")
                    with col2:
                        cancel = st.form_submit_button("Cancel")
                    
                    if submit and new_step_name:
                        st.success(f"Step '{new_step_name}' added successfully!")
                        st.session_state.show_add_step = False
                        st.experimental_rerun()
                    elif cancel:
                        st.session_state.show_add_step = False
                        st.experimental_rerun()
            
            # Display pathway steps
            steps = get_patient_pathway_steps(st.session_state.selected_pathway["pathway_id"])
            
            for step in steps:
                status_class = step["status"]
                status_display = "Complete" if status_class == "complete" else "In Progress" if status_class == "in-progress" else "Not Started"
                
                with st.expander(f"{step['step_id']}. {step['step_name']} ({status_display})", expanded=True):
                    st.markdown(f"**Description:** {step['description']}")
                    
                    # Display customizations if any
                    if step["customizations"]:
                        st.markdown("**Customizations:**")
                        for custom in step["customizations"]:
                            st.markdown(f"- {custom}")
                    
                    # Action Buttons - outside of columns
                    if st.button("Edit", key=f"edit_{step['step_id']}", use_container_width=True):
                        st.session_state.editing_step = step["step_id"]
                        st.session_state.show_edit_step = True
                    
                    status_options = {
                        "not-started": "Mark Not Started",
                        "in-progress": "Mark In Progress",
                        "complete": "Mark Complete"
                    }
                    current_status = step["status"]
                    next_status = "in-progress" if current_status == "not-started" else "complete" if current_status == "in-progress" else "not-started"
                    if st.button(status_options[next_status], key=f"status_{step['step_id']}", use_container_width=True):
                        st.info(f"Status updated to {status_options[next_status]}")
            
            # Edit step form
            if 'show_edit_step' in st.session_state and st.session_state.show_edit_step:
                editing_step = next((s for s in steps if s["step_id"] == st.session_state.editing_step), None)
                if editing_step:
                    with st.form("edit_step_form"):
                        st.subheader(f"Edit Step: {editing_step['step_name']}")
                        edit_step_name = st.text_input("Step Name", value=editing_step["step_name"])
                        edit_step_description = st.text_area("Description", value=editing_step["description"])
                        edit_step_status = st.selectbox("Status", ["not-started", "in-progress", "complete"], index=["not-started", "in-progress", "complete"].index(editing_step["status"]))
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            save = st.form_submit_button("Save Changes")
                        with col2:
                            cancel = st.form_submit_button("Cancel")
                        
                        if save:
                            st.success(f"Step '{edit_step_name}' updated successfully!")
                            st.session_state.show_edit_step = False
                            st.experimental_rerun()
                        elif cancel:
                            st.session_state.show_edit_step = False
                            st.experimental_rerun()
        
        elif st.session_state.current_tab == "Interventions":
            st.subheader("Interventions")
            st.markdown("Configure interventions for this care pathway.")
            
            # Display interventions without using nested columns
            interventions = [
                {"id": 1, "name": "Daily Weight Monitoring", "description": "Patient to record weight each morning", "assigned": True},
                {"id": 2, "name": "Fluid Restriction", "description": "Limit fluid intake to 1.5L per day", "assigned": True},
                {"id": 3, "name": "Sodium Restriction", "description": "Low sodium diet (<2000mg/day)", "assigned": True},
                {"id": 4, "name": "Cardiac Rehabilitation", "description": "Structured exercise program", "assigned": False},
                {"id": 5, "name": "Home Oxygen Therapy", "description": "Supplemental oxygen as needed", "assigned": False}
            ]
            
            for intervention in interventions:
                st.markdown(f"**{intervention['name']}**  \n{intervention['description']}")
                
                if intervention["assigned"]:
                    if st.button("Remove", key=f"remove_{intervention['id']}", use_container_width=True):
                        st.info(f"Removed {intervention['name']} from pathway")
                else:
                    if st.button("Add", key=f"add_{intervention['id']}", use_container_width=True):
                        st.success(f"Added {intervention['name']} to pathway")
                
                st.markdown("---")
            
            with st.expander("Add Custom Intervention"):
                with st.form("add_intervention_form"):
                    new_intervention_name = st.text_input("Intervention Name")
                    new_intervention_desc = st.text_area("Description")
                    if st.form_submit_button("Add Intervention"):
                        if new_intervention_name:
                            st.success(f"Added custom intervention: {new_intervention_name}")
                        else:
                            st.error("Intervention name is required")
        
        elif st.session_state.current_tab == "Medications":
            st.subheader("Medications")
            st.markdown("Configure medication recommendations for this care pathway.")
            
            # Display medications without nested columns
            medications = [
                {"id": 1, "name": "Lisinopril", "dosage": "10mg", "frequency": "Daily", "assigned": True},
                {"id": 2, "name": "Furosemide", "dosage": "40mg", "frequency": "Twice daily", "assigned": True},
                {"id": 3, "name": "Metoprolol", "dosage": "25mg", "frequency": "Twice daily", "assigned": True},
                {"id": 4, "name": "Spironolactone", "dosage": "25mg", "frequency": "Daily", "assigned": False},
                {"id": 5, "name": "Digoxin", "dosage": "0.125mg", "frequency": "Daily", "assigned": False}
            ]
            
            for med in medications:
                st.markdown(f"**{med['name']}** - {med['dosage']} - {med['frequency']}")
                
                if med["assigned"]:
                    if st.button("Remove", key=f"remove_med_{med['id']}", use_container_width=True):
                        st.info(f"Removed {med['name']} from pathway")
                else:
                    if st.button("Add", key=f"add_med_{med['id']}", use_container_width=True):
                        st.success(f"Added {med['name']} to pathway")
                
                st.markdown("---")
            
            with st.expander("Add Custom Medication"):
                with st.form("add_medication_form"):
                    new_med_name = st.text_input("Medication Name")
                    new_med_dosage = st.text_input("Dosage")
                    new_med_frequency = st.text_input("Frequency")
                    
                    if st.form_submit_button("Add Medication"):
                        if new_med_name and new_med_dosage and new_med_frequency:
                            st.success(f"Added custom medication: {new_med_name} {new_med_dosage} {new_med_frequency}")
                        else:
                            st.error("All fields are required")
        
        elif st.session_state.current_tab == "Education":
            st.subheader("Patient Education")
            st.markdown("Configure education resources for this care pathway.")
            
            # Display education topics without nested columns
            education_topics = [
                {"id": 1, "name": "Heart Failure Basics", "format": "Video", "duration": "10 min", "assigned": True},
                {"id": 2, "name": "Medication Management", "format": "Handout", "duration": "N/A", "assigned": True},
                {"id": 3, "name": "Symptom Recognition", "format": "Interactive Module", "duration": "15 min", "assigned": True},
                {"id": 4, "name": "Dietary Guidelines", "format": "Booklet", "duration": "N/A", "assigned": False},
                {"id": 5, "name": "Exercise Safety", "format": "Video", "duration": "12 min", "assigned": False}
            ]
            
            for topic in education_topics:
                st.markdown(f"**{topic['name']}** - {topic['format']} - {topic['duration']}")
                
                if topic["assigned"]:
                    if st.button("Remove", key=f"remove_edu_{topic['id']}", use_container_width=True):
                        st.info(f"Removed {topic['name']} from pathway")
                else:
                    if st.button("Add", key=f"add_edu_{topic['id']}", use_container_width=True):
                        st.success(f"Added {topic['name']} to pathway")
                
                st.markdown("---")
            
            with st.expander("Add Custom Education Resource"):
                with st.form("add_education_form"):
                    new_topic_name = st.text_input("Topic Name")
                    new_topic_format = st.selectbox("Format", ["Video", "Handout", "Interactive Module", "Booklet", "Website"])
                    new_topic_duration = st.text_input("Duration (if applicable)")
                    
                    if st.form_submit_button("Add Education Resource"):
                        if new_topic_name and new_topic_format:
                            st.success(f"Added custom education topic: {new_topic_name}")
                        else:
                            st.error("Topic name and format are required")
        
        st.markdown('</div></div>', unsafe_allow_html=True)
    
    # Column 3: Progress & Social Determinants
    with col3:
        # Progress Tracker
        st.markdown("""
        <div class="panel">
            <div class="panel-header">
                <h3>Progress & Support Factors</h3>
            </div>
            <div class="panel-body">
        """, unsafe_allow_html=True)
        
        # Calculate progress
        steps = get_patient_pathway_steps(st.session_state.selected_pathway["pathway_id"])
        complete_count = sum(1 for step in steps if step["status"] == "complete")
        in_progress_count = sum(1 for step in steps if step["status"] == "in-progress")
        not_started_count = sum(1 for step in steps if step["status"] == "not-started")
        total_steps = len(steps)
        progress_percent = int((complete_count / total_steps) * 100) if total_steps > 0 else 0
        
        st.subheader("Pathway Progress")
        
        # Progress bar
        progress_bar = st.progress(progress_percent / 100)
        
        # Progress stats
        progress_cols = st.columns(3)
        with progress_cols[0]:
            st.metric("Complete", complete_count)
        with progress_cols[1]:
            st.metric("In Progress", in_progress_count)
        with progress_cols[2]:
            st.metric("Not Started", not_started_count)
        
        st.markdown("<hr>", unsafe_allow_html=True)
        
        # Social Determinants
        st.subheader("Social Determinants")
        
        if st.button("Add Factor", key="add_factor", use_container_width=True):
            st.session_state.show_add_determinant = True
        
        # Add social determinant form
        if 'show_add_determinant' in st.session_state and st.session_state.show_add_determinant:
            with st.form("add_determinant_form"):
                st.subheader("Add Social Determinant")
                determinant_options = [
                    "Transportation", "Housing Insecurity", "Food Insecurity", 
                    "Financial Strain", "Social Isolation", "Health Literacy",
                    "Medication Access", "Technology Access"
                ]
                new_determinant = st.selectbox("Social Determinant", determinant_options)
                new_description = st.text_area("Description")
                new_impact = st.select_slider("Impact Level", ["MILD", "MODERATE", "SEVERE"])
                new_intervention = st.text_input("Planned Intervention")
                
                # Form buttons
                form_cols = st.columns(2)
                with form_cols[0]:
                    submit = st.form_submit_button("Add Factor")
                with form_cols[1]:
                    cancel = st.form_submit_button("Cancel")
                
                if submit and new_determinant and new_description:
                    # This would actually call add_social_determinant() with the form data
                    st.success(f"Social determinant '{new_determinant}' added successfully!")
                    st.session_state.show_add_determinant = False
                    st.experimental_rerun()
                elif cancel:
                    st.session_state.show_add_determinant = False
                    st.experimental_rerun()
        
        # Display social determinants
        social_determinants = get_patient_social_determinants(st.session_state.current_patient["patient_id"])
        
        for determinant in social_determinants:
            with st.expander(determinant["determinant_name"], expanded=True):
                st.markdown(f"**Impact Level:** {determinant['impact_level']}")
                st.markdown(f"**Description:** {determinant['description']}")
                st.markdown(f"**Intervention:** {determinant['intervention']}")
                
                if st.button("Edit", key=f"edit_determinant_{determinant['determinant_id']}", use_container_width=True):
                    st.session_state.editing_determinant = determinant["determinant_id"]
                    st.session_state.show_edit_determinant = True
        
        # Edit social determinant form
        if 'show_edit_determinant' in st.session_state and st.session_state.show_edit_determinant:
            editing_determinant = next((d for d in social_determinants if d["determinant_id"] == st.session_state.editing_determinant), None)
            if editing_determinant:
                with st.form("edit_determinant_form"):
                    st.subheader(f"Edit: {editing_determinant['determinant_name']}")
                    edit_description = st.text_area("Description", value=editing_determinant["description"])
                    edit_impact = st.select_slider("Impact Level", ["MILD", "MODERATE", "SEVERE"], value=editing_determinant["impact_level"])
                    edit_intervention = st.text_input("Planned Intervention", value=editing_determinant["intervention"])
                    
                    edit_cols = st.columns(2)
                    with edit_cols[0]:
                        save = st.form_submit_button("Save Changes")
                    with edit_cols[1]:
                        cancel = st.form_submit_button("Cancel")
                    
                    if save:
                        st.success(f"Social determinant updated successfully!")
                        st.session_state.show_edit_determinant = False
                        st.experimental_rerun()
                    elif cancel:
                        st.session_state.show_edit_determinant = False
                        st.experimental_rerun()
        
        st.markdown("<hr>", unsafe_allow_html=True)
        
        # Team Communication
        st.subheader("Team Communication")
        
        notes = get_pathway_notes()
        
        for note in notes:
            st.markdown(f"""
            <div style="padding: 10px; background-color: #f9fbfd; border-radius: 5px; margin-bottom: 10px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                    <div style="font-weight: 600;">{note["author"]}</div>
                    <div style="font-size: 12px; color: #95aac9;">{note["time"]}</div>
                </div>
                <div>{note["content"]}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Add note form
        with st.form("add_note_form"):
            new_note = st.text_area("Add a note for the care team...")
            if st.form_submit_button("Post Note", use_container_width=True):
                if new_note.strip():
                    st.success("Note posted successfully!")
                    # Clear the input
                    st.session_state.note_text = ""
                    # In a real app, this would call an API to save the note
                else:
                    st.warning("Please enter a note before posting.")
        
        st.markdown('</div></div>', unsafe_allow_html=True)

# Run the main function
if __name__ == "__main__":
    main()

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Care Pathway Management")
