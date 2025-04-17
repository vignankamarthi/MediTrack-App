import streamlit as st
import sys
import os
import requests
import pandas as pd
from datetime import datetime

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

# Custom CSS for medication reconciliation
st.markdown("""
<style>
    /* Card Styles */
    .card {
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    .card-header {
        padding: 15px;
        border-bottom: 1px solid #edf2f9;
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #f9fbfd;
    }
    
    .card-body {
        padding: 15px;
    }
    
    /* Patient Header */
    .patient-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
        padding: 15px;
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    
    .patient-info {
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .patient-avatar {
        width: 50px;
        height: 50px;
        background-color: #95aac9;
        color: white;
        border-radius: 8px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 20px;
        font-weight: bold;
    }
    
    .patient-details h2 {
        margin: 0;
        color: #12263f;
        font-size: 18px;
    }
    
    .patient-details p {
        margin: 5px 0 0;
        color: #95aac9;
        font-size: 14px;
    }
    
    /* Status badge */
    .status-badge {
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 500;
    }
    
    .status-badge.pending {
        background-color: #fef5e6;
        color: #f6c343;
    }
    
    .status-badge.complete {
        background-color: #e4f7ed;
        color: #00d97e;
    }
    
    /* Comparison header */
    .comparison-header {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 30px;
        margin-bottom: 15px;
    }
    
    .comparison-column h4 {
        margin: 0 0 5px;
        color: #12263f;
    }
    
    .comparison-column p {
        margin: 0;
        color: #95aac9;
        font-size: 12px;
    }
    
    /* Medication groups */
    .medication-group {
        display: grid;
        grid-template-columns: 1fr auto 1fr;
        gap: 15px;
        margin-bottom: 15px;
        padding: 10px;
        border-radius: 8px;
        background-color: #f9fbfd;
        align-items: center;
    }
    
    .medication-group.reconciled {
        border-left: 4px solid #00d97e;
    }
    
    .medication-group.unreconciled {
        border-left: 4px solid #f6c343;
    }
    
    .comparison-item {
        padding: 15px;
        background-color: white;
        border-radius: 5px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }
    
    .med-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
    }
    
    .med-name {
        font-weight: 600;
        color: #12263f;
    }
    
    .med-status {
        font-size: 12px;
        padding: 2px 8px;
        border-radius: 10px;
        background-color: #edf2f9;
        color: #95aac9;
    }
    
    .med-status.continued {
        background-color: #e4f7ed;
        color: #00d97e;
    }
    
    .med-status.modified {
        background-color: #fef5e6;
        color: #f6c343;
    }
    
    .med-status.new {
        background-color: #eaeffd;
        color: #2c7be5;
    }
    
    .med-details p {
        margin: 5px 0;
        font-size: 13px;
    }
    
    .comparison-arrow {
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative;
    }
    
    .arrow-icon {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
    }
    
    .continued .arrow-icon {
        background-color: #00d97e;
    }
    
    .modified .arrow-icon {
        background-color: #f6c343;
    }
    
    .discontinued .arrow-icon {
        background-color: #e63757;
    }
    
    .new .arrow-icon {
        background-color: #2c7be5;
    }
    
    .modification-tag {
        position: absolute;
        font-size: 10px;
        background-color: #f9fbfd;
        padding: 2px 5px;
        border-radius: 10px;
        white-space: nowrap;
        color: #95aac9;
        top: -15px;
    }
</style>
""", unsafe_allow_html=True)

# Get patient ID from session state or use default for demo
patient_id = st.session_state.get('selected_patient_id', 101)

# Function to get patient data
def get_patient_data(patient_id):
    """Get basic patient information"""
    # In a real app, this would call an API endpoint
    # Here we're using mock data for demonstration
    
    patients = {
        101: {
            "patient_id": 101,
            "first_name": "John",
            "last_name": "Doe",
            "dob": "1968-05-15",
            "gender": "Male",
            "admission_date": "2025-03-20",
            "discharge_date": "2025-03-23",
            "primary_provider": "Dr. James Wilson"
        },
        102: {
            "patient_id": 102,
            "first_name": "Sarah",
            "last_name": "Smith",
            "dob": "1992-08-22",
            "gender": "Female",
            "admission_date": "2025-03-15",
            "discharge_date": "2025-03-22",
            "primary_provider": "Dr. Michael Chen"
        }
    }
    
    return patients.get(patient_id, patients[101])  # Default to John Doe if not found

# Function to get medication reconciliation data
def get_medication_reconciliation_data(patient_id):
    """Get medication reconciliation data for a patient
    
    In a real implementation, this would call:
    response = requests.get(f"http://web-api:4000/ph/prescription-patient-records/{patient_id}")
    if response.status_code == 200:
        return response.json()
    return None
    """
    
    # Mock data for demonstration purposes
    reconciliation_data = {
        "pre_admission": [
            {
                "medication_name": "Lisinopril 10mg",
                "status": "Continued",
                "dose": "10mg oral tablet",
                "frequency": "Once daily",
                "prescriber": "Dr. Jones (PCP)",
                "last_filled": "Mar 10, 2025"
            },
            {
                "medication_name": "Metformin 500mg",
                "status": "Modified",
                "dose": "500mg oral tablet",
                "frequency": "Once daily",
                "prescriber": "Dr. Jones (PCP)",
                "last_filled": "Mar 05, 2025"
            },
            {
                "medication_name": "Atorvastatin 20mg",
                "status": "Discontinued",
                "dose": "20mg oral tablet",
                "frequency": "Once daily at bedtime",
                "prescriber": "Dr. Jones (PCP)",
                "last_filled": "Feb 15, 2025"
            }
        ],
        "post_discharge": [
            {
                "medication_name": "Lisinopril 10mg",
                "status": "Continued",
                "dose": "10mg oral tablet",
                "frequency": "Once daily",
                "prescriber": "Dr. Wilson",
                "supply": "30 days"
            },
            {
                "medication_name": "Metformin 500mg",
                "status": "Modified",
                "dose": "500mg oral tablet",
                "frequency": "Twice daily",
                "prescriber": "Dr. Wilson",
                "supply": "30 days"
            },
            {
                "medication_name": "Rosuvastatin 10mg",
                "status": "New",
                "dose": "10mg oral tablet",
                "frequency": "Once daily at bedtime",
                "prescriber": "Dr. Wilson",
                "supply": "30 days"
            }
        ],
        "status": "In Progress"
    }
    
    return reconciliation_data

# Get patient data
patient_data = get_patient_data(patient_id)
med_reconciliation_data = get_medication_reconciliation_data(patient_id)

# Calculate patient age
birth_year = int(patient_data["dob"].split('-')[0])
current_year = datetime.now().year
age = current_year - birth_year

# Title
st.title("Medication Reconciliation")

# Patient header with initials in avatar
patient_initials = f"{patient_data['first_name'][0]}{patient_data['last_name'][0]}"

st.markdown(f"""
<div class="patient-header">
    <div class="patient-info">
        <div class="patient-avatar">{patient_initials}</div>
        <div class="patient-details">
            <h2>{patient_data['first_name']} {patient_data['last_name']}</h2>
            <p>ID: {patient_data['patient_id']} • {age} years • {patient_data['gender']}</p>
            <p>Admission: {patient_data['admission_date']} • Discharge: {patient_data['discharge_date']} (Planned)</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Action buttons for patient
col1, col2 = st.columns(2)
with col1:
    st.button("View Full Profile", use_container_width=True)
with col2:
    st.button("Complete Reconciliation", use_container_width=True)

# Tab navigation
tab1, tab2, tab3, tab4 = st.tabs(["Medication Reconciliation", "Schedule Optimization", "Patient Counseling", "Transition Checklist"])

# Tab 1: Medication Reconciliation
with tab1:
    # Card header with status badge
    st.markdown(f"""
    <div class="card">
        <div class="card-header">
            <h3>Medication Reconciliation</h3>
            <div>
                <span class="status-badge pending">{med_reconciliation_data["status"]}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Filter options
    filter_option = st.selectbox(
        "Filter medications", 
        ["All Medications", "Unreconciled Only", "Reconciled Only"]
    )
    
    # Comparison header
    st.markdown("""
    <div class="comparison-header">
        <div class="comparison-column">
            <h4>Pre-Admission Medications</h4>
            <p>Home medications reported at intake</p>
        </div>
        <div class="comparison-column">
            <h4>Post-Discharge Medications</h4>
            <p>Medications prescribed for discharge</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Create medication comparison for continued medications
    for pre_med in med_reconciliation_data["pre_admission"]:
        # Find matching post-discharge medication
        post_med = None
        arrow_class = "continued"
        group_class = "reconciled"
        icon = "→"
        tag = ""
        
        if pre_med["status"] == "Continued":
            # Find matching continued medication
            for med in med_reconciliation_data["post_discharge"]:
                if med["medication_name"] == pre_med["medication_name"] and med["status"] == "Continued":
                    post_med = med
                    break
                    
        elif pre_med["status"] == "Modified":
            # Find matching modified medication
            for med in med_reconciliation_data["post_discharge"]:
                if med["medication_name"] == pre_med["medication_name"] and med["status"] == "Modified":
                    post_med = med
                    arrow_class = "modified"
                    tag = "Dose/Frequency Changed"
                    break
                    
        elif pre_med["status"] == "Discontinued":
            # This is a discontinued medication
            arrow_class = "discontinued"
            group_class = "unreconciled"
            icon = "✕"
            tag = "Discontinued"
            post_med = {
                "medication_name": "N/A",
                "reason": "Switched to alternative"
            }
            
        # Skip if filtering and doesn't match
        if filter_option == "Reconciled Only" and group_class != "reconciled":
            continue
        if filter_option == "Unreconciled Only" and group_class != "unreconciled":
            continue
            
        # Create the medication comparison group
        st.markdown(f"""
        <div class="medication-group {group_class}">
            <div class="comparison-item">
                <div class="med-header">
                    <div class="med-name">{pre_med["medication_name"]}</div>
                    <div class="med-status">{pre_med["status"]}</div>
                </div>
                <div class="med-details">
                    <p><strong>Dose:</strong> {pre_med["dose"]}</p>
                    <p><strong>Frequency:</strong> {pre_med["frequency"]}</p>
                    <p><strong>Prescriber:</strong> {pre_med["prescriber"]}</p>
                    <p><strong>Last Filled:</strong> {pre_med["last_filled"]}</p>
                </div>
            </div>
            <div class="comparison-arrow {arrow_class}">
                <div class="arrow-icon">{icon}</div>
                {f'<div class="modification-tag">{tag}</div>' if tag else ''}
            </div>
            <div class="comparison-item">
                <div class="med-header">
                    <div class="med-name">{post_med["medication_name"]}</div>
                    {f'<div class="med-status {arrow_class.replace("discontinued", "")}">{post_med["status"]}</div>' if "status" in post_med else ''}
                </div>
                <div class="med-details">
                    {f'<p><strong>Dose:</strong> {post_med["dose"]}</p>' if "dose" in post_med else ''}
                    {f'<p><strong>Frequency:</strong> {post_med["frequency"]}</p>' if "frequency" in post_med else ''}
                    {f'<p><strong>Prescriber:</strong> {post_med["prescriber"]}</p>' if "prescriber" in post_med else ''}
                    {f'<p><strong>Supply:</strong> {post_med["supply"]}</p>' if "supply" in post_med else ''}
                    {f'<p><strong>Reason:</strong> {post_med["reason"]}</p>' if "reason" in post_med else ''}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Handle document reason button for discontinued medications
    if any(med["status"] == "Discontinued" for med in med_reconciliation_data["pre_admission"]):
        st.button("Document Reason", key="document_reason_button", use_container_width=True)
    
    # Add new medications (not in pre-admission)
    for post_med in med_reconciliation_data["post_discharge"]:
        # Check if this is a new medication (not in pre-admission)
        if not any(pre_med["medication_name"] == post_med["medication_name"] for pre_med in med_reconciliation_data["pre_admission"]):
            # Skip if filtering and doesn't match
            if filter_option == "Reconciled Only":
                continue
                
            # Create new medication group
            st.markdown(f"""
            <div class="medication-group unreconciled">
                <div class="comparison-item">
                    <div class="med-header">
                        <div class="med-name">N/A</div>
                    </div>
                    <div class="med-details">
                        <p>New medication added during hospitalization</p>
                    </div>
                </div>
                <div class="comparison-arrow new">
                    <div class="arrow-icon">+</div>
                    <div class="modification-tag">New Medication</div>
                </div>
                <div class="comparison-item">
                    <div class="med-header">
                        <div class="med-name">{post_med["medication_name"]}</div>
                        <div class="med-status new">{post_med["status"]}</div>
                    </div>
                    <div class="med-details">
                        <p><strong>Dose:</strong> {post_med["dose"]}</p>
                        <p><strong>Frequency:</strong> {post_med["frequency"]}</p>
                        <p><strong>Prescriber:</strong> {post_med["prescriber"]}</p>
                        <p><strong>Supply:</strong> {post_med["supply"]}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# Tab 2: Schedule Optimization (placeholder)
with tab2:
    st.subheader("Medication Schedule Optimization")
    st.info("This tab would contain the medication schedule optimization interface, helping to create an optimal medication schedule based on patient preferences and medication requirements.")
    
    # Basic layout of schedule optimization
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("### Medications")
        st.checkbox("Lisinopril 10mg", value=True)
        st.checkbox("Metformin 500mg", value=True)
        st.checkbox("Rosuvastatin 10mg", value=True)
        
        st.markdown("### Patient Preferences")
        st.time_input("Wake-up time", value=datetime.strptime("07:00", "%H:%M"))
        st.time_input("Bedtime", value=datetime.strptime("22:00", "%H:%M"))
        
    with col2:
        st.markdown("### Daily Schedule")
        st.image("https://via.placeholder.com/800x200?text=Medication+Schedule+Timeline")

# Tab 3: Patient Counseling (placeholder)
with tab3:
    st.subheader("Patient Counseling Documentation")
    st.info("This tab would contain the patient counseling interface, where pharmacists can document counseling sessions for each medication.")
    
    # Simple counseling layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### Medications Requiring Counseling")
        
        # Display list of medications requiring counseling
        st.markdown("""
        <div style="padding: 10px; background-color: #f9fbfd; border-radius: 5px; margin-bottom: 10px;">
            <div style="display: flex; align-items: center;">
                <span style="color: #00d97e; margin-right: 10px;">✓</span>
                <div>
                    <div style="font-weight: 600;">Lisinopril 10mg</div>
                    <div style="font-size: 12px; color: #95aac9;">Continued</div>
                </div>
            </div>
        </div>
        
        <div style="padding: 10px; background-color: #f9fbfd; border-radius: 5px; margin-bottom: 10px;">
            <div style="display: flex; align-items: center;">
                <span style="color: #00d97e; margin-right: 10px;">✓</span>
                <div>
                    <div style="font-weight: 600;">Metformin 500mg</div>
                    <div style="font-size: 12px; color: #95aac9;">Modified</div>
                </div>
            </div>
        </div>
        
        <div style="padding: 10px; background-color: #eaeffd; border-radius: 5px; margin-bottom: 10px; border-left: 3px solid #2c7be5;">
            <div style="display: flex; align-items: center;">
                <span style="color: #2c7be5; margin-right: 10px;">○</span>
                <div>
                    <div style="font-weight: 600;">Rosuvastatin 10mg</div>
                    <div style="font-size: 12px; color: #95aac9;">New</div>
                </div>
            </div>
        </div>
        
        <div style="padding: 10px; background-color: #f9fbfd; border-radius: 5px; margin-bottom: 10px;">
            <div style="display: flex; align-items: center;">
                <span style="color: #95aac9; margin-right: 10px;">○</span>
                <div>
                    <div style="font-weight: 600;">Atorvastatin 20mg</div>
                    <div style="font-size: 12px; color: #95aac9;">Discontinued</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("### Rosuvastatin 10mg - Counseling Documentation")
        
        # Documentation form
        with st.form("counseling_form"):
            # Medication information checkboxes
            st.markdown("#### Medication Information Provided")
            col_a, col_b = st.columns(2)
            with col_a:
                st.checkbox("Purpose of medication", value=True)
                st.checkbox("How to take medication", value=True)
                st.checkbox("Expected benefits", value=True)
                st.checkbox("Potential side effects", value=True)
            with col_b:
                st.checkbox("What to do if dose is missed", value=False)
                st.checkbox("Storage instructions", value=False)
                st.checkbox("Refill information", value=True)
            
            # Patient understanding assessment
            st.markdown("#### Patient Understanding Assessment")
            understanding = st.radio("Patient demonstrated understanding:", 
                                    ["Excellent", "Good", "Fair", "Poor"], index=1,
                                    horizontal=True)
            
            # Additional notes
            st.markdown("#### Additional Notes")
            notes = st.text_area("Notes", placeholder="Enter additional counseling notes here...")
            
            # Educational materials
            st.markdown("#### Educational Materials Provided")
            col_c, col_d = st.columns(2)
            with col_c:
                st.checkbox("Medication information sheet", value=True)
                st.checkbox("Visual medication schedule", value=False)
            with col_d:
                st.checkbox("Side effect management guide", value=True)
                st.checkbox("Condition-specific education", value=False)
            
            # Form buttons
            col_submit1, col_submit2 = st.columns(2)
            with col_submit1:
                st.form_submit_button("Save Draft")
            with col_submit2:
                if st.form_submit_button("Complete Counseling"):
                    st.success("Counseling documentation completed successfully!")

# Tab 4: Transition Checklist (placeholder)
with tab4:
    st.subheader("Transition of Care Checklist")
    st.info("This tab would contain the transition of care checklist, ensuring all necessary steps are completed before discharge.")
    
    # Progress tracker
    st.markdown("### Completion Progress")
    st.progress(0.66, text="8 of 12 tasks complete")
    
    # Checklist categories
    with st.expander("✅ Medication Verification", expanded=True):
        st.checkbox("Verify Pre-Admission Medications", value=True)
        st.checkbox("Review Discharge Medication List", value=True)
        st.checkbox("Identify and Resolve Discrepancies", value=True)
    
    with st.expander("🔄 Patient Education and Support", expanded=True):
        st.checkbox("Patient Medication Counseling", value=True)
        st.checkbox("Provide Written Medication Schedule", value=True)
        st.checkbox("Assess Adherence Barriers", value=False)
    
    with st.expander("🔄 Care Coordination", expanded=True):
        st.checkbox("Communicate with Primary Care Provider", value=True)
        st.checkbox("Coordinate with Community Pharmacy", value=False)
        st.checkbox("Schedule Follow-up Appointment", value=False)
    
    with st.expander("🔄 Prescriber Synchronization", expanded=True):
        st.checkbox("Identify All Current Prescribers", value=True)
        st.checkbox("Create Prescriber Matrix", value=True)
        st.checkbox("Resolve Overlapping Prescriptions", value=False)
    
    # Complete checklist button
    st.button("Mark Transition of Care Complete", use_container_width=True)
    
    # Prescriber synchronization section
    st.markdown("### Prescriber Synchronization View")
    st.markdown("""
    <div style="background-color: white; border-radius: 8px; padding: 15px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); margin-bottom: 20px;">
        <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-bottom: 20px;">
            <!-- Primary prescriber card -->
            <div style="display: flex; align-items: center; gap: 10px; padding: 10px; background-color: rgba(44, 123, 229, 0.1); border-radius: 5px; border: 1px solid #2c7be5; min-width: 250px;">
                <div style="width: 40px; height: 40px; border-radius: 50%; background-color: #2c7be5; color: white; display: flex; justify-content: center; align-items: center;">👨‍⚕️</div>
                <div>
                    <div style="font-weight: 600;">Dr. James Wilson</div>
                    <div style="font-size: 12px; color: #95aac9;">Primary Care Physician</div>
                </div>
            </div>
            
            <!-- Secondary prescriber card -->
            <div style="display: flex; align-items: center; gap: 10px; padding: 10px; background-color: #f9fbfd; border-radius: 5px; border: 1px solid #edf2f9; min-width: 250px;">
                <div style="width: 40px; height: 40px; border-radius: 50%; background-color: #95aac9; color: white; display: flex; justify-content: center; align-items: center;">👩‍⚕️</div>
                <div>
                    <div style="font-weight: 600;">Dr. Maria Lopez</div>
                    <div style="font-size: 12px; color: #95aac9;">Endocrinologist</div>
                </div>
            </div>
        </div>
        
        <!-- Medication-prescriber matrix -->
        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr style="background-color: #f9fbfd;">
                    <th style="padding: 10px; text-align: left; color: #95aac9; font-weight: 500;">Medication</th>
                    <th style="padding: 10px; text-align: left; color: #95aac9; font-weight: 500;">Dr. Wilson (PCP)</th>
                    <th style="padding: 10px; text-align: left; color: #95aac9; font-weight: 500;">Dr. Lopez (Endo)</th>
                    <th style="padding: 10px; text-align: left; color: #95aac9; font-weight: 500;">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #edf2f9;">Lisinopril 10mg</td>
                    <td style="padding: 10px; border-bottom: 1px solid #edf2f9; color: #00d97e;">✓ Current</td>
                    <td style="padding: 10px; border-bottom: 1px solid #edf2f9;"></td>
                    <td style="padding: 10px; border-bottom: 1px solid #edf2f9;"></td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #edf2f9;">Metformin 500mg</td>
                    <td style="padding: 10px; border-bottom: 1px solid #edf2f9;"></td>
                    <td style="padding: 10px; border-bottom: 1px solid #edf2f9; color: #00d97e;">✓ Current</td>
                    <td style="padding: 10px; border-bottom: 1px solid #edf2f9;"></td>
                </tr>
                <tr style="background-color: rgba(246, 195, 67, 0.1);">
                    <td style="padding: 10px; border-bottom: 1px solid #edf2f9;">Rosuvastatin 10mg</td>
                    <td style="padding: 10px; border-bottom: 1px solid #edf2f9; color: #00d97e;">✓ Current</td>
                    <td style="padding: 10px; border-bottom: 1px solid #edf2f9; color: #00d97e;">✓ Current</td>
                    <td style="padding: 10px; border-bottom: 1px solid #edf2f9;">
                        <button style="background-color: #f6c343; color: white; border: none; padding: 5px 10px; border-radius: 3px; cursor: pointer; font-size: 12px;">Resolve</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)

    # Matrix actions
    col1, col2 = st.columns(2)
    with col1:
        st.button("Print Report", use_container_width=True)
    with col2:
        st.button("Contact Prescribers", use_container_width=True)

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Medication Reconciliation Tool")
