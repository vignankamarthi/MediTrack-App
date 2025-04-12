import streamlit as st

# Inject CSS styles with wider layout
st.markdown("""
<style>
/* Expand the main content area */
.main .block-container {
  max-width: 1400px;
  padding-left: 2rem;
  padding-right: 2rem;
}

.dashboard-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
}
.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 0;
  border-bottom: 1px solid #e0e4e8;
  margin-bottom: 20px;
}
.dashboard-header h1 {
  font-size: 28px;
  margin: 0;
}

.dashboard-header h2 {
  font-size: 20px;
  margin: 0;
}

.dashboard-header h3 {
  font-size: 14px;
  margin: 0;
}
           
            
.logo {
  font-size: 22px;
  font-weight: bold;
  color: #2c7be5;
}
            
.user-info {
  display: flex;
  align-items: center;
}
.user-name {
  margin-right: 10px;
  font-weight: 500;
}
.avatar {
  border-radius: 50%;
  width: 40px;
  height: 40px;
  object-fit: cover;
}
.metric-card, .chart-container, .performance-indicators {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
  margin-bottom: 20px;
}
.metric-value {
  font-size: 24px;
  font-weight: bold;
  color: #12263f;
}
.metric-trend.positive { color: #00d97e; }
.metric-trend.negative { color: #e63757; }
.status-indicator { display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 5px; }
.status-indicator.success { background-color: #00d97e; }
.status-indicator.warning { background-color: #f6c343; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="dashboard-container">', unsafe_allow_html=True)

st.markdown('''
<div class="dashboard-header">
  <div class="logo">MediTrack</div>
  <h1>Population Health Dashboard</h1>
  <div class="user-info">
    <span class="user-name">Dr. James Wilson</span>
    <img src="https://as2.ftcdn.net/v2/jpg/03/20/52/31/1000_F_320523164_tx7Rdd7I2XDTvvKfz2oRuRpKOPE5z0ni.jpg" class="avatar">
  </div>
</div>
''', unsafe_allow_html=True)

# Controls
st.text_input("Search patients or conditions...")
col1, col2, col3, col4 = st.columns(4)
col1.selectbox("Condition", ["All Conditions", "Diabetes", "Hypertension", "COPD", "CHF"])
col2.selectbox("Age Group", ["All Ages", "18-30", "31-45", "46-60", "61+"])
col3.selectbox("Gender", ["All Genders", "Male", "Female", "Other"])
col4.selectbox("Time Period", ["Last 3 Months", "Last 6 Months", "Last Year", "Custom..."])
st.button("Apply Filters")

# Metrics
st.markdown("### Metrics Overview")
metric_cols = st.columns(4)
metric_cols[0].markdown("""<div class='metric-card'><h4>Total Patients</h3><p class='metric-value'>2,487</p><p class='metric-trend positive'>+5.2% from last period</p></div>""", unsafe_allow_html=True)
metric_cols[1].markdown("""<div class='metric-card'><h4>Avg. Treatment Success</h3><p class='metric-value'>76%</p><p class='metric-trend positive'>+3.8% from last period</p></div>""", unsafe_allow_html=True)
metric_cols[2].markdown("""<div class='metric-card'><h4>Readmission Rate</h3><p class='metric-value'>8.7%</p><p class='metric-trend negative'>+1.2% from last period</p></div>""", unsafe_allow_html=True)
metric_cols[3].markdown("""<div class='metric-card'><h4>Medication Adherence</h3><p class='metric-value'>82%</p><p class='metric-trend positive'>+2.5% from last period</p></div>""", unsafe_allow_html=True)

# Placeholder Charts
st.markdown("### Treatment Outcomes by Condition")
st.empty()

st.markdown("### Demographic Breakdown vs Timeline Comparison")
chart_row = st.columns(2)
chart_row[0].empty()
chart_row[1].empty()

# KPI Table
st.markdown("""
<div class="performance-indicators">
<h3>Key Performance Indicators</h3>
<table class="kpi-table">
<thead><tr><th>Metric</th><th>Current</th><th>Target</th><th>Status</th></tr></thead>
<tbody>
<tr><td>HbA1c Control (Diabetes)</td><td>68%</td><td>75%</td><td><span class="status-indicator warning"></span> Below Target</td></tr>
<tr><td>BP Control (Hypertension)</td><td>72%</td><td>70%</td><td><span class="status-indicator success"></span> Above Target</td></tr>
<tr><td>Preventative Screenings</td><td>81%</td><td>85%</td><td><span class="status-indicator warning"></span> Below Target</td></tr>
<tr><td>Follow-up Compliance</td><td>88%</td><td>80%</td><td><span class="status-indicator success"></span> Above Target</td></tr>
</tbody>
</table>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

