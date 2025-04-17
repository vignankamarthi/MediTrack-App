import streamlit as st
import sys
import os
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Add the modules directory to the path so we can import the nav module
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modules'))
from nav import SideBarLinks

# Page configuration
st.set_page_config(
    page_title="Population Health Dashboard | MediTrack",
    page_icon="🏥",
    layout="wide"
)

# Authentication check - simplified without callbacks
if 'is_authenticated' not in st.session_state or not st.session_state.is_authenticated:
    st.switch_page("Home.py")
elif 'role' not in st.session_state or st.session_state.role != "physician":
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
    .status-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        margin-right: 5px;
    }
    .status-success {
        background-color: #00d97e;
    }
    .status-warning {
        background-color: #f6c343;
    }
    .filter-section {
        background-color: white;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Page header
st.title("Population Health Dashboard")

# Filter section
with st.container():
    st.markdown('<div class="filter-section">', unsafe_allow_html=True)
    
    # Search bar
    search = st.text_input("Search patients or conditions...")
    
    # Filters
    st.markdown("### Filters")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        condition = st.selectbox("Condition", 
                                ["All Conditions", "Diabetes", "Hypertension", "COPD", "CHF", "Asthma"])
    
    with col2:
        age_group = st.selectbox("Age Group", 
                               ["All Ages", "18-30", "31-45", "46-60", "61+"])
    
    with col3:
        gender = st.selectbox("Gender", 
                            ["All Genders", "Male", "Female", "Other"])
    
    with col4:
        time_period = st.selectbox("Time Period", 
                                 ["Last 3 Months", "Last 6 Months", "Last Year", "Custom..."])
    
    # Apply button
    apply_filters = st.button("Apply Filters")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Metrics overview
st.markdown("### Key Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Total Patients</div>
        <div class="metric-value">2,487</div>
        <div class="metric-trend-positive">+5.2% from last period</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Avg. Treatment Success</div>
        <div class="metric-value">76%</div>
        <div class="metric-trend-positive">+3.8% from last period</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Readmission Rate</div>
        <div class="metric-value">8.7%</div>
        <div class="metric-trend-negative">+1.2% from last period</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Medication Adherence</div>
        <div class="metric-value">82%</div>
        <div class="metric-trend-positive">+2.5% from last period</div>
    </div>
    """, unsafe_allow_html=True)

# Treatment Outcomes Chart
st.markdown("### Treatment Outcomes by Condition")
# Create tabs for different chart types
tab1, tab2, tab3 = st.tabs(["Bar", "Line", "Pie"])

# Sample data for treatment outcomes
outcome_data = {
    "Condition": ["Diabetes", "Hypertension", "COPD", "CHF", "Asthma"],
    "Success Rate": [72, 65, 48, 58, 80]
}
df_outcomes = pd.DataFrame(outcome_data)

with tab1:
    fig = px.bar(
        df_outcomes, 
        x="Condition", 
        y="Success Rate",
        text="Success Rate",
        color="Condition",
        labels={"Success Rate": "Success Rate (%)", "Condition": "Condition"},
        height=400,
        color_discrete_sequence=["#2c7be5", "#6e84a3", "#12263f", "#95aac9", "#d2ddec"]
    )
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(
        uniformtext_minsize=8, 
        uniformtext_mode='hide',
        margin=dict(t=30, b=0, l=0, r=0),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    fig = px.line(
        df_outcomes, 
        x="Condition", 
        y="Success Rate",
        markers=True,
        labels={"Success Rate": "Success Rate (%)", "Condition": "Condition"},
        height=400
    )
    fig.update_traces(line=dict(color="#2c7be5", width=3))
    fig.update_layout(
        margin=dict(t=30, b=0, l=0, r=0),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    fig = px.pie(
        df_outcomes, 
        values="Success Rate", 
        names="Condition",
        height=400,
        color_discrete_sequence=["#2c7be5", "#6e84a3", "#12263f", "#95aac9", "#d2ddec"]
    )
    fig.update_layout(
        margin=dict(t=30, b=0, l=0, r=0),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    st.plotly_chart(fig, use_container_width=True)

# Create two columns for the smaller charts
col1, col2 = st.columns(2)

# Demographic Breakdown
with col1:
    st.markdown("### Demographic Breakdown")
    
    # Sample data for demographics
    demographic_data = {
        "Age Group": ["18-30", "31-45", "46-60", "61+"],
        "Percentage": [15, 25, 35, 25]
    }
    df_demographics = pd.DataFrame(demographic_data)
    
    fig = px.pie(
        df_demographics, 
        values="Percentage", 
        names="Age Group",
        height=350,
        color_discrete_sequence=["#2c7be5", "#6e84a3", "#12263f", "#95aac9"]
    )
    fig.update_layout(
        margin=dict(t=10, b=10, l=10, r=10),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    st.plotly_chart(fig, use_container_width=True)

# Timeline Comparison
with col2:
    st.markdown("### Timeline Comparison")
    
    # Sample data for timeline
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    success_rates = [65, 59, 70, 72, 68, 74]
    
    timeline_data = {
        "Month": months,
        "Success Rate": success_rates
    }
    df_timeline = pd.DataFrame(timeline_data)
    
    fig = px.line(
        df_timeline, 
        x="Month", 
        y="Success Rate",
        markers=True,
        labels={"Success Rate": "Success Rate (%)", "Month": "Month"},
        height=350
    )
    fig.update_traces(line=dict(color="#2c7be5", width=3))
    fig.update_layout(
        margin=dict(t=10, b=10, l=10, r=10),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    st.plotly_chart(fig, use_container_width=True)

# Key Performance Indicators
st.markdown("### Key Performance Indicators")

kpi_data = {
    "Metric": ["HbA1c Control (Diabetes)", "BP Control (Hypertension)", "Preventative Screenings", "Follow-up Compliance"],
    "Current": ["68%", "72%", "81%", "88%"],
    "Target": ["75%", "70%", "85%", "80%"],
    "Status": ["Below Target", "Above Target", "Below Target", "Above Target"]
}
df_kpi = pd.DataFrame(kpi_data)

# Custom formatter for the Status column
def highlight_status(val):
    if val == "Above Target":
        return f'<span><span class="status-indicator status-success"></span>{val}</span>'
    else:
        return f'<span><span class="status-indicator status-warning"></span>{val}</span>'

# Apply formatting to the Status column
df_kpi["Status"] = df_kpi["Status"].apply(highlight_status)

# Display the table with custom formatting
st.write(df_kpi.to_html(escape=False, index=False), unsafe_allow_html=True)

# Add API endpoints information as comments for future implementation
"""
# API Endpoints to integrate:
# - /dr/treatment-outcomes - For treatment outcome data
# - /dr/healthcare-providers - For provider performance metrics
# - /dr/patient-treatment-records - For readmission analysis
# - /dr/medication-records/<patient_id> - For medication adherence data
"""

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Population Health Dashboard")
