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
    page_title="Care Tasks | MediTrack", 
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
st.title("Care Tasks Management")
st.subheader("Create, view, and manage patient care tasks")

# Mock API for demo purposes (would be replaced with actual API calls)
def get_care_tasks():
    """Simulate an API call to /n/care-tasks endpoint"""
    # In a real app, this would call the Flask API:
    # response = requests.get("http://web-api:4000/n/care-tasks")
    # return response.json()
    
    # Return simulated data
    return [
        {"task_id": 1, "task_name": "Administer Medication", "description": "Administer IV antibiotics for patient #101", "priority": "HIGH", "estimated_duration": 15},
        {"task_id": 2, "task_name": "Vital Signs Check", "description": "Record vitals for all assigned patients", "priority": "MEDIUM", "estimated_duration": 30},
        {"task_id": 3, "task_name": "Update Care Documentation", "description": "Complete care notes for morning rounds", "priority": "LOW", "estimated_duration": 20},
        {"task_id": 4, "task_name": "Patient Assessment", "description": "Conduct assessment for new patient #108", "priority": "HIGH", "estimated_duration": 45},
        {"task_id": 5, "task_name": "Medication Inventory", "description": "Check and update medication inventory", "priority": "MEDIUM", "estimated_duration": 25},
        {"task_id": 6, "task_name": "Family Consultation", "description": "Meet with patient #104 family members", "priority": "MEDIUM", "estimated_duration": 60},
        {"task_id": 7, "task_name": "Discharge Planning", "description": "Prepare discharge documents for patient #115", "priority": "LOW", "estimated_duration": 40},
        {"task_id": 8, "task_name": "Physical Therapy Session", "description": "Assist with PT for patient #120", "priority": "MEDIUM", "estimated_duration": 45}
    ]

def get_task_by_id(task_id):
    """Simulate an API call to /n/care-tasks/<task_id> endpoint"""
    # In a real implementation:
    # response = requests.get(f"http://web-api:4000/n/care-tasks/{task_id}")
    # return response.json()
    
    tasks = get_care_tasks()
    for task in tasks:
        if task["task_id"] == task_id:
            return task
    return None

def create_task(task_data):
    """Simulate an API call to POST /n/care-tasks endpoint"""
    # In a real implementation:
    # response = requests.post("http://web-api:4000/n/care-tasks", json=task_data)
    # return response.json()
    
    # For demo purposes:
    st.success(f"Task '{task_data['task_name']}' created successfully!")
    return {"task_id": len(get_care_tasks()) + 1, **task_data}

def update_task(task_id, task_data):
    """Simulate an API call to PUT /n/care-tasks/<task_id> endpoint"""
    # In a real implementation:
    # response = requests.put(f"http://web-api:4000/n/care-tasks/{task_id}", json=task_data)
    # return response.json()
    
    # For demo purposes:
    st.success(f"Task {task_id} updated successfully!")
    return {"task_id": task_id, **task_data}

# Custom CSS for styling
st.markdown("""
<style>
    .task-filter {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .priority-badge {
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
        color: white;
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
    .task-form {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Tabs for different views
tab1, tab2, tab3 = st.tabs(["Task List", "Create Task", "Manage Task"])

# Tab 1: Task List
with tab1:
    # Task filtering section
    st.markdown('<div class="task-filter">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        filter_priority = st.selectbox("Filter by Priority", ["All", "HIGH", "MEDIUM", "LOW"])
    
    with col2:
        filter_duration = st.slider("Max Duration (minutes)", 0, 120, 120)
    
    with col3:
        search_term = st.text_input("Search Tasks", placeholder="Enter keywords...")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Get tasks data (would come from API in real app)
    try:
        tasks = get_care_tasks()
        
        # Apply filters
        if filter_priority != "All":
            tasks = [task for task in tasks if task["priority"] == filter_priority]
        
        tasks = [task for task in tasks if task["estimated_duration"] <= filter_duration]
        
        if search_term:
            tasks = [task for task in tasks if search_term.lower() in task["task_name"].lower() or 
                    search_term.lower() in task["description"].lower()]
        
        # Convert to DataFrame for display
        if tasks:
            df = pd.DataFrame(tasks)
            
            # Add color-coded priority
            def highlight_priority(val):
                if val == 'HIGH':
                    return 'background-color: #ffecec; color: #e63757;'
                elif val == 'MEDIUM':
                    return 'background-color: #fff8e7; color: #f6c343;'
                elif val == 'LOW':
                    return 'background-color: #e7fff2; color: #00d97e;'
                return ''
            
            # Display the table with styling
            st.dataframe(
                df.style.applymap(highlight_priority, subset=['priority']),
                column_config={
                    "task_id": st.column_config.NumberColumn("ID"),
                    "task_name": st.column_config.TextColumn("Task Name"),
                    "description": st.column_config.TextColumn("Description"),
                    "priority": st.column_config.TextColumn("Priority"),
                    "estimated_duration": st.column_config.NumberColumn("Est. Duration (min)")
                },
                hide_index=True,
                use_container_width=True
            )
        else:
            st.info("No tasks match your filters.")
    
    except Exception as e:
        st.error(f"Could not load tasks: {str(e)}")

# Tab 2: Create Task
with tab2:
    st.markdown('<div class="task-form">', unsafe_allow_html=True)
    st.subheader("Create New Care Task")
    
    # Task creation form
    with st.form("task_creation_form"):
        task_name = st.text_input("Task Name", placeholder="Enter task name")
        task_description = st.text_area("Description", placeholder="Enter task description")
        
        col1, col2 = st.columns(2)
        with col1:
            task_priority = st.selectbox("Priority", ["HIGH", "MEDIUM", "LOW"])
        with col2:
            task_duration = st.number_input("Estimated Duration (minutes)", min_value=1, max_value=180, value=30)
        
        submit_button = st.form_submit_button("Create Task")
        
        if submit_button:
            if not task_name:
                st.error("Task name is required.")
            elif not task_priority:
                st.error("Priority is required.")
            else:
                # Prepare data for API call
                task_data = {
                    "task_name": task_name,
                    "description": task_description,
                    "priority": task_priority,
                    "estimated_duration": task_duration
                }
                
                # Call the API (simulated)
                created_task = create_task(task_data)
                
                # In a real app, you might want to refresh the page or clear the form
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 3: Manage Task
with tab3:
    st.markdown('<div class="task-form">', unsafe_allow_html=True)
    st.subheader("Update Existing Task")
    
    # Task selection
    task_id_to_update = st.number_input("Enter Task ID to Update", min_value=1, value=1)
    
    # Load button
    if st.button("Load Task Details"):
        task = get_task_by_id(task_id_to_update)
        
        if task:
            st.session_state.current_task = task
            st.success(f"Task {task_id_to_update} loaded successfully!")
        else:
            st.error(f"Task with ID {task_id_to_update} not found.")
    
    # Task update form
    if 'current_task' in st.session_state:
        task = st.session_state.current_task
        
        with st.form("task_update_form"):
            update_name = st.text_input("Task Name", value=task["task_name"])
            update_description = st.text_area("Description", value=task["description"])
            
            col1, col2 = st.columns(2)
            with col1:
                update_priority = st.selectbox(
                    "Priority", 
                    ["HIGH", "MEDIUM", "LOW"],
                    index=["HIGH", "MEDIUM", "LOW"].index(task["priority"])
                )
            with col2:
                update_duration = st.number_input(
                    "Estimated Duration (minutes)", 
                    min_value=1, 
                    max_value=180, 
                    value=task["estimated_duration"]
                )
            
            update_button = st.form_submit_button("Update Task")
            
            if update_button:
                # Prepare data for API call
                update_data = {
                    "description": update_description,
                    "priority": update_priority,
                    "estimated_duration": update_duration
                }
                
                # Call the API (simulated)
                updated_task = update_task(task_id_to_update, update_data)
                
                # Update the current task in session state
                st.session_state.current_task = {
                    "task_id": task_id_to_update,
                    "task_name": update_name,
                    **update_data
                }
    
    st.markdown('</div>', unsafe_allow_html=True)

# Call to action section at the bottom
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/13_Patient_Symptoms.py", label="View Patient Symptoms", icon="🤒", use_container_width=True)

with col2:
    st.page_link("pages/14_Lab_Results.py", label="Check Lab Results", icon="🔬", use_container_width=True)

with col3:
    st.page_link("pages/15_Medication_Administration.py", label="Medication Administration", icon="💊", use_container_width=True)

# Footer
st.caption("© 2025 MediTrack - Care Tasks Management")
