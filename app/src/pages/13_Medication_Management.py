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
    page_title="Medication Management | MediTrack", 
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

# Custom CSS for styling
st.markdown("""
<style>
    .admin-filter {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .admin-form {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .patient-name {
        font-weight: 600;
    }
    .med-card {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
    }
    .med-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
    }
    .med-name {
        font-weight: 600;
        font-size: 16px;
    }
    .med-details {
        display: flex;
        gap: 20px;
        margin-bottom: 10px;
        font-size: 14px;
        color: #6e84a3;
    }
    .med-patient {
        font-weight: 500;
        color: #12263f;
    }
    .med-meta {
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        color: #95aac9;
    }
    .schedule-badge {
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
        color: white;
    }
    .scheduled {
        background-color: #f6c343;
    }
    .prn {
        background-color: #2c7be5;
    }
    .completed {
        background-color: #00d97e;
    }
</style>
""", unsafe_allow_html=True)

# Page title
st.title("Medication Management")
st.subheader("Administer and track patient medications")

# Mock API for demo purposes (would be replaced with actual API calls)
def get_medication_administration():
    """Simulate an API call to /n/medication-administration endpoint"""
    # In a real app, this would call the Flask API:
    # response = requests.get("http://web-api:4000/n/medication-administration")
    # return response.json()
    
    # Return simulated data
    return [
        {
            "medication_id": 1, 
            "medication_name": "Lisinopril", 
            "dosage_form": "Tablet", 
            "strength": "10mg",
            "result_id": 1, 
            "patient_id": 101, 
            "first_name": "John", 
            "last_name": "Doe",
            "administered_date": "2023-04-15", 
            "test_name": "Blood Pressure", 
            "result_value": "120/80", 
            "unit_of_measure": "mmHg"
        },
        {
            "medication_id": 2, 
            "medication_name": "Metformin", 
            "dosage_form": "Tablet", 
            "strength": "500mg",
            "result_id": 2, 
            "patient_id": 101, 
            "first_name": "John", 
            "last_name": "Doe",
            "administered_date": "2023-04-15", 
            "test_name": "Blood Glucose", 
            "result_value": "110", 
            "unit_of_measure": "mg/dL"
        },
        {
            "medication_id": 3, 
            "medication_name": "Albuterol", 
            "dosage_form": "Inhaler", 
            "strength": "90mcg",
            "result_id": 3, 
            "patient_id": 104, 
            "first_name": "Emily", 
            "last_name": "Davis",
            "administered_date": "2023-04-14", 
            "test_name": "Respiratory Rate", 
            "result_value": "16", 
            "unit_of_measure": "/min"
        },
        {
            "medication_id": 5, 
            "medication_name": "Amlodipine", 
            "dosage_form": "Tablet", 
            "strength": "5mg",
            "result_id": 4, 
            "patient_id": 108, 
            "first_name": "William", 
            "last_name": "Wilson",
            "administered_date": "2023-04-14", 
            "test_name": "Blood Pressure", 
            "result_value": "135/85", 
            "unit_of_measure": "mmHg"
        },
        {
            "medication_id": 6, 
            "medication_name": "Levothyroxine", 
            "dosage_form": "Tablet", 
            "strength": "50mcg",
            "result_id": 5, 
            "patient_id": 103, 
            "first_name": "Michael", 
            "last_name": "Brown",
            "administered_date": "2023-04-13", 
            "test_name": "Thyroid Function", 
            "result_value": "3.2", 
            "unit_of_measure": "mIU/L"
        },
        {
            "medication_id": 7, 
            "medication_name": "Omeprazole", 
            "dosage_form": "Capsule", 
            "strength": "20mg",
            "result_id": 6, 
            "patient_id": 103, 
            "first_name": "Michael", 
            "last_name": "Brown",
            "administered_date": "2023-04-13", 
            "test_name": "Gastritis Symptoms", 
            "result_value": "Mild", 
            "unit_of_measure": None
        },
        {
            "medication_id": 9, 
            "medication_name": "Hydrochlorothiazide", 
            "dosage_form": "Tablet", 
            "strength": "25mg",
            "result_id": 7, 
            "patient_id": 105, 
            "first_name": "William", 
            "last_name": "Johnson",
            "administered_date": "2023-04-12", 
            "test_name": "Fluid Balance", 
            "result_value": "Balanced", 
            "unit_of_measure": None
        },
        {
            "medication_id": 10, 
            "medication_name": "Ibuprofen", 
            "dosage_form": "Tablet", 
            "strength": "200mg",
            "result_id": 8, 
            "patient_id": 104, 
            "first_name": "Emily", 
            "last_name": "Davis",
            "administered_date": "2023-04-12", 
            "test_name": "Pain Level", 
            "result_value": "3", 
            "unit_of_measure": "/10"
        }
    ]

def get_medications():
    """Return a list of medications"""
    return [
        {"medication_id": 1, "medication_name": "Lisinopril", "dosage_form": "Tablet", "strength": "10mg"},
        {"medication_id": 2, "medication_name": "Metformin", "dosage_form": "Tablet", "strength": "500mg"},
        {"medication_id": 3, "medication_name": "Albuterol", "dosage_form": "Inhaler", "strength": "90mcg"},
        {"medication_id": 4, "medication_name": "Atorvastatin", "dosage_form": "Tablet", "strength": "20mg"},
        {"medication_id": 5, "medication_name": "Amlodipine", "dosage_form": "Tablet", "strength": "5mg"},
        {"medication_id": 6, "medication_name": "Levothyroxine", "dosage_form": "Tablet", "strength": "50mcg"},
        {"medication_id": 7, "medication_name": "Omeprazole", "dosage_form": "Capsule", "strength": "20mg"},
        {"medication_id": 8, "medication_name": "Sertraline", "dosage_form": "Tablet", "strength": "50mg"},
        {"medication_id": 9, "medication_name": "Hydrochlorothiazide", "dosage_form": "Tablet", "strength": "25mg"},
        {"medication_id": 10, "medication_name": "Ibuprofen", "dosage_form": "Tablet", "strength": "200mg"}
    ]

def get_lab_results():
    """Return list of lab results for dropdown"""
    return [
        {"result_id": 1, "patient_id": 101, "test_name": "Blood Pressure", "result_value": "120/80"},
        {"result_id": 2, "patient_id": 101, "test_name": "Blood Glucose", "result_value": "110"},
        {"result_id": 3, "patient_id": 104, "test_name": "Respiratory Rate", "result_value": "16"},
        {"result_id": 4, "patient_id": 108, "test_name": "Blood Pressure", "result_value": "135/85"},
        {"result_id": 5, "patient_id": 103, "test_name": "Thyroid Function", "result_value": "3.2"},
        {"result_id": 6, "patient_id": 103, "test_name": "Gastritis Symptoms", "result_value": "Mild"},
        {"result_id": 7, "patient_id": 105, "test_name": "Fluid Balance", "result_value": "Balanced"},
        {"result_id": 8, "patient_id": 104, "test_name": "Pain Level", "result_value": "3"}
    ]

def get_patient_list():
    """Return a list of patients"""
    return [
        {"patient_id": 101, "first_name": "John", "last_name": "Doe"},
        {"patient_id": 102, "first_name": "Sarah", "last_name": "Smith"},
        {"patient_id": 103, "first_name": "Michael", "last_name": "Brown"},
        {"patient_id": 104, "first_name": "Emily", "last_name": "Davis"},
        {"patient_id": 105, "first_name": "William", "last_name": "Johnson"},
        {"patient_id": 108, "first_name": "William", "last_name": "Wilson"}
    ]

def create_medication_administration(admin_data):
    """Simulate an API call to POST /n/medication-administration endpoint"""
    # In real implementation:
    # response = requests.post("http://web-api:4000/n/medication-administration", json=admin_data)
    # return response.json()
    
    # For demo purposes:
    st.success(f"Medication administration record created successfully!")
    return {"status": "created", **admin_data}

# Tabs for different views
tab1, tab2, tab3 = st.tabs(["Medication Schedule", "Administration Records", "Record Administration"])

# Tab 1: Medication Schedule
with tab1:
    st.markdown('<div class="admin-filter">', unsafe_allow_html=True)
    
    # Patient selection for schedules
    patients = get_patient_list()
    patient_options = [f"{p['first_name']} {p['last_name']} (#{p['patient_id']})" for p in patients]
    selected_patient = st.selectbox("Select Patient", patient_options, key="patient_select_schedule")
    
    # Date selection
    schedule_date = st.date_input("Schedule Date", datetime.now(), key="schedule_date")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Extract patient_id from selection
    patient_id = int(selected_patient.split("(#")[1].split(")")[0])
    patient_name = selected_patient.split(" (#")[0]
    
    # Display schedule (static demo data)
    st.subheader(f"Medication Schedule for {patient_name}")
    
    # Sample schedule data
    schedule_times = ["Morning (8:00 AM)", "Noon (12:00 PM)", "Evening (6:00 PM)"]
    
    for i, time_slot in enumerate(schedule_times):
        st.markdown(f"### {time_slot}")
        
        # Morning medications
        if i == 0:
            st.markdown("""
            <div class="med-card">
                <div class="med-header">
                    <div class="med-name">Lisinopril 10mg</div>
                    <div class="schedule-badge completed">Administered</div>
                </div>
                <div class="med-details">
                    <div>Form: Tablet</div>
                    <div>Route: Oral</div>
                    <div>Dosage: 1 tablet</div>
                </div>
                <div class="med-meta">
                    <div>Administered by: Maria Rodriguez</div>
                    <div>Time: 8:15 AM</div>
                </div>
            </div>
            
            <div class="med-card">
                <div class="med-header">
                    <div class="med-name">Metformin 500mg</div>
                    <div class="schedule-badge completed">Administered</div>
                </div>
                <div class="med-details">
                    <div>Form: Tablet</div>
                    <div>Route: Oral</div>
                    <div>Dosage: 1 tablet</div>
                </div>
                <div class="med-meta">
                    <div>Administered by: Maria Rodriguez</div>
                    <div>Time: 8:15 AM</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Noon medications
        elif i == 1:
            st.markdown("""
            <div class="med-card">
                <div class="med-header">
                    <div class="med-name">Metformin 500mg</div>
                    <div class="schedule-badge scheduled">Due Soon</div>
                </div>
                <div class="med-details">
                    <div>Form: Tablet</div>
                    <div>Route: Oral</div>
                    <div>Dosage: 1 tablet</div>
                </div>
                <div class="med-meta">
                    <div>Scheduled with food</div>
                    <div>Due in 30 min</div>
                </div>
            </div>
            
            <div class="med-card">
                <div class="med-header">
                    <div class="med-name">Aspirin 81mg</div>
                    <div class="schedule-badge scheduled">Due Soon</div>
                </div>
                <div class="med-details">
                    <div>Form: Tablet</div>
                    <div>Route: Oral</div>
                    <div>Dosage: 1 tablet</div>
                </div>
                <div class="med-meta">
                    <div>Scheduled with food</div>
                    <div>Due in 30 min</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.button("Mark as Administered", use_container_width=True, key="mark_adm_noon")
            with col2:
                st.button("Delay Administration", use_container_width=True, key="delay_adm_noon")
        
        # Evening medications
        else:
            st.markdown("""
            <div class="med-card">
                <div class="med-header">
                    <div class="med-name">Lisinopril 10mg</div>
                    <div class="schedule-badge prn">Upcoming</div>
                </div>
                <div class="med-details">
                    <div>Form: Tablet</div>
                    <div>Route: Oral</div>
                    <div>Dosage: 1 tablet</div>
                </div>
                <div class="med-meta">
                    <div>Take with food</div>
                    <div>Due at 6:00 PM</div>
                </div>
            </div>
            
            <div class="med-card">
                <div class="med-header">
                    <div class="med-name">Metformin 500mg</div>
                    <div class="schedule-badge prn">Upcoming</div>
                </div>
                <div class="med-details">
                    <div>Form: Tablet</div>
                    <div>Route: Oral</div>
                    <div>Dosage: 1 tablet</div>
                </div>
                <div class="med-meta">
                    <div>Take with food</div>
                    <div>Due at 6:00 PM</div>
                </div>
            </div>
            
            <div class="med-card">
                <div class="med-header">
                    <div class="med-name">Atorvastatin 20mg</div>
                    <div class="schedule-badge prn">Upcoming</div>
                </div>
                <div class="med-details">
                    <div>Form: Tablet</div>
                    <div>Route: Oral</div>
                    <div>Dosage: 1 tablet</div>
                </div>
                <div class="med-meta">
                    <div>Take at bedtime</div>
                    <div>Due at 6:00 PM</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # PRN Medications section
    st.markdown("### PRN Medications (As Needed)")
    st.markdown("""
    <div class="med-card">
        <div class="med-header">
            <div class="med-name">Ibuprofen 200mg</div>
            <div class="schedule-badge prn">PRN</div>
        </div>
        <div class="med-details">
            <div>Form: Tablet</div>
            <div>Route: Oral</div>
            <div>Dosage: 1-2 tablets</div>
        </div>
        <div class="med-meta">
            <div>For pain or fever</div>
            <div>Every 6 hours as needed</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Button to administer PRN medication
    col1, col2 = st.columns(2)
    with col1:
        st.button("Administer PRN Medication", use_container_width=True, key="adm_prn")
    with col2:
        st.button("View Administration History", use_container_width=True, key="view_history")

# Tab 2: Administration Records
with tab2:
    # Filter section
    st.markdown('<div class="admin-filter">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    # Get unique patients for filter
    patients = get_patient_list()
    patient_options = ["All Patients"] + [f"{p['first_name']} {p['last_name']} (#{p['patient_id']})" for p in patients]
    
    with col1:
        filter_patient = st.selectbox("Filter by Patient", patient_options, key="filter_patient_tab2")
    
    with col2:
        filter_date = st.date_input("Filter by Date", datetime.now(), key="filter_date_tab2")
    
    with col3:
        search_term = st.text_input("Search Medications", placeholder="Enter medication name...", key="search_med_tab2")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Get medication administration data
    try:
        admin_records = get_medication_administration()
        
        # Apply filters
        if filter_patient != "All Patients":
            # Extract patient_id from the option string
            selected_id = filter_patient.split("(#")[1].split(")")[0]
            admin_records = [record for record in admin_records if str(record["patient_id"]) == selected_id]
        
        # Filter by date
        filter_date_str = filter_date.strftime('%Y-%m-%d')
        admin_records = [record for record in admin_records if record["administered_date"] <= filter_date_str]
        
        if search_term:
            admin_records = [record for record in admin_records if 
                           search_term.lower() in record["medication_name"].lower()]
        
        # Sort by date (most recent first)
        admin_records = sorted(admin_records, key=lambda x: x["administered_date"], reverse=True)
        
        # Display records
        if admin_records:
            for record in admin_records:
                st.markdown(f"""
                <div class="med-card">
                    <div class="med-header">
                        <div class="med-name">{record['medication_name']} {record['strength']}</div>
                        <div class="schedule-badge completed">Administered</div>
                    </div>
                    <div class="med-patient">
                        {record['first_name']} {record['last_name']} (#{record['patient_id']})
                    </div>
                    <div class="med-details">
                        <div>Form: {record['dosage_form']}</div>
                        <div>Date: {record['administered_date']}</div>
                    </div>
                    <div class="med-meta">
                        <div>Related Test: {record['test_name']}</div>
                        <div>Result: {record['result_value']} {record['unit_of_measure'] if record['unit_of_measure'] else ''}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No medication administration records match your filters.")
            
    except Exception as e:
        st.error(f"Could not load medication administration records: {str(e)}")

# Tab 3: Record New Administration
with tab3:
    st.markdown('<div class="admin-form">', unsafe_allow_html=True)
    st.subheader("Record New Medication Administration")
    
    # Form for recording new administration
    with st.form("med_admin_form"):
        # Patient selection
        patients = get_patient_list()
        patient_options = [f"{p['first_name']} {p['last_name']} (#{p['patient_id']})" for p in patients]
        selected_patient = st.selectbox("Select Patient", patient_options, key="patient_select_admin")
        
        # Extract patient_id from selection
        patient_id = int(selected_patient.split("(#")[1].split(")")[0])
        
        # Medication selection
        medications = get_medications()
        medication_options = [f"{m['medication_name']} {m['strength']} ({m['dosage_form']})" for m in medications]
        selected_medication = st.selectbox("Select Medication", medication_options, key="med_select_admin")
        
        # Extract medication_id from selection
        medication_index = medication_options.index(selected_medication)
        medication_id = medications[medication_index]["medication_id"]
        
        # Administration details
        col1, col2 = st.columns(2)
        
        with col1:
            admin_date = st.date_input("Administration Date", datetime.now(), key="admin_date")
            admin_time = st.time_input("Administration Time", datetime.now().time(), key="admin_time")
        
        with col2:
            route = st.selectbox("Administration Route", ["Oral", "Intravenous", "Intramuscular", "Subcutaneous", "Inhalation"], key="admin_route")
            dosage = st.text_input("Dosage", placeholder="Enter dosage amount", key="admin_dosage")
        
        # Lab result selection
        lab_results = get_lab_results()
        # Filter lab results for the selected patient
        patient_results = [r for r in lab_results if r["patient_id"] == patient_id]
        
        if not patient_results:
            st.warning("No lab results found for this patient. Please add a lab result first.")
            lab_result_options = ["No results available"]
            selected_result = st.selectbox("Related Lab Result", lab_result_options, disabled=True, key="lab_result_admin")
            result_id = None
        else:
            lab_result_options = [f"{r['test_name']} - {r['result_value']}" for r in patient_results]
            selected_result = st.selectbox("Related Lab Result", lab_result_options, key="lab_result_select")
            
            # Extract result_id from selection
            result_index = lab_result_options.index(selected_result)
            result_id = patient_results[result_index]["result_id"]
        
        # Notes
        notes = st.text_area("Administration Notes", placeholder="Enter any notes about this administration", key="admin_notes")
        
        submit_button = st.form_submit_button("Record Administration")
        
        if submit_button:
            if not result_id:
                st.error("Cannot record administration without a related lab result.")
            else:
                # Prepare data for API call
                admin_data = {
                    "medication_id": medication_id,
                    "result_id": result_id,
                    "administered_date": admin_date.strftime('%Y-%m-%d'),
                    "administered_time": admin_time.strftime('%H:%M:%S'),
                    "route": route,
                    "dosage": dosage,
                    "notes": notes
                }
                
                # Call the API (simulated)
                created_record = create_medication_administration(admin_data)
                
                # In a real app, you might want to refresh the page or clear the form
                st.experimental_rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Medication scan interface
    st.markdown("### Barcode Scanning")
    st.info("Connect a barcode scanner to quickly scan medication packages.")
    
    col1, col2 = st.columns(2)
    with col1:
        barcode = st.text_input("Scan or Enter Medication Barcode", placeholder="Scan barcode or enter NDC code...")
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        scan_button = st.button("Process Barcode", use_container_width=True)
    
    if scan_button and barcode:
        st.success(f"Found medication: Lisinopril 10mg Tablet (NDC: {barcode})")
        
        # Display quick administration form
        st.markdown("### Quick Administration")
        quick_cols = st.columns(3)
        with quick_cols[0]:
            quick_patient = st.selectbox("Patient", patient_options, key="quick_patient")
        with quick_cols[1]:
            quick_route = st.selectbox("Route", ["Oral", "Intravenous", "Intramuscular", "Subcutaneous", "Inhalation"], key="quick_route")
        with quick_cols[2]:
            quick_dosage = st.text_input("Dosage", value="1 tablet", key="quick_dosage")
        
        if st.button("Record Quick Administration", use_container_width=True):
            st.success("Medication administration recorded successfully!")

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Medication Management")
