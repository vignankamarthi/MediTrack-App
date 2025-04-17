import streamlit as st
import sys
import os
import pandas as pd
from datetime import datetime, timedelta

# Add the modules directory to the path so we can import the nav module
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "modules"))
from nav import SideBarLinks

# Page configuration
st.set_page_config(
    page_title="Patient Education | MediTrack", 
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
    
    .education-record {
        border-left: 3px solid #2c7be5;
        padding: 15px;
        border-radius: 5px;
        background-color: #f9fbfd;
        margin-bottom: 15px;
    }
    
    .record-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
    }
    
    .record-title {
        font-weight: 600;
        color: #12263f;
    }
    
    .record-meta {
        font-size: 12px;
        color: #95aac9;
    }
    
    .comprehension-badge {
        padding: 3px 8px;
        border-radius: 10px;
        font-size: 12px;
        font-weight: 500;
    }
    
    .high {
        background-color: #e4f7ed;
        color: #00d97e;
    }
    
    .moderate {
        background-color: #fff8e7;
        color: #f6c343;
    }
    
    .low {
        background-color: #fae7eb;
        color: #e63757;
    }
    
    .material-card {
        padding: 15px;
        border-radius: 8px;
        background-color: white;
        border: 1px solid #edf2f9;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .material-icon {
        width: 40px;
        height: 40px;
        background-color: #f5f8fa;
        border-radius: 8px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 20px;
    }
    
    .material-info {
        flex: 1;
    }
    
    .material-title {
        font-weight: 500;
        color: #12263f;
        margin-bottom: 5px;
    }
    
    .material-description {
        font-size: 12px;
        color: #95aac9;
    }
</style>
""", unsafe_allow_html=True)

# Page header
st.title("Patient Education")
st.subheader("Create and manage patient education materials")

# Function to get patient data
def get_patients():
    """Get a list of patients"""
    # In a real app, this would call an API endpoint
    # Here we're using mock data for demonstration
    
    patients = [
        {"patient_id": 101, "first_name": "John", "last_name": "Doe", "dob": "1968-05-15", "gender": "Male"},
        {"patient_id": 102, "first_name": "Sarah", "last_name": "Smith", "dob": "1992-08-22", "gender": "Female"},
        {"patient_id": 103, "first_name": "Michael", "last_name": "Brown", "dob": "1975-03-10", "gender": "Male"},
        {"patient_id": 104, "first_name": "Emily", "last_name": "Davis", "dob": "1988-11-30", "gender": "Female"},
        {"patient_id": 108, "first_name": "William", "last_name": "Wilson", "dob": "1965-07-19", "gender": "Male"}
    ]
    
    return patients

# Function to get patient education records
def get_education_records():
    """Get education records for patients"""
    # In a real app, this would call:
    # response = requests.get("http://web-api:4000/ph/patient-education-records")
    # return response.json()
    
    # Return mock data
    return [
        {
            "education_id": 1,
            "patient_id": 101,
            "patient_name": "John Doe",
            "education_type": "Medication Instructions",
            "comprehension_level": "Moderate",
            "education_date": "2025-04-10",
            "provider": "Sarah Chen, PharmD",
            "notes": "Reviewed proper administration of insulin. Patient demonstrated moderate understanding of injection technique. Provided additional visual aids and scheduled follow-up."
        },
        {
            "education_id": 2,
            "patient_id": 104,
            "patient_name": "Emily Davis",
            "education_type": "Disease Management",
            "comprehension_level": "High",
            "education_date": "2025-04-12",
            "provider": "Sarah Chen, PharmD",
            "notes": "Discussed asthma triggers and proper inhaler use. Patient showed excellent comprehension and was able to demonstrate correct technique."
        },
        {
            "education_id": 3,
            "patient_id": 108,
            "patient_name": "William Wilson",
            "education_type": "Medication Side Effects",
            "comprehension_level": "Low",
            "education_date": "2025-04-05",
            "provider": "Sarah Chen, PharmD",
            "notes": "Reviewed potential side effects of warfarin therapy. Patient had difficulty recalling important information. Simplified instructions and provided written materials with large text."
        }
    ]

# Function to get educational materials
def get_educational_materials():
    """Get available educational materials"""
    return [
        {
            "material_id": 1,
            "title": "Understanding Your Blood Pressure Medication",
            "type": "Brochure",
            "format": "PDF",
            "target_conditions": ["Hypertension"],
            "description": "Illustrated guide explaining how blood pressure medications work and proper administration."
        },
        {
            "material_id": 2,
            "title": "Diabetes Self-Management",
            "type": "Video Series",
            "format": "Online",
            "target_conditions": ["Diabetes"],
            "description": "Series of short videos covering glucose monitoring, insulin administration, and diet management."
        },
        {
            "material_id": 3,
            "title": "Managing Your Cholesterol",
            "type": "Handout",
            "format": "PDF",
            "target_conditions": ["Hyperlipidemia"],
            "description": "Explanation of cholesterol levels, medication information, and lifestyle recommendations."
        },
        {
            "material_id": 4,
            "title": "Heart Failure Care",
            "type": "Booklet",
            "format": "Print",
            "target_conditions": ["Heart Failure"],
            "description": "Comprehensive guide to managing heart failure, including medication schedules, fluid restrictions, and warning signs."
        },
        {
            "material_id": 5,
            "title": "Medication Calendar Template",
            "type": "Tool",
            "format": "Print",
            "target_conditions": ["Multiple Medications"],
            "description": "Customizable calendar for tracking multiple medication schedules."
        }
    ]

# Function to create a new education record
def create_education_record(data):
    """Simulate creating a new education record
    
    In a real app, this would call:
    response = requests.post("http://web-api:4000/ph/patient-education", json=data)
    return response.json()
    """
    return {"message": "Education record created successfully", "education_id": 4}

# Function to create patient-education relationship
def create_patient_education_relationship(data):
    """Simulate creating a patient-education relationship
    
    In a real app, this would call:
    response = requests.post("http://web-api:4000/ph/patient-education-records", json=data)
    return response.json()
    """
    return {"message": "Patient education relationship created successfully"}

# Get data for the page
patients = get_patients()
education_records = get_education_records()
educational_materials = get_educational_materials()

# Layout the page with tabs
tab1, tab2, tab3 = st.tabs(["Education Records", "Create New Record", "Education Materials"])

# Tab 1: Education Records
with tab1:
    # Filters for education records
    st.markdown("### Patient Education Records")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        patient_filter = st.selectbox(
            "Filter by Patient",
            ["All Patients"] + [f"{p['first_name']} {p['last_name']}" for p in patients]
        )
    
    with col2:
        comprehension_filter = st.selectbox(
            "Filter by Comprehension",
            ["All Levels", "High", "Moderate", "Low"]
        )
    
    with col3:
        date_range = st.selectbox(
            "Date Range",
            ["Last 7 Days", "Last 30 Days", "Last 90 Days", "All Time"]
        )
    
    # Apply filters
    filtered_records = education_records
    if patient_filter != "All Patients":
        filtered_records = [record for record in filtered_records if record["patient_name"] == patient_filter]
    
    if comprehension_filter != "All Levels":
        filtered_records = [record for record in filtered_records if record["comprehension_level"].lower() == comprehension_filter.lower()]
    
    # Display records
    if filtered_records:
        for record in filtered_records:
            # Set comprehension badge class
            badge_class = "moderate"
            if record["comprehension_level"].lower() == "high":
                badge_class = "high"
            elif record["comprehension_level"].lower() == "low":
                badge_class = "low"
            
            st.markdown(f"""
            <div class="education-record">
                <div class="record-header">
                    <div class="record-title">{record["education_type"]} - {record["patient_name"]}</div>
                    <div class="record-meta">
                        <span class="comprehension-badge {badge_class}">{record["comprehension_level"]}</span>
                    </div>
                </div>
                <div>
                    <div class="record-meta">Date: {record["education_date"]} • Provider: {record["provider"]}</div>
                    <p>{record["notes"]}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Action buttons
            col1, col2 = st.columns(2)
            with col1:
                st.button("Edit Record", key=f"edit_{record['education_id']}", use_container_width=True)
            with col2:
                st.button("View Patient History", key=f"view_{record['education_id']}", use_container_width=True)
    else:
        st.info("No education records match your filters.")

# Tab 2: Create New Record
with tab2:
    st.markdown("### Create New Education Record")
    
    with st.form("education_form"):
        # Patient selection
        patient_options = [f"{p['first_name']} {p['last_name']} (ID: {p['patient_id']})" for p in patients]
        selected_patient = st.selectbox("Select Patient", patient_options)
        
        # Extract patient ID from selection
        patient_id = int(selected_patient.split("ID: ")[1].split(")")[0])
        
        # Education type
        education_type = st.selectbox(
            "Education Type",
            ["Medication Instructions", "Disease Management", "Medication Side Effects", "Lifestyle Modifications", "Other"]
        )
        
        # Educational materials
        st.markdown("#### Educational Materials Provided")
        material_cols = st.columns(2)
        material_selections = {}
        
        for i, material in enumerate(educational_materials[:4]):  # Display up to 4 materials
            col_idx = i % 2
            with material_cols[col_idx]:
                material_selections[material["material_id"]] = st.checkbox(
                    f"{material['title']} ({material['type']})",
                    key=f"material_{material['material_id']}"
                )
        
        # Comprehension assessment
        st.markdown("#### Patient Comprehension Assessment")
        comprehension = st.radio(
            "Patient demonstrated understanding:",
            ["High", "Moderate", "Low"],
            horizontal=True
        )
        
        # Notes
        st.markdown("#### Education Notes")
        notes = st.text_area(
            "Notes",
            placeholder="Enter details about the education session, including topics covered, patient questions, and follow-up plans..."
        )
        
        # Follow-up
        st.markdown("#### Follow-up Plan")
        followup_needed = st.checkbox("Follow-up needed")
        
        if followup_needed:
            followup_date = st.date_input(
                "Follow-up Date",
                datetime.now() + timedelta(days=14)
            )
            followup_type = st.selectbox(
                "Follow-up Type",
                ["In-person", "Phone", "Video Call"]
            )
        
        # Submit button
        submit = st.form_submit_button("Create Education Record")
        
        if submit:
            # Prepare data for API call
            education_data = {
                "patient_id": patient_id,
                "education_type": education_type,
                "comprehension_level": comprehension,
                "notes": notes,
                "follow_up_needed": followup_needed,
                "materials": [mid for mid, selected in material_selections.items() if selected]
            }
            
            if followup_needed:
                education_data["followup_date"] = followup_date.strftime("%Y-%m-%d")
                education_data["followup_type"] = followup_type
            
            # Create record (would call API in real app)
            response = create_education_record(education_data)
            
            # Show success message
            st.success("Education record created successfully!")
            
            # In a real app, you might want to clear the form or redirect to the records list
            st.experimental_rerun()

# Tab 3: Education Materials
with tab3:
    st.markdown("### Available Education Materials")
    
    # Filter for materials
    material_filter = st.selectbox(
        "Filter by Condition",
        ["All Conditions"] + list(set(sum([m["target_conditions"] for m in educational_materials], [])))
    )
    
    # Apply filter
    filtered_materials = educational_materials
    if material_filter != "All Conditions":
        filtered_materials = [m for m in filtered_materials if material_filter in m["target_conditions"]]
    
    # Display materials
    for material in filtered_materials:
        st.markdown(f"""
        <div class="material-card">
            <div class="material-icon">{"📄" if material["type"] == "Brochure" or material["type"] == "Handout" else "📹" if material["type"] == "Video Series" else "📚" if material["type"] == "Booklet" else "🔧"}</div>
            <div class="material-info">
                <div class="material-title">{material["title"]}</div>
                <div class="material-description">{material["type"]} • {material["format"]} • For: {", ".join(material["target_conditions"])}</div>
                <div>{material["description"]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Add new material section
    st.markdown("### Add New Educational Material")
    
    with st.form("add_material_form"):
        material_title = st.text_input("Title")
        
        col1, col2 = st.columns(2)
        with col1:
            material_type = st.selectbox(
                "Type",
                ["Brochure", "Video Series", "Handout", "Booklet", "Tool", "App", "Website"]
            )
        
        with col2:
            material_format = st.selectbox(
                "Format",
                ["PDF", "Print", "Online", "Video", "Audio", "Interactive"]
            )
        
        material_description = st.text_area("Description")
        
        material_conditions = st.multiselect(
            "Target Conditions",
            ["Hypertension", "Diabetes", "Hyperlipidemia", "Heart Failure", "Asthma", "COPD", 
             "Depression", "Anxiety", "Pain Management", "Osteoporosis", "Multiple Medications"]
        )
        
        material_file = st.file_uploader("Upload Material", type=["pdf", "docx", "mp4", "jpg", "png"])
        
        if st.form_submit_button("Add Material"):
            if material_title and material_description and material_conditions:
                st.success("Educational material added successfully!")
            else:
                st.error("Please fill in all required fields.")

# Quick action buttons at the bottom
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.page_link("pages/22_Medication_Review.py", label="Medication Review", icon="💊", use_container_width=True)

with col2:
    st.page_link("pages/23_Prescription_Outcomes.py", label="Prescription Outcomes", icon="📋", use_container_width=True)

with col3:
    st.page_link("pages/24_Medication_Reconciliation.py", label="Medication Reconciliation", icon="✅", use_container_width=True)

with col4:
    st.page_link("pages/21_Pharmacist_Home.py", label="Back to Dashboard", icon="🏠", use_container_width=True)

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Patient Education Management")
