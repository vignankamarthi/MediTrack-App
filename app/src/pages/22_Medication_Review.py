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
    page_title="Medication Review | MediTrack", 
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

# Add CSS for medication review layout
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
    
    /* Card Styles */
    .card {
        background-color: var(--white);
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        overflow: hidden;
        margin-bottom: 20px;
    }
    
    .card-header {
        padding: 15px;
        border-bottom: 1px solid var(--gray);
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: var(--light);
    }
    
    .card-title {
        font-size: 16px;
        font-weight: 600;
        color: var(--dark);
        margin: 0;
    }
    
    .card-actions {
        display: flex;
        gap: 10px;
    }
    
    .card-body {
        padding: 15px;
    }
    
    /* Medication Table */
    .medication-table {
        width: 100%;
        border-collapse: collapse;
    }
    
    .medication-table th {
        background-color: var(--light);
        padding: 10px;
        text-align: left;
        color: var(--secondary);
        font-weight: 600;
        font-size: 12px;
        text-transform: uppercase;
    }
    
    .medication-table td {
        padding: 12px 10px;
        border-bottom: 1px solid var(--gray);
        color: var(--dark);
    }
    
    .medication-table tr:last-child td {
        border-bottom: none;
    }
    
    .medication-table tr:hover {
        background-color: var(--light);
    }
    
    .med-name {
        display: flex;
        flex-direction: column;
    }
    
    .med-brand {
        font-weight: 600;
        color: var(--dark);
    }
    
    .med-generic {
        font-size: 12px;
        color: var(--secondary);
    }
    
    .action-icons {
        display: flex;
        gap: 10px;
    }
    
    .med-flagged {
        background-color: rgba(246, 195, 67, 0.1);
    }
    
    /* Timeline Styles */
    .timeline-container {
        padding: 15px 0;
    }
    
    .timeline-header {
        display: flex;
        border-bottom: 1px solid var(--gray);
        padding-bottom: 10px;
        margin-bottom: 15px;
    }
    
    .time-marker {
        flex: 1;
        text-align: center;
        font-size: 12px;
        color: var(--secondary);
    }
    
    .timeline-body {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }
    
    .timeline-item {
        display: flex;
        align-items: center;
        height: 40px;
    }
    
    .timeline-item-label {
        width: 20%;
        font-size: 14px;
        font-weight: 500;
        color: var(--dark);
        padding-right: 15px;
    }
    
    .timeline-item-bar {
        position: relative;
        height: 20px;
        background-color: var(--primary);
        border-radius: 4px;
        flex: 1;
    }
    
    .timeline-item.discontinued .timeline-item-bar {
        background-color: var(--secondary);
        opacity: 0.7;
    }
    
    .timeline-item.discontinued .timeline-item-label {
        text-decoration: line-through;
        color: var(--secondary);
    }
    
    .dosage-change {
        position: absolute;
        width: 4px;
        height: 20px;
        background-color: var(--warning);
        cursor: pointer;
    }
    
    .discontinue-marker {
        position: absolute;
        width: 4px;
        height: 20px;
        background-color: var(--danger);
        cursor: pointer;
    }
    
    /* Alert Styles */
    .alerts-container {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }
    
    .alert {
        display: flex;
        border-radius: 5px;
        overflow: hidden;
    }
    
    .alert-danger {
        border: 1px solid var(--danger);
        background-color: rgba(230, 55, 87, 0.1);
    }
    
    .alert-warning {
        border: 1px solid var(--warning);
        background-color: rgba(246, 195, 67, 0.1);
    }
    
    .alert-icon {
        width: 50px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 24px;
    }
    
    .alert-danger .alert-icon {
        background-color: var(--danger);
        color: white;
    }
    
    .alert-warning .alert-icon {
        background-color: var(--warning);
        color: white;
    }
    
    .alert-content {
        padding: 15px;
        flex: 1;
    }
    
    .alert-content h4 {
        margin-bottom: 5px;
        color: var(--dark);
    }
    
    .alert-content p {
        margin-bottom: 10px;
        color: var(--dark);
    }
    
    .alert-actions {
        display: flex;
        gap: 10px;
    }
    
    /* Efficacy Feedback Styles */
    .feedback-item {
        padding: 15px;
        border-bottom: 1px solid var(--gray);
    }
    
    .feedback-item:last-child {
        border-bottom: none;
    }
    
    .feedback-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
    
    .feedback-header h4 {
        color: var(--dark);
        margin: 0;
    }
    
    .badge {
        padding: 4px 8px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 500;
    }
    
    .badge-success {
        background-color: var(--success);
        color: white;
    }
    
    .badge-warning {
        background-color: var(--warning);
        color: var(--dark);
    }
    
    .feedback-metrics {
        display: flex;
        gap: 15px;
        margin-bottom: 10px;
    }
    
    .metric {
        flex: 1;
        background-color: var(--light);
        padding: 10px;
        border-radius: 5px;
        text-align: center;
    }
    
    .metric-label {
        font-size: 12px;
        color: var(--secondary);
        margin-bottom: 5px;
    }
    
    .metric-value {
        font-size: 16px;
        font-weight: 600;
        color: var(--dark);
        margin-bottom: 5px;
    }
    
    .metric-target {
        font-size: 11px;
        color: var(--secondary);
    }
    
    .feedback-notes {
        margin-bottom: 10px;
    }
    
    .feedback-notes p {
        font-size: 14px;
        color: var(--dark);
    }
    
    .feedback-actions {
        display: flex;
        justify-content: flex-end;
    }
    
    /* Message Styles */
    .message-list {
        display: flex;
        flex-direction: column;
        gap: 15px;
        margin-bottom: 15px;
        max-height: 300px;
        overflow-y: auto;
    }
    
    .message {
        padding: 12px;
        background-color: var(--light);
        border-radius: 5px;
        border-top-left-radius: 0;
    }
    
    .message.outgoing {
        background-color: rgba(44, 123, 229, 0.1);
        border-top-right-radius: 0;
        border-top-left-radius: 5px;
        align-self: flex-end;
    }
    
    .message-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 8px;
    }
    
    .message-from {
        font-weight: 600;
        color: var(--dark);
        font-size: 14px;
    }
    
    .message-time {
        font-size: 12px;
        color: var(--secondary);
    }
    
    .message-content {
        font-size: 14px;
        color: var(--dark);
    }
    
    /* Dashboard Layout */
    .dashboard {
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 20px;
    }
    
    .main-section {
        display: flex;
        flex-direction: column;
        gap: 20px;
    }
    
    /* Adjustment Form Styles */
    .adjustment-form {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }
    
    .form-group {
        display: flex;
        flex-direction: column;
        gap: 5px;
    }
    
    .form-group label {
        font-size: 14px;
        font-weight: 500;
        color: var(--dark);
    }
    
    .form-actions {
        display: flex;
        justify-content: flex-end;
        gap: 10px;
        margin-top: 10px;
    }
    
    /* Icon styles (simulated) */
    .icon-container {
        display: inline-flex;
        width: 24px;
        height: 24px;
        align-items: center;
        justify-content: center;
        border-radius: 4px;
        background-color: #f5f8fa;
    }
</style>
""", unsafe_allow_html=True)

# Check if a patient ID is passed, otherwise use a default
patient_id = st.session_state.get('selected_patient_id', 101)  # Default to patient 101 if none selected

# Mock function to get patient data (would be replaced with actual API call)
def get_patient_data(patient_id):
    # In a real app, this would call:
    # response = requests.get(f"http://web-api:4000/ph/medication-record/{patient_id}")
    # return response.json()
    
    # For demo purposes, return mock data
    patients = {
        101: {
            "patient_id": 101,
            "first_name": "John",
            "last_name": "Doe",
            "dob": "1968-05-15",
            "gender": "Male",
            "allergies": "Penicillin, Sulfa",
            "primary_provider": "Dr. James Wilson"
        },
        103: {
            "patient_id": 103,
            "first_name": "Michael",
            "last_name": "Brown",
            "dob": "1975-03-10",
            "gender": "Male",
            "allergies": "None",
            "primary_provider": "Dr. Michael Chen"
        },
        108: {
            "patient_id": 108,
            "first_name": "William",
            "last_name": "Wilson",
            "dob": "1960-07-22",
            "gender": "Male",
            "allergies": "Codeine",
            "primary_provider": "Dr. James Wilson"
        }
    }
    
    return patients.get(patient_id, patients[101])  # Default to John Doe if patient not found

# Mock function to get patient medications
def get_patient_medications(patient_id):
    # In a real app, this would call:
    # response = requests.get(f"http://web-api:4000/ph/medication-record/{patient_id}")
    # return response.json()
    
    # For demo, return mock data
    medications = {
        101: [
            {
                "medication_id": 1,
                "medication_name": "Lisinopril",
                "generic_name": "lisinopril",
                "dosage": "10mg",
                "frequency": "Once daily",
                "prescriber": "Dr. James Wilson",
                "start_date": "Jan 15, 2025",
                "is_flagged": False
            },
            {
                "medication_id": 2,
                "medication_name": "Metformin",
                "generic_name": "metformin hcl",
                "dosage": "500mg",
                "frequency": "Twice daily",
                "prescriber": "Dr. Maria Lopez",
                "start_date": "Dec 10, 2024",
                "is_flagged": False
            },
            {
                "medication_id": 3,
                "medication_name": "Lipitor",
                "generic_name": "atorvastatin",
                "dosage": "20mg",
                "frequency": "Once daily at bedtime",
                "prescriber": "Dr. James Wilson",
                "start_date": "Feb 05, 2025",
                "is_flagged": True
            },
            {
                "medication_id": 4,
                "medication_name": "Aspirin",
                "generic_name": "acetylsalicylic acid",
                "dosage": "81mg",
                "frequency": "Once daily",
                "prescriber": "Dr. James Wilson",
                "start_date": "Jan 15, 2025",
                "is_flagged": False
            }
        ],
        103: [
            {
                "medication_id": 6,
                "medication_name": "Levothyroxine",
                "generic_name": "levothyroxine sodium",
                "dosage": "50mcg",
                "frequency": "Once daily",
                "prescriber": "Dr. Michael Chen",
                "start_date": "Jan 03, 2025",
                "is_flagged": False
            },
            {
                "medication_id": 7,
                "medication_name": "Omeprazole",
                "generic_name": "omeprazole",
                "dosage": "20mg",
                "frequency": "Once daily",
                "prescriber": "Dr. Michael Chen",
                "start_date": "Feb 12, 2025",
                "is_flagged": False
            }
        ],
        108: [
            {
                "medication_id": 5,
                "medication_name": "Amlodipine",
                "generic_name": "amlodipine besylate",
                "dosage": "5mg",
                "frequency": "Once daily",
                "prescriber": "Dr. James Wilson",
                "start_date": "Dec 22, 2024",
                "is_flagged": False
            },
            {
                "medication_id": 9,
                "medication_name": "Hydrochlorothiazide",
                "generic_name": "hydrochlorothiazide",
                "dosage": "25mg",
                "frequency": "Once daily",
                "prescriber": "Dr. James Wilson",
                "start_date": "Dec 22, 2024",
                "is_flagged": False
            },
            {
                "medication_id": 11,
                "medication_name": "Warfarin",
                "generic_name": "warfarin sodium",
                "dosage": "2mg",
                "frequency": "Once daily",
                "prescriber": "Dr. Emily Rodriguez",
                "start_date": "Jan 10, 2025",
                "is_flagged": True
            },
            {
                "medication_id": 12,
                "medication_name": "Nifedipine",
                "generic_name": "nifedipine",
                "dosage": "30mg",
                "frequency": "Once daily",
                "prescriber": "Dr. James Wilson",
                "start_date": "Jan 20, 2025",
                "is_flagged": True
            }
        ]
    }
    
    return medications.get(patient_id, [])  # Return empty list if patient has no medications

# Function to get drug interactions
def get_drug_interactions(patient_id):
    # In a real app, this would call an API
    # For demo purposes, return mock data
    interactions = {
        101: [
            {
                "severity": "high",
                "title": "Significant Interaction Detected",
                "description": "Lipitor (atorvastatin) and Gemfibrozil interaction increases risk of myopathy and rhabdomyolysis.",
                "medications": ["Lipitor", "Gemfibrozil"]
            },
            {
                "severity": "medium",
                "title": "Moderate Interaction",
                "description": "Aspirin may decrease the effectiveness of Lisinopril. Monitor blood pressure closely.",
                "medications": ["Aspirin", "Lisinopril"]
            }
        ],
        108: [
            {
                "severity": "high",
                "title": "Significant Interaction Detected",
                "description": "Warfarin and Amlodipine interaction may increase anticoagulant effect. Monitor INR closely.",
                "medications": ["Warfarin", "Amlodipine"]
            },
            {
                "severity": "medium",
                "title": "Duplicate Therapy",
                "description": "Amlodipine and Nifedipine are both calcium channel blockers. Possible therapeutic duplication.",
                "medications": ["Amlodipine", "Nifedipine"]
            }
        ],
        103: []  # No interactions for patient 103
    }
    
    return interactions.get(patient_id, [])

# Function to get medication efficacy data
def get_medication_efficacy(patient_id):
    # In a real app, this would call an API endpoint
    # For demo purposes, return mock data
    efficacy_data = {
        101: [
            {
                "medication_name": "Lisinopril 10mg",
                "status": "Effective",
                "metrics": [
                    {
                        "label": "Blood Pressure",
                        "value": "130/82 mmHg",
                        "target": "Target: <140/90"
                    }
                ],
                "notes": "Patient reports good tolerance. Blood pressure adequately controlled."
            },
            {
                "medication_name": "Metformin 500mg",
                "status": "Partially Effective",
                "metrics": [
                    {
                        "label": "HbA1c",
                        "value": "7.8%",
                        "target": "Target: <7.0%"
                    },
                    {
                        "label": "Fasting Glucose",
                        "value": "142 mg/dL",
                        "target": "Target: 80-130 mg/dL"
                    }
                ],
                "notes": "Patient reports occasional GI discomfort. Glycemic control improving but not at target."
            }
        ],
        108: [
            {
                "medication_name": "Amlodipine 5mg",
                "status": "Effective",
                "metrics": [
                    {
                        "label": "Blood Pressure",
                        "value": "128/76 mmHg",
                        "target": "Target: <130/80"
                    }
                ],
                "notes": "Good blood pressure control with no reported side effects."
            },
            {
                "medication_name": "Warfarin 2mg",
                "status": "Partially Effective",
                "metrics": [
                    {
                        "label": "INR",
                        "value": "1.8",
                        "target": "Target: 2.0-3.0"
                    }
                ],
                "notes": "INR slightly below target range. Consider dose adjustment."
            }
        ],
        103: [
            {
                "medication_name": "Levothyroxine 50mcg",
                "status": "Effective",
                "metrics": [
                    {
                        "label": "TSH",
                        "value": "2.4 mIU/L",
                        "target": "Target: 0.5-4.0 mIU/L"
                    }
                ],
                "notes": "Thyroid function well controlled at current dose."
            }
        ]
    }
    
    return efficacy_data.get(patient_id, [])

# Function to get prescriber messages
def get_prescriber_messages(patient_id):
    # In a real app, this would call an API endpoint
    # For demo purposes, return mock data
    messages = {
        101: [
            {
                "from": "Dr. James Wilson",
                "time": "Yesterday, 3:45 PM",
                "content": "Thank you for the recommendation. I've adjusted the Lipitor dosage as suggested.",
                "outgoing": False
            },
            {
                "from": "You (Sarah Chen, PharmD)",
                "time": "Yesterday, 2:30 PM",
                "content": "Patient reports muscle pain that may be related to Lipitor. Consider reducing dosage to 10mg and monitoring symptoms.",
                "outgoing": True
            }
        ],
        108: [
            {
                "from": "Dr. Emily Rodriguez",
                "time": "Today, 10:15 AM",
                "content": "Would you recommend any adjustments to patient's Warfarin dosage based on latest INR results?",
                "outgoing": False
            }
        ],
        103: []  # No messages for patient 103
    }
    
    return messages.get(patient_id, [])

# Get patient data
patient = get_patient_data(patient_id)
medications = get_patient_medications(patient_id)
interactions = get_drug_interactions(patient_id)
efficacy_data = get_medication_efficacy(patient_id)
messages = get_prescriber_messages(patient_id)

# Calculate patient age
birth_year = int(patient["dob"].split('-')[0])
current_year = 2025  # Using current year from project
age = current_year - birth_year

# Initialize state for showing the adjustment panel
if 'show_adjustment_panel' not in st.session_state:
    st.session_state.show_adjustment_panel = False

# Display patient header
st.markdown(f"""
<div class="patient-header">
    <div class="patient-info">
        <div class="patient-avatar">{patient['first_name'][0]}{patient['last_name'][0]}</div>
        <div class="patient-details">
            <h2>{patient['first_name']} {patient['last_name']}</h2>
            <p>ID: {patient['patient_id']} • {age} years • {patient['gender']}</p>
            <p>Known Allergies: {patient['allergies']} • Primary: {patient['primary_provider']}</p>
        </div>
    </div>
    <div class="action-buttons">
    </div>
</div>
""", unsafe_allow_html=True)

# Action buttons for patient
col1, col2 = st.columns(2)
with col1:
    st.button("Patient History", use_container_width=True)
with col2:
    if st.button("Medication Reconciliation", use_container_width=True):
        st.switch_page("pages/24_Medication_Reconciliation.py")

# Create dashboard layout
dashboard_container = st.container()
col_left, col_right = dashboard_container.columns([2, 1])

# Left column - Main content
with col_left:
    # Current Medications Panel
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">Current Medication Profile</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Action buttons for medications panel
    col1, col2 = st.columns([6, 1])
    with col2:
        st.button("Add Medication", use_container_width=True)
    with col1:
        st.write("")  # Empty space for alignment
    
    # Create medication table
    if medications:
        # Define state for medication flags if it doesn't exist
        if 'med_flags' not in st.session_state:
            st.session_state.med_flags = {m['medication_id']: m['is_flagged'] for m in medications}
        
        # Create a dataframe for display
        med_data = []
        for med in medications:
            med_data.append({
                "Medication": f"<div class='med-name'><span class='med-brand'>{med['medication_name']}</span><span class='med-generic'>{med['generic_name']}</span></div>",
                "Dosage": med['dosage'],
                "Frequency": med['frequency'],
                "Prescriber": med['prescriber'],
                "Start Date": med['start_date'],
                "Actions": f"""
                    <div class='action-icons'>
                        <span class='icon-container'>✏️</span>
                        <span class='icon-container'>✓</span>
                        <span class='icon-container' id='flag_{med['medication_id']}'>🚩</span>
                    </div>
                """,
                "is_flagged": st.session_state.med_flags[med['medication_id']],
                "medication_id": med['medication_id']
            })
        
        df = pd.DataFrame(med_data)
        
        # Display table
        st.write("""
        <table class="medication-table">
            <thead>
                <tr>
                    <th>Medication</th>
                    <th>Dosage</th>
                    <th>Frequency</th>
                    <th>Prescriber</th>
                    <th>Start Date</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
        """, unsafe_allow_html=True)
        
        for idx, row in df.iterrows():
            flagged_class = "med-flagged" if row['is_flagged'] else ""
            st.write(f"""
            <tr class="{flagged_class}" id="med_row_{row['medication_id']}">
                <td>{row['Medication']}</td>
                <td>{row['Dosage']}</td>
                <td>{row['Frequency']}</td>
                <td>{row['Prescriber']}</td>
                <td>{row['Start Date']}</td>
                <td>{row['Actions']}</td>
            </tr>
            """, unsafe_allow_html=True)
        
        st.write("""
            </tbody>
        </table>
        """, unsafe_allow_html=True)
        
        # Add flag toggle functionality via buttons
        st.markdown("<div style='display: flex; gap: 10px; margin-top: 15px;'>", unsafe_allow_html=True)
        
        # Generate a toggle button for each medication
        cols = st.columns(len(medications))
        for i, med in enumerate(medications):
            med_id = med['medication_id']
            med_name = med['medication_name']
            is_flagged = st.session_state.med_flags[med_id]
            
            # Create a unique key for each button
            key = f"flag_toggle_{med_id}"
            
            # Create button with appropriate label
            label = f"Unflag {med_name}" if is_flagged else f"Flag {med_name}"
            with cols[i]:
                if st.button(label, key=key):
                    # Toggle the flag state in session_state
                    st.session_state.med_flags[med_id] = not is_flagged
                    st.experimental_rerun()  # Rerun the app to update UI
    
    st.markdown("</div>", unsafe_allow_html=True)  # Close the medication panel
    
    # Medication Timeline Panel
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">Medication Timeline</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Timeline filters
    col1, col2 = st.columns(2)
    with col1:
        filter_type = st.selectbox(
            "Filter medications",
            ["All Medications", "Active Only", "Discontinued"],
            label_visibility="collapsed"
        )
    with col2:
        time_range = st.selectbox(
            "Time range",
            ["Last 12 Months", "Last 6 Months", "Last 3 Months", "All Time"],
            label_visibility="collapsed"
        )
    
    # Timeline visualization
    st.markdown("""
    <div class="timeline-container">
        <div class="timeline-header">
            <div class="time-marker">Jan 2025</div>
            <div class="time-marker">Feb 2025</div>
            <div class="time-marker">Mar 2025</div>
        </div>
        <div class="timeline-body">
    """, unsafe_allow_html=True)
    
    # Display timeline items
    for med in medications:
        # For demo purposes, we'll just display based on the medication name
        # In a real app, this would use actual start/end dates and calculate positions
        
        # Determine the position and width based on medication start date
        if "Jan" in med["start_date"]:
            left_pos = "5%"
            width = "95%"
        elif "Feb" in med["start_date"]:
            left_pos = "40%"
            width = "60%"
        elif "Dec" in med["start_date"]:
            left_pos = "0%"
            width = "100%"
        else:
            left_pos = "20%"
            width = "80%"
        
        # Add discontinued class if needed (for demo, we'll just add one)
        discontinued_class = "discontinued" if med["medication_name"] == "Ibuprofen" else ""
        
        st.markdown(f"""
        <div class="timeline-item {discontinued_class}">
            <div class="timeline-item-label">{med['medication_name']} {med['dosage']}</div>
            <div class="timeline-item-bar" style="left: {left_pos}; width: {width};">
                <!-- Add markers here if needed -->
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Add one discontinued medication for demo
    if patient_id == 101:
        st.markdown("""
        <div class="timeline-item discontinued">
            <div class="timeline-item-label">Ibuprofen 400mg</div>
            <div class="timeline-item-bar" style="left: 0%; width: 20%;">
                <div class="discontinue-marker" style="right: 0;" title="Discontinued on Jan 20, 2025"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)  # Close the timeline container
    
    st.markdown("</div>", unsafe_allow_html=True)  # Close the timeline panel card
    
    # Drug Interaction Panel
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">Interaction Analysis</h3>
        </div>
        <div class="card-body">
            <div class="alerts-container">
    """, unsafe_allow_html=True)
    
    # Display interactions if any
    if interactions:
        for interaction in interactions:
            alert_class = "alert-danger" if interaction["severity"] == "high" else "alert-warning"
            icon = "⚠️" if interaction["severity"] == "high" else "ℹ️"
            
            st.markdown(f"""
            <div class="alert {alert_class}">
                <div class="alert-icon">{icon}</div>
                <div class="alert-content">
                    <h4>{interaction['title']}</h4>
                    <p>{interaction['description']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Add action buttons for interactions
            col1, col2 = st.columns(2)
            with col1:
                st.button("View Details", key=f"view_details_{interaction['title'][:10]}", use_container_width=True)
            with col2:
                if interaction["severity"] == "high":
                    # Request adjustment button that toggles the panel
                    if st.button("Request Adjustment", key=f"req_adj_{interaction['title'][:10]}", use_container_width=True):
                        st.session_state.show_adjustment_panel = True
                else:
                    st.button("Add Monitoring Note", key=f"add_note_{interaction['title'][:10]}", use_container_width=True)
    else:
        st.info("No medication interactions detected for this patient.")
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)  # Close the interaction panel

# Right column - Sidebar content
with col_right:
    # Medication Efficacy Feedback Panel
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">Medication Efficacy Feedback</h3>
        </div>
        <div class="card-body">
    """, unsafe_allow_html=True)
    
    # Display efficacy data
    if efficacy_data:
        for item in efficacy_data:
            status_class = "badge-success" if item["status"] == "Effective" else "badge-warning"
            
            st.markdown(f"""
            <div class="feedback-item">
                <div class="feedback-header">
                    <h4>{item['medication_name']}</h4>
                    <span class="badge {status_class}">{item['status']}</span>
                </div>
                <div class="feedback-metrics">
            """, unsafe_allow_html=True)
            
            # Display metrics
            for metric in item["metrics"]:
                st.markdown(f"""
                <div class="metric">
                    <div class="metric-label">{metric['label']}</div>
                    <div class="metric-value">{metric['value']}</div>
                    <div class="metric-target">{metric['target']}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("""
                </div>
                <div class="feedback-notes">
                    <p>{}</p>
                </div>
            """.format(item["notes"]), unsafe_allow_html=True)
            
            # Add update efficacy button
            if st.button("Update Efficacy", key=f"update_efficacy_{item['medication_name'][:10]}", use_container_width=True):
                st.session_state.show_efficacy_form = item['medication_name']
    else:
        st.info("No efficacy data available for this patient.")
    
    # Show efficacy update form if requested
    if "show_efficacy_form" in st.session_state and st.session_state.show_efficacy_form:
        med_name = st.session_state.show_efficacy_form
        with st.form(key=f"efficacy_form_{med_name}"):
            st.subheader(f"Update Efficacy for {med_name}")
            status = st.selectbox("Effectiveness", ["Effective", "Partially Effective", "Not Effective"])
            metric_value = st.text_input("Metric Value (e.g. 130/80 mmHg)")
            notes = st.text_area("Clinical Notes")
            
            col1, col2 = st.columns(2)
            with col1:
                submit = st.form_submit_button("Save")
            with col2:
                cancel = st.form_submit_button("Cancel")
                
            if submit:
                st.success(f"Efficacy data updated for {med_name}")
                st.session_state.show_efficacy_form = None
                st.experimental_rerun()
            elif cancel:
                st.session_state.show_efficacy_form = None
                st.experimental_rerun()
    
    st.markdown("</div></div>", unsafe_allow_html=True)  # Close the efficacy panel
    
    # Prescriber Communication Panel
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">Prescriber Communication</h3>
        </div>
        <div class="card-body">
            <div class="message-list">
    """, unsafe_allow_html=True)
    
    # Display messages
    if messages:
        for message in messages:
            message_class = "outgoing" if message["outgoing"] else ""
            
            st.markdown(f"""
            <div class="message {message_class}">
                <div class="message-header">
                    <div class="message-from">{message['from']}</div>
                    <div class="message-time">{message['time']}</div>
                </div>
                <div class="message-content">
                    {message['content']}
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No communication history with prescribers for this patient.")
    
    st.markdown("</div>", unsafe_allow_html=True)  # Close message list
    
    # Message composer
    prescriber_options = ["Dr. James Wilson", "Dr. Maria Lopez", "Dr. Michael Chen", "Dr. Emily Rodriguez"]
    selected_prescriber = st.selectbox("Select Prescriber", ["Select Prescriber"] + prescriber_options)
    message_text = st.text_area("Type your message here...", height=100)
    
    if st.button("Send Message", use_container_width=True, disabled=(selected_prescriber == "Select Prescriber" or not message_text)):
        if selected_prescriber != "Select Prescriber" and message_text:
            st.success(f"Message sent to {selected_prescriber}")
            # In a real app, this would call an API to send the message
            
            # Add the message to the display (would normally come from API)
            if 'custom_messages' not in st.session_state:
                st.session_state.custom_messages = []
                
            # Get current time
            now = datetime.now()
            time_str = now.strftime("%I:%M %p")
            
            # Add message to state
            st.session_state.custom_messages.append({
                "from": "You (Sarah Chen, PharmD)",
                "time": f"Today, {time_str}",
                "content": message_text,
                "outgoing": True
            })
            
            # Clear the text area
            message_text = ""
            
            # Rerun to update the display
            st.experimental_rerun()
    
    st.markdown("</div></div>", unsafe_allow_html=True)  # Close the communication panel
    
    # Prescription Adjustment Panel (shown conditionally)
    if st.session_state.show_adjustment_panel:
        st.markdown("""
        <div class="card">
            <div class="card-header">
                <h3 class="card-title">Prescription Adjustment Request</h3>
            </div>
            <div class="card-body">
        """, unsafe_allow_html=True)
        
        # Form for adjustment request
        with st.form("adjustment_form"):
            # Pre-filled with the medication in question
            medication = st.text_input("Medication", value="Lipitor (atorvastatin) 20mg", disabled=True)
            prescriber = st.text_input("Current Prescriber", value="Dr. James Wilson", disabled=True)
            
            adjustment_type = st.selectbox(
                "Adjustment Type",
                ["Dosage Change", "Discontinue", "Change Administration Schedule", "Alternative Medication"]
            )
            
            recommendation = st.text_area(
                "Recommended Action",
                value="Recommend reducing Lipitor dosage to 10mg due to patient reports of muscle pain. Consider monitoring liver function tests."
            )
            
            urgency = st.selectbox(
                "Urgency",
                ["Routine (24-48 hours)", "Priority (within 24 hours)", "Urgent (ASAP)"],
                index=1
            )
            
            # Form buttons
            col1, col2 = st.columns(2)
            with col1:
                cancel = st.form_submit_button("Cancel")
            with col2:
                submit = st.form_submit_button("Submit Request")
                
            if submit:
                st.success("Adjustment request submitted successfully")
                st.session_state.show_adjustment_panel = False
                st.experimental_rerun()
            elif cancel:
                st.session_state.show_adjustment_panel = False
                st.experimental_rerun()
        
        st.markdown("</div></div>", unsafe_allow_html=True)  # Close the adjustment panel

# Navigation buttons at the bottom
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Back to Dashboard", use_container_width=True):
        st.switch_page("pages/21_Pharmacist_Home.py")

with col2:
    if st.button("View Prescription Outcomes", use_container_width=True):
        # Set patient_id in session state for the next page
        st.session_state.selected_patient_id = patient_id
        st.switch_page("pages/23_Prescription_Outcomes.py")

with col3:
    if st.button("Patient Education", use_container_width=True):
        # Set patient_id in session state for the next page
        st.session_state.selected_patient_id = patient_id
        st.switch_page("pages/25_Patient_Education.py")

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Medication Review Interface")
