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
    page_title="Patient Care | MediTrack", 
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
    .record-filter {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .severity-badge, .abnormal-badge {
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
        color: white;
    }
    .SEVERE, .abnormal {
        background-color: #e63757;
    }
    .MODERATE {
        background-color: #f6c343;
    }
    .MILD, .normal {
        background-color: #00d97e;
    }
    .form-card {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .patient-name {
        font-weight: 600;
    }
    .lab-detail-card {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .lab-detail-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;
    }
    .lab-detail-info {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
    }
    .lab-detail-item {
        margin-bottom: 10px;
    }
    .lab-detail-label {
        font-size: 12px;
        color: #95aac9;
    }
    .lab-detail-value {
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Page title
st.title("Patient Care")
st.subheader("Record symptoms, lab results, and assessments")

# Main tabs for symptom records and lab results
tab1, tab2, tab3 = st.tabs(["Patient Symptoms", "Lab Results", "Patient Assessment"])

# ---------------------------
# TAB 1: PATIENT SYMPTOMS
# ---------------------------
with tab1:
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

    # Secondary tabs for viewing and adding symptoms
    symptom_tab1, symptom_tab2 = st.tabs(["View Symptoms", "Record New Symptoms"])
    
    with symptom_tab1:
        # Filter section
        st.markdown('<div class="record-filter">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        # Get unique patients for filter
        patients = get_patient_list()
        patient_options = ["All Patients"] + [f"{p['first_name']} {p['last_name']} (#{p['patient_id']})" for p in patients]
        
        with col1:
            filter_patient = st.selectbox("Filter by Patient", patient_options, key="sym_patient")
        
        with col2:
            filter_severity = st.selectbox("Filter by Severity", ["All", "SEVERE", "MODERATE", "MILD"], key="sym_severity")
        
        with col3:
            search_term = st.text_input("Search Symptoms", placeholder="Enter keywords...", key="sym_search")
        
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
    
    with symptom_tab2:
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        
        # Get data for form
        patients = get_patient_list()
        symptoms = get_symptom_list()
        
        # Form for recording new symptom
        with st.form("symptom_record_form"):
            # Patient selection
            patient_options = [f"{p['first_name']} {p['last_name']} (#{p['patient_id']})" for p in patients]
            selected_patient = st.selectbox("Select Patient", patient_options, key="sym_select_patient")
            
            # Extract patient_id from selection
            patient_id = int(selected_patient.split("(#")[1].split(")")[0])
            
            # Symptom selection
            symptom_options = [f"{s['symptom_name']} - {s['description']}" for s in symptoms]
            selected_symptom = st.selectbox("Select Symptom", symptom_options, key="sym_select_symptom")
            
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
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Add section for updating symptom severity
        st.markdown("### Update Symptom Severity")
        
        # Get symptom records
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
                (symptom["symptom_id"] for symptom in symptoms if symptom["symptom_name"] == symptom_name),
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

# ---------------------------
# TAB 2: LAB RESULTS
# ---------------------------
with tab2:
    # Mock API for demo purposes (would be replaced with actual API calls)
    def get_lab_results():
        """Simulate an API call to /n/lab-results endpoint"""
        # In a real app, this would call the Flask API:
        # response = requests.get("http://web-api:4000/n/lab-results")
        # return response.json()
        
        # Return simulated data
        return [
            {
                "result_id": 1, 
                "patient_id": 101, 
                "first_name": "John", 
                "last_name": "Doe", 
                "test_name": "Complete Blood Count", 
                "test_date": "2023-06-01", 
                "result_date": "2023-06-02", 
                "result_value": "14.5", 
                "reference_range": "12.0-15.5", 
                "unit_of_measure": "g/dL", 
                "is_abnormal": False, 
                "lab_notes": "Results within normal range"
            },
            {
                "result_id": 2, 
                "patient_id": 101, 
                "first_name": "John", 
                "last_name": "Doe", 
                "test_name": "Blood Glucose", 
                "test_date": "2023-06-01", 
                "result_date": "2023-06-02", 
                "result_value": "243", 
                "reference_range": "70-99", 
                "unit_of_measure": "mg/dL", 
                "is_abnormal": True, 
                "lab_notes": "Elevated fasting glucose"
            },
            {
                "result_id": 3, 
                "patient_id": 102, 
                "first_name": "Sarah", 
                "last_name": "Smith", 
                "test_name": "Lipid Panel", 
                "test_date": "2023-07-10", 
                "result_date": "2023-07-11", 
                "result_value": "200", 
                "reference_range": "<200", 
                "unit_of_measure": "mg/dL", 
                "is_abnormal": True, 
                "lab_notes": "Elevated total cholesterol"
            },
            {
                "result_id": 4, 
                "patient_id": 104, 
                "first_name": "Emily", 
                "last_name": "Davis", 
                "test_name": "Basic Metabolic Panel", 
                "test_date": "2023-08-15", 
                "result_date": "2023-08-16", 
                "result_value": "135", 
                "reference_range": "135-145", 
                "unit_of_measure": "mmol/L", 
                "is_abnormal": False, 
                "lab_notes": "Sodium levels normal"
            },
            {
                "result_id": 5, 
                "patient_id": 104, 
                "first_name": "Emily", 
                "last_name": "Davis", 
                "test_name": "WBC Count", 
                "test_date": "2023-09-05", 
                "result_date": "2023-09-06", 
                "result_value": "15500", 
                "reference_range": "4500-11000", 
                "unit_of_measure": "/μL", 
                "is_abnormal": True, 
                "lab_notes": "Elevated white blood cell count"
            },
            {
                "result_id": 6, 
                "patient_id": 108, 
                "first_name": "William", 
                "last_name": "Wilson", 
                "test_name": "Liver Function Test", 
                "test_date": "2023-09-05", 
                "result_date": "2023-09-06", 
                "result_value": "0.9", 
                "reference_range": "0.2-1.0", 
                "unit_of_measure": "mg/dL", 
                "is_abnormal": False, 
                "lab_notes": "Normal bilirubin levels"
            },
            {
                "result_id": 7, 
                "patient_id": 108, 
                "first_name": "William", 
                "last_name": "Wilson", 
                "test_name": "Potassium Level", 
                "test_date": "2023-10-01", 
                "result_date": "2023-10-02", 
                "result_value": "5.8", 
                "reference_range": "3.5-5.0", 
                "unit_of_measure": "mEq/L", 
                "is_abnormal": True, 
                "lab_notes": "Above normal range"
            },
            {
                "result_id": 8, 
                "patient_id": 103, 
                "first_name": "Michael", 
                "last_name": "Brown", 
                "test_name": "Urinalysis", 
                "test_date": "2023-11-12", 
                "result_date": "2023-11-13", 
                "result_value": "Negative", 
                "reference_range": "Negative", 
                "unit_of_measure": None, 
                "is_abnormal": False, 
                "lab_notes": "No signs of infection"
            }
        ]

    def get_lab_patient_list():
        """Return a list of unique patients from lab results"""
        lab_results = get_lab_results()
        patients = {}
        
        for result in lab_results:
            patient_id = result["patient_id"]
            if patient_id not in patients:
                patients[patient_id] = {
                    "patient_id": patient_id,
                    "first_name": result["first_name"],
                    "last_name": result["last_name"],
                    "full_name": f"{result['first_name']} {result['last_name']}"
                }
        
        return list(patients.values())

    def update_lab_result_review(update_data):
        """Simulate an API call to PUT /n/lab-results endpoint"""
        # In real implementation:
        # response = requests.put("http://web-api:4000/n/lab-results", json=update_data)
        # return response.json()
        
        # For demo purposes:
        st.success(f"Lab result #{update_data['result_id']} review status updated successfully!")
        return {"status": "updated", **update_data}

    # Secondary tabs for viewing and analyzing lab results
    lab_tab1, lab_tab2 = st.tabs(["Lab Results List", "Result Analysis"])
    
    with lab_tab1:
        # Filter section
        st.markdown('<div class="record-filter">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        # Get unique patients for filter
        lab_patients = get_lab_patient_list()
        lab_patient_options = ["All Patients"] + [f"{p['first_name']} {p['last_name']} (#{p['patient_id']})" for p in lab_patients]
        
        with col1:
            lab_filter_patient = st.selectbox("Filter by Patient", lab_patient_options, key="lab_patient")
        
        with col2:
            lab_filter_abnormal = st.selectbox("Filter by Status", ["All", "Abnormal Only", "Normal Only"], key="lab_abnormal")
        
        with col3:
            lab_search_term = st.text_input("Search Tests", placeholder="Enter test name...", key="lab_search")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Get lab results data
        try:
            lab_results = get_lab_results()
            
            # Apply filters
            if lab_filter_patient != "All Patients":
                # Extract patient_id from the option string
                selected_id = lab_filter_patient.split("(#")[1].split(")")[0]
                lab_results = [result for result in lab_results if str(result["patient_id"]) == selected_id]
            
            if lab_filter_abnormal == "Abnormal Only":
                lab_results = [result for result in lab_results if result["is_abnormal"]]
            elif lab_filter_abnormal == "Normal Only":
                lab_results = [result for result in lab_results if not result["is_abnormal"]]
            
            if lab_search_term:
                lab_results = [result for result in lab_results if 
                              lab_search_term.lower() in result["test_name"].lower()]
            
            # Convert to DataFrame for display
            if lab_results:
                lab_df = pd.DataFrame(lab_results)
                
                # Create formatted patient name column
                lab_df['patient_name'] = lab_df.apply(lambda row: f"{row['first_name']} {row['last_name']} (#{row['patient_id']})", axis=1)
                
                # Create formatted result column
                lab_df['formatted_result'] = lab_df.apply(
                    lambda row: f"{row['result_value']} {row['unit_of_measure'] if row['unit_of_measure'] else ''}", 
                    axis=1
                )
                
                # Format dates better
                lab_df['result_date'] = pd.to_datetime(lab_df['result_date']).dt.strftime('%Y-%m-%d')
                
                # Add color coding for abnormal results
                def highlight_abnormal(val):
                    if val == True:
                        return 'background-color: #ffecec; color: #e63757; font-weight: bold;'
                    return 'background-color: #e7fff2; color: #00d97e;'
                
                # Display the table with styling
                st.dataframe(
                    lab_df.style.applymap(highlight_abnormal, subset=['is_abnormal']),
                    column_config={
                        "patient_name": st.column_config.TextColumn("Patient"),
                        "test_name": st.column_config.TextColumn("Test"),
                        "formatted_result": st.column_config.TextColumn("Result"),
                        "reference_range": st.column_config.TextColumn("Reference Range"),
                        "is_abnormal": st.column_config.CheckboxColumn("Abnormal"),
                        "result_date": st.column_config.DateColumn("Date"),
                        "lab_notes": st.column_config.TextColumn("Notes"),
                    },
                    column_order=["patient_name", "test_name", "formatted_result", "reference_range", "is_abnormal", "result_date", "lab_notes"],
                    hide_index=True,
                    use_container_width=True
                )
            else:
                st.info("No lab results match your filters.")
        
        except Exception as e:
            st.error(f"Could not load lab results: {str(e)}")
    
    with lab_tab2:
        # Lab result trend analysis
        st.markdown("### Patient Lab Result Trends")
        
        # Get patient list for selection
        lab_patients = get_lab_patient_list()
        
        if not lab_patients:
            st.info("No patient data available for trending.")
        else:
            # Patient selection
            patient_options = [f"{p['first_name']} {p['last_name']} (#{p['patient_id']})" for p in lab_patients]
            selected_patient = st.selectbox("Select Patient", patient_options, key="trend_patient")
            
            # Extract patient_id from selection
            patient_id = int(selected_patient.split("(#")[1].split(")")[0])
            
            # Filter lab results for selected patient
            lab_results = get_lab_results()
            patient_results = [r for r in lab_results if r["patient_id"] == patient_id]
            
            # Group results by test type
            test_types = list(set([r["test_name"] for r in patient_results]))
            
            if not test_types:
                st.info(f"No lab results found for {selected_patient.split(' (')[0]}.")
            else:
                selected_test = st.selectbox("Select Test Type", test_types, key="selected_test")
                
                # Filter results by selected test
                test_results = [r for r in patient_results if r["test_name"] == selected_test]
                
                if not test_results:
                    st.info(f"No {selected_test} results found for {selected_patient.split(' (')[0]}.")
                else:
                    # Convert to DataFrame for plotting
                    df = pd.DataFrame(test_results)
                    df['result_date'] = pd.to_datetime(df['result_date'])
                    df['result_value_numeric'] = pd.to_numeric(df['result_value'], errors='coerce')
                    
                    # Skip plotting if the results are not numeric
                    if df['result_value_numeric'].isna().all():
                        st.info(f"Cannot plot trend for {selected_test} as the results are not numeric values.")
                    else:
                        # Sort by date
                        df = df.sort_values('result_date')
                        
                        # Plot the trend
                        chart_df = df[['result_date', 'result_value_numeric']].rename(
                            columns={'result_date': 'Date', 'result_value_numeric': 'Value'}
                        )
                        
                        st.line_chart(chart_df.set_index('Date'))
                        
                        # Display a table of the results
                        st.subheader("Result History")
                        
                        # Format the table data
                        display_df = df[['result_date', 'result_value', 'is_abnormal', 'lab_notes']].copy()
                        display_df['result_date'] = display_df['result_date'].dt.strftime('%Y-%m-%d')
                        display_df['result_value'] = display_df['result_value'] + " " + (df.iloc[0]['unit_of_measure'] if df.iloc[0]['unit_of_measure'] else '')
                        
                        # Display the table
                        st.dataframe(
                            display_df,
                            column_config={
                                "result_date": st.column_config.DateColumn("Date"),
                                "result_value": st.column_config.TextColumn("Result"),
                                "is_abnormal": st.column_config.CheckboxColumn("Abnormal"),
                                "lab_notes": st.column_config.TextColumn("Notes")
                            },
                            hide_index=True,
                            use_container_width=True
                        )

# ---------------------------
# TAB 3: PATIENT ASSESSMENT
# ---------------------------
with tab3:
    st.markdown("### Patient Assessment")
    
    # Get patients
    assessment_patients = get_patient_list()
    if not assessment_patients:
        assessment_patients = get_lab_patient_list()
    
    if not assessment_patients:
        st.info("No patients available for assessment.")
    else:
        # Patient selection
        patient_options = [f"{p['first_name']} {p['last_name']} (#{p['patient_id']})" for p in assessment_patients]
        selected_patient = st.selectbox("Select Patient", patient_options, key="assessment_patient")
        
        # Extract patient_id from selection
        patient_id = int(selected_patient.split("(#")[1].split(")")[0])
        patient_name = selected_patient.split(" (#")[0]
        
        # Assessment form
        with st.form("assessment_form"):
            st.subheader(f"Assessment for {patient_name}")
            
            # Vital signs
            st.markdown("#### Vital Signs")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                temperature = st.number_input("Temperature (°F)", min_value=95.0, max_value=105.0, value=98.6, step=0.1)
            
            with col2:
                pulse = st.number_input("Pulse (bpm)", min_value=40, max_value=200, value=80, step=1)
            
            with col3:
                respiration = st.number_input("Respiration (breaths/min)", min_value=8, max_value=40, value=16, step=1)
            
            with col4:
                blood_pressure = st.text_input("Blood Pressure (mmHg)", value="120/80")
            
            # Consciousness level
            consciousness = st.selectbox(
                "Level of Consciousness",
                ["Alert", "Responsive to Voice", "Responsive to Pain", "Unresponsive"]
            )
            
            # Numeric pain scale
            pain_level = st.slider("Pain Level (0-10)", min_value=0, max_value=10, value=0)
            
            # Assessment notes
            assessment_notes = st.text_area("Assessment Notes", placeholder="Enter detailed assessment notes here...")
            
            # Plan of care
            care_plan = st.text_area("Plan of Care", placeholder="Enter plan of care based on assessment...")
            
            # Submit button
            submit_assessment = st.form_submit_button("Save Assessment")
            
            if submit_assessment:
                if not assessment_notes or not care_plan:
                    st.error("Assessment notes and plan of care are required.")
                else:
                    # In a real app, this would call an API to save the assessment
                    st.success(f"Assessment saved successfully for {patient_name}!")

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Patient Care")
