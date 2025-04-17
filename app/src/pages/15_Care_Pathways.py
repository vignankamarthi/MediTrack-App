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
    page_title="Care Pathways | MediTrack", 
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
    /* General Layout Styles */
    .container {
        max-width: 1400px;
        margin: 0 auto;
    }

    /* Card Styles */
    .pathway-card {
        background-color: white;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
    }
    
    .pathway-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
    
    .pathway-title {
        font-size: 18px;
        font-weight: 600;
        color: #12263f;
    }
    
    .pathway-meta {
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        margin-bottom: 15px;
    }
    
    .pathway-patient {
        color: #12263f;
    }
    
    .pathway-duration {
        color: #95aac9;
    }
    
    .pathway-progress {
        height: 10px;
        background-color: #edf2f9;
        border-radius: 5px;
        overflow: hidden;
        margin-bottom: 5px;
    }
    
    .progress-bar {
        height: 100%;
        background-color: #2c7be5;
    }
    
    .progress-text {
        text-align: right;
        font-size: 12px;
        color: #95aac9;
    }
    
    /* Step Styles */
    .step-card {
        background-color: white;
        border-radius: 8px;
        border: 1px solid #edf2f9;
        margin-bottom: 15px;
        overflow: hidden;
    }
    
    .step-header {
        display: flex;
        align-items: center;
        padding: 12px 15px;
        background-color: #f9fbfd;
        gap: 10px;
        border-bottom: 1px solid #edf2f9;
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
    
    .step-complete {
        background-color: #00d97e;
    }
    
    .step-in-progress {
        background-color: #f6c343;
    }
    
    .step-not-started {
        background-color: #95aac9;
    }
    
    .step-body {
        padding: 15px;
    }
    
    .step-description {
        margin-bottom: 15px;
        color: #12263f;
    }
    
    /* Patient Avatar */
    .patient-avatar {
        width: 40px;
        height: 40px;
        border-radius: 8px;
        background-color: #95aac9;
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 16px;
        font-weight: bold;
    }
    
    /* Status badges */
    .status-badge {
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
        color: white;
    }
    
    .active {
        background-color: #00d97e;
    }
    
    .on-hold {
        background-color: #f6c343;
    }
    
    .completed {
        background-color: #95aac9;
    }
    
    /* Form styles */
    .form-card {
        background-color: white;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    /* Filter controls */
    .filter-controls {
        background-color: white;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Page title
st.title("Care Pathways")
st.subheader("Manage and monitor standardized care plans")

# Mock API functions for demo purposes
def get_care_pathways():
    """Return a list of care pathway templates"""
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

def get_patient_pathways():
    """Return a list of active patient-pathway assignments"""
    return [
        {
            "id": 1,
            "pathway_id": 1,
            "pathway_name": "Heart Failure Management",
            "patient_id": 101,
            "patient_name": "John Doe",
            "start_date": "2025-03-20",
            "expected_end_date": "2025-06-18",
            "status": "ACTIVE",
            "progress": 35,
            "steps_completed": 2,
            "total_steps": 6
        },
        {
            "id": 2,
            "pathway_id": 2,
            "pathway_name": "Diabetes Care Plan",
            "patient_id": 103,
            "patient_name": "Michael Brown",
            "start_date": "2025-02-10",
            "expected_end_date": "2025-08-09",
            "status": "ACTIVE",
            "progress": 45,
            "steps_completed": 4,
            "total_steps": 9
        },
        {
            "id": 3,
            "pathway_id": 3,
            "pathway_name": "Post-Surgical Recovery",
            "patient_id": 104,
            "patient_name": "Emily Davis",
            "start_date": "2025-04-05",
            "expected_end_date": "2025-05-20",
            "status": "ACTIVE",
            "progress": 60,
            "steps_completed": 3,
            "total_steps": 5
        },
        {
            "id": 4,
            "pathway_id": 4,
            "pathway_name": "COPD Management",
            "patient_id": 108,
            "patient_name": "William Wilson",
            "start_date": "2025-01-15",
            "expected_end_date": "2025-05-15",
            "status": "ACTIVE",
            "progress": 80,
            "steps_completed": 8,
            "total_steps": 10
        },
        {
            "id": 5,
            "pathway_id": 5,
            "pathway_name": "Stroke Recovery Protocol",
            "patient_id": 115,
            "patient_name": "James Walker",
            "start_date": "2025-03-01",
            "expected_end_date": "2025-05-30",
            "status": "ON_HOLD",
            "progress": 20,
            "steps_completed": 2,
            "total_steps": 10
        }
    ]

def get_patient_list():
    """Return a list of patients"""
    return [
        {"patient_id": 101, "first_name": "John", "last_name": "Doe", "dob": "1968-05-15", "gender": "Male", "admission_date": "2025-03-20", "primary_provider": "Dr. James Wilson"},
        {"patient_id": 102, "first_name": "Sarah", "last_name": "Smith", "dob": "1992-08-22", "gender": "Female", "admission_date": "2025-03-25", "primary_provider": "Dr. James Wilson"},
        {"patient_id": 103, "first_name": "Michael", "last_name": "Brown", "dob": "1975-03-10", "gender": "Male", "admission_date": "2025-03-28", "primary_provider": "Dr. Michael Chen"},
        {"patient_id": 104, "first_name": "Emily", "last_name": "Davis", "dob": "1988-11-30", "gender": "Female", "admission_date": "2025-04-01", "primary_provider": "Dr. James Wilson"},
        {"patient_id": 105, "first_name": "William", "last_name": "Johnson", "dob": "1965-07-19", "gender": "Male", "admission_date": "2025-04-05", "primary_provider": "Dr. Michael Chen"},
        {"patient_id": 108, "first_name": "William", "last_name": "Wilson", "dob": "1960-07-22", "gender": "Male", "admission_date": "2025-03-15", "primary_provider": "Dr. James Wilson"},
        {"patient_id": 115, "first_name": "James", "last_name": "Walker", "dob": "1972-11-05", "gender": "Male", "admission_date": "2025-03-01", "primary_provider": "Dr. Emily Rodriguez"}
    ]

def get_pathway_steps(pathway_id):
    """Return the steps for a specific pathway"""
    steps_by_pathway = {
        1: [  # Heart Failure Management
            {
                "step_id": 1,
                "step_name": "Initial Assessment",
                "description": "Comprehensive baseline evaluation including vital signs, weight, edema assessment, and symptom evaluation.",
                "status": "COMPLETED",
                "completion_date": "2025-03-25"
            },
            {
                "step_id": 2,
                "step_name": "Medication Reconciliation",
                "description": "Review and adjust medications based on current status and symptoms. Ensure compliance with heart failure regimen.",
                "status": "COMPLETED",
                "completion_date": "2025-04-01"
            },
            {
                "step_id": 3,
                "step_name": "Dietary Counseling",
                "description": "Sodium restriction education and fluid management guidance. Referral to nutritionist if needed.",
                "status": "IN_PROGRESS",
                "completion_date": None
            },
            {
                "step_id": 4,
                "step_name": "Activity Planning",
                "description": "Establish appropriate exercise regimen based on capacity. Refer to cardiac rehabilitation if appropriate.",
                "status": "NOT_STARTED",
                "completion_date": None
            },
            {
                "step_id": 5,
                "step_name": "Patient Education",
                "description": "Educate on symptom recognition, when to seek medical attention, and medication adherence importance.",
                "status": "NOT_STARTED",
                "completion_date": None
            },
            {
                "step_id": 6,
                "step_name": "Follow-up Schedule",
                "description": "Establish regular follow-up appointments and monitoring plan.",
                "status": "NOT_STARTED",
                "completion_date": None
            }
        ],
        2: [  # Diabetes Care Plan
            {
                "step_id": 1,
                "step_name": "Initial Assessment",
                "description": "Comprehensive evaluation including A1C, blood glucose monitoring, and complication screening.",
                "status": "COMPLETED",
                "completion_date": "2025-02-15"
            },
            # Additional steps would be here
        ],
        3: [  # Post-Surgical Recovery
            {
                "step_id": 1,
                "step_name": "Immediate Post-Op Care",
                "description": "Monitor vital signs, pain management, and wound assessment.",
                "status": "COMPLETED",
                "completion_date": "2025-04-06"
            },
            # Additional steps would be here
        ],
        4: [  # COPD Management
            {
                "step_id": 1,
                "step_name": "Pulmonary Function Assessment",
                "description": "Evaluate current lung function and establish baseline.",
                "status": "COMPLETED",
                "completion_date": "2025-01-20"
            },
            # Additional steps would be here
        ]
    }
    
    # Return default empty list if pathway not found
    return steps_by_pathway.get(pathway_id, [])

def assign_pathway_to_patient(data):
    """Simulate API call to assign pathway to patient"""
    st.success(f"Pathway successfully assigned to patient #{data['patient_id']}")
    return {"status": "success"}

def update_pathway_step(data):
    """Simulate API call to update pathway step status"""
    st.success(f"Pathway step '{data['step_name']}' status updated to {data['status']}")
    return {"status": "success"}

# Main tabs for different views
tab1, tab2, tab3 = st.tabs(["Active Pathways", "Assign Pathway", "Pathway Templates"])

# Tab 1: Active Pathways
with tab1:
    # Filter section
    st.markdown('<div class="filter-controls">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Get patient list for filter
        patients = get_patient_list()
        patient_options = ["All Patients"] + [f"{p['first_name']} {p['last_name']}" for p in patients]
        filter_patient = st.selectbox("Filter by Patient", patient_options)
    
    with col2:
        # Get pathway list for filter
        pathways = get_care_pathways()
        pathway_options = ["All Pathways"] + [p["pathway_name"] for p in pathways]
        filter_pathway = st.selectbox("Filter by Pathway", pathway_options)
    
    with col3:
        filter_status = st.selectbox("Filter by Status", ["All", "ACTIVE", "ON_HOLD", "COMPLETED"])
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Display active pathways
    st.subheader("Active Care Pathways")
    
    # Get pathway data
    patient_pathways = get_patient_pathways()
    
    # Apply filters
    filtered_pathways = patient_pathways
    
    if filter_patient != "All Patients":
        filtered_pathways = [p for p in filtered_pathways if p["patient_name"] == filter_patient]
    
    if filter_pathway != "All Pathways":
        filtered_pathways = [p for p in filtered_pathways if p["pathway_name"] == filter_pathway]
    
    if filter_status != "All":
        filtered_pathways = [p for p in filtered_pathways if p["status"] == filter_status]
    
    # Display pathways
    if filtered_pathways:
        for pathway in filtered_pathways:
            # Determine status class
            status_class = "active" if pathway["status"] == "ACTIVE" else "on-hold" if pathway["status"] == "ON_HOLD" else "completed"
            
            st.markdown(f"""
            <div class="pathway-card">
                <div class="pathway-header">
                    <div class="pathway-title">{pathway['pathway_name']}</div>
                    <div class="status-badge {status_class}">{pathway['status']}</div>
                </div>
                <div class="pathway-meta">
                    <div class="pathway-patient">Patient: {pathway['patient_name']}</div>
                    <div class="pathway-duration">Started: {pathway['start_date']} • Expected End: {pathway['expected_end_date']}</div>
                </div>
                <div class="pathway-progress">
                    <div class="progress-bar" style="width: {pathway['progress']}%;"></div>
                </div>
                <div class="progress-text">{pathway['progress']}% complete • {pathway['steps_completed']}/{pathway['total_steps']} steps</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Button to view pathway details
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button(f"View Details", key=f"view_{pathway['id']}", use_container_width=True):
                    # Store selected pathway in session state
                    st.session_state.selected_pathway = pathway
                    st.session_state.show_pathway_details = True
    else:
        st.info("No pathways match your filter criteria.")
    
    # Display pathway steps if a pathway is selected
    if 'show_pathway_details' in st.session_state and st.session_state.show_pathway_details:
        pathway = st.session_state.selected_pathway
        steps = get_pathway_steps(pathway["pathway_id"])
        
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown(f"### Pathway Details: {pathway['pathway_name']} for {pathway['patient_name']}")
        
        # Display overview
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Progress", f"{pathway['progress']}%")
        
        with col2:
            st.metric("Steps Completed", f"{pathway['steps_completed']}/{pathway['total_steps']}")
        
        with col3:
            # Calculate days remaining
            try:
                end_date = datetime.strptime(pathway['expected_end_date'], '%Y-%m-%d')
                days_remaining = (end_date - datetime.now()).days
                st.metric("Days Remaining", max(0, days_remaining))
            except:
                st.metric("Days Remaining", "N/A")
        
        with col4:
            # Status button
            if pathway["status"] == "ACTIVE":
                if st.button("Put On Hold", use_container_width=True):
                    st.success("Pathway has been put on hold.")
                    # In a real app, this would update the API
            elif pathway["status"] == "ON_HOLD":
                if st.button("Resume Pathway", use_container_width=True):
                    st.success("Pathway has been resumed.")
                    # In a real app, this would update the API
        
        # Display steps
        st.markdown("### Pathway Steps")
        
        if steps:
            for i, step in enumerate(steps):
                # Determine status badge class
                status_class = "step-complete" if step["status"] == "COMPLETED" else "step-in-progress" if step["status"] == "IN_PROGRESS" else "step-not-started"
                status_text = "Complete" if step["status"] == "COMPLETED" else "In Progress" if step["status"] == "IN_PROGRESS" else "Not Started"
                
                # Create step card
                st.markdown(f"""
                <div class="step-card">
                    <div class="step-header">
                        <div class="step-number">{i+1}</div>
                        <div class="step-title">{step['step_name']}</div>
                        <div class="step-status {status_class}">{status_text}</div>
                    </div>
                    <div class="step-body">
                        <div class="step-description">{step['description']}</div>
                        {f"<div>Completed on: {step['completion_date']}</div>" if step['completion_date'] else ""}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Add action buttons based on step status
                col1, col2, col3 = st.columns([1, 1, 2])
                
                with col1:
                    if step["status"] == "NOT_STARTED":
                        if st.button("Mark In Progress", key=f"progress_{step['step_id']}", use_container_width=True):
                            # This would call the API
                            update_data = {
                                "pathway_id": pathway["pathway_id"],
                                "patient_id": pathway["patient_id"],
                                "step_id": step["step_id"],
                                "step_name": step["step_name"],
                                "status": "IN_PROGRESS"
                            }
                            update_pathway_step(update_data)
                    
                    elif step["status"] == "IN_PROGRESS":
                        if st.button("Mark Complete", key=f"complete_{step['step_id']}", use_container_width=True):
                            # This would call the API
                            update_data = {
                                "pathway_id": pathway["pathway_id"],
                                "patient_id": pathway["patient_id"],
                                "step_id": step["step_id"],
                                "step_name": step["step_name"],
                                "status": "COMPLETED"
                            }
                            update_pathway_step(update_data)
                
                with col2:
                    if step["status"] == "COMPLETED":
                        if st.button("Reopen Step", key=f"reopen_{step['step_id']}", use_container_width=True):
                            # This would call the API
                            update_data = {
                                "pathway_id": pathway["pathway_id"],
                                "patient_id": pathway["patient_id"],
                                "step_id": step["step_id"],
                                "step_name": step["step_name"],
                                "status": "IN_PROGRESS"
                            }
                            update_pathway_step(update_data)
        else:
            st.info("No steps found for this pathway.")
        
        # Add notes or documentation section
        st.markdown("### Notes & Documentation")
        
        with st.form("pathway_notes_form"):
            note_text = st.text_area("Add a note to this pathway", height=100)
            note_submit = st.form_submit_button("Save Note")
            
            if note_submit and note_text:
                st.success("Note added successfully.")
                # In a real app, this would save to the API
        
        # Button to close details view
        if st.button("Back to Pathway List", use_container_width=True):
            st.session_state.show_pathway_details = False
            st.experimental_rerun()

# Tab 2: Assign Pathway
with tab2:
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.subheader("Assign Care Pathway to Patient")
    
    with st.form("assign_pathway_form"):
        # Patient selection
        patients = get_patient_list()
        patient_options = [f"{p['first_name']} {p['last_name']} (#{p['patient_id']})" for p in patients]
        selected_patient = st.selectbox("Select Patient", patient_options)
        
        # Extract patient_id from selection
        patient_id = int(selected_patient.split("(#")[1].split(")")[0])
        
        # Pathway selection
        pathways = get_care_pathways()
        pathway_options = [p["pathway_name"] for p in pathways]
        selected_pathway = st.selectbox("Select Care Pathway", pathway_options)
        
        # Find pathway_id for selected pathway
        pathway_id = next((p["pathway_id"] for p in pathways if p["pathway_name"] == selected_pathway), None)
        
        # Start date
        start_date = st.date_input("Start Date", datetime.now())
        
        # Custom duration
        default_duration = next((p["standard_duration"] for p in pathways if p["pathway_name"] == selected_pathway), 90)
        custom_duration = st.number_input("Duration (days)", min_value=1, max_value=365, value=default_duration)
        
        # Calculate expected end date
        end_date = start_date + timedelta(days=custom_duration)
        st.markdown(f"**Expected End Date:** {end_date.strftime('%Y-%m-%d')}")
        
        # Notes
        notes = st.text_area("Notes", placeholder="Enter any notes about this pathway assignment...")
        
        # Submit button
        submit = st.form_submit_button("Assign Pathway")
        
        if submit:
            if not pathway_id:
                st.error("Please select a valid pathway.")
            else:
                # Call API to assign pathway
                assignment_data = {
                    "patient_id": patient_id,
                    "pathway_id": pathway_id,
                    "start_date": start_date.strftime('%Y-%m-%d'),
                    "expected_end_date": end_date.strftime('%Y-%m-%d'),
                    "notes": notes
                }
                
                # This would call the API in a real app
                assign_pathway_to_patient(assignment_data)
                
                # Clear form or redirect
                st.session_state.active_tab = "Active Pathways"
                st.experimental_rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Display existing pathways for the selected patient
    if 'patient_id' in locals():
        patient_pathways = get_patient_pathways()
        patient_existing_pathways = [p for p in patient_pathways if p["patient_id"] == patient_id]
        
        if patient_existing_pathways:
            st.subheader(f"Existing Pathways for {selected_patient.split(' (#')[0]}")
            
            for pathway in patient_existing_pathways:
                status_class = "active" if pathway["status"] == "ACTIVE" else "on-hold" if pathway["status"] == "ON_HOLD" else "completed"
                
                st.markdown(f"""
                <div class="pathway-card">
                    <div class="pathway-header">
                        <div class="pathway-title">{pathway['pathway_name']}</div>
                        <div class="status-badge {status_class}">{pathway['status']}</div>
                    </div>
                    <div class="pathway-meta">
                        <div class="pathway-duration">Started: {pathway['start_date']} • Expected End: {pathway['expected_end_date']}</div>
                    </div>
                    <div class="pathway-progress">
                        <div class="progress-bar" style="width: {pathway['progress']}%;"></div>
                    </div>
                    <div class="progress-text">{pathway['progress']}% complete • {pathway['steps_completed']}/{pathway['total_steps']} steps</div>
                </div>
                """, unsafe_allow_html=True)

# Tab 3: Pathway Templates
with tab3:
    st.subheader("Care Pathway Templates")
    
    # Search and filter
    search_term = st.text_input("Search Templates", placeholder="Enter pathway name or keyword...")
    
    # Get pathway templates
    pathways = get_care_pathways()
    
    # Apply search filter
    if search_term:
        pathways = [p for p in pathways if search_term.lower() in p["pathway_name"].lower() or 
                   search_term.lower() in p["description"].lower()]
    
    # Display pathway templates
    if pathways:
        # Convert to DataFrame for display
        df = pd.DataFrame(pathways)
        
        # Add "View Details" button column
        df["is_active"] = df["is_active"].apply(lambda x: "Active" if x else "Inactive")
        
        # Display in table
        st.dataframe(
            df[["pathway_id", "pathway_name", "description", "standard_duration", "is_active"]],
            column_config={
                "pathway_id": st.column_config.NumberColumn("ID"),
                "pathway_name": st.column_config.TextColumn("Pathway Name"),
                "description": st.column_config.TextColumn("Description"),
                "standard_duration": st.column_config.NumberColumn("Duration (days)"),
                "is_active": st.column_config.TextColumn("Status")
            },
            hide_index=True,
            use_container_width=True
        )
        
        # Allow selecting a pathway to view details
        selected_pathway_id = st.selectbox(
            "Select a pathway to view details",
            options=[p["pathway_id"] for p in pathways],
            format_func=lambda x: next((p["pathway_name"] for p in pathways if p["pathway_id"] == x), "")
        )
        
        if st.button("View Pathway Details"):
            # Get the selected pathway
            selected_pathway = next((p for p in pathways if p["pathway_id"] == selected_pathway_id), None)
            
            if selected_pathway:
                # Get the steps for this pathway
                steps = get_pathway_steps(selected_pathway_id)
                
                # Display pathway info
                st.markdown(f"### {selected_pathway['pathway_name']}")
                st.markdown(f"**Description:** {selected_pathway['description']}")
                st.markdown(f"**Standard Duration:** {selected_pathway['standard_duration']} days")
                st.markdown(f"**Status:** {'Active' if selected_pathway['is_active'] else 'Inactive'}")
                
                # Display steps
                st.markdown("### Pathway Steps")
                
                if steps:
                    for i, step in enumerate(steps):
                        st.markdown(f"**Step {i+1}: {step['step_name']}**")
                        st.markdown(f"{step['description']}")
                        st.markdown("---")
                else:
                    st.info("No steps defined for this pathway.")
                
                # Assign button
                if st.button("Assign This Pathway", use_container_width=True):
                    # Switch to assign tab
                    st.session_state.active_tab = "Assign Pathway"
                    st.experimental_rerun()
    else:
        st.info("No pathway templates match your search.")
    
    # Button to create new pathway template (would require admin privileges)
    if st.button("Request New Pathway Template", use_container_width=True):
        st.info("Feature not available in demo. In a real application, this would allow requesting new pathway templates from administrators.")

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Care Pathway Management")
