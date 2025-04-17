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
    page_title="Medication Reconciliation | MediTrack", 
    page_icon="🏥", 
    layout="wide"
)

# Authentication check
if 'is_authenticated' not in st.session_state or not st.session_state.is_authenticated:
    st.switch_page("Home.py")
elif 'role' not in st.session_state or st.session_state.role != "pharmacist":
    st.warning("You don't have permission to access this page.")
    st.switch_page("Home.py")

# Display sidebar navigation
SideBarLinks(st.session_state.role)

# Custom CSS for medication reconciliation layout
st.markdown("""
<style>
    /* General Styles */
    :root {
      --primary: #2c7be5;
      --success: #00d97e;
      --warning: #f6c343;
      --danger: #e63757;
      --secondary: #95aac9;
      --light: #f9fbfd;
      --dark: #12263f;
      --white: #ffffff;
      --gray: #edf2f9;
    }

    /* Container Layout */
    .container {
        max-width: 100%;
        margin: 0 auto;
        padding: 0;
    }
    
    /* Patient Header */
    .patient-header {
        background-color: var(--white);
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
        width: 50px;
        height: 50px;
        border-radius: 8px;
        background-color: var(--secondary);
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 18px;
        font-weight: bold;
    }
    
    .patient-details h2 {
        margin-bottom: 5px;
        color: var(--dark);
        font-size: 20px;
    }
    
    .patient-details p {
        color: var(--secondary);
        margin-bottom: 3px;
        font-size: 14px;
    }
    
    /* Tabs Styling */
    .reconciliation-tabs {
        display: flex;
        border-bottom: 1px solid var(--gray);
        margin-bottom: 20px;
    }
    
    .reconciliation-tab {
        padding: 10px 20px;
        cursor: pointer;
        border-bottom: 2px solid transparent;
        color: var(--secondary);
    }
    
    .reconciliation-tab.active {
        color: var(--primary);
        border-bottom-color: var(--primary);
        font-weight: 600;
    }
    
    /* Filter Bar */
    .filter-bar {
        background-color: var(--white);
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        display: flex;
        gap: 15px;
    }
    
    /* Medication Cards */
    .comparison-item {
        background-color: var(--white);
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
        overflow: hidden;
        display: flex;
        border-left: 4px solid var(--primary);
    }
    
    .comparison-item.continued {
        border-left-color: var(--success);
    }
    
    .comparison-item.discontinued {
        border-left-color: var(--danger);
    }
    
    .comparison-item.new {
        border-left-color: var(--warning);
    }
    
    .med-column {
        flex: 1;
        padding: 15px;
        position: relative;
    }
    
    .med-column:first-child {
        border-right: 1px solid var(--gray);
    }
    
    .med-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
    }
    
    .med-name {
        font-weight: 600;
        font-size: 16px;
        color: var(--dark);
    }
    
    .med-status {
        font-size: 12px;
        padding: 3px 8px;
        border-radius: 20px;
        font-weight: 500;
    }
    
    .med-status.continued {
        background-color: rgba(0, 217, 126, 0.1);
        color: var(--success);
    }
    
    .med-status.discontinued {
        background-color: rgba(230, 55, 87, 0.1);
        color: var(--danger);
    }
    
    .med-status.new {
        background-color: rgba(246, 195, 67, 0.1);
        color: var(--warning);
    }
    
    .med-details {
        margin-bottom: 10px;
    }
    
    .med-details p {
        display: flex;
        justify-content: space-between;
        margin-bottom: 5px;
        font-size: 14px;
    }
    
    .med-detail-label {
        font-weight: 500;
        color: var(--dark);
    }
    
    .med-detail-value {
        color: var(--secondary);
    }
    
    .med-actions {
        display: flex;
        justify-content: flex-end;
        gap: 10px;
    }
    
    .action-button {
        padding: 5px 10px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
        cursor: pointer;
    }
    
    .primary-action {
        background-color: var(--primary);
        color: white;
    }
    
    .secondary-action {
        background-color: var(--light);
        color: var(--secondary);
    }
    
    .comparison-divider {
        position: absolute;
        width: 30px;
        height: 30px;
        background-color: var(--white);
        border: 1px solid var(--gray);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        top: 50%;
        right: -15px;
        transform: translateY(-50%);
        z-index: 10;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }
</style>
""", unsafe_allow_html=True)

# Check if a patient ID is passed, otherwise use a default
patient_id = st.session_state.get('selected_patient_id', 101)  # Default to patient 101 if none selected

# Mock function to get patient data (would be replaced with actual API call)
def get_patient_data(patient_id):
    # In a real app, this would call an API endpoint
    patients = {
        101: {
            "patient_id": 101,
            "first_name": "John",
            "last_name": "Doe",
            "dob": "1968-05-15",
            "gender": "Male",
            "admission": "2025-03-20",
            "discharge": "2025-03-23",
            "discharge_status": "Planned"
        },
        103: {
            "patient_id": 103,
            "first_name": "Michael",
            "last_name": "Brown",
            "dob": "1975-03-10",
            "gender": "Male",
            "admission": "2025-03-15",
            "discharge": "2025-03-22",
            "discharge_status": "Planned"
        },
        108: {
            "patient_id": 108,
            "first_name": "William",
            "last_name": "Wilson",
            "dob": "1960-07-22",
            "gender": "Male",
            "admission": "2025-03-10",
            "discharge": "2025-03-25",
            "discharge_status": "Planned"
        }
    }
    
    return patients.get(patient_id, patients[101])  # Default to John Doe if patient not found

# Mock function to get medication reconciliation data
def get_medication_reconciliation(patient_id):
    # In a real app, this would call the API:
    # response = requests.get(f"http://web-api:4000/ph/prescription-patient-records/{patient_id}")
    # return response.json()
    
    # For demo, return mock data
    if patient_id == 101:
        return {
            "pre_admission": [
                {
                    "medication_name": "Lisinopril 10mg",
                    "status": "continued",
                    "dosage": "10mg oral tablet",
                    "frequency": "Once daily",
                    "prescriber": "Dr. Jones (PCP)",
                    "last_filled": "Mar 10, 2025"
                },
                {
                    "medication_name": "Metformin 500mg",
                    "status": "continued",
                    "dosage": "500mg oral tablet",
                    "frequency": "Twice daily",
                    "prescriber": "Dr. Jones (PCP)",
                    "last_filled": "Mar 5, 2025"
                },
                {
                    "medication_name": "Aspirin 81mg",
                    "status": "discontinued",
                    "dosage": "81mg oral tablet",
                    "frequency": "Once daily",
                    "prescriber": "Dr. Jones (PCP)",
                    "last_filled": "Feb 20, 2025"
                }
            ],
            "post_discharge": [
                {
                    "medication_name": "Lisinopril 10mg",
                    "status": "continued",
                    "dosage": "10mg oral tablet",
                    "frequency": "Once daily",
                    "prescriber": "Dr. Wilson",
                    "supply": "30 days"
                },
                {
                    "medication_name": "Metformin 500mg",
                    "status": "continued",
                    "dosage": "500mg oral tablet",
                    "frequency": "Twice daily",
                    "prescriber": "Dr. Wilson",
                    "supply": "30 days"
                },
                {
                    "medication_name": "Atorvastatin 20mg",
                    "status": "new",
                    "dosage": "20mg oral tablet",
                    "frequency": "Once daily at bedtime",
                    "prescriber": "Dr. Wilson",
                    "supply": "30 days"
                }
            ]
        }
    else:
        # Return similar structure but with different medications for other patients
        return {
            "pre_admission": [
                {
                    "medication_name": "Sample Medication 1",
                    "status": "continued",
                    "dosage": "Sample dosage",
                    "frequency": "Sample frequency",
                    "prescriber": "Sample prescriber",
                    "last_filled": "Sample date"
                }
            ],
            "post_discharge": [
                {
                    "medication_name": "Sample Medication 1",
                    "status": "continued",
                    "dosage": "Sample dosage",
                    "frequency": "Sample frequency",
                    "prescriber": "Sample prescriber",
                    "supply": "Sample supply"
                }
            ]
        }

# Get patient data
patient = get_patient_data(patient_id)
med_reconciliation = get_medication_reconciliation(patient_id)

# Calculate patient age
birth_year = int(patient["dob"].split('-')[0])
current_year = 2025  # Using current year from project
age = current_year - birth_year

# Page title
st.title("Medication Reconciliation")

# Patient header
st.markdown(f"""
<div class="patient-header">
    <div class="patient-info">
        <div class="patient-avatar">{patient['first_name'][0]}{patient['last_name'][0]}</div>
        <div class="patient-details">
            <h2>{patient['first_name']} {patient['last_name']}</h2>
            <p>ID: {patient['patient_id']} • {age} years • {patient['gender']}</p>
            <p>Admission: {patient['admission']} • Discharge: {patient['discharge']} ({patient['discharge_status']})</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Action buttons
col1, col2 = st.columns(2)
with col1:
    st.button("View Full Profile", use_container_width=True)
with col2:
    st.button("Complete Reconciliation", use_container_width=True)

# Reconciliation tabs
if 'reconciliation_tab' not in st.session_state:
    st.session_state.reconciliation_tab = "medication_reconciliation"

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Medication Reconciliation", "Schedule Optimization", "Patient Counseling", "Transition Checklist"])

with tab1:
    # Filter section
    st.subheader("Medication Reconciliation")
    
    # Filter options
    filter_options = ["All Medications", "Continued Only", "Discontinued", "New Medications"]
    selected_filter = st.selectbox("Filter medications", filter_options, label_visibility="visible")
    
    # Pre-Admission Medications section
    st.subheader("Pre-Admission Medications")
    st.caption("Home medications reported at intake")
    
    # Post-Discharge Medications section
    pre_col, post_col = st.columns(2)
    
    with pre_col:
        # Pre-admission medications
        for medication in med_reconciliation["pre_admission"]:
            # Apply filter if needed
            if selected_filter != "All Medications":
                if (selected_filter == "Continued Only" and medication["status"] != "continued") or \
                   (selected_filter == "Discontinued" and medication["status"] != "discontinued") or \
                   (selected_filter == "New Medications" and medication["status"] != "new"):
                    continue
            
            st.markdown(f"""
            <div style="border-left: 4px solid {'#00d97e' if medication['status'] == 'continued' else '#e63757'}; padding: 15px; margin-bottom: 15px; background-color: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
                <h3>{medication['medication_name']}</h3>
                <p><strong>Dose:</strong> {medication['dosage']}</p>
                <p><strong>Frequency:</strong> {medication['frequency']}</p>
                <p><strong>Prescriber:</strong> {medication['prescriber']}</p>
                <p><strong>Last Filled:</strong> {medication['last_filled']}</p>
                <div style="background-color: {'rgba(0, 217, 126, 0.1)' if medication['status'] == 'continued' else 'rgba(230, 55, 87, 0.1)'}; 
                            color: {'#00d97e' if medication['status'] == 'continued' else '#e63757'}; 
                            display: inline-block; 
                            padding: 5px 10px; 
                            border-radius: 20px; 
                            font-size: 12px; 
                            margin-top: 10px;">
                    {medication['status'].capitalize()}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with post_col:
        # Post-discharge medications
        st.subheader("Post-Discharge Medications")
        st.caption("Medications prescribed for discharge")
        
        for medication in med_reconciliation["post_discharge"]:
            # Apply filter if needed
            if selected_filter != "All Medications":
                if (selected_filter == "Continued Only" and medication["status"] != "continued") or \
                   (selected_filter == "Discontinued" and medication["status"] != "discontinued") or \
                   (selected_filter == "New Medications" and medication["status"] != "new"):
                    continue
            
            status_color = "#00d97e" if medication['status'] == "continued" else "#f6c343" if medication['status'] == "new" else "#e63757"
            status_bg = f"rgba({','.join(str(int(status_color[i:i+2], 16)) for i in (1, 3, 5))}, 0.1)"
            
            st.markdown(f"""
            <div style="border-left: 4px solid {status_color}; padding: 15px; margin-bottom: 15px; background-color: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
                <h3>{medication['medication_name']}</h3>
                <p><strong>Dose:</strong> {medication['dosage']}</p>
                <p><strong>Frequency:</strong> {medication['frequency']}</p>
                <p><strong>Prescriber:</strong> {medication['prescriber']}</p>
                <p><strong>Supply:</strong> {medication['supply']}</p>
                <div style="background-color: {status_bg}; 
                            color: {status_color}; 
                            display: inline-block; 
                            padding: 5px 10px; 
                            border-radius: 20px; 
                            font-size: 12px; 
                            margin-top: 10px;">
                    {medication['status'].capitalize()}
                </div>
            </div>
            """, unsafe_allow_html=True)

# Optional: Additional functionality for other tabs
with tab2:
    st.write("Schedule Optimization functionality will be implemented here.")

with tab3:
    st.write("Patient Counseling functionality will be implemented here.")

with tab4:
    st.write("Transition Checklist functionality will be implemented here.")

# Navigation buttons at the bottom
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Back to Dashboard", use_container_width=True):
        st.switch_page("pages/21_Pharmacist_Home.py")

with col2:
    if st.button("Medication Review", use_container_width=True):
        # Set patient_id in session state for the next page
        st.session_state.selected_patient_id = patient_id
        st.switch_page("pages/22_Medication_Review.py")

with col3:
    if st.button("Patient Education", use_container_width=True):
        # Set patient_id in session state for the next page
        st.session_state.selected_patient_id = patient_id
        st.switch_page("pages/25_Patient_Education.py")

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Medication Reconciliation")
