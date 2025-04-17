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
    page_title="Prescription Outcomes | MediTrack", 
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

# Custom CSS for styling
st.markdown("""
<style>
    .card {
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin-bottom: 20px;
    }
    
    .outcome-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
        padding-bottom: 15px;
        border-bottom: 1px solid #edf2f9;
    }
    
    .filter-group {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .status-badge {
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 500;
    }
    
    .status-effective {
        background-color: #e4f7ed;
        color: #00d97e;
    }
    
    .status-partial {
        background-color: #fef5e6;
        color: #f6c343;
    }
    
    .status-ineffective {
        background-color: #fae7eb;
        color: #e63757;
    }
    
    .outcome-table th {
        background-color: #f9fbfd;
        color: #95aac9;
        font-weight: 500;
    }
    
    .outcome-card {
        padding: 15px;
        border-radius: 8px;
        background-color: #f9fbfd;
        margin-bottom: 15px;
        border-left: 3px solid #2c7be5;
    }
    
    .outcome-card h4 {
        margin-top: 0;
        margin-bottom: 10px;
        color: #12263f;
    }
    
    .outcome-meta {
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        color: #95aac9;
        margin-bottom: 10px;
    }
    
    .outcome-metrics {
        display: flex;
        gap: 15px;
        margin-bottom: 15px;
    }
    
    .outcome-metric {
        background-color: white;
        padding: 10px;
        border-radius: 5px;
        flex: 1;
        text-align: center;
    }
    
    .metric-label {
        font-size: 12px;
        color: #95aac9;
        margin-bottom: 5px;
    }
    
    .metric-value {
        font-size: 18px;
        font-weight: 600;
        color: #12263f;
    }
    
    .metric-target {
        font-size: 11px;
        color: #95aac9;
    }
</style>
""", unsafe_allow_html=True)

# Page header
st.title("Prescription Outcomes")
st.subheader("Track and analyze medication effectiveness")

# Function to get prescription outcomes data (mock)
def get_prescription_outcomes():
    """Simulate an API call to /ph/prescription-outcome-records"""
    # In a real app, this would call:
    # response = requests.get("http://web-api:4000/ph/prescription-outcome-records")
    # return response.json()
    
    # Return simulated data
    return [
        {
            "outcome_id": 1,
            "prescription_id": 1001,
            "prescription_date": "2025-03-10",
            "medication_name": "Lisinopril 10mg",
            "duration": 30,
            "refills": 2,
            "outcome_name": "Blood Pressure Control",
            "effectiveness": "Effective",
            "patient_name": "John Doe",
            "patient_id": 101,
            "baseline_value": "145/90 mmHg",
            "current_value": "128/82 mmHg",
            "target_value": "<130/80 mmHg",
            "prescriber": "Dr. James Wilson",
            "notes": "Patient reports good tolerance. Blood pressure adequately controlled."
        },
        {
            "outcome_id": 2,
            "prescription_id": 1002,
            "prescription_date": "2025-03-05",
            "medication_name": "Metformin 500mg",
            "duration": 30,
            "refills": 2,
            "outcome_name": "Glycemic Control",
            "effectiveness": "Partially Effective",
            "patient_name": "John Doe",
            "patient_id": 101,
            "baseline_value": "HbA1c 8.2%",
            "current_value": "HbA1c 7.8%",
            "target_value": "HbA1c <7.0%",
            "prescriber": "Dr. Maria Lopez",
            "notes": "Patient reports occasional GI discomfort. Glycemic control improving but not at target."
        },
        {
            "outcome_id": 3,
            "prescription_id": 1003,
            "prescription_date": "2025-03-01",
            "medication_name": "Atorvastatin 20mg",
            "duration": 30,
            "refills": 0,
            "outcome_name": "Lipid Management",
            "effectiveness": "Ineffective",
            "patient_name": "John Doe",
            "patient_id": 101,
            "baseline_value": "LDL 165 mg/dL",
            "current_value": "LDL 155 mg/dL",
            "target_value": "LDL <100 mg/dL",
            "prescriber": "Dr. James Wilson",
            "notes": "Patient reports muscle pain. Minimal improvement in lipid profile. Consider alternative statin."
        },
        {
            "outcome_id": 4,
            "prescription_id": 1004,
            "prescription_date": "2025-02-15",
            "medication_name": "Levothyroxine 50mcg",
            "duration": 30,
            "refills": 3,
            "outcome_name": "Thyroid Function",
            "effectiveness": "Effective",
            "patient_name": "Sarah Smith",
            "patient_id": 102,
            "baseline_value": "TSH 7.2 mIU/L",
            "current_value": "TSH 2.4 mIU/L",
            "target_value": "TSH 0.5-4.0 mIU/L",
            "prescriber": "Dr. Michael Chen",
            "notes": "Thyroid function well controlled with current dose."
        }
    ]

# Function to update outcome effectiveness
def update_outcome_effectiveness(outcome_id, prescription_id, effectiveness, notes):
    """Simulate updating prescription outcome effectiveness"""
    # In a real app, this would call:
    # data = {
    #     "outcome_id": outcome_id,
    #     "prescription_id": prescription_id,
    #     "effectiveness": effectiveness,
    #     "notes": notes
    # }
    # response = requests.put("http://web-api:4000/ph/prescription-outcome-records", json=data)
    # return response.json()
    
    # For demo, just return a success message
    return {"message": "Prescription effectiveness successfully updated"}

# Get prescription outcomes
prescription_outcomes = get_prescription_outcomes()

# Filter controls
st.markdown('<div class="card">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    patient_filter = st.selectbox(
        "Filter by Patient",
        ["All Patients"] + list(set([outcome["patient_name"] for outcome in prescription_outcomes]))
    )

with col2:
    effectiveness_filter = st.selectbox(
        "Filter by Effectiveness",
        ["All", "Effective", "Partially Effective", "Ineffective"]
    )

with col3:
    date_range = st.selectbox(
        "Date Range",
        ["Last 30 Days", "Last 90 Days", "Last 6 Months", "Last Year", "All Time"]
    )

st.markdown('</div>', unsafe_allow_html=True)

# Apply filters
filtered_outcomes = prescription_outcomes
if patient_filter != "All Patients":
    filtered_outcomes = [outcome for outcome in filtered_outcomes if outcome["patient_name"] == patient_filter]

if effectiveness_filter != "All":
    filtered_outcomes = [outcome for outcome in filtered_outcomes if outcome["effectiveness"] == effectiveness_filter]

# Display outcomes in tabular form
st.markdown("### Prescription Outcomes Overview")

if filtered_outcomes:
    # Convert to DataFrame
    df = pd.DataFrame(filtered_outcomes)
    
    # Display as table
    st.dataframe(
        df[["prescription_id", "medication_name", "patient_name", "outcome_name", "effectiveness", "prescription_date"]],
        column_config={
            "prescription_id": st.column_config.NumberColumn("Rx ID"),
            "medication_name": st.column_config.TextColumn("Medication"),
            "patient_name": st.column_config.TextColumn("Patient"),
            "outcome_name": st.column_config.TextColumn("Outcome"),
            "effectiveness": st.column_config.TextColumn("Effectiveness"),
            "prescription_date": st.column_config.DateColumn("Date")
        },
        hide_index=True,
        use_container_width=True
    )
else:
    st.info("No prescription outcomes match your filters.")

# Display detailed outcomes
st.markdown("### Detailed Outcomes Analysis")

# Container for detailed outcome cards
for outcome in filtered_outcomes:
    # Create effectiveness badge class
    badge_class = "status-effective"
    if outcome["effectiveness"] == "Partially Effective":
        badge_class = "status-partial"
    elif outcome["effectiveness"] == "Ineffective":
        badge_class = "status-ineffective"
    
    # Create outcome card
    st.markdown(f"""
    <div class="outcome-card">
        <h4>{outcome["medication_name"]} - {outcome["outcome_name"]}</h4>
        <div class="outcome-meta">
            <div>Patient: {outcome["patient_name"]} (#{outcome["patient_id"]})</div>
            <div>Prescribed: {outcome["prescription_date"]} • Duration: {outcome["duration"]} days • Refills: {outcome["refills"]}</div>
        </div>
        <div class="outcome-metrics">
            <div class="outcome-metric">
                <div class="metric-label">Baseline</div>
                <div class="metric-value">{outcome["baseline_value"]}</div>
            </div>
            <div class="outcome-metric">
                <div class="metric-label">Current</div>
                <div class="metric-value">{outcome["current_value"]}</div>
            </div>
            <div class="outcome-metric">
                <div class="metric-label">Target</div>
                <div class="metric-value">{outcome["target_value"]}</div>
            </div>
            <div class="outcome-metric">
                <div class="metric-label">Effectiveness</div>
                <div class="metric-value">
                    <span class="status-badge {badge_class}">{outcome["effectiveness"]}</span>
                </div>
            </div>
        </div>
        <div>
            <strong>Notes:</strong> {outcome["notes"]}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add update buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Update Effectiveness", key=f"update_{outcome['outcome_id']}", use_container_width=True):
            st.session_state.editing_outcome = outcome
    with col2:
        if st.button("View Patient History", key=f"history_{outcome['outcome_id']}", use_container_width=True):
            # Would navigate to patient view in a real app
            st.session_state.selected_patient_id = outcome["patient_id"]
            st.info(f"This would navigate to the patient history view for {outcome['patient_name']}")

# Show effectiveness update form if requested
if "editing_outcome" in st.session_state:
    outcome = st.session_state.editing_outcome
    
    st.markdown(f"### Update Effectiveness for {outcome['medication_name']} - {outcome['outcome_name']}")
    
    with st.form(key="effectiveness_form"):
        effectiveness = st.selectbox(
            "Effectiveness",
            ["Effective", "Partially Effective", "Ineffective"],
            index=["Effective", "Partially Effective", "Ineffective"].index(outcome["effectiveness"])
        )
        
        notes = st.text_area("Clinical Notes", value=outcome["notes"])
        
        col1, col2 = st.columns(2)
        with col1:
            cancel = st.form_submit_button("Cancel")
        with col2:
            submit = st.form_submit_button("Save Changes")
        
        if submit:
            # Update effectiveness (would call API in real app)
            update_outcome_effectiveness(
                outcome["outcome_id"],
                outcome["prescription_id"],
                effectiveness,
                notes
            )
            
            st.success("Effectiveness updated successfully!")
            
            # Clear editing state
            st.session_state.pop("editing_outcome")
            st.experimental_rerun()
            
        elif cancel:
            # Clear editing state
            st.session_state.pop("editing_outcome")
            st.experimental_rerun()

# Quick actions section
st.markdown("### Quick Actions")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Generate Outcomes Report", use_container_width=True):
        st.download_button(
            "Download PDF Report",
            data="This would be a PDF report in a real app",
            file_name="prescription_outcomes_report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

with col2:
    if st.button("Contact Prescribers", use_container_width=True):
        st.info("This would open a communication tool to contact prescribers about outcomes")

with col3:
    if st.button("Back to Dashboard", use_container_width=True):
        st.switch_page("pages/21_Pharmacist_Home.py")

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Prescription Outcomes Analysis")
