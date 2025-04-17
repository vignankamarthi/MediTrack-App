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
    page_title="Task Management | MediTrack", 
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
    .task-card {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
    }
    .task-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
    .task-title {
        font-size: 18px;
        font-weight: 600;
    }
    .task-details {
        color: #95aac9;
        margin-bottom: 15px;
    }
    .task-meta {
        display: flex;
        justify-content: space-between;
        font-size: 14px;
    }
    .task-patient {
        color: #12263f;
        font-weight: 500;
    }
    .task-time {
        color: #95aac9;
    }
    .task-status {
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
        color: white;
    }
    .pending {
        background-color: #f6c343;
    }
    .completed {
        background-color: #00d97e;
    }
    .overdue {
        background-color: #e63757;
    }
</style>
""", unsafe_allow_html=True)

# Page title
st.title("Care Task Management")
st.subheader("Create, view, and manage patient care tasks")

# Mock API for demo purposes (would be replaced with actual API calls)
def get_care_tasks():
    """Simulate an API call to /n/care-tasks endpoint"""
    # In a real app, this would call the Flask API:
    # response = requests.get("http://web-api:4000/n/care-tasks")
    # return response.json()
    
    # Return simulated data
    return [
        {
            "task_id": 1, 
            "task_name": "Administer Medication", 
            "description": "Administer IV antibiotics for patient #101", 
            "priority": "HIGH", 
            "patient_id": 101,
            "patient_name": "John Doe",
            "status": "PENDING",
            "due_time": "15:30",
            "estimated_duration": 15
        },
        {
            "task_id": 2, 
            "task_name": "Vital Signs Check", 
            "description": "Record vitals for all assigned patients", 
            "priority": "MEDIUM", 
            "patient_id": None,
            "patient_name": "All Patients",
            "status": "PENDING",
            "due_time": "16:00",
            "estimated_duration": 30
        },
        {
            "task_id": 3, 
            "task_name": "Update Care Documentation", 
            "description": "Complete care notes for morning rounds", 
            "priority": "LOW", 
            "patient_id": None,
            "patient_name": "Multiple Patients",
            "status": "COMPLETED",
            "due_time": "13:00",
            "estimated_duration": 20
        },
        {
            "task_id": 4, 
            "task_name": "Patient Assessment", 
            "description": "Conduct assessment for new patient", 
            "priority": "HIGH", 
            "patient_id": 108,
            "patient_name": "William Wilson",
            "status": "OVERDUE",
            "due_time": "10:30",
            "estimated_duration": 45
        },
        {
            "task_id": 5, 
            "task_name": "Medication Inventory", 
            "description": "Check and update medication inventory", 
            "priority": "MEDIUM", 
            "patient_id": None,
            "patient_name": "Administrative",
            "status": "PENDING",
            "due_time": "18:00",
            "estimated_duration": 25
        },
        {
            "task_id": 6, 
            "task_name": "Family Consultation", 
            "description": "Meet with patient's family members", 
            "priority": "MEDIUM", 
            "patient_id": 104,
            "patient_name": "Emily Davis",
            "status": "PENDING",
            "due_time": "17:30",
            "estimated_duration": 60
        },
        {
            "task_id": 7, 
            "task_name": "Discharge Planning", 
            "description": "Prepare discharge documents", 
            "priority": "LOW", 
            "patient_id": 115,
            "patient_name": "James Walker",
            "status": "PENDING",
            "due_time": "19:00",
            "estimated_duration": 40
        },
        {
            "task_id": 8, 
            "task_name": "Physical Therapy Session", 
            "description": "Assist with PT session", 
            "priority": "MEDIUM", 
            "patient_id": 120,
            "patient_name": "Robert Taylor",
            "status": "COMPLETED",
            "due_time": "14:00",
            "estimated_duration": 45
        }
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

def get_patient_list():
    """Return a list of patients"""
    return [
        {"patient_id": 101, "name": "John Doe"},
        {"patient_id": 102, "name": "Sarah Smith"},
        {"patient_id": 103, "name": "Michael Brown"},
        {"patient_id": 104, "name": "Emily Davis"},
        {"patient_id": 105, "name": "William Johnson"},
        {"patient_id": 108, "name": "William Wilson"},
        {"patient_id": 115, "name": "James Walker"},
        {"patient_id": 120, "name": "Robert Taylor"}
    ]

# Main tabs for different views
tab1, tab2, tab3 = st.tabs(["Task Dashboard", "Create Task", "Task Management"])

# ---------------------------
# TAB 1: TASK DASHBOARD
# ---------------------------
with tab1:
    # Task filtering section
    st.markdown('<div class="task-filter">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        filter_priority = st.selectbox("Filter by Priority", ["All", "HIGH", "MEDIUM", "LOW"], key="dash_priority")
    
    with col2:
        filter_status = st.selectbox("Filter by Status", ["All", "PENDING", "OVERDUE", "COMPLETED"], key="dash_status")
    
    with col3:
        search_term = st.text_input("Search Tasks", placeholder="Enter keywords...", key="dash_search")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Task statistics
    col1, col2, col3, col4 = st.columns(4)
    
    # Calculate stats from task data
    tasks = get_care_tasks()
    total_tasks = len(tasks)
    pending_tasks = sum(1 for task in tasks if task["status"] == "PENDING")
    overdue_tasks = sum(1 for task in tasks if task["status"] == "OVERDUE")
    completed_tasks = sum(1 for task in tasks if task["status"] == "COMPLETED")
    
    with col1:
        st.metric("Total Tasks", total_tasks)
    with col2:
        st.metric("Pending Tasks", pending_tasks)
    with col3:
        st.metric("Overdue Tasks", overdue_tasks, delta=overdue_tasks, delta_color="inverse")
    with col4:
        st.metric("Completed Today", completed_tasks)
    
    # Today's tasks section
    st.markdown("### Today's Tasks")
    
    # Get tasks data and apply filters
    try:
        filtered_tasks = tasks
        
        # Apply priority filter
        if filter_priority != "All":
            filtered_tasks = [task for task in filtered_tasks if task["priority"] == filter_priority]
        
        # Apply status filter
        if filter_status != "All":
            filtered_tasks = [task for task in filtered_tasks if task["status"] == filter_status]
        
        # Apply search filter
        if search_term:
            filtered_tasks = [task for task in filtered_tasks if 
                            search_term.lower() in task["task_name"].lower() or 
                            search_term.lower() in task["description"].lower() or
                            search_term.lower() in task["patient_name"].lower()]
        
        # Sort tasks: OVERDUE first, then HIGH priority PENDING, then by due time
        def task_sort_key(task):
            status_order = {"OVERDUE": 0, "PENDING": 1, "COMPLETED": 2}
            priority_order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
            
            status_value = status_order.get(task["status"], 3)
            priority_value = priority_order.get(task["priority"], 3)
            
            return (status_value, priority_value, task["due_time"])
        
        filtered_tasks = sorted(filtered_tasks, key=task_sort_key)
        
        # Display tasks
        if filtered_tasks:
            for task in filtered_tasks:
                # Determine status badge class
                status_class = task["status"].lower()
                
                st.markdown(f"""
                <div class="task-card">
                    <div class="task-header">
                        <div class="task-title">{task['task_name']}</div>
                        <div class="priority-badge {task['priority'].lower()}">{task['priority']}</div>
                    </div>
                    <div class="task-details">{task['description']}</div>
                    <div class="task-meta">
                        <div class="task-patient">Patient: {task['patient_name']}</div>
                        <div class="task-time">Due: {task['due_time']} • Est. {task['estimated_duration']} min</div>
                        <div class="task-status {status_class}">{task['status']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Add action buttons based on task status
                col1, col2, col3 = st.columns([1, 1, 2])
                
                with col1:
                    if task["status"] == "PENDING" or task["status"] == "OVERDUE":
                        if st.button("Mark Complete", key=f"complete_{task['task_id']}", use_container_width=True):
                            # This would call the API to update the task status
                            st.success(f"Task '{task['task_name']}' marked as complete!")
                            # In a real app, you would reload the page or update the state
                
                with col2:
                    if st.button("Edit Task", key=f"edit_{task['task_id']}", use_container_width=True):
                        # Set the task to edit in session state
                        st.session_state.task_to_edit = task["task_id"]
                        # Switch to the edit tab
                        st.session_state.active_tab = "Task Management"
                        st.experimental_rerun()
                
                # Add progress tracking for longer tasks
                if task["estimated_duration"] > 30 and task["status"] == "PENDING":
                    st.progress(0.0, text="Not started")
                elif task["status"] == "COMPLETED":
                    st.progress(1.0, text="Completed")
        else:
            st.info("No tasks match your filters.")
    
    except Exception as e:
        st.error(f"Could not load tasks: {str(e)}")
    
    # Quick actions
    st.markdown("### Quick Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Add New Task", use_container_width=True):
            # Switch to create task tab
            st.switch_page("pages/14_Task_Management.py")  # Will reload the page and we'll set active tab
    
    with col2:
        if st.button("View Team Tasks", use_container_width=True):
            st.info("Team view would be displayed here (not implemented in demo)")
    
    with col3:
        if st.button("Generate Task Report", use_container_width=True):
            st.download_button(
                label="Download Report",
                data="This would be a CSV report of tasks",
                file_name="task_report.csv",
                mime="text/csv",
            )

# ---------------------------
# TAB 2: CREATE TASK
# ---------------------------
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
            task_duration = st.number_input("Estimated Duration (minutes)", min_value=5, max_value=180, value=30, step=5)
        
        col1, col2 = st.columns(2)
        with col1:
            # Get patient list for selection
            patients = get_patient_list()
            patient_options = ["All Patients", "Administrative"] + [p["name"] for p in patients]
            selected_patient = st.selectbox("Patient", patient_options)
            
            # Determine patient_id
            if selected_patient == "All Patients" or selected_patient == "Administrative":
                patient_id = None
            else:
                patient_id = next((p["patient_id"] for p in patients if p["name"] == selected_patient), None)
        
        with col2:
            due_date = st.date_input("Due Date", datetime.now())
            due_time = st.time_input("Due Time", datetime.now().time())
        
        # Additional task details in expandable section
        with st.expander("Additional Task Details (Optional)"):
            col1, col2 = st.columns(2)
            
            with col1:
                recurrence = st.selectbox("Recurrence", ["One-time", "Daily", "Weekly", "Monthly"])
            
            with col2:
                if recurrence != "One-time":
                    end_date = st.date_input("Recurrence End Date", datetime.now() + timedelta(days=30))
            
            task_notes = st.text_area("Notes", placeholder="Additional notes for the task")
        
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
                    "estimated_duration": task_duration,
                    "patient_id": patient_id,
                    "patient_name": selected_patient,
                    "due_date": due_date.strftime('%Y-%m-%d'),
                    "due_time": due_time.strftime('%H:%M'),
                    "status": "PENDING"
                }
                
                # Call the API (simulated)
                created_task = create_task(task_data)
                
                # Direct user to the task list
                st.session_state.active_tab = "Task Dashboard"
                st.experimental_rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# TAB 3: TASK MANAGEMENT
# ---------------------------
with tab3:
    st.markdown('<div class="task-form">', unsafe_allow_html=True)
    st.subheader("Manage Existing Tasks")
    
    # Task selection section
    task_view_mode = st.radio("View Mode", ["Calendar View", "Task ID Search", "Filter View"], horizontal=True)
    
    if task_view_mode == "Task ID Search":
        # Task ID input field 
        task_id_to_edit = st.number_input("Enter Task ID to Edit", min_value=1, value=1)
        
        # Load button
        if st.button("Load Task Details"):
            task = get_task_by_id(task_id_to_edit)
            
            if task:
                st.session_state.current_task = task
                st.success(f"Task {task_id_to_edit} loaded successfully!")
            else:
                st.error(f"Task with ID {task_id_to_edit} not found.")
    
    elif task_view_mode == "Filter View":
        # Similar filters as in Dashboard tab
        col1, col2, col3 = st.columns(3)
        
        with col1:
            mgmt_filter_priority = st.selectbox("Filter by Priority", ["All", "HIGH", "MEDIUM", "LOW"], key="mgmt_priority")
        
        with col2:
            mgmt_filter_status = st.selectbox("Filter by Status", ["All", "PENDING", "OVERDUE", "COMPLETED"], key="mgmt_status")
        
        with col3:
            mgmt_search_term = st.text_input("Search Tasks", placeholder="Enter keywords...", key="mgmt_search")
        
        # Get tasks based on filters and display in a table
        tasks = get_care_tasks()
        filtered_tasks = tasks
        
        # Apply priority filter
        if mgmt_filter_priority != "All":
            filtered_tasks = [task for task in filtered_tasks if task["priority"] == mgmt_filter_priority]
        
        # Apply status filter
        if mgmt_filter_status != "All":
            filtered_tasks = [task for task in filtered_tasks if task["status"] == mgmt_filter_status]
        
        # Apply search filter
        if mgmt_search_term:
            filtered_tasks = [task for task in filtered_tasks if 
                            mgmt_search_term.lower() in task["task_name"].lower() or 
                            mgmt_search_term.lower() in task["description"].lower() or
                            mgmt_search_term.lower() in task["patient_name"].lower()]
        
        # Display table of tasks
        if filtered_tasks:
            task_df = pd.DataFrame(filtered_tasks)
            
            # Add select button column
            task_df["actions"] = None
            
            # Display the table
            st.dataframe(
                task_df[["task_id", "task_name", "patient_name", "priority", "status", "due_time"]],
                column_config={
                    "task_id": st.column_config.NumberColumn("ID"),
                    "task_name": st.column_config.TextColumn("Task Name"),
                    "patient_name": st.column_config.TextColumn("Patient"),
                    "priority": st.column_config.TextColumn("Priority"),
                    "status": st.column_config.TextColumn("Status"),
                    "due_time": st.column_config.TextColumn("Due Time"),
                },
                hide_index=True,
                use_container_width=True
            )
            
            # Add a selection for editing
            selected_task_id = st.selectbox(
                "Select Task to Edit", 
                options=[task["task_id"] for task in filtered_tasks],
                format_func=lambda x: f"Task #{x}: {next((t['task_name'] for t in filtered_tasks if t['task_id'] == x), '')}"
            )
            
            if st.button("Load Selected Task"):
                task = get_task_by_id(selected_task_id)
                if task:
                    st.session_state.current_task = task
                    st.success(f"Task {selected_task_id} loaded successfully!")
                    st.experimental_rerun()
        else:
            st.info("No tasks match your filters.")
    
    else:  # Calendar View
        st.info("Calendar view would display tasks organized by date/time (not implemented in demo)")
        
        # Simple date picker for demo
        cal_date = st.date_input("Select Date", datetime.now())
        
        # Show tasks for the selected date (for demo we'll show all)
        tasks = get_care_tasks()
        
        # Group by morning, afternoon, evening
        st.markdown("### Morning Tasks (8:00 AM - 12:00 PM)")
        morning_tasks = [t for t in tasks if t["due_time"] < "12:00"]
        if morning_tasks:
            for task in morning_tasks:
                st.markdown(f"• **{task['due_time']}** - {task['task_name']} ({task['patient_name']})")
        else:
            st.markdown("No tasks scheduled")
            
        st.markdown("### Afternoon Tasks (12:00 PM - 5:00 PM)")
        afternoon_tasks = [t for t in tasks if "12:00" <= t["due_time"] < "17:00"]
        if afternoon_tasks:
            for task in afternoon_tasks:
                st.markdown(f"• **{task['due_time']}** - {task['task_name']} ({task['patient_name']})")
        else:
            st.markdown("No tasks scheduled")
            
        st.markdown("### Evening Tasks (5:00 PM - 8:00 PM)")
        evening_tasks = [t for t in tasks if t["due_time"] >= "17:00"]
        if evening_tasks:
            for task in evening_tasks:
                st.markdown(f"• **{task['due_time']}** - {task['task_name']} ({task['patient_name']})")
        else:
            st.markdown("No tasks scheduled")
    
    # Task update form (shown when a task is selected)
    if 'current_task' in st.session_state:
        task = st.session_state.current_task
        
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown(f"### Edit Task: {task['task_name']}")
        
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
                update_status = st.selectbox(
                    "Status",
                    ["PENDING", "COMPLETED", "OVERDUE"],
                    index=["PENDING", "COMPLETED", "OVERDUE"].index(task["status"])
                )
                
            col1, col2 = st.columns(2)
            with col1:
                patients = get_patient_list()
                patient_options = ["All Patients", "Administrative"] + [p["name"] for p in patients]
                
                if task["patient_id"] is None:
                    default_patient = task["patient_name"]
                else:
                    default_patient = next((p["name"] for p in patients if p["patient_id"] == task["patient_id"]), "All Patients")
                
                update_patient = st.selectbox(
                    "Patient", 
                    patient_options,
                    index=patient_options.index(default_patient) if default_patient in patient_options else 0
                )
                
                # Determine patient_id
                if update_patient == "All Patients" or update_patient == "Administrative":
                    update_patient_id = None
                else:
                    update_patient_id = next((p["patient_id"] for p in patients if p["name"] == update_patient), None)
                
            with col2:
                update_duration = st.number_input(
                    "Estimated Duration (minutes)", 
                    min_value=5, 
                    max_value=180, 
                    value=task["estimated_duration"],
                    step=5
                )
                
                # Parse time from string
                current_time = datetime.strptime(task["due_time"], "%H:%M").time() if "due_time" in task else datetime.now().time()
                update_time = st.time_input("Due Time", current_time)
            
            # Add notes section
            update_notes = st.text_area("Notes", value=task.get("notes", ""))
            
            # Form buttons
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                update_button = st.form_submit_button("Update Task")
            with col2:
                delete_button = st.form_submit_button("Delete Task")
            with col3:
                cancel_button = st.form_submit_button("Cancel")
            
            if update_button:
                # Prepare data for API call
                update_data = {
                    "task_name": update_name,
                    "description": update_description,
                    "priority": update_priority,
                    "status": update_status,
                    "patient_id": update_patient_id,
                    "patient_name": update_patient,
                    "due_time": update_time.strftime('%H:%M'),
                    "estimated_duration": update_duration,
                    "notes": update_notes
                }
                
                # Call the API (simulated)
                updated_task = update_task(task["task_id"], update_data)
                
                # Clear the current task and redirect to task list
                st.session_state.current_task = None
                st.session_state.active_tab = "Task Dashboard"
                st.experimental_rerun()
                
            elif delete_button:
                # Show a confirmation before deleting
                st.warning(f"Task '{task['task_name']}' has been deleted (simulation only).")
                st.session_state.current_task = None
                
            elif cancel_button:
                # Clear the current task
                st.session_state.current_task = None
                st.experimental_rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Bulk action section at the bottom
st.markdown("### Bulk Actions")

col1, col2, col3 = st.columns(3)

with col1:
    st.button("Mark Selected Tasks Complete", use_container_width=True)

with col2:
    st.button("Generate Task Report", key="bulk_report", use_container_width=True)

with col3:
    st.button("Re-assign Tasks", use_container_width=True)

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Task Management")
