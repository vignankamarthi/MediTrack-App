import streamlit as st
import sys
import os
import pandas as pd
import requests
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px

# Add the modules directory to the path so we can import the nav module
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "modules"))
from nav import SideBarLinks

# Page configuration
st.set_page_config(
    page_title="Admin Dashboard | MediTrack", 
    page_icon="🏥", 
    layout="wide"
)

# Authentication check
if 'is_authenticated' not in st.session_state or not st.session_state.is_authenticated:
    st.switch_page("Home.py")
elif 'role' not in st.session_state or st.session_state.role != "admin":
    st.warning("You don't have permission to access this page.")
    st.switch_page("Home.py")

# Display sidebar navigation
SideBarLinks(st.session_state.role)

# Custom CSS for styling
st.markdown("""
<style>
    /* General Styles */
    :root {
      --primary: #6550e6;
      --success: #00d97e;
      --warning: #f6c343;
      --danger: #e63757;
      --secondary: #95aac9;
      --light: #f9fbfd;
      --dark: #12263f;
      --white: #ffffff;
      --gray: #edf2f9;
    }
    
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
    
    .status-badge {
        display: inline-block;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 12px;
        color: white;
    }
    
    .status-active {
        background-color: #00d97e;
    }
    
    .status-inactive {
        background-color: #e63757;
    }
    
    .status-pending {
        background-color: #f6c343;
    }
    
    .user-card {
        border: 1px solid #edf2f9;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
        background-color: white;
    }
    
    .user-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
    }
    
    .user-role {
        color: #95aac9;
        font-size: 12px;
    }
    
    .alert-card {
        border-left: 4px solid #f6c343;
        background-color: white;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }
    
    .alert-card.critical {
        border-left-color: #e63757;
    }
    
    .alert-card.info {
        border-left-color: #0ea5e9;
    }
    
    .alert-time {
        color: #95aac9;
        font-size: 12px;
    }
    
    .progress-container {
        height: 8px;
        background-color: #edf2f9;
        border-radius: 4px;
        margin-bottom: 5px;
    }
    
    .progress-bar {
        height: 100%;
        border-radius: 4px;
    }
    
    .backup-card {
        background-color: white;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
    }
    
    .backup-success {
        color: #00d97e;
    }
    
    .backup-warning {
        color: #f6c343;
    }
    
    .backup-error {
        color: #e63757;
    }
</style>
""", unsafe_allow_html=True)

# Admin dashboard header
st.title("System Dashboard")
st.caption(f"Welcome, {st.session_state.user_name}")

# Mock API call functions
def get_system_health():
    # In a real app, this would call an API endpoint
    return {
        "cpu_usage": 32,
        "memory_usage": 54,
        "disk_space": 68,
        "status": "Healthy"
    }

def get_system_users():
    # In a real app, this would call:
    # response = requests.get("http://web-api:4000/admin/system-users")
    # return response.json()
    
    return [
        {
            "user_id": 1,
            "user_name": "james.wilson",
            "first_name": "James",
            "last_name": "Wilson",
            "role": "physician",
            "email": "james.wilson@meditrack.com",
            "is_active": True,
            "last_login": "2025-04-17 08:25:13"
        },
        {
            "user_id": 2,
            "user_name": "maria.rodriguez",
            "first_name": "Maria",
            "last_name": "Rodriguez",
            "role": "nurse",
            "email": "maria.rodriguez@meditrack.com",
            "is_active": True,
            "last_login": "2025-04-17 09:18:03"
        },
        {
            "user_id": 3,
            "user_name": "sarah.chen",
            "first_name": "Sarah",
            "last_name": "Chen",
            "role": "pharmacist",
            "email": "sarah.chen@meditrack.com",
            "is_active": True,
            "last_login": "2025-04-17 08:42:56"
        },
        {
            "user_id": 4,
            "user_name": "michael.brown",
            "first_name": "Michael",
            "last_name": "Brown",
            "role": "physician",
            "email": "michael.brown@meditrack.com",
            "is_active": False,
            "last_login": "2025-04-10 14:32:18"
        },
        {
            "user_id": 5,
            "user_name": "brennan.admin",
            "first_name": "Brennan",
            "last_name": "Johnson",
            "role": "admin",
            "email": "brennan.admin@meditrack.com",
            "is_active": True,
            "last_login": "2025-04-17 07:30:45"
        }
    ]

def get_user_permissions():
    # In a real app, this would call the API
    return [
        {"permission_id": 1, "permission_name": "View Patient Records", "user_id": 1, "is_active": True},
        {"permission_id": 2, "permission_name": "Edit Patient Records", "user_id": 1, "is_active": True},
        {"permission_id": 3, "permission_name": "View Patient Records", "user_id": 2, "is_active": True},
        {"permission_id": 4, "permission_name": "Edit Medication Records", "user_id": 3, "is_active": True},
        {"permission_id": 5, "permission_name": "Admin Access", "user_id": 5, "is_active": True},
        {"permission_id": 6, "permission_name": "System Configuration", "user_id": 5, "is_active": True}
    ]

def get_system_alerts():
    # In a real app, this would call an API endpoint
    return [
        {
            "alert_id": 1,
            "level": "critical",
            "title": "Database Connection Issue",
            "message": "Intermittent connection failures to secondary database",
            "time": "10 minutes ago"
        },
        {
            "alert_id": 2,
            "level": "warning",
            "title": "Memory Usage High",
            "message": "Application server memory usage above 80%",
            "time": "45 minutes ago"
        },
        {
            "alert_id": 3,
            "level": "info",
            "title": "System Update Available",
            "message": "New security patch available for installation",
            "time": "2 hours ago"
        }
    ]

def get_backup_status():
    # In a real app, this would call an API endpoint
    return {
        "last_backup": {
            "timestamp": "2025-04-17 03:15:00",
            "status": "success",
            "size": "2.3GB"
        },
        "next_backup": "2025-04-17 15:15:00",
        "recent_backups": [
            {"date": "2025-04-17", "time": "03:15 AM", "status": "success", "size": "2.3GB"},
            {"date": "2025-04-16", "time": "03:15 AM", "status": "success", "size": "2.2GB"},
            {"date": "2025-04-15", "time": "03:15 AM", "status": "warning", "size": "2.1GB"}
        ]
    }

def get_recent_activity():
    # In a real app, this would call an API endpoint
    return [
        {
            "user": "Dr. James Wilson",
            "action": "read",
            "resource": "Patient Record #38291",
            "timestamp": "2025-04-17 09:43:12"
        },
        {
            "user": "Sarah Chen",
            "action": "update",
            "resource": "Medication Record #77423",
            "timestamp": "2025-04-17 09:38:27"
        },
        {
            "user": "Maria Rodriguez",
            "action": "create",
            "resource": "Patient Note #45219",
            "timestamp": "2025-04-17 09:36:11"
        },
        {
            "user": "Brennan Johnson",
            "action": "permission",
            "resource": "User Account #28742",
            "timestamp": "2025-04-17 09:32:55"
        }
    ]

def get_activity_graphs():
    # In a real app, this would calculate from real data
    dates = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    logins = [320, 280, 315, 290, 310, 200, 190]
    api_calls = [1250, 1100, 1350, 1200, 1400, 850, 790]
    
    return {"dates": dates, "logins": logins, "api_calls": api_calls}

def get_system_stats():
    return {
        "total_users": 284,
        "new_users_today": 32,
        "actions_today": 1423,
        "online_users": 87
    }

# Get data for the dashboard
system_health = get_system_health()
system_users = get_system_users()
user_permissions = get_user_permissions()
system_alerts = get_system_alerts()
backup_status = get_backup_status()
recent_activity = get_recent_activity()
activity_graphs = get_activity_graphs()
system_stats = get_system_stats()

# Create dashboard layout
col1, col2, col3, col4 = st.columns(4)

# System health metrics in the first row
with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">CPU Usage</div>
        <div class="metric-value">{0}%</div>
        <div class="progress-container">
            <div class="progress-bar" style="width: {0}%; background-color: {1};"></div>
        </div>
    </div>
    """.format(
        system_health["cpu_usage"], 
        "#00d97e" if system_health["cpu_usage"] < 50 else "#f6c343" if system_health["cpu_usage"] < 80 else "#e63757"
    ), unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Memory Usage</div>
        <div class="metric-value">{0}%</div>
        <div class="progress-container">
            <div class="progress-bar" style="width: {0}%; background-color: {1};"></div>
        </div>
    </div>
    """.format(
        system_health["memory_usage"], 
        "#00d97e" if system_health["memory_usage"] < 50 else "#f6c343" if system_health["memory_usage"] < 80 else "#e63757"
    ), unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Disk Space</div>
        <div class="metric-value">{0}%</div>
        <div class="progress-container">
            <div class="progress-bar" style="width: {0}%; background-color: {1};"></div>
        </div>
    </div>
    """.format(
        system_health["disk_space"], 
        "#00d97e" if system_health["disk_space"] < 50 else "#f6c343" if system_health["disk_space"] < 80 else "#e63757"
    ), unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">System Status</div>
        <div class="metric-value">{0}</div>
        <div style="color: {1};">{2}</div>
    </div>
    """.format(
        system_health["status"],
        "#00d97e" if system_health["status"] == "Healthy" else "#f6c343" if system_health["status"] == "Warning" else "#e63757",
        "All systems operational" if system_health["status"] == "Healthy" else "Some issues detected"
    ), unsafe_allow_html=True)

# Second row with user activity and system stats
col_left, col_right = st.columns([2, 1])

with col_left:
    # User activity chart
    st.subheader("User Activity")
    
    # Create a DataFrame for the activity data
    activity_data = pd.DataFrame({
        "Day": activity_graphs["dates"],
        "Logins": activity_graphs["logins"],
        "API Calls": activity_graphs["api_calls"]
    })
    
    # Create a bar chart with Plotly
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=activity_data["Day"],
        y=activity_data["Logins"],
        name="Logins",
        marker_color="#3b82f6"
    ))
    
    fig.add_trace(go.Bar(
        x=activity_data["Day"],
        y=activity_data["API Calls"],
        name="API Calls",
        marker_color="#93c5fd"
    ))
    
    fig.update_layout(
        title=None,
        barmode="group",
        height=300,
        margin=dict(l=40, r=40, t=20, b=20),
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#12263f"),
        xaxis=dict(
            title=None,
            showgrid=False,
            showline=True,
            linecolor="#edf2f9"
        ),
        yaxis=dict(
            title=None,
            gridcolor="#edf2f9",
            showline=True,
            linecolor="#edf2f9"
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Activity stats
    act_col1, act_col2, act_col3, act_col4 = st.columns(4)
    
    with act_col1:
        st.markdown(f"""
        <div style="text-align: center;">
            <div style="font-size: 24px; font-weight: bold; color: #12263f;">{system_stats["total_users"]}</div>
            <div style="font-size: 14px; color: #95aac9;">Active Users</div>
        </div>
        """, unsafe_allow_html=True)
    
    with act_col2:
        st.markdown(f"""
        <div style="text-align: center;">
            <div style="font-size: 24px; font-weight: bold; color: #12263f;">{system_stats["new_users_today"]}</div>
            <div style="font-size: 14px; color: #95aac9;">New Today</div>
        </div>
        """, unsafe_allow_html=True)
    
    with act_col3:
        st.markdown(f"""
        <div style="text-align: center;">
            <div style="font-size: 24px; font-weight: bold; color: #12263f;">{system_stats["actions_today"]}</div>
            <div style="font-size: 14px; color: #95aac9;">Actions Today</div>
        </div>
        """, unsafe_allow_html=True)
    
    with act_col4:
        st.markdown(f"""
        <div style="text-align: center;">
            <div style="font-size: 24px; font-weight: bold; color: #12263f;">{system_stats["online_users"]}</div>
            <div style="font-size: 14px; color: #95aac9;">Online Now</div>
        </div>
        """, unsafe_allow_html=True)

with col_right:
    # System alerts
    st.subheader("System Alerts")
    
    for alert in system_alerts:
        st.markdown(f"""
        <div class="alert-card {alert['level']}">
            <div style="font-weight: 500; margin-bottom: 5px;">{alert['title']}</div>
            <div style="font-size: 14px;">{alert['message']}</div>
            <div class="alert-time">{alert['time']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("View All Alerts", use_container_width=True):
        # This would navigate to a detailed alerts page
        st.info("This would navigate to a detailed alerts page in a real application.")

# Third row with user management and backup status
col_left, col_right = st.columns([2, 1])

with col_left:
    # User management section
    st.subheader("User Management")
    
    # Search and filter controls
    search_col, filter_col, button_col = st.columns([2, 1, 1])
    
    with search_col:
        search_term = st.text_input("Search users", placeholder="Search by name or role...")
    
    with filter_col:
        role_filter = st.selectbox("Filter by role", ["All Roles", "Physician", "Nurse", "Pharmacist", "Admin"])
    
    with button_col:
        st.button("Add New User", use_container_width=True)
    
    # Filter users based on search and filter
    filtered_users = system_users
    
    if search_term:
        filtered_users = [user for user in filtered_users if 
                        search_term.lower() in user["first_name"].lower() or 
                        search_term.lower() in user["last_name"].lower() or 
                        search_term.lower() in user["user_name"].lower() or
                        search_term.lower() in user["email"].lower()]
    
    if role_filter != "All Roles":
        filtered_users = [user for user in filtered_users if user["role"].lower() == role_filter.lower()]
    
    # Create a DataFrame for display
    df = pd.DataFrame(filtered_users)
    
    # Handle empty results
    if df.empty:
        st.info("No users match your search criteria.")
    else:
        # Display users in a table
        st.dataframe(
            df,
            column_config={
                "user_id": st.column_config.NumberColumn("ID"),
                "user_name": st.column_config.TextColumn("Username"),
                "first_name": st.column_config.TextColumn("First Name"),
                "last_name": st.column_config.TextColumn("Last Name"),
                "role": st.column_config.TextColumn("Role"),
                "email": st.column_config.TextColumn("Email"),
                "is_active": st.column_config.CheckboxColumn("Active"),
                "last_login": st.column_config.DatetimeColumn("Last Login")
            },
            use_container_width=True,
            hide_index=True
        )
    
    # View users button
    if st.button("Manage User Permissions", use_container_width=True):
        # This would navigate to a detailed user permissions page
        st.info("This would navigate to a user permissions management page in a real application.")

with col_right:
    # Backup status section
    st.subheader("Backup Status")
    
    st.markdown(f"""
    <div class="backup-card">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <div style="font-size: 24px; margin-right: 10px; color: #00d97e;"><i class="fas fa-check-circle"></i> ✅</div>
            <div>
                <div style="font-weight: 500;">Last Backup</div>
                <div style="font-size: 14px;">{backup_status['last_backup']['timestamp']}</div>
                <div style="font-size: 12px; color: #95aac9;">Completed successfully ({backup_status['last_backup']['size']})</div>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 15px;">
            <div style="font-size: 14px; color: #95aac9;">Next Scheduled</div>
            <div style="font-size: 14px;">{backup_status['next_backup']}</div>
        </div>
        <div style="margin-bottom: 10px; font-weight: 500;">Recent Backups</div>
    """, unsafe_allow_html=True)
    
    for backup in backup_status["recent_backups"]:
        status_class = "backup-success" if backup["status"] == "success" else "backup-warning" if backup["status"] == "warning" else "backup-error"
        
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #edf2f9;">
            <div style="font-size: 14px;">{backup['date']}</div>
            <div style="font-size: 14px;">{backup['time']}</div>
            <div class="{status_class}" style="font-size: 14px;">{backup['status'].capitalize()}</div>
            <div style="font-size: 14px;">{backup['size']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Backup button
    if st.button("Run Manual Backup", use_container_width=True):
        # This would trigger a backup in a real application
        st.success("Backup process started. This will take a few minutes.")

# Fourth row with recent activity and compliance
col_left, col_right = st.columns([2, 1])

with col_left:
    # Recent activity section
    st.subheader("Recent Activity")
    
    # Create a DataFrame for activity data
    activity_df = pd.DataFrame(recent_activity)
    
    # Display activity in a table
    st.dataframe(
        activity_df,
        column_config={
            "user": st.column_config.TextColumn("User"),
            "action": st.column_config.TextColumn("Action"),
            "resource": st.column_config.TextColumn("Resource"),
            "timestamp": st.column_config.DatetimeColumn("Timestamp")
        },
        use_container_width=True,
        hide_index=True
    )
    
    # View activity button
    if st.button("View All Activity", use_container_width=True):
        # Navigate to the compliance page which shows all activity
        st.switch_page("pages/32_Admin_Compliance.py")

with col_right:
    # Quick actions section
    st.subheader("Quick Actions")
    
    # Create a grid of action buttons
    action_col1, action_col2 = st.columns(2)
    
    with action_col1:
        if st.button("Generate Reports", use_container_width=True):
            st.info("This would open the report generation interface.")
    
    with action_col2:
        if st.button("System Settings", use_container_width=True):
            st.info("This would navigate to system settings.")
    
    action_col1, action_col2 = st.columns(2)
    
    with action_col1:
        if st.button("View Audit Logs", use_container_width=True):
            st.switch_page("pages/32_Admin_Compliance.py")
    
    with action_col2:
        if st.button("Database Admin", use_container_width=True):
            st.info("This would open the database administration interface.")

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - System Administration")
