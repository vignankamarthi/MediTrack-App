import streamlit as st
import sys
import os
import pandas as pd
import plotly.express as px
import requests
from datetime import datetime, timedelta

# Add the modules directory to the path so we can import the nav module
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "modules"))
from nav import SideBarLinks

# Page configuration
st.set_page_config(
    page_title="Lab Results | MediTrack", 
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
st.title("Patient Lab Results")
st.subheader("View and review laboratory test results")

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

def get_patient_list():
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

# Custom CSS for styling
st.markdown("""
<style>
    .lab-filter {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .abnormal-badge {
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
        color: white;
    }
    .abnormal {
        background-color: #e63757;
    }
    .normal {
        background-color: #00d97e;
    }
    .lab-form {
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

# Tabs for different views
tab1, tab2, tab3 = st.tabs(["Lab Results", "Review Results", "Result Trends"])

# Tab 1: Lab Results List
with tab1:
    # Filter section
    st.markdown('<div class="lab-filter">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    # Get unique patients for filter
    patients = get_patient_list()
    patient_options = ["All Patients"] + [f"{p['first_name']} {p['last_name']} (#{p['patient_id']})" for p in patients]
    
    with col1:
        filter_patient = st.selectbox("Filter by Patient", patient_options)
    
    with col2:
        filter_abnormal = st.selectbox("Filter by Status", ["All", "Abnormal Only", "Normal Only"])
    
    with col3:
        search_term = st.text_input("Search Tests", placeholder="Enter test name...")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Get lab results data
    try:
        lab_results = get_lab_results()
        
        # Apply filters
        if filter_patient != "All Patients":
            # Extract patient_id from the option string
            selected_id = filter_patient.split("(#")[1].split(")")[0]
            lab_results = [result for result in lab_results if str(result["patient_id"]) == selected_id]
        
        if filter_abnormal == "Abnormal Only":
            lab_results = [result for result in lab_results if result["is_abnormal"]]
        elif filter_abnormal == "Normal Only":
            lab_results = [result for result in lab_results if not result["is_abnormal"]]
        
        if search_term:
            lab_results = [result for result in lab_results if 
                          search_term.lower() in result["test_name"].lower()]
        
        # Convert to DataFrame for display
        if lab_results:
            df = pd.DataFrame(lab_results)
            
            # Create formatted patient name column
            df['patient_name'] = df.apply(lambda row: f"{row['first_name']} {row['last_name']} (#{row['patient_id']})", axis=1)
            
            # Create formatted result column
            df['formatted_result'] = df.apply(
                lambda row: f"{row['result_value']} {row['unit_of_measure'] if row['unit_of_measure'] else ''}", 
                axis=1
            )
            
            # Format dates better
            df['result_date'] = pd.to_datetime(df['result_date']).dt.strftime('%Y-%m-%d')
            
            # Add color coding for abnormal results
            def highlight_abnormal(val):
                if val == True:
                    return 'background-color: #ffecec; color: #e63757; font-weight: bold;'
                return 'background-color: #e7fff2; color: #00d97e;'
            
            # Display the table with styling
            st.dataframe(
                df.style.applymap(highlight_abnormal, subset=['is_abnormal']),
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

# Tab 2: Result Review
with tab2:
    # Review form
    st.markdown('<div class="lab-form">', unsafe_allow_html=True)
    st.subheader("Review Lab Results")
    
    # Get lab results data
    lab_results = get_lab_results()
    abnormal_results = [r for r in lab_results if r["is_abnormal"]]
    
    if not abnormal_results:
        st.info("No abnormal lab results found that need review.")
    else:
        # Format options for selectbox
        result_options = [
            f"{r['test_name']} - {r['result_value']} {r['unit_of_measure'] if r['unit_of_measure'] else ''} - {r['first_name']} {r['last_name']} (#{r['patient_id']})"
            for r in abnormal_results
        ]
        
        selected_result = st.selectbox("Select Lab Result to Review", result_options)
        
        # Match the selected option to the actual result
        selected_index = result_options.index(selected_result)
        result_to_review = abnormal_results[selected_index]
        
        # Display the selected result details
        st.markdown('<div class="lab-detail-card">', unsafe_allow_html=True)
        st.markdown('<div class="lab-detail-header">', unsafe_allow_html=True)
        st.markdown(f"<h3>{result_to_review['test_name']}</h3>", unsafe_allow_html=True)
        
        if result_to_review['is_abnormal']:
            st.markdown('<span class="abnormal-badge abnormal">Abnormal</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="abnormal-badge normal">Normal</span>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="lab-detail-info">', unsafe_allow_html=True)
        
        # Left column
        st.markdown(f"""
        <div class="lab-detail-item">
            <div class="lab-detail-label">Patient</div>
            <div class="lab-detail-value">{result_to_review['first_name']} {result_to_review['last_name']} (#{result_to_review['patient_id']})</div>
        </div>
        <div class="lab-detail-item">
            <div class="lab-detail-label">Test Date</div>
            <div class="lab-detail-value">{result_to_review['test_date']}</div>
        </div>
        <div class="lab-detail-item">
            <div class="lab-detail-label">Result Date</div>
            <div class="lab-detail-value">{result_to_review['result_date']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Right column
        st.markdown(f"""
        <div class="lab-detail-item">
            <div class="lab-detail-label">Result Value</div>
            <div class="lab-detail-value">{result_to_review['result_value']} {result_to_review['unit_of_measure'] if result_to_review['unit_of_measure'] else ''}</div>
        </div>
        <div class="lab-detail-item">
            <div class="lab-detail-label">Reference Range</div>
            <div class="lab-detail-value">{result_to_review['reference_range']} {result_to_review['unit_of_measure'] if result_to_review['unit_of_measure'] else ''}</div>
        </div>
        <div class="lab-detail-item">
            <div class="lab-detail-label">Current Notes</div>
            <div class="lab-detail-value">{result_to_review['lab_notes'] if result_to_review['lab_notes'] else 'No notes'}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Review form
        with st.form("lab_review_form"):
            is_reviewed = st.checkbox("Mark as Reviewed")
            review_notes = st.text_area("Review Notes", placeholder="Enter your notes about this lab result...")
            
            review_button = st.form_submit_button("Update Review Status")
            
            if review_button:
                if not is_reviewed and not review_notes:
                    st.error("Please either mark as reviewed or add review notes.")
                else:
                    # Prepare data for API call
                    update_data = {
                        "result_id": result_to_review['result_id'],
                        "is_reviewed": is_reviewed,
                        "review_notes": review_notes
                    }
                    
                    # Call the API (simulated)
                    updated_result = update_lab_result_review(update_data)
                    
                    # In a real app, you might want to refresh the page or clear the form
                    st.session_state.lab_tab = 0
    
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 3: Result Trends
with tab3:
    st.markdown('<div class="lab-form">', unsafe_allow_html=True)
    st.subheader("Patient Lab Result Trends")
    
    # Get patient list for selection
    patients = get_patient_list()
    
    if not patients:
        st.info("No patient data available for trending.")
    else:
        # Patient selection
        patient_options = [f"{p['first_name']} {p['last_name']} (#{p['patient_id']})" for p in patients]
        selected_patient = st.selectbox("Select Patient", patient_options)
        
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
            selected_test = st.selectbox("Select Test Type", test_types)
            
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
                    
                    # Extract reference range for plotting
                    if '-' in df.iloc[0]['reference_range']:
                        try:
                            ref_min, ref_max = map(float, df.iloc[0]['reference_range'].split('-'))
                            show_reference = True
                        except:
                            show_reference = False
                    elif '<' in df.iloc[0]['reference_range']:
                        try:
                            ref_max = float(df.iloc[0]['reference_range'].replace('<', ''))
                            ref_min = None
                            show_reference = True
                        except:
                            show_reference = False
                    elif '>' in df.iloc[0]['reference_range']:
                        try:
                            ref_min = float(df.iloc[0]['reference_range'].replace('>', ''))
                            ref_max = None
                            show_reference = True
                        except:
                            show_reference = False
                    else:
                        show_reference = False
                    
                    # Create plot
                    fig = px.line(
                        df, 
                        x='result_date', 
                        y='result_value_numeric',
                        markers=True,
                        title=f"{selected_test} Trend for {selected_patient.split(' (')[0]}",
                        labels={
                            'result_date': 'Date',
                            'result_value_numeric': f"Result ({df.iloc[0]['unit_of_measure'] if df.iloc[0]['unit_of_measure'] else ''})"
                        },
                        height=400
                    )
                    
                    # Add reference range if available
                    if show_reference:
                        if ref_min is not None:
                            fig.add_hline(
                                y=ref_min,
                                line_dash="dash",
                                line_color="#95aac9",
                                annotation_text="Min Reference"
                            )
                        if ref_max is not None:
                            fig.add_hline(
                                y=ref_max,
                                line_dash="dash",
                                line_color="#95aac9",
                                annotation_text="Max Reference"
                            )
                    
                    # Customize plot
                    fig.update_traces(
                        line=dict(color="#2c7be5", width=3),
                        marker=dict(size=10, color="#2c7be5")
                    )
                    fig.update_layout(
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        margin=dict(t=40, b=40, l=40, r=40)
                    )
                    
                    # Display the plot
                    st.plotly_chart(fig, use_container_width=True)
                    
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
    
    st.markdown('</div>', unsafe_allow_html=True)

# Call to action section at the bottom
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/12_Care_Tasks.py", label="Manage Care Tasks", icon="📋", use_container_width=True)

with col2:
    st.page_link("pages/13_Patient_Symptoms.py", label="View Patient Symptoms", icon="🤒", use_container_width=True)

with col3:
    st.page_link("pages/15_Medication_Administration.py", label="Medication Administration", icon="💊", use_container_width=True)

# Footer
st.caption("© 2025 MediTrack - Lab Results Management")
