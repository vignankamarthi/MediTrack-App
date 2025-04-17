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
    page_title="Nurse Dashboard | MediTrack", page_icon="🏥", layout="wide"
)

# Authentication check
if "is_authenticated" not in st.session_state or not st.session_state.is_authenticated:
    st.switch_page("Home.py")
elif "role" not in st.session_state or st.session_state.role != "nurse":
    st.warning("You don't have permission to access this page.")
    st.switch_page("Home.py")

# Display sidebar navigation
SideBarLinks(st.session_state.role)

# Custom CSS for styling
st.markdown("""
<style>
    .patient-card {
        padding: 20px;
        border-radius: 8px;
        background-color: white;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
    }
    .patient-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
    }
    .patient-name {
        font-weight: bold;
        font-size: 18px;
    }
    .patient-id {
        color: #95aac9;
    }
    .patient-details {
        display: flex;
        gap: 10px;
    }
    .patient-item {
        padding: 5px 10px;
        background-color: #f5f8fa;
        border-radius: 5px;
        font-size: 14px;
    }
    .task-card {
        padding: 15px;
        border-radius: 8px;
        background-color: white;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
    }
    .task-header {
        display: flex;
        gap: 10px;
        align-items: center;
        margin-bottom: 5px;
    }
    .priority-indicator {
        width: 12px;
        height: 12px;
        border-radius: 50%;
    }
    .high {
        background-color: #e63757;
    }
    .medium {
        background-color: #f6c343;
    }
    .low {
        background-color: #00d97e;
    }
    .task-title {
        font-weight: 600;
    }
    .task-description {
        color: #95aac9;
        font-size: 14px;
        margin-bottom: 5px;
    }
    .task-meta {
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        color: #95aac9;
    }
    .lab-notification {
        padding: 15px;
        border-radius: 8px;
        background-color: #fff8e7;
        border-left: 4px solid #f6c343;
        margin-bottom: 10px;
    }
    .lab-title {
        font-weight: 600;
        margin-bottom: 5px;
    }
    .lab-details {
        color: #95aac9;
        font-size: 14px;
    }
    .vital-card {
        text-align: center;
        padding: 15px;
        background-color: #f5f8fa;
        border-radius: 8px;
    }
    .vital-value {
        font-size: 24px;
        font-weight: 600;
        margin-bottom: 5px;
    }
    .vital-label {
        color: #95aac9;
        font-size: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Page header
st.title(f"Welcome, Nurse {st.session_state.user_name}")
st.subheader("Nurse Dashboard")

# Quick stats
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Assigned Patients", value="8", delta="2 new today")
with col2:
    st.metric(label="Tasks Due Today", value="12", delta="-3 from yesterday")
with col3:
    st.metric(label="Clinical Pathways", value="5", delta="+1 new")

# Layout for main content
main_col1, main_col2 = st.columns([2, 1])

# Left column - Patient list and tasks
with main_col1:
    # Active patients section
    st.markdown("### Your Assigned Patients")
    
    # Simulated patient data (in a real app this would come from the API)
    patients = [
        {"id": 101, "name": "John Doe", "age": 56, "room": "204A", "admitted_date": "2025-03-20", "condition": "Stable"},
        {"id": 104, "name": "Emily Davis", "age": 35, "room": "210B", "admitted_date": "2025-04-12", "condition": "Improving"},
        {"id": 108, "name": "William Wilson", "age": 67, "room": "215A", "admitted_date": "2025-04-05", "condition": "Needs Attention"},
    ]
    
    # Display each patient card
    for patient in patients:
        st.markdown(f"""
        <div class="patient-card">
            <div class="patient-header">
                <div class="patient-name">{patient['name']}</div>
                <div class="patient-id">ID: {patient['id']}</div>
            </div>
            <div class="patient-details">
                <div class="patient-item">{patient['age']} years</div>
                <div class="patient-item">Room {patient['room']}</div>
                <div class="patient-item">Admitted: {patient['admitted_date']}</div>
                <div class="patient-item">{patient['condition']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # View all patients button
    st.button("View All Patients", use_container_width=True)
    
    # Tasks section
    st.markdown("### Today's Care Tasks")
    
    # Try to fetch real data from API
    try:
        # URL would point to the Flask API running in the container
        # Example: http://web-api:4000/n/care-tasks
        # For now, we'll simulate the API data
        
        # In a real implementation, use requests:
        # response = requests.get("http://web-api:4000/n/care-tasks")
        # if response.status_code == 200:
        #     tasks = response.json()
        
        # Simulated tasks data
        tasks = [
            {"task_id": 1, "task_name": "Administer Medication", "description": "Administer IV antibiotics for patient #101", "priority": "HIGH", "estimated_duration": 15},
            {"task_id": 2, "task_name": "Vital Signs Check", "description": "Record vitals for all assigned patients", "priority": "MEDIUM", "estimated_duration": 30},
            {"task_id": 3, "task_name": "Update Care Documentation", "description": "Complete care notes for morning rounds", "priority": "LOW", "estimated_duration": 20},
            {"task_id": 4, "task_name": "Patient Assessment", "description": "Conduct assessment for new patient #108", "priority": "HIGH", "estimated_duration": 45}
        ]
        
        # Display each task card
        for task in tasks:
            priority_class = "high" if task["priority"] == "HIGH" else "medium" if task["priority"] == "MEDIUM" else "low"
            
            st.markdown(f"""
            <div class="task-card">
                <div class="task-header">
                    <div class="priority-indicator {priority_class}"></div>
                    <div class="task-title">{task["task_name"]}</div>
                </div>
                <div class="task-description">{task["description"]}</div>
                <div class="task-meta">
                    <div>Priority: {task["priority"]}</div>
                    <div>Est. Duration: {task["estimated_duration"]} min</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    except Exception as e:
        st.error(f"Could not load tasks data: {str(e)}")
    
    # Links to care management pages
    st.page_link("pages/12_Care_Tasks.py", label="Manage Care Tasks", icon="📋")
    st.page_link("pages/13_Patient_Symptoms.py", label="View Patient Symptoms", icon="🤒")
    st.page_link("pages/16_Care_Pathway_Management.py", label="Manage Care Pathways", icon="🛤️")

# Right column - Lab results and quick actions
with main_col2:
    # Critical lab results
    st.markdown("### Critical Lab Notifications")
    
    # Try to fetch real data from API
    try:
        # Simulated lab results (in a real app, this would come from the API)
        lab_results = [
            {"patient_id": 101, "patient_name": "John Doe", "test_name": "Potassium Level", "result_value": "5.8 mEq/L", "reference_range": "3.5-5.0 mEq/L", "reported_time": "Today, 9:15 AM"},
            {"patient_id": 104, "patient_name": "Emily Davis", "test_name": "WBC Count", "result_value": "15,500/μL", "reference_range": "4,500-11,000/μL", "reported_time": "Today, 8:30 AM"},
            {"patient_id": 108, "patient_name": "William Wilson", "test_name": "Blood Glucose", "result_value": "243 mg/dL", "reference_range": "70-140 mg/dL", "reported_time": "Just now"}
        ]
        
        # Display each lab notification
        for lab in lab_results:
            st.markdown(f"""
            <div class="lab-notification">
                <div class="lab-title">{lab['test_name']}: {lab['result_value']}</div>
                <div class="lab-details">
                    <p>Patient: {lab['patient_name']} (#{lab['patient_id']})</p>
                    <p>Above normal range ({lab['reference_range']})</p>
                    <p>Reported: {lab['reported_time']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    except Exception as e:
        st.error(f"Could not load lab results: {str(e)}")
    
    # Link to lab results page
    st.page_link("pages/14_Lab_Results.py", label="View Lab Results", icon="🔬")
    st.page_link("pages/15_Medication_Administration.py", label="Medication Administration", icon="💊")
    
    # Quick Actions
    st.markdown("### Quick Actions")
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("Add Task", use_container_width=True)
        st.button("Log Vital Signs", use_container_width=True)
    with col2:
        st.button("Record Medication", use_container_width=True)
        if st.button("Manage Pathways", use_container_width=True):
            st.switch_page("pages/16_Care_Pathway_Management.py")
    
    # Care pathways section
    st.markdown("### Active Care Pathways")
    
    # Sample pathways data
    pathways = [
        {"patient_id": 101, "patient_name": "John Doe", "pathway_name": "Heart Failure Management", "progress": 35},
        {"patient_id": 104, "patient_name": "Emily Davis", "pathway_name": "Asthma Control Protocol", "progress": 60},
        {"patient_id": 108, "patient_name": "William Wilson", "pathway_name": "Diabetes Care Plan", "progress": 20}
    ]
    
    for pathway in pathways:
        st.markdown(f"""
        <div style="padding: 15px; background-color: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); margin-bottom: 10px;">
            <div style="font-weight: 600; margin-bottom: 5px;">{pathway['pathway_name']}</div>
            <div style="font-size: 14px; color: #95aac9; margin-bottom: 8px;">Patient: {pathway['patient_name']}</div>
            <div style="height: 8px; background-color: #edf2f9; border-radius: 4px; overflow: hidden;">
                <div style="height: 100%; width: {pathway['progress']}%; background-color: #2c7be5;"></div>
            </div>
            <div style="font-size: 12px; color: #95aac9; text-align: right; margin-top: 3px;">{pathway['progress']}% complete</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Link to pathway management page
    st.page_link("pages/16_Care_Pathway_Management.py", label="View All Pathways", icon="🛤️", use_container_width=True)

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Nurse Dashboard")
