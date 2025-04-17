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
    page_title="System Settings | MediTrack", 
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

# Custom CSS for settings page
st.markdown("""
<style>
    .settings-card {
        background-color: white;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    
    .settings-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 15px;
        padding-bottom: 15px;
        border-bottom: 1px solid #edf2f9;
    }
    
    .settings-icon {
        background-color: #f1f5f9;
        width: 40px;
        height: 40px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
    }
    
    .settings-section {
        margin-bottom: 30px;
    }
    
    .settings-section h3 {
        margin-bottom: 15px;
        font-size: 16px;
        font-weight: 600;
    }
    
    .setting-item {
        margin-bottom: 15px;
        padding-bottom: 15px;
        border-bottom: 1px solid #edf2f9;
    }
    
    .setting-item:last-child {
        border-bottom: none;
    }
    
    .setting-label {
        font-weight: 500;
        margin-bottom: 5px;
    }
    
    .setting-description {
        font-size: 14px;
        color: #64748b;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Page header
st.title("System Settings")
st.caption("Configure system parameters and global settings")

# Mock functions to simulate settings retrieval and saving
def get_system_settings():
    # In a real app, this would call an API endpoint
    return {
        "session_timeout": 30,
        "max_login_attempts": 5,
        "password_expiry_days": 90,
        "require_mfa": True,
        "allow_password_reset": True,
        "maintenance_mode": False,
        "maintenance_message": "System is currently undergoing scheduled maintenance. Please try again later.",
        "log_retention_days": 90,
        "backup_schedule": "daily",
        "backup_time": "03:00",
        "backup_retention_days": 30,
        "email_notifications": True,
        "notification_email": "admin@meditrack.com",
        "api_request_limit": 1000,
        "throttle_limit": 100,
        "default_language": "en-US",
        "enable_automatic_updates": True
    }

def save_system_settings(settings):
    # In a real app, this would call an API endpoint to save settings
    # For demo, just return success message
    return {"status": "success", "message": "Settings updated successfully"}

# Get current settings
current_settings = get_system_settings()

# Create settings form
with st.form("system_settings_form"):
    # Security Settings
    st.markdown("<div class='settings-section'>", unsafe_allow_html=True)
    st.markdown("""
    <div class="settings-header">
        <div class="settings-icon">🔒</div>
        <h2>Security Settings</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
        st.markdown("<div class='setting-label'>Session Timeout (minutes)</div>", unsafe_allow_html=True)
        st.markdown("<div class='setting-description'>Time of inactivity after which users will be automatically logged out</div>", unsafe_allow_html=True)
        session_timeout = st.number_input("Session Timeout", 
                                         min_value=5, 
                                         max_value=120, 
                                         value=current_settings["session_timeout"],
                                         step=5,
                                         label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
        st.markdown("<div class='setting-label'>Maximum Login Attempts</div>", unsafe_allow_html=True)
        st.markdown("<div class='setting-description'>Number of failed login attempts before account lockout</div>", unsafe_allow_html=True)
        max_login_attempts = st.number_input("Max Login Attempts", 
                                            min_value=3, 
                                            max_value=10, 
                                            value=current_settings["max_login_attempts"],
                                            step=1,
                                            label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
        st.markdown("<div class='setting-label'>Password Expiry (days)</div>", unsafe_allow_html=True)
        st.markdown("<div class='setting-description'>Number of days after which passwords must be changed</div>", unsafe_allow_html=True)
        password_expiry = st.number_input("Password Expiry", 
                                         min_value=30, 
                                         max_value=365, 
                                         value=current_settings["password_expiry_days"],
                                         step=30,
                                         label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
        st.markdown("<div class='setting-label'>Require Multi-Factor Authentication</div>", unsafe_allow_html=True)
        st.markdown("<div class='setting-description'>Require MFA for all user logins</div>", unsafe_allow_html=True)
        require_mfa = st.checkbox("Require MFA", 
                                 value=current_settings["require_mfa"],
                                 label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
        st.markdown("<div class='setting-label'>Allow Self-Service Password Reset</div>", unsafe_allow_html=True)
        st.markdown("<div class='setting-description'>Enable users to reset their own passwords</div>", unsafe_allow_html=True)
        allow_password_reset = st.checkbox("Allow Password Reset", 
                                          value=current_settings["allow_password_reset"],
                                          label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)  # Close security section
    
    # System Maintenance
    st.markdown("<div class='settings-section'>", unsafe_allow_html=True)
    st.markdown("""
    <div class="settings-header">
        <div class="settings-icon">⚙️</div>
        <h2>System Maintenance</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
        st.markdown("<div class='setting-label'>Maintenance Mode</div>", unsafe_allow_html=True)
        st.markdown("<div class='setting-description'>When enabled, only administrators can access the system</div>", unsafe_allow_html=True)
        maintenance_mode = st.checkbox("Maintenance Mode", 
                                      value=current_settings["maintenance_mode"],
                                      label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
        st.markdown("<div class='setting-label'>Log Retention Period (days)</div>", unsafe_allow_html=True)
        st.markdown("<div class='setting-description'>Number of days to retain system logs before archiving</div>", unsafe_allow_html=True)
        log_retention = st.number_input("Log Retention", 
                                       min_value=30, 
                                       max_value=365, 
                                       value=current_settings["log_retention_days"],
                                       step=30,
                                       label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
        st.markdown("<div class='setting-label'>Maintenance Message</div>", unsafe_allow_html=True)
        st.markdown("<div class='setting-description'>Message to display to users during maintenance mode</div>", unsafe_allow_html=True)
        maintenance_message = st.text_area("Maintenance Message", 
                                          value=current_settings["maintenance_message"],
                                          height=100,
                                          label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
        st.markdown("<div class='setting-label'>Enable Automatic Updates</div>", unsafe_allow_html=True)
        st.markdown("<div class='setting-description'>Automatically install system updates when available</div>", unsafe_allow_html=True)
        enable_updates = st.checkbox("Enable Updates", 
                                    value=current_settings["enable_automatic_updates"],
                                    label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)  # Close maintenance section
    
    # Backup Settings
    st.markdown("<div class='settings-section'>", unsafe_allow_html=True)
    st.markdown("""
    <div class="settings-header">
        <div class="settings-icon">💾</div>
        <h2>Backup & Recovery</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
        st.markdown("<div class='setting-label'>Backup Schedule</div>", unsafe_allow_html=True)
        st.markdown("<div class='setting-description'>How frequently system backups should be performed</div>", unsafe_allow_html=True)
        backup_schedule = st.selectbox("Backup Schedule", 
                                      options=["hourly", "daily", "weekly", "monthly"],
                                      index=["hourly", "daily", "weekly", "monthly"].index(current_settings["backup_schedule"]),
                                      label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
        st.markdown("<div class='setting-label'>Backup Retention (days)</div>", unsafe_allow_html=True)
        st.markdown("<div class='setting-description'>Number of days to retain backup files before deletion</div>", unsafe_allow_html=True)
        backup_retention = st.number_input("Backup Retention", 
                                          min_value=7, 
                                          max_value=365, 
                                          value=current_settings["backup_retention_days"],
                                          step=7,
                                          label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
        st.markdown("<div class='setting-label'>Backup Time</div>", unsafe_allow_html=True)
        st.markdown("<div class='setting-description'>Time of day when scheduled backups will run</div>", unsafe_allow_html=True)
        backup_time = st.time_input("Backup Time", 
                                   value=datetime.strptime(current_settings["backup_time"], "%H:%M").time(),
                                   label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
        st.markdown("<div class='setting-label'>Email Notifications</div>", unsafe_allow_html=True)
        st.markdown("<div class='setting-description'>Send email notifications for backup success/failure</div>", unsafe_allow_html=True)
        email_notifications = st.checkbox("Email Notifications", 
                                         value=current_settings["email_notifications"],
                                         label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
        
        if email_notifications:
            st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
            st.markdown("<div class='setting-label'>Notification Email</div>", unsafe_allow_html=True)
            st.markdown("<div class='setting-description'>Email address to receive system notifications</div>", unsafe_allow_html=True)
            notification_email = st.text_input("Notification Email", 
                                             value=current_settings["notification_email"],
                                             label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)  # Close backup section
    
    # API & Performance Settings
    st.markdown("<div class='settings-section'>", unsafe_allow_html=True)
    st.markdown("""
    <div class="settings-header">
        <div class="settings-icon">🚀</div>
        <h2>API & Performance</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
        st.markdown("<div class='setting-label'>API Request Limit (per day)</div>", unsafe_allow_html=True)
        st.markdown("<div class='setting-description'>Maximum number of API requests allowed per day per user</div>", unsafe_allow_html=True)
        api_limit = st.number_input("API Limit", 
                                  min_value=100, 
                                  max_value=10000, 
                                  value=current_settings["api_request_limit"],
                                  step=100,
                                  label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
        st.markdown("<div class='setting-label'>Rate Throttling (requests per minute)</div>", unsafe_allow_html=True)
        st.markdown("<div class='setting-description'>Maximum number of requests allowed per minute per user</div>", unsafe_allow_html=True)
        throttle_limit = st.number_input("Throttle Limit", 
                                       min_value=10, 
                                       max_value=1000, 
                                       value=current_settings["throttle_limit"],
                                       step=10,
                                       label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)  # Close API section
    
    # System Localization
    st.markdown("<div class='settings-section'>", unsafe_allow_html=True)
    st.markdown("""
    <div class="settings-header">
        <div class="settings-icon">🌐</div>
        <h2>Localization</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='setting-item'>", unsafe_allow_html=True)
    st.markdown("<div class='setting-label'>Default Language</div>", unsafe_allow_html=True)
    st.markdown("<div class='setting-description'>System-wide default language setting</div>", unsafe_allow_html=True)
    default_language = st.selectbox("Default Language", 
                                   options=["en-US", "es-ES", "fr-FR", "de-DE", "zh-CN", "ja-JP"],
                                   index=["en-US", "es-ES", "fr-FR", "de-DE", "zh-CN", "ja-JP"].index(current_settings["default_language"]),
                                   label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)  # Close localization section
    
    # Form submission buttons
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        submit_button = st.form_submit_button("Save Settings", use_container_width=True, type="primary")
    
    with col2:
        reset_button = st.form_submit_button("Reset to Defaults", use_container_width=True)

# Handle form submission
if submit_button:
    # Collect all updated settings
    updated_settings = {
        "session_timeout": session_timeout,
        "max_login_attempts": max_login_attempts,
        "password_expiry_days": password_expiry,
        "require_mfa": require_mfa,
        "allow_password_reset": allow_password_reset,
        "maintenance_mode": maintenance_mode,
        "maintenance_message": maintenance_message,
        "log_retention_days": log_retention,
        "backup_schedule": backup_schedule,
        "backup_time": backup_time.strftime("%H:%M"),
        "backup_retention_days": backup_retention,
        "email_notifications": email_notifications,
        "notification_email": notification_email if email_notifications else current_settings["notification_email"],
        "api_request_limit": api_limit,
        "throttle_limit": throttle_limit,
        "default_language": default_language,
        "enable_automatic_updates": enable_updates
    }
    
    # Save settings (in a real app, this would call an API)
    result = save_system_settings(updated_settings)
    
    if result["status"] == "success":
        st.success("Settings saved successfully!")
    else:
        st.error(f"Error saving settings: {result.get('message', 'Unknown error')}")

elif reset_button:
    st.warning("Settings have been reset to default values. Click 'Save Settings' to apply.")

# Navigation at the bottom
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    if st.button("Back to Dashboard", use_container_width=True):
        st.switch_page("pages/31_Admin_Home.py")

with col2:
    if st.button("View System Status", use_container_width=True):
        st.info("This would navigate to a system status page in a real application.")

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - System Settings")
