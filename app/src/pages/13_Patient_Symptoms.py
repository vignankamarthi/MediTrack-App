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
    page_title="Patient Symptoms | MediTrack", 
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
st.title("Patient Symptom Records")
st.subheader("Monitor and update patient symptom information")

# Mock API for demo purposes (would be replaced with actual API calls)
def get_patient_symptom_records():
    """Simulate an API call to /n/patient-symptom-records endpoint"""
    # In a real app, this would call the Flask API:
    # response = requests.get("http://web-api:4000/n/patient-symptom-records")
    # return response.json()
    
    # Return simulated data
    return [
        {"patient_id": 101, "first_name": "John", "last_name": "Doe", "symptom_name": "Headache", "description": "Pain in the head or upper neck", "severity": "MODERATE"},
        {"patient_id": 101, "first_name": "John", "last_name": "Doe", "symptom_name": "Fever", "description": "Elevated body temperature above normal range", "severity": "MILD"},
        {"patient_id": 103, "first_name": "Michael", "last_name": "Brown", "symptom_name": "Chest Pain", "description": "Pain or discomfort in the chest area", "severity": "SEVERE"},
        {"patient_id": 104, "first_name": "Emily", "last_name": "Davis", "symptom_name": "Cough", "description": "Sudden expulsion of air from the lungs", "severity": "MODERATE"},
        {"patient_id": 104, "first_name": "Emily", "last_name": "Davis", "symptom_name": "Shortness of Breath", "description": "Difficulty breathing or feeling of suffocation", "severity": "MODERATE"},
        {"patient_id": 108, "first_name": "William", "last_name": "Wilson", "symptom_name": "Joint Pain", "description": "Pain or stiffness in the joints", "severity": "MILD"},
        {"patient_id": 108, "first_name": "William", "last_name": "Wilson", "symptom_name": "Dizziness", "description": "Sensation of spinning or loss of balance", "severity": "MODERATE"},
        {"patient_id": 115, "first_name": "James", "last_name": "Walker", "symptom_name": "Nausea", "description": "Feeling of unease and urge to vomit", "severity": "MODERATE"}
    ]

def get_patient_list():
    """Return a list of unique patients from symptom records"""
    symptom_records = get_patient_symptom_records()
    patients = {}
    
    for record in symptom_records:
        patient_id = record["patient_id"]
        if patient_id not in patients:
            patients[patient_id] = {
                "patient_id": patient_id,
                "first_name": record["first_name"],
                "last_name": record["last_name"],
                "full_name": f"{record['first_name']} {record['last_name']}"
            }
    
    return list(patients.values())

def get_symptom_list():
    """Return a list of unique symptoms"""
    return [
        {"symptom_id": 1, "symptom_name": "Headache", "description": "Pain in the head or upper neck", "severity_code": "MILD-MOD"},
        {"symptom_id": 2, "symptom_name": "Fatigue", "description": "Persistent tiredness or lack of energy", "severity_code": "MILD-MOD"},
        {"symptom_id": 3, "symptom_name": "Cough", "description": "Sudden expulsion of air from the lungs", "severity_code": "MOD"},
        {"symptom_id": 4, "symptom_name": "Fever", "description": "Elevated body temperature above normal range", "severity_code": "MOD-SEV"},
        {"symptom_id": 5, "symptom_name": "Shortness of Breath", "description": "Difficulty breathing or feeling of suffocation", "severity_code": "MOD-SEV"},
        {"symptom_id": 6, "symptom_name": "Chest Pain", "description": "Pain or discomfort in the chest area", "severity_code": "SEV"},
        {"symptom_id": 7, "symptom_name": "Joint Pain", "description": "Pain or stiffness in the joints", "severity_code": "MILD-MOD"},
        {"symptom_id": 8, "symptom_name": "Nausea", "description": "Feeling of unease and urge to vomit", "severity_code": "MILD-MOD"},
        {"symptom_id": 9, "symptom_name": "Abdominal Pain", "description": "Pain in the stomach or abdominal region", "severity_code": "MOD-SEV"},
        {"symptom_id": 10, "symptom_name": "Dizziness", "description": "Sensation of spinning or loss of balance", "severity_code": "MILD-MOD"}
    ]

def create_symptom_record(record_data):
    """Simulate an API call to POST /n/patient-symptom-records endpoint"""
    # In real implementation:
    # response = requests.post("http://web-api:4000/n/patient-symptom-records", json=record_data)
    # return response.json()
    
    # For demo purposes:
    st.success(f"Symptom record created successfully for patient #{record_data['patient_id']}!")
    return {"status": "created", **record_data}

def update_symptom_severity(update_data):
    """Simulate an API call to PUT /n/patient-symptom-records endpoint"""
    # In real implementation:
    # response = requests.put("http://web-api:4000/n/patient-symptom-records", json=update_data)
    # return response.json()
    
    # For demo purposes:
    st.success(f"Symptom severity updated successfully for patient #{update_data['patient_id']}!")
    return {"status": "updated", **update_data}

# Custom CSS for styling
st.markdown("""
<style>
    .record-filter {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .severity-badge {
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
        color: white;
    }
    .SEVERE {
        background-color: #e63757;
    }
    .MODERATE {
        background-color: #f6c343;
    }
    .MILD {
        background-color: #00d97e;
    }
    .symptom-form {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .patient-name {
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Tabs for different views
tab1, tab2, tab3 = st.tabs(["Symptom Records", "Add New Symptom", "Update Severity"])

# Tab 1: Symptom Records
with tab1:
    # Filter section
    st.markdown('<div class="record-filter">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    # Get unique patients for filter
    patients = get_patient_list()
    patient_options = ["All Patients"] + [f"{p['first_name']} {p['last_name']} (#{p['patient_id']})" for p in patients]
    
    with col1:
        filter_patient = st.selectbox("Filter by Patient", patient_options)
    
    with col2:
        filter_severity = st.selectbox("Filter by Severity", ["All", "SEVERE", "MODERATE", "MILD"])
    
    with col3:
        search_term = st.text_input("Search Symptoms", placeholder="Enter keywords...")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Get symptom records data
    try:
        symptom_records = get_patient_symptom_records()
        
        # Apply filters
        if filter_patient != "All Patients":
            # Extract patient_id from the option string
            selected_id = filter_patient.split("(#")[1].split(")")[0]
            symptom_records = [record for record in symptom_records if str(record["patient_id"]) == selected_id]
        
        if filter_severity != "All":
            symptom_records = [record for record in symptom_records if record["severity"] == filter_severity]
        
        if search_term:
            symptom_records = [record for record in symptom_records if 
                              search_term.lower() in record["symptom_name"].lower() or 
                              search_term.lower() in record["description"].lower()]
        
        # Convert to DataFrame for display
        if symptom_records:
            df = pd.DataFrame(symptom_records)
            
            # Create formatted patient name column
            df['patient_name'] = df.apply(lambda row: f"{row['first_name']} {row['last_name']} (#{row['patient_id']})", axis=1)
            
            # Add color-coded severity
            def highlight_severity(val):
                if val == 'SEVERE':
                    return 'background-color: #ffecec; color: #e63757; font-weight: bold;'
                elif val == 'MODERATE':
                    return 'background-color: #fff8e7; color: #f6c343;'
                elif val == 'MILD':
                    return 'background-color: #e7fff2; color: #00d97e;'
                return ''
            
            # Display the table with styling
            st.dataframe(
                df.style.applymap(highlight_severity, subset=['severity']),
                column_config={
                    "patient_name": st.column_config.TextColumn("Patient"),
                    "symptom_name": st.column_config.TextColumn("Symptom"),
                    "description": st.column_config.TextColumn("Description"),
                    "severity": st.column_config.TextColumn("Severity"),
                },
                column_order=["patient_name", "symptom_name", "description", "severity"],
                hide_index=True,
                use_container_width=True
            )
        else:
            st.info("No symptom records match your filters.")
    
    except Exception as e:
        st.error(f"Could not load symptom records: {str(e)}")

# Tab 2: Add New Symptom
with tab2:
    st.markdown('<div class="symptom-form">', unsafe_allow_html=True)
    st.subheader("Record New Patient Symptom")
    
    # Get data for form
    patients = get_patient_list()
    symptoms = get_symptom_list()
    
    # Form for recording new symptom
    with st.form("symptom_record_form"):
        # Patient selection
        patient_options = [f"{p['first_name']} {p['last_name']} (#{p['patient_id']})" for p in patients]
        selected_patient = st.selectbox("Select Patient", patient_options)
        
        # Extract patient_id from selection
        patient_id = int(selected_patient.split("(#")[1].split(")")[0])
        
        # Symptom selection
        symptom_options = [f"{s['symptom_name']} - {s['description']}" for s in symptoms]
        selected_symptom = st.selectbox("Select Symptom", symptom_options)
        
        # Extract symptom_id from selection
        symptom_index = symptom_options.index(selected_symptom)
        symptom_id = symptoms[symptom_index]["symptom_id"]
        
        # Severity selection
        severity = st.select_slider(
            "Symptom Severity",
            options=["MILD", "MODERATE", "SEVERE"],
            value="MODERATE"
        )
        
        # Notes
        notes = st.text_area("Additional Notes", placeholder="Enter any additional details about the symptom")
        
        submit_button = st.form_submit_button("Record Symptom")
        
        if submit_button:
            # Prepare data for API call
            record_data = {
                "patient_id": patient_id,
                "symptom_id": symptom_id,
                "severity": severity,
                "notes": notes
            }
            
            # Call the API (simulated)
            created_record = create_symptom_record(record_data)
            
            # In a real app, you might want to refresh the page or clear the form
            st.session_state.symptom_tab = 0
    
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 3: Update Severity
with tab3:
    st.markdown('<div class="symptom-form">', unsafe_allow_html=True)
    st.subheader("Update Symptom Severity")
    
    # Get data for form
    symptom_records = get_patient_symptom_records()
    
    # Create formatted records for selection
    formatted_records = [
        f"{record['first_name']} {record['last_name']} (#{record['patient_id']}) - {record['symptom_name']} - Current: {record['severity']}"
        for record in symptom_records
    ]
    
    # Form for updating symptom severity
    with st.form("update_severity_form"):
        # Record selection
        selected_record = st.selectbox("Select Patient Symptom Record", formatted_records)
        
        # Extract patient_id and symptom info from selection
        record_parts = selected_record.split("(#")[1].split(")")
        patient_id = int(record_parts[0])
        symptom_name = record_parts[1].split("-")[1].strip()
        
        # Find the symptom_id
        symptom_id = next(
            (symptom["symptom_id"] for symptom in get_symptom_list() if symptom["symptom_name"] == symptom_name),
            None
        )
        
        # New severity selection
        new_severity = st.select_slider(
            "New Severity Level",
            options=["MILD", "MODERATE", "SEVERE"],
            value="MODERATE"
        )
        
        # Update reason
        update_reason = st.text_area("Reason for Update", placeholder="Enter reason for changing the severity")
        
        update_button = st.form_submit_button("Update Severity")
        
        if update_button:
            if not symptom_id:
                st.error("Could not identify the symptom. Please try again.")
            else:
                # Prepare data for API call
                update_data = {
                    "patient_id": patient_id,
                    "symptom_id": symptom_id,
                    "severity": new_severity,
                    "update_reason": update_reason
                }
                
                # Call the API (simulated)
                updated_record = update_symptom_severity(update_data)
                
                # In a real app, you might want to refresh the page or clear the form
                st.session_state.symptom_tab = 0
    
    st.markdown('</div>', unsafe_allow_html=True)

# Call to action section at the bottom
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/12_Care_Tasks.py", label="Manage Care Tasks", icon="📋", use_container_width=True)

with col2:
    st.page_link("pages/14_Lab_Results.py", label="Check Lab Results", icon="🔬", use_container_width=True)

with col3:
    st.page_link("pages/15_Medication_Administration.py", label="Medication Administration", icon="💊", use_container_width=True)

# Footer
st.caption("© 2025 MediTrack - Patient Symptom Records")
