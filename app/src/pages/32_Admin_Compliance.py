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
    page_title="Audit & Compliance | MediTrack", 
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

# Custom CSS for compliance and audit styling
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
    
    .compliance-container {
        margin-bottom: 25px;
    }
    
    .filter-controls {
        background-color: white;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }
    
    .filter-group {
        display: flex;
        flex-direction: column;
    }
    
    .filter-label {
        font-size: 12px;
        color: #95aac9;
        margin-bottom: 5px;
    }
    
    .badge {
        display: inline-block;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 500;
        color: white;
    }
    
    .badge-read {
        background-color: #0ea5e9;
    }
    
    .badge-create {
        background-color: #00d97e;
    }
    
    .badge-update {
        background-color: #f6c343;
    }
    
    .badge-delete {
        background-color: #e63757;
    }
    
    .badge-permission {
        background-color: #6550e6;
    }
    
    .badge-login {
        background-color: #8b5cf6;
    }
    
    .archive-stats {
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;
    }
    
    .stat-card {
        flex: 1;
        background-color: white;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        display: flex;
        align-items: center;
        gap: 10px;
        margin: 0 5px;
    }
    
    .stat-icon {
        font-size: 24px;
        color: #6550e6;
    }
    
    .stat-info {
        display: flex;
        flex-direction: column;
    }
    
    .stat-value {
        font-size: 18px;
        font-weight: 600;
    }
    
    .stat-label {
        font-size: 12px;
        color: #95aac9;
    }
    
    .compliance-card {
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    
    .compliance-tabs {
        display: flex;
        border-bottom: 1px solid #edf2f9;
    }
    
    .compliance-tab {
        padding: 10px 20px;
        cursor: pointer;
        border-bottom: 2px solid transparent;
        font-weight: 500;
    }
    
    .compliance-tab.active {
        border-bottom-color: #6550e6;
        color: #6550e6;
    }
    
    .checklist-item {
        display: flex;
        align-items: flex-start;
        padding: 15px;
        border-bottom: 1px solid #edf2f9;
    }
    
    .checklist-item:last-child {
        border-bottom: none;
    }
    
    .check-status {
        margin-right: 15px;
        font-size: 18px;
    }
    
    .check-content {
        flex: 1;
    }
    
    .check-title {
        font-weight: 500;
        margin-bottom: 5px;
    }
    
    .check-description {
        font-size: 14px;
        color: #64748b;
        margin-bottom: 5px;
    }
    
    .check-meta {
        font-size: 12px;
        color: #95aac9;
    }
    
    .status-compliant {
        color: #00d97e;
    }
    
    .status-warning {
        color: #f6c343;
    }
    
    .status-non-compliant {
        color: #e63757;
    }
    
    .vulnerability-summary {
        display: flex;
        justify-content: space-around;
        margin-bottom: 20px;
    }
    
    .vulnerability-metric {
        text-align: center;
        padding: 10px;
        border-radius: 8px;
        min-width: 80px;
    }
    
    .vulnerability-count {
        font-size: 24px;
        font-weight: 600;
    }
    
    .vulnerability-label {
        font-size: 12px;
        color: #64748b;
    }
    
    .critical-bg {
        background-color: rgba(230, 55, 87, 0.1);
    }
    
    .critical-text {
        color: #e63757;
    }
    
    .high-bg {
        background-color: rgba(245, 158, 11, 0.1);
    }
    
    .high-text {
        color: #f6c343;
    }
    
    .medium-bg {
        background-color: rgba(168, 85, 247, 0.1);
    }
    
    .medium-text {
        color: #8b5cf6;
    }
    
    .low-bg {
        background-color: rgba(14, 165, 233, 0.1);
    }
    
    .low-text {
        color: #0ea5e9;
    }
    
    .vulnerability-item {
        background-color: white;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
        border-left: 4px solid transparent;
        display: flex;
    }
    
    .vulnerability-item.critical {
        border-left-color: #e63757;
    }
    
    .vulnerability-item.high {
        border-left-color: #f6c343;
    }
    
    .vulnerability-item.medium {
        border-left-color: #8b5cf6;
    }
    
    .vulnerability-item.low {
        border-left-color: #0ea5e9;
    }
    
    .vuln-details {
        flex: 1;
    }
    
    .vuln-title {
        font-weight: 500;
        margin-bottom: 5px;
    }
    
    .vuln-description {
        font-size: 14px;
        color: #64748b;
    }
    
    .archive-criteria {
        margin-bottom: 20px;
    }
    
    .archive-criteria h4 {
        font-size: 16px;
        margin-bottom: 10px;
    }
    
    .criteria-item {
        display: flex;
        align-items: center;
        margin-bottom: 5px;
    }
    
    .criteria-item input {
        margin-right: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Page header
st.title("Audit & Compliance Management")
st.caption(f"Welcome, {st.session_state.user_name}")

# Mock API call functions
def get_audit_logs():
    # In a real app, this would call:
    # response = requests.get("http://web-api:4000/admin/audit-logs")
    # return response.json()
    
    return [
        {
            "log_id": 1001,
            "user_id": 1,
            "user_name": "James Wilson",
            "action_type": "READ",
            "table_affected": "PATIENT",
            "record_id": 38291,
            "ip_address": "192.168.1.45",
            "action_timestamp": "2025-04-17 09:43:12",
            "details": "Viewed patient medical history"
        },
        {
            "log_id": 1002,
            "user_id": 3,
            "user_name": "Sarah Chen",
            "action_type": "UPDATE",
            "table_affected": "MEDICATION",
            "record_id": 77423,
            "ip_address": "192.168.1.102",
            "action_timestamp": "2025-04-17 09:38:27",
            "details": "Updated medication dosage"
        },
        {
            "log_id": 1003,
            "user_id": 2,
            "user_name": "Maria Rodriguez",
            "action_type": "CREATE",
            "table_affected": "PATIENT_NOTES",
            "record_id": 45219,
            "ip_address": "192.168.1.87",
            "action_timestamp": "2025-04-17 09:36:11",
            "details": "Created new patient note"
        },
        {
            "log_id": 1004,
            "user_id": 5,
            "user_name": "Brennan Johnson",
            "action_type": "PERMISSION",
            "table_affected": "SYSTEM_USERS",
            "record_id": 28742,
            "ip_address": "192.168.1.10",
            "action_timestamp": "2025-04-17 09:32:55",
            "details": "Updated user permissions"
        },
        {
            "log_id": 1005,
            "user_id": 1,
            "user_name": "James Wilson",
            "action_type": "UPDATE",
            "table_affected": "TREATMENT_PLAN",
            "record_id": 58324,
            "ip_address": "192.168.1.45",
            "action_timestamp": "2025-04-17 09:27:42",
            "details": "Updated treatment plan"
        },
        {
            "log_id": 1006,
            "user_id": 3,
            "user_name": "Sarah Chen",
            "action_type": "READ",
            "table_affected": "PATIENT",
            "record_id": 67234,
            "ip_address": "192.168.1.102",
            "action_timestamp": "2025-04-17 09:22:18",
            "details": "Viewed patient record"
        },
        {
            "log_id": 1007,
            "user_id": 2,
            "user_name": "Maria Rodriguez",
            "action_type": "LOGIN",
            "table_affected": "SYSTEM",
            "record_id": None,
            "ip_address": "192.168.1.87",
            "action_timestamp": "2025-04-17 09:18:03",
            "details": "User login"
        }
    ]

def get_archive_stats():
    # In a real app, this would call an API endpoint
    return {
        "total_records": 231456,
        "last_archive_date": "2025-03-15",
        "archive_size": "4.2 TB"
    }

def get_hipaa_compliance_items():
    # In a real app, this would call an API endpoint
    return [
        {
            "requirement_id": "164.308(a)(1)(i)",
            "title": "Security Management Process",
            "description": "Implement policies and procedures to prevent, detect, contain, and correct security violations.",
            "status": "compliant",
            "last_review": "2025-01-10"
        },
        {
            "requirement_id": "164.308(a)(3)(i)",
            "title": "Workforce Security",
            "description": "Implement policies and procedures to ensure appropriate access to ePHI.",
            "status": "compliant",
            "last_review": "2025-02-22"
        },
        {
            "requirement_id": "164.308(a)(5)(i)",
            "title": "Security Awareness and Training",
            "description": "Implement security awareness and training program for all workforce members.",
            "status": "warning",
            "last_review": "2024-09-15"
        },
        {
            "requirement_id": "164.308(a)(6)(i)",
            "title": "Security Incident Procedures",
            "description": "Implement policies and procedures to address security incidents.",
            "status": "compliant",
            "last_review": "2025-03-01"
        },
        {
            "requirement_id": "164.312(e)(1)",
            "title": "Transmission Security",
            "description": "Implement technical security measures to guard against unauthorized access to ePHI transmitted over electronic networks.",
            "status": "non-compliant",
            "last_review": "2024-11-05"
        }
    ]

def get_vulnerabilities():
    # In a real app, this would call an API endpoint
    return {
        "summary": {
            "critical": 2,
            "high": 5,
            "medium": 12,
            "low": 23
        },
        "scan_date": "2025-03-20",
        "scan_status": "Medium Risk",
        "vulnerabilities": [
            {
                "cve_id": "CVE-2024-8901",
                "title": "SQL Injection in Patient Search",
                "description": "SQL injection vulnerability in patient search functionality could allow unauthorized access to patient records.",
                "severity": "critical",
                "status": "Pending",
                "remediation_action": "Remediate"
            },
            {
                "cve_id": "CVE-2024-9207",
                "title": "Authentication Bypass",
                "description": "Authentication bypass vulnerability in API endpoint could allow unauthorized system access.",
                "severity": "critical",
                "status": "In Progress",
                "remediation_action": "View Details"
            },
            {
                "cve_id": "CVE-2024-7654",
                "title": "Cross-Site Scripting",
                "description": "XSS vulnerability in messaging system could allow execution of malicious scripts.",
                "severity": "high",
                "status": "Scheduled",
                "remediation_action": "Remediate"
            }
        ]
    }

# Get data for the page
audit_logs = get_audit_logs()
archive_stats = get_archive_stats()
hipaa_compliance = get_hipaa_compliance_items()
vulnerabilities = get_vulnerabilities()

# Create a tab structure for different sections
tab1, tab2, tab3, tab4 = st.tabs(["Activity Log", "Archive Management", "Regulatory Compliance", "Vulnerability Scanning"])

# Tab 1: Activity Log
with tab1:
    st.subheader("Activity Log")
    
    # Filter controls
    with st.container():
        st.markdown('<div class="filter-controls">', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns([1, 1, 2, 1])
        
        with col1:
            user_filter = st.selectbox(
                "User:",
                ["All Users"] + list(set([log["user_name"] for log in audit_logs])),
                label_visibility="collapsed"
            )
        
        with col2:
            action_filter = st.selectbox(
                "Action:",
                ["All Actions", "READ", "CREATE", "UPDATE", "DELETE", "PERMISSION", "LOGIN"],
                label_visibility="collapsed"
            )
        
        with col3:
            date_cols = st.columns(2)
            with date_cols[0]:
                start_date = st.date_input(
                    "From:",
                    value=datetime.now() - timedelta(days=7),
                    label_visibility="collapsed"
                )
            with date_cols[1]:
                end_date = st.date_input(
                    "To:",
                    value=datetime.now(),
                    label_visibility="collapsed"
                )
        
        with col4:
            apply_filter = st.button("Apply", use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Filter logs based on selections
    filtered_logs = audit_logs
    
    if user_filter != "All Users":
        filtered_logs = [log for log in filtered_logs if log["user_name"] == user_filter]
    
    if action_filter != "All Actions":
        filtered_logs = [log for log in filtered_logs if log["action_type"] == action_filter]
    
    # Convert dates to datetime objects for comparison
    start_datetime = datetime.combine(start_date, datetime.min.time())
    end_datetime = datetime.combine(end_date, datetime.max.time())
    
    filtered_logs = [
        log for log in filtered_logs if 
        start_datetime <= datetime.strptime(log["action_timestamp"], "%Y-%m-%d %H:%M:%S") <= end_datetime
    ]
    
    # Display logs in a table
    if filtered_logs:
        # Create a DataFrame
        logs_df = pd.DataFrame(filtered_logs)
        
        # Add formatted action column with badges
        def format_action(action):
            action_lower = action.lower()
            color_class = {
                "read": "badge-read",
                "create": "badge-create",
                "update": "badge-update",
                "delete": "badge-delete",
                "permission": "badge-permission",
                "login": "badge-login"
            }.get(action_lower, "")
            
            return f'<span class="badge {color_class}">{action}</span>'
        
        # Display the table with customizations
        st.dataframe(
            logs_df,
            column_order=["action_timestamp", "user_name", "action_type", "table_affected", "record_id", "details", "ip_address"],
            column_config={
                "log_id": None,  # Hide log_id column
                "user_id": None,  # Hide user_id column
                "action_timestamp": st.column_config.DatetimeColumn("Timestamp"),
                "user_name": st.column_config.TextColumn("User"),
                "action_type": st.column_config.TextColumn("Action"),
                "table_affected": st.column_config.TextColumn("Resource"),
                "record_id": st.column_config.NumberColumn("Record ID"),
                "details": st.column_config.TextColumn("Details"),
                "ip_address": st.column_config.TextColumn("IP Address")
            },
            use_container_width=True,
            hide_index=True
        )
        
        # Pagination controls
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
                <button class="btn-icon"><i class="fas fa-chevron-left"></i> ◀</button>
                <span>Page 1 of 42</span>
                <button class="btn-icon">▶ <i class="fas fa-chevron-right"></i></button>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No audit logs match your filter criteria.")
    
    # Action buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Export Logs", use_container_width=True):
            st.success("Logs exported successfully!")
    with col2:
        if st.button("View Detailed Logs", use_container_width=True):
            # In a real app, this would call:
            # response = requests.get("http://web-api:4000/admin/audit-logs/details")
            st.info("This would show detailed audit logs in a real application.")

# Tab 2: Archive Management
with tab2:
    st.subheader("Archive Management")
    
    # Archive statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-icon">📊</div>
            <div class="stat-info">
                <div class="stat-value">{archive_stats['total_records']:,}</div>
                <div class="stat-label">Archived Records</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-icon">🗓️</div>
            <div class="stat-info">
                <div class="stat-value">{archive_stats['last_archive_date']}</div>
                <div class="stat-label">Last Archive Date</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-icon">💾</div>
            <div class="stat-info">
                <div class="stat-value">{archive_stats['archive_size']}</div>
                <div class="stat-label">Archive Size</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Archive criteria
    st.markdown("<h4>Archive Criteria</h4>", unsafe_allow_html=True)
    
    criteria_col1, criteria_col2 = st.columns(2)
    
    with criteria_col1:
        st.checkbox("Patient records inactive for 7+ years", value=True)
        st.checkbox("Fully resolved cases older than 5 years")
        st.checkbox("Audit logs older than 2 years")
    
    with criteria_col2:
        custom_criteria = st.checkbox("Custom criteria")
        if custom_criteria:
            st.text_area("Define custom criteria", placeholder="E.g., Archive test records created before 2024")
    
    # Archive schedule
    st.markdown("<h4>Archive Schedule</h4>", unsafe_allow_html=True)
    
    schedule_option = st.radio(
        "Schedule archives to run:",
        ["Monthly (15th, 2:00 AM)", "Quarterly", "Manual only"],
        horizontal=True
    )
    
    # Archive actions
    if st.button("Archive Records Now", type="primary"):
        # In a real app, this would call:
        # response = requests.post("http://web-api:4000/admin/run-archive")
        st.success("Archive process initiated! This may take several minutes to complete.")

# Tab 3: Regulatory Compliance
with tab3:
    st.subheader("Regulatory Compliance")
    
    # Compliance status indicator
    col1, col2 = st.columns([3, 1])
    with col2:
        st.markdown("""
        <div style="text-align: right;">
            <span class="badge" style="background-color: #f6c343;">Review Needed</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Compliance category tabs
    category_options = ["HIPAA", "GDPR", "HITECH", "PCI DSS"]
    selected_category = st.radio("Select compliance framework:", category_options, horizontal=True)
    
    # Display compliance checklist based on selection
    if selected_category == "HIPAA":
        for item in hipaa_compliance:
            status_class = f"status-{item['status']}"
            status_icon = "✅" if item['status'] == "compliant" else "⚠️" if item['status'] == "warning" else "❌"
            
            st.markdown(f"""
            <div class="checklist-item">
                <div class="check-status {status_class}">{status_icon}</div>
                <div class="check-content">
                    <div class="check-title">§{item['requirement_id']} - {item['title']}</div>
                    <div class="check-description">{item['description']}</div>
                    <div class="check-meta">Last review: {item['last_review']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info(f"{selected_category} compliance requirements would be displayed here in a real application.")
    
    # Compliance actions
    col1, col2 = st.columns(2)
    with col1:
        if st.button("View All Requirements", use_container_width=True):
            st.info("This would show all compliance requirements in a real application.")
    with col2:
        if st.button("Schedule Review", use_container_width=True, type="primary"):
            st.success("Compliance review scheduled successfully!")

# Tab 4: Vulnerability Scanning
with tab4:
    st.subheader("Vulnerability Scanning")
    
    # Scan status and information
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 10px;">
            <div>Last scan completed: {vulnerabilities['scan_date']}</div>
            <div>
                <span class="badge" style="background-color: #f6c343;">{vulnerabilities['scan_status']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if st.button("Run New Scan", use_container_width=True, type="primary"):
            st.info("Vulnerability scan initiated. This may take some time to complete.")
    
    # Vulnerability summary
    st.markdown("""
    <div class="vulnerability-summary">
        <div class="vulnerability-metric critical-bg">
            <div class="vulnerability-count critical-text">{}</div>
            <div class="vulnerability-label">Critical</div>
        </div>
        <div class="vulnerability-metric high-bg">
            <div class="vulnerability-count high-text">{}</div>
            <div class="vulnerability-label">High</div>
        </div>
        <div class="vulnerability-metric medium-bg">
            <div class="vulnerability-count medium-text">{}</div>
            <div class="vulnerability-label">Medium</div>
        </div>
        <div class="vulnerability-metric low-bg">
            <div class="vulnerability-count low-text">{}</div>
            <div class="vulnerability-label">Low</div>
        </div>
    </div>
    """.format(
        vulnerabilities['summary']['critical'],
        vulnerabilities['summary']['high'],
        vulnerabilities['summary']['medium'],
        vulnerabilities['summary']['low']
    ), unsafe_allow_html=True)
    
    # List of vulnerabilities
    for vuln in vulnerabilities['vulnerabilities']:
        st.markdown(f"""
        <div class="vulnerability-item {vuln['severity']}">
            <div class="vuln-details">
                <div class="vuln-title">{vuln['cve_id']}: {vuln['title']}</div>
                <div class="vuln-description">{vuln['description']}</div>
            </div>
            <div>
                <span class="badge" style="background-color: #95aac9;">{vuln['status']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Action buttons for each vulnerability
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Remediate", key=f"remediate_{vuln['cve_id']}", use_container_width=True):
                st.success(f"Remediation process initiated for {vuln['cve_id']}!")
        with col2:
            if st.button("View Details", key=f"details_{vuln['cve_id']}", use_container_width=True):
                st.info(f"This would show detailed information for {vuln['cve_id']} in a real application.")
    
    # Scan schedule
    st.markdown("<h4>Scan Schedule</h4>", unsafe_allow_html=True)
    scan_schedule = st.radio(
        "Schedule scans to run:",
        ["Weekly (Sunday, 1:00 AM)", "Daily (1:00 AM)", "Manual only"],
        horizontal=True
    )
    
    # Additional actions
    col1, col2 = st.columns(2)
    with col1:
        if st.button("View All Vulnerabilities", use_container_width=True):
            st.info("This would show all vulnerabilities in a real application.")
    with col2:
        if st.button("Export Scan Report", use_container_width=True):
            st.success("Scan report exported successfully!")

# Navigation at the bottom
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    if st.button("Back to Dashboard", use_container_width=True):
        st.switch_page("pages/31_Admin_Home.py")

with col2:
    if st.button("Generate Compliance Report", use_container_width=True):
        st.success("Generating compliance report...")

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Audit & Compliance Management")
