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
    page_title="Pharmacist Dashboard | MediTrack", 
    page_icon="🏥", 
    layout="wide"
)

# Authentication check
if "is_authenticated" not in st.session_state or not st.session_state.is_authenticated:
    st.switch_page("Home.py")
elif "role" not in st.session_state or st.session_state.role != "pharmacist":
    st.warning("You don't have permission to access this page.")
    st.switch_page("Home.py")

# Display sidebar navigation
SideBarLinks(st.session_state.role)

# Custom CSS for styling
st.markdown("""
<style>
    .metric-card {
        background-color: white;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }
    .metric-title {
        font-size: 14px;
        color: #95aac9;
        margin-bottom: 10px;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #12263f;
        margin-bottom: 5px;
    }
    .metric-trend-positive {
        color: #00d97e;
        font-size: 12px;
    }
    .metric-trend-negative {
        color: #e63757;
        font-size: 12px;
    }
    .patient-card {
        padding: 15px;
        border-radius: 8px;
        background-color: white;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
    }
    .patient-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
    .patient-name {
        font-weight: 600;
        font-size: 16px;
    }
    .patient-id {
        color: #95aac9;
        font-size: 12px;
    }
    .patient-meds {
        margin-bottom: 10px;
    }
    .med-item {
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        padding: 5px 0;
        border-bottom: 1px solid #f5f8fa;
    }
    .med-name {
        color: #12263f;
    }
    .med-details {
        color: #95aac9;
    }
    .alert-card {
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .alert-high {
        background-color: rgba(230, 55, 87, 0.1);
        border-left: 4px solid #e63757;
    }
    .alert-medium {
        background-color: rgba(246, 195, 67, 0.1);
        border-left: 4px solid #f6c343;
    }
    .alert-title {
        font-weight: 600;
        margin-bottom: 5px;
    }
    .alert-details {
        font-size: 14px;
        color: #12263f;
    }
    .activity-card {
        display: flex;
        padding: 10px;
        border-radius: 5px;
        background-color: white;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        margin-bottom: 8px;
    }
    .activity-icon {
        width: 40px;
        height: 40px;
        border-radius: 8px;
        background-color: #f5f8fa;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-right: 10px;
    }
    .activity-details {
        flex: 1;
    }
    .activity-title {
        font-weight: 500;
        margin-bottom: 3px;
    }
    .activity-time {
        font-size: 12px;
        color: #95aac9;
    }
</style>
""", unsafe_allow_html=True)

# Page header
st.title(f"Welcome, {st.session_state.user_name}")
st.subheader("Pharmacist Dashboard")

# Quick stats
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Medication Reviews</div>
        <div class="metric-value">24</div>
        <div class="metric-trend-positive">+5 from yesterday</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Interactions Detected</div>
        <div class="metric-value">7</div>
        <div class="metric-trend-negative">+2 from yesterday</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Prescriber Messages</div>
        <div class="metric-value">12</div>
        <div class="metric-trend-positive">83% response rate</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Education Sessions</div>
        <div class="metric-value">8</div>
        <div class="metric-trend-positive">100% completed</div>
    </div>
    """, unsafe_allow_html=True)

# Main dashboard content in two columns
col_left, col_right = st.columns([2, 1])

# Left column - Patients needing review
with col_left:
    st.markdown("### Patients Needing Medication Review")
    
    # Mock function to simulate API call (to be replaced with actual API)
    def get_patients_for_review():
        # In a real app, call the API:
        # response = requests.get("http://web-api:4000/ph/medication-records-for-review")
        # return response.json()
        
        # For demo, return mock data
        return [
            {
                "patient_id": 101, 
                "first_name": "John", 
                "last_name": "Doe",
                "medications": [
                    {"name": "Lisinopril", "dosage": "10mg", "frequency": "Once daily", "start_date": "Jan 15, 2025"},
                    {"name": "Metformin", "dosage": "500mg", "frequency": "Twice daily", "start_date": "Dec 10, 2024"},
                    {"name": "Atorvastatin", "dosage": "20mg", "frequency": "Once daily at bedtime", "start_date": "Feb 05, 2025"}
                ],
                "review_status": "Due today"
            },
            {
                "patient_id": 103, 
                "first_name": "Michael", 
                "last_name": "Brown",
                "medications": [
                    {"name": "Levothyroxine", "dosage": "50mcg", "frequency": "Once daily", "start_date": "Jan 03, 2025"},
                    {"name": "Omeprazole", "dosage": "20mg", "frequency": "Once daily", "start_date": "Feb 12, 2025"}
                ],
                "review_status": "Overdue"
            },
            {
                "patient_id": 108, 
                "first_name": "William", 
                "last_name": "Wilson",
                "medications": [
                    {"name": "Amlodipine", "dosage": "5mg", "frequency": "Once daily", "start_date": "Dec 22, 2024"},
                    {"name": "Hydrochlorothiazide", "dosage": "25mg", "frequency": "Once daily", "start_date": "Dec 22, 2024"},
                    {"name": "Warfarin", "dosage": "2mg", "frequency": "Once daily", "start_date": "Jan 10, 2025"}
                ],
                "review_status": "Due tomorrow"
            }
        ]
    
    # Get patient data and display cards
    patients = get_patients_for_review()
    
    for patient in patients:
        st.markdown(f"""
        <div class="patient-card">
            <div class="patient-header">
                <div class="patient-name">{patient['first_name']} {patient['last_name']}</div>
                <div class="patient-id">ID: {patient['patient_id']} | {patient['review_status']}</div>
            </div>
            <div class="patient-meds">
        """, unsafe_allow_html=True)
        
        # Display medications
        for med in patient['medications'][:3]:  # Show first 3 medications
            st.markdown(f"""
            <div class="med-item">
                <span class="med-name">{med['name']} {med['dosage']}</span>
                <span class="med-details">{med['frequency']} | Started: {med['start_date']}</span>
            </div>
            """, unsafe_allow_html=True)
        
        if len(patient['medications']) > 3:
            st.markdown(f"""
            <div class="med-item">
                <span class="med-details">+ {len(patient['medications']) - 3} more medications...</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Review Medications", key=f"review_{patient['patient_id']}", use_container_width=True):
                # Navigate to medication review page with patient ID
                st.session_state.selected_patient_id = patient['patient_id']
                st.switch_page("pages/22_Medication_Review.py")
        with col2:
            st.button(f"View Patient History", key=f"history_{patient['patient_id']}", use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Educational materials section
    st.markdown("### Educational Materials")
    
    # Mock function for education records
    def get_patient_education_records():
        # In a real app, call the API:
        # response = requests.get("http://web-api:4000/ph/patient-education-records")
        # return response.json()
        
        # Return mock data
        return [
            {
                "patient_id": 101, 
                "first_name": "John", 
                "last_name": "Doe", 
                "education_id": 1, 
                "comprehension_level": "Moderate",
                "notes": "Needs follow-up on medication adherence strategies", 
                "education_date": "2025-04-10"
            },
            {
                "patient_id": 104, 
                "first_name": "Emily", 
                "last_name": "Davis", 
                "education_id": 2, 
                "comprehension_level": "High",
                "notes": "Understands medication regimen well", 
                "education_date": "2025-04-12"
            },
            {
                "patient_id": 108, 
                "first_name": "William", 
                "last_name": "Wilson", 
                "education_id": 3, 
                "comprehension_level": "Low",
                "notes": "Needs simplified instructions and visual aids", 
                "education_date": "2025-04-05"
            }
        ]
    
    education_records = get_patient_education_records()
    
    # Display in a table
    if education_records:
        # Create DataFrame
        df = pd.DataFrame(education_records)
        
        # Format for display
        df['patient_name'] = df.apply(lambda row: f"{row['first_name']} {row['last_name']}", axis=1)
        
        # Display table
        st.dataframe(
            df[['patient_name', 'comprehension_level', 'notes', 'education_date']],
            column_config={
                "patient_name": st.column_config.TextColumn("Patient"),
                "comprehension_level": st.column_config.TextColumn("Comprehension"),
                "notes": st.column_config.TextColumn("Notes"),
                "education_date": st.column_config.DateColumn("Date")
            },
            hide_index=True,
            use_container_width=True
        )
    
    # Create new education record button
    if st.button("Create New Education Record", use_container_width=True):
        st.switch_page("pages/25_Patient_Education.py")

# Right column - Alerts and Activities
with col_right:
    # Medication Alerts section
    st.markdown("### Medication Alerts")
    
    # Mock function for medication alerts
    def get_medication_alerts():
        # In a real app, call the API
        # Return mock data for now
        return [
            {
                "level": "high",
                "title": "Significant Interaction Detected",
                "details": "Lipitor (atorvastatin) and Gemfibrozil interaction increases risk of myopathy and rhabdomyolysis.",
                "patient_id": 101
            },
            {
                "level": "medium",
                "title": "Potential Duplicate Therapy",
                "details": "Patient #108 is on two similar antihypertensives (Amlodipine and Nifedipine).",
                "patient_id": 108
            },
            {
                "level": "medium",
                "title": "Adherence Concern",
                "details": "Patient #103 has not picked up Levothyroxine refill for 5 days.",
                "patient_id": 103
            }
        ]
    
    alerts = get_medication_alerts()
    
    for alert in alerts:
        alert_class = "alert-high" if alert["level"] == "high" else "alert-medium"
        st.markdown(f"""
        <div class="alert-card {alert_class}">
            <div class="alert-title">{alert["title"]}</div>
            <div class="alert-details">{alert["details"]}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Action button based on alert level
        if alert["level"] == "high":
            if st.button("Address Immediately", key=f"alert_high_{alert['patient_id']}", use_container_width=True):
                st.session_state.selected_patient_id = alert['patient_id']
                st.switch_page("pages/22_Medication_Review.py")
        else:
            if st.button("Review Issue", key=f"alert_med_{alert['patient_id']}", use_container_width=True):
                st.session_state.selected_patient_id = alert['patient_id']
                st.switch_page("pages/22_Medication_Review.py")
    
    # Recent Activity section
    st.markdown("### Recent Activity")
    
    activities = [
        {
            "icon": "💊",
            "title": "Updated dosage for William Wilson's Amlodipine",
            "time": "10 minutes ago"
        },
        {
            "icon": "📝",
            "title": "Completed medication review for Emily Davis",
            "time": "1 hour ago"
        },
        {
            "icon": "💬",
            "title": "Received message from Dr. James Wilson",
            "time": "2 hours ago"
        },
        {
            "icon": "📋",
            "title": "Created education record for Michael Brown",
            "time": "Yesterday, 3:45 PM"
        },
        {
            "icon": "⚠️",
            "title": "Resolved drug interaction alert for John Doe",
            "time": "Yesterday, 2:30 PM"
        }
    ]
    
    for activity in activities:
        st.markdown(f"""
        <div class="activity-card">
            <div class="activity-icon">{activity['icon']}</div>
            <div class="activity-details">
                <div class="activity-title">{activity['title']}</div>
                <div class="activity-time">{activity['time']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Upcoming tasks
    st.markdown("### Upcoming Tasks")
    
    tasks = [
        "Complete medication reconciliation for 3 patients",
        "Review prescription outcomes for today's patients",
        "Follow up on education session with patient #108",
        "Respond to Dr. Wilson's message about Lipitor dosage",
        "Prepare monthly medication usage report"
    ]
    
    for i, task in enumerate(tasks):
        st.checkbox(task, key=f"task_{i}")

# Quick access buttons at the bottom
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.page_link("pages/22_Medication_Review.py", label="Medication Review", icon="💊", use_container_width=True)

with col2:
    st.page_link("pages/23_Prescription_Outcomes.py", label="Prescription Outcomes", icon="📋", use_container_width=True)

with col3:
    st.page_link("pages/24_Medication_Reconciliation.py", label="Medication Reconciliation", icon="✅", use_container_width=True)

with col4:
    st.page_link("pages/25_Patient_Education.py", label="Patient Education", icon="📚", use_container_width=True)

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Pharmacist Dashboard")
