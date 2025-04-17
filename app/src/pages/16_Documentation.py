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
    page_title="Documentation | MediTrack", 
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
    .doc-container {
        background-color: white;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    .doc-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
        padding-bottom: 10px;
        border-bottom: 1px solid #edf2f9;
    }
    
    .doc-title {
        font-size: 18px;
        font-weight: 600;
        color: #12263f;
    }
    
    .doc-meta {
        display: flex;
        gap: 20px;
        color: #95aac9;
        font-size: 14px;
    }
    
    .doc-content {
        margin-bottom: 20px;
        color: #12263f;
        line-height: 1.6;
    }
    
    .doc-tags {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
    }
    
    .doc-tag {
        background-color: #f9fafc;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        color: #2c7be5;
    }
    
    .patient-info {
        margin-bottom: 20px;
    }
    
    .patient-header {
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 10px;
        color: #12263f;
    }
    
    .patient-details {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 10px;
    }
    
    .patient-detail {
        display: flex;
        flex-direction: column;
    }
    
    .detail-label {
        font-size: 12px;
        color: #95aac9;
    }
    
    .detail-value {
        font-weight: 500;
        color: #12263f;
    }
    
    .template-item {
        background-color: #f9fafc;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
        cursor: pointer;
    }
    
    .template-item:hover {
        background-color: #edf2f9;
    }
    
    .template-title {
        font-weight: 600;
        margin-bottom: 5px;
        color: #12263f;
    }
    
    .template-desc {
        font-size: 14px;
        color: #95aac9;
    }
    
    .badge {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
    }
    
    .badge-blue {
        background-color: rgba(44, 123, 229, 0.1);
        color: #2c7be5;
    }
    
    .badge-green {
        background-color: rgba(0, 217, 126, 0.1);
        color: #00d97e;
    }
    
    .badge-yellow {
        background-color: rgba(246, 195, 67, 0.1);
        color: #f6c343;
    }
    
    .doc-form-section {
        margin-bottom: 20px;
    }
    
    .form-header {
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 10px;
        color: #12263f;
    }
</style>
""", unsafe_allow_html=True)

# Mock API functions for demo purposes
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

def get_note_templates():
    """Return a list of note templates"""
    return [
        {
            "template_id": 1,
            "template_name": "Shift Change Report",
            "category": "Handoff",
            "description": "Comprehensive shift change documentation including patient status, medications, and care plan updates.",
            "content": """
# SHIFT CHANGE REPORT

## Patient Status
- Vital signs:
- Pain level (0-10):
- Mental status:
- Notable changes since last shift:

## Medications
- Administered during shift:
- Due in next shift:
- PRN medications given:

## Care Plan Updates
- Tasks completed:
- Pending tasks:
- New orders:

## Additional Notes

"""
        },
        {
            "template_id": 2,
            "template_name": "Wound Assessment",
            "category": "Assessment",
            "description": "Detailed wound assessment including size, appearance, drainage, and treatment.",
            "content": """
# WOUND ASSESSMENT

## Wound Characteristics
- Location:
- Size (length x width x depth):
- Wound bed appearance:
- Periwound skin:
- Drainage (amount, color, odor):
- Pain level (0-10):

## Treatment
- Cleaning method:
- Dressing applied:
- Frequency of dressing change:

## Assessment
- Healing progress:
- Complications:
- Interventions:

## Plan
- Next assessment date:
- Changes to treatment plan:

"""
        },
        {
            "template_id": 3,
            "template_name": "Patient Education",
            "category": "Education",
            "description": "Documentation of patient education provided, comprehension, and follow-up needs.",
            "content": """
# PATIENT EDUCATION RECORD

## Education Topic
- Subject:
- Materials provided:
- Teaching method:

## Patient Response
- Comprehension level:
- Questions asked:
- Demonstrated skills:

## Follow-up
- Reinforcement needed:
- Next education session:
- Family/caregiver involvement:

## Additional Notes

"""
        },
        {
            "template_id": 4,
            "template_name": "Pain Assessment",
            "category": "Assessment",
            "description": "Comprehensive pain assessment including location, severity, quality, and interventions.",
            "content": """
# PAIN ASSESSMENT

## Pain Characteristics
- Location:
- Severity (0-10):
- Quality (sharp, dull, throbbing, etc.):
- Onset:
- Duration:
- Aggravating factors:
- Relieving factors:

## Interventions
- Medications given:
- Non-pharmacological interventions:
- Effectiveness:

## Plan
- Next assessment time:
- Changes to pain management:

## Additional Notes

"""
        },
        {
            "template_id": 5,
            "template_name": "Fall Risk Assessment",
            "category": "Assessment",
            "description": "Evaluation of patient's risk for falls including history, medications, and environmental factors.",
            "content": """
# FALL RISK ASSESSMENT

## Risk Factors
- History of falls:
- Medications increasing risk:
- Mobility status:
- Cognitive status:
- Elimination needs:
- Environmental hazards:

## Interventions
- Fall precautions implemented:
- Patient/family education provided:
- Assistive devices:

## Risk Level
- Score:
- Risk category (Low, Moderate, High):

## Plan
- Next assessment date:
- Additional interventions needed:

"""
        }
    ]

def get_patient_documentation(patient_id):
    """Return documentation for a specific patient"""
    # In a real app, this would call an API
    
    docs_by_patient = {
        101: [
            {
                "doc_id": 1,
                "title": "Medication Administration",
                "date": "2025-04-15",
                "time": "08:15 AM",
                "author": "Maria Rodriguez, RN",
                "content": "Administered Lisinopril 10mg and Metformin 500mg as scheduled. Patient tolerated well with no adverse reactions. Blood pressure measured at 130/82 mmHg.",
                "tags": ["Medication", "Vital Signs"]
            },
            {
                "doc_id": 2,
                "title": "Wound Care",
                "date": "2025-04-14",
                "time": "02:30 PM",
                "author": "Maria Rodriguez, RN",
                "content": "Changed dressing on right lower extremity wound. Wound measures 2.5cm x 1.8cm x 0.3cm. Minimal serous drainage noted. Wound bed is pink with granulation tissue forming. Periwound skin intact without maceration. Applied silver alginate dressing and secured with gauze wrap. Patient reported pain level of 2/10 during procedure.",
                "tags": ["Wound Care", "Assessment"]
            },
            {
                "doc_id": 3,
                "title": "Patient Education",
                "date": "2025-04-13",
                "time": "11:45 AM",
                "author": "Maria Rodriguez, RN",
                "content": "Provided education on heart failure self-management. Covered topics included daily weight monitoring, low sodium diet (< 2g/day), and medication adherence. Patient demonstrated understanding by correctly explaining when to call provider based on weight gain and symptom changes. Provided printed materials for reference.",
                "tags": ["Education", "Heart Failure"]
            }
        ],
        104: [
            {
                "doc_id": 4,
                "title": "Respiratory Assessment",
                "date": "2025-04-16",
                "time": "10:00 AM",
                "author": "Maria Rodriguez, RN",
                "content": "Patient reports mild shortness of breath with exertion. Respirations 18/min, unlabored. Lung sounds clear in all fields. O2 saturation 96% on room air. Using incentive spirometer every hour while awake, achieving 1500ml consistently.",
                "tags": ["Assessment", "Respiratory"]
            },
            {
                "doc_id": 5,
                "title": "Pain Assessment",
                "date": "2025-04-15",
                "time": "03:15 PM",
                "author": "Maria Rodriguez, RN",
                "content": "Patient reports pain of 5/10 in surgical site. Describes as sharp with movement, dull at rest. Administered ibuprofen 400mg PO as ordered. Repositioned patient and applied ice pack. Reassessed after 45 minutes - pain reduced to 2/10.",
                "tags": ["Assessment", "Pain Management"]
            }
        ]
    }
    
    return docs_by_patient.get(patient_id, [])

def create_documentation(data):
    """Simulate creating a new documentation entry"""
    st.success("Documentation created successfully!")
    return {"status": "success", "doc_id": 101}  # Would be a real ID in API response

# Page title
st.title("Documentation")
st.subheader("Create and manage patient documentation")

# Main tabs
tab1, tab2 = st.tabs(["Create Documentation", "View Documentation"])

# Tab 1: Create Documentation
with tab1:
    st.markdown('<div class="doc-container">', unsafe_allow_html=True)
    
    # Form for creating documentation
    with st.form("create_documentation_form"):
        # Patient selection
        st.markdown('<div class="doc-form-section">', unsafe_allow_html=True)
        st.markdown('<div class="form-header">Patient Information</div>', unsafe_allow_html=True)
        
        patients = get_patient_list()
        patient_options = [f"{p['first_name']} {p['last_name']} (#{p['patient_id']})" for p in patients]
        selected_patient = st.selectbox("Select Patient", patient_options)
        
        # Extract patient_id from selection
        patient_id = int(selected_patient.split("(#")[1].split(")")[0])
        
        # Show patient details
        selected_patient_obj = next((p for p in patients if p["patient_id"] == patient_id), None)
        if selected_patient_obj:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"**DOB:** {selected_patient_obj['dob']}")
            
            with col2:
                st.markdown(f"**Gender:** {selected_patient_obj['gender']}")
            
            with col3:
                st.markdown(f"**Provider:** {selected_patient_obj['primary_provider']}")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Documentation details
        st.markdown('<div class="doc-form-section">', unsafe_allow_html=True)
        st.markdown('<div class="form-header">Documentation Details</div>', unsafe_allow_html=True)
        
        # Get templates
        templates = get_note_templates()
        
        # Documentation type/template selection
        documentation_type = st.radio(
            "Documentation Type",
            ["Free-form Note", "Use Template"],
            horizontal=True
        )
        
        if documentation_type == "Use Template":
            # Template selection
            template_categories = list(set([t["category"] for t in templates]))
            selected_category = st.selectbox("Select Category", ["All Categories"] + template_categories)
            
            # Filter templates by category
            filtered_templates = templates
            if selected_category != "All Categories":
                filtered_templates = [t for t in templates if t["category"] == selected_category]
            
            # Display templates as selectable items
            selected_template_id = st.selectbox(
                "Select a Template",
                options=[t["template_id"] for t in filtered_templates],
                format_func=lambda x: next((t["template_name"] for t in filtered_templates if t["template_id"] == x), "")
            )
            
            # Get the selected template
            selected_template = next((t for t in templates if t["template_id"] == selected_template_id), None)
            
            if selected_template:
                st.info(f"Template: {selected_template['template_name']} - {selected_template['description']}")
                title = st.text_input("Documentation Title", value=selected_template["template_name"])
                content = st.text_area("Documentation Content", value=selected_template["content"], height=400)
        else:
            # Free-form note
            title = st.text_input("Documentation Title", placeholder="Enter title...")
            content = st.text_area("Documentation Content", placeholder="Enter documentation content...", height=400)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Additional metadata
        st.markdown('<div class="doc-form-section">', unsafe_allow_html=True)
        st.markdown('<div class="form-header">Additional Information</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            doc_date = st.date_input("Date", datetime.now())
        
        with col2:
            doc_time = st.time_input("Time", datetime.now().time())
        
        # Tags input
        tags_input = st.text_input("Tags (comma-separated)", placeholder="E.g., Assessment, Wound Care, Education")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Submit button
        submit = st.form_submit_button("Save Documentation")
        
        if submit:
            if not title:
                st.error("Documentation title is required.")
            elif not content:
                st.error("Documentation content is required.")
            else:
                # Parse tags
                tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else []
                
                # Prepare data for API call
                doc_data = {
                    "patient_id": patient_id,
                    "title": title,
                    "content": content,
                    "date": doc_date.strftime('%Y-%m-%d'),
                    "time": doc_time.strftime('%H:%M:%S'),
                    "author": f"{st.session_state.user_name}, RN",  # Using session state user name
                    "tags": tags
                }
                
                # Call API (simulated)
                result = create_documentation(doc_data)
                
                # In a real app, this would redirect to the view page or clear the form
    
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 2: View Documentation
with tab2:
    st.markdown('<div class="doc-container">', unsafe_allow_html=True)
    
    # Patient selection for viewing
    patients = get_patient_list()
    patient_options = [f"{p['first_name']} {p['last_name']} (#{p['patient_id']})" for p in patients]
    selected_patient = st.selectbox("Select Patient", patient_options, key="view_patient")
    
    # Extract patient_id from selection
    patient_id = int(selected_patient.split("(#")[1].split(")")[0])
    
    # Get documentation for selected patient
    documentation = get_patient_documentation(patient_id)
    
    # Search and filter
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search_term = st.text_input("Search Documentation", placeholder="Enter keywords...")
    
    with col2:
        sort_order = st.selectbox("Sort By", ["Newest First", "Oldest First"])
    
    # Apply search filter
    if search_term:
        documentation = [doc for doc in documentation if 
                       search_term.lower() in doc["title"].lower() or 
                       search_term.lower() in doc["content"].lower() or
                       any(search_term.lower() in tag.lower() for tag in doc["tags"])]
    
    # Apply sorting
    if sort_order == "Newest First":
        documentation = sorted(documentation, key=lambda x: (x["date"], x["time"]), reverse=True)
    else:
        documentation = sorted(documentation, key=lambda x: (x["date"], x["time"]))
    
    # Display documentation
    if documentation:
        for doc in documentation:
            st.markdown(f"""
            <div class="doc-container">
                <div class="doc-header">
                    <div class="doc-title">{doc['title']}</div>
                    <div class="doc-meta">
                        <div>{doc['date']} {doc['time']}</div>
                        <div>{doc['author']}</div>
                    </div>
                </div>
                <div class="doc-content">{doc['content']}</div>
                <div class="doc-tags">
                    {' '.join([f'<div class="doc-tag">{tag}</div>' for tag in doc['tags']])}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Action buttons
            col1, col2, col3 = st.columns([1, 1, 2])
            
            with col1:
                st.button("Edit", key=f"edit_{doc['doc_id']}", use_container_width=True)
            
            with col2:
                st.button("Print", key=f"print_{doc['doc_id']}", use_container_width=True)
    else:
        st.info(f"No documentation found for {selected_patient.split(' (#')[0]}.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Document templates section
with st.expander("Documentation Templates Library"):
    templates = get_note_templates()
    
    # Group templates by category
    categories = {}
    for template in templates:
        category = template["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(template)
    
    # Display templates by category
    for category, category_templates in categories.items():
        st.markdown(f"### {category}")
        
        for template in category_templates:
            st.markdown(f"""
            <div class="template-item" id="template_{template['template_id']}">
                <div class="template-title">{template['template_name']} <span class="badge badge-blue">{category}</span></div>
                <div class="template-desc">{template['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # View template button
            if st.button(f"View Template", key=f"view_template_{template['template_id']}"):
                st.code(template["content"], language="markdown")

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Documentation")
