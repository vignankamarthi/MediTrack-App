import streamlit as st
import sys
import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Add the modules directory to the path so we can import the nav module
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modules'))
from nav import SideBarLinks

# Page configuration
st.set_page_config(
    page_title="Provider Performance Comparison | MediTrack",
    page_icon="🏥",
    layout="wide"
)

# Authentication check
if 'is_authenticated' not in st.session_state or not st.session_state.is_authenticated:
    st.switch_page("Home.py")
elif 'role' not in st.session_state or st.session_state.role != "physician":
    st.warning("You don't have permission to access this page.")
    st.switch_page("Home.py")

# Display sidebar navigation
SideBarLinks(st.session_state.role)

# Load custom CSS
try:
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'css', 'physician_dashboard.css'), 'r') as css_file:
        st.markdown(f'<style>{css_file.read()}</style>', unsafe_allow_html=True)
except Exception as e:
    st.warning(f"Could not load CSS file: {e}")

# Page header
st.markdown('<div class="dashboard-header"><div class="logo">MediTrack</div><h1>Provider Performance Comparison</h1><div class="user-info"><span class="user-name">Dr. James Wilson</span></div></div>', unsafe_allow_html=True)

# Filter controls
st.container()
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    department = st.selectbox("Department", ["All Departments", "Cardiology", "Neurology", "Internal Medicine", "Orthopedics", "Oncology"])

with col2:
    condition = st.selectbox("Condition Type", ["All Conditions", "Diabetes", "Hypertension", "COPD", "CHF", "Stroke"])

with col3:
    time_period = st.selectbox("Time Period", ["Last 3 Months", "Last 6 Months", "Last Year", "Custom..."])

with col4:
    provider1 = st.selectbox("Provider 1", ["Dr. Sarah Johnson", "Dr. Michael Chen", "Dr. Emily Rodriguez", "Dr. David Kim"])

with col5:
    provider2 = st.selectbox("Provider 2", ["Dr. Michael Chen", "Dr. Sarah Johnson", "Dr. Emily Rodriguez", "Dr. David Kim"])

# Provider cards
col_left, col_right = st.columns(2)

# Dr. Sarah Johnson card
with col_left:
    st.markdown("""
    <div style="background-color: white; border-radius: 8px; padding: 20px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; padding-bottom: 15px; border-bottom: 1px solid #e0e4e8;">
            <div style="font-size: 18px; font-weight: 600; color: #12263f;">Dr. Sarah Johnson</div>
            <span style="padding: 5px 10px; border-radius: 4px; font-size: 12px; font-weight: 500; background-color: #00d97e; color: white;">Excellent</span>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
            <div style="padding: 15px; border-radius: 4px; background-color: #f9fafc;">
                <div style="font-size: 12px; color: #95aac9; margin-bottom: 5px;">Patient Count</div>
                <div style="font-size: 20px; font-weight: bold; color: #12263f;">437</div>
            </div>
            <div style="padding: 15px; border-radius: 4px; background-color: #f9fafc;">
                <div style="font-size: 12px; color: #95aac9; margin-bottom: 5px;">Avg. Visits per Patient</div>
                <div style="font-size: 20px; font-weight: bold; color: #12263f;">3.8</div>
            </div>
            <div style="padding: 15px; border-radius: 4px; background-color: #f9fafc;">
                <div style="font-size: 12px; color: #95aac9; margin-bottom: 5px;">Readmission Rate</div>
                <div style="font-size: 20px; font-weight: bold; color: #12263f;">7.2%</div>
            </div>
            <div style="padding: 15px; border-radius: 4px; background-color: #f9fafc;">
                <div style="font-size: 12px; color: #95aac9; margin-bottom: 5px;">Protocol Compliance</div>
                <div style="font-size: 20px; font-weight: bold; color: #12263f;">94%</div>
            </div>
            <div style="padding: 15px; border-radius: 4px; background-color: #f9fafc;">
                <div style="font-size: 12px; color: #95aac9; margin-bottom: 5px;">Avg. Treatment Duration</div>
                <div style="font-size: 20px; font-weight: bold; color: #12263f;">18 days</div>
            </div>
            <div style="padding: 15px; border-radius: 4px; background-color: #f9fafc;">
                <div style="font-size: 12px; color: #95aac9; margin-bottom: 5px;">Patient Satisfaction</div>
                <div style="font-size: 20px; font-weight: bold; color: #12263f;">4.8/5</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Dr. Michael Chen card
with col_right:
    st.markdown("""
    <div style="background-color: white; border-radius: 8px; padding: 20px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; padding-bottom: 15px; border-bottom: 1px solid #e0e4e8;">
            <div style="font-size: 18px; font-weight: 600; color: #12263f;">Dr. Michael Chen</div>
            <span style="padding: 5px 10px; border-radius: 4px; font-size: 12px; font-weight: 500; background-color: #4bb4e6; color: white;">Good</span>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
            <div style="padding: 15px; border-radius: 4px; background-color: #f9fafc;">
                <div style="font-size: 12px; color: #95aac9; margin-bottom: 5px;">Patient Count</div>
                <div style="font-size: 20px; font-weight: bold; color: #12263f;">392</div>
            </div>
            <div style="padding: 15px; border-radius: 4px; background-color: #f9fafc;">
                <div style="font-size: 12px; color: #95aac9; margin-bottom: 5px;">Avg. Visits per Patient</div>
                <div style="font-size: 20px; font-weight: bold; color: #12263f;">4.2</div>
            </div>
            <div style="padding: 15px; border-radius: 4px; background-color: #f9fafc;">
                <div style="font-size: 12px; color: #95aac9; margin-bottom: 5px;">Readmission Rate</div>
                <div style="font-size: 20px; font-weight: bold; color: #12263f;">9.1%</div>
            </div>
            <div style="padding: 15px; border-radius: 4px; background-color: #f9fafc;">
                <div style="font-size: 12px; color: #95aac9; margin-bottom: 5px;">Protocol Compliance</div>
                <div style="font-size: 20px; font-weight: bold; color: #12263f;">87%</div>
            </div>
            <div style="padding: 15px; border-radius: 4px; background-color: #f9fafc;">
                <div style="font-size: 12px; color: #95aac9; margin-bottom: 5px;">Avg. Treatment Duration</div>
                <div style="font-size: 20px; font-weight: bold; color: #12263f;">21 days</div>
            </div>
            <div style="padding: 15px; border-radius: 4px; background-color: #f9fafc;">
                <div style="font-size: 12px; color: #95aac9; margin-bottom: 5px;">Patient Satisfaction</div>
                <div style="font-size: 20px; font-weight: bold; color: #12263f;">4.6/5</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Readmission rate comparison chart
st.markdown("""
<div style="background-color: white; border-radius: 8px; padding: 20px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05); margin-top: 20px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
        <h2 style="font-size: 18px; color: #12263f; margin: 0;">Readmission Rates Comparison</h2>
    </div>
""", unsafe_allow_html=True)

# Sample data for the chart
conditions = ["Diabetes", "Hypertension", "CHF", "COPD", "Stroke"]
dr_johnson = [6.5, 7.2, 9.8, 5.4, 8.3]
dr_chen = [8.2, 9.1, 11.4, 7.9, 10.2]

# Create DataFrame for the chart
data = {
    "Condition": conditions,
    "Dr. Sarah Johnson": dr_johnson,
    "Dr. Michael Chen": dr_chen
}
df = pd.DataFrame(data)

# Create the bar chart
fig = go.Figure()
fig.add_trace(go.Bar(
    x=df['Condition'],
    y=df['Dr. Sarah Johnson'],
    name='Dr. Sarah Johnson',
    marker_color='#2c7be5'
))
fig.add_trace(go.Bar(
    x=df['Condition'],
    y=df['Dr. Michael Chen'],
    name='Dr. Michael Chen',
    marker_color='#95aac9'
))

# Customize the layout
fig.update_layout(
    barmode='group',
    title="",
    xaxis_title="",
    yaxis_title="Readmission Rate (%)",
    legend_title="Providers",
    font=dict(
        family="Arial, sans-serif",
        size=12,
        color="#333"
    ),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    height=350,
    margin=dict(l=40, r=40, t=20, b=40),
)

# Add data labels above the bars
fig.update_traces(
    texttemplate='%{y:.1f}%',
    textposition='outside',
    textfont=dict(size=11)
)

# Display the chart
st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Protocol compliance tracking table
st.markdown("""
<div style="background-color: white; border-radius: 8px; padding: 20px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05); margin-top: 20px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
        <h2 style="font-size: 18px; color: #12263f; margin: 0;">Protocol Compliance Tracking</h2>
    </div>
""", unsafe_allow_html=True)

# Create the table data
protocols_data = {
    "Protocol Name": ["Hypertension Management 2024", "Diabetes Care Protocol", "CHF Management 2023", "Stroke Prevention Protocol", "COPD Treatment 2022"],
    "Condition": ["Hypertension", "Diabetes", "CHF", "Stroke", "COPD"],
    "Last Updated": ["Feb 12, 2025", "Jan 5, 2025", "Nov 10, 2024", "Mar 22, 2025", "Aug 17, 2023"],
    "Status": ["Active", "Active", "Update Recommended", "Active", "Deprecated"],
    "Compliance (Dr. Johnson)": ["96%", "92%", "98%", "91%", "N/A"],
    "Compliance (Dr. Chen)": ["89%", "85%", "94%", "88%", "N/A"]
}

# Convert to DataFrame
protocols_df = pd.DataFrame(protocols_data)

# Define a function to color the status column
def highlight_status(val):
    color_map = {
        'Active': 'background-color: rgba(0, 217, 126, 0.2); color: #00d97e;',
        'Update Recommended': 'background-color: rgba(246, 195, 67, 0.2); color: #f6c343;',
        'Deprecated': 'background-color: rgba(149, 170, 201, 0.2); color: #95aac9;'
    }
    return color_map.get(val, '')

# Display the styled table
st.dataframe(
    protocols_df.style.applymap(highlight_status, subset=['Status']),
    column_config={
        "Protocol Name": st.column_config.TextColumn("Protocol Name"),
        "Condition": st.column_config.TextColumn("Condition"),
        "Last Updated": st.column_config.TextColumn("Last Updated"),
        "Status": st.column_config.TextColumn("Status"),
        "Compliance (Dr. Johnson)": st.column_config.TextColumn("Compliance (Dr. Johnson)"),
        "Compliance (Dr. Chen)": st.column_config.TextColumn("Compliance (Dr. Chen)")
    },
    hide_index=True,
    use_container_width=True
)

# Add action buttons (these will be non-functional placeholders)
col_actions = st.columns(5)
with col_actions[0]:
    st.button("View Protocol", use_container_width=True)
with col_actions[4]:
    st.button("Deprecate Protocol", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("© 2025 MediTrack - Provider Performance Comparison")
