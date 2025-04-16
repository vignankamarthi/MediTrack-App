# lab_viewer_dash_page3.py
import streamlit as st
import requests
from layout_template import render_header

API_URL = "http://localhost:5000"
PATIENT_ID = st.session_state.get("current_patient_id", 1)

def run():
    render_header()

    st.markdown("## Lab Results Viewer")

    try:
        response = requests.get(f"{API_URL}/lab-results", params={"patient_id": PATIENT_ID})
        response.raise_for_status()
        lab_results = response.json()
    except Exception as e:
        st.error(f"Error fetching lab results: {e}")
        lab_results = []

    st.markdown("""
        <style>
            .lab-section .card {
                background: #fff;
                border-radius: 8px;
                padding: 1rem;
                box-shadow: 0 2px 6px rgba(0,0,0,0.05);
                margin-bottom: 2rem;
            }
            .card-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 1rem;
            }
            .card-title {
                font-size: 20px;
                font-weight: bold;
                color: #003366;
            }
            .lab-notification {
                display: flex;
                align-items: flex-start;
                gap: 1rem;
                border-bottom: 1px solid #eee;
                padding: 0.75rem 0;
            }
            .lab-icon {
                font-weight: bold;
                font-size: 20px;
                color: #dc3545;
            }
            .lab-info h4 {
                margin: 0;
                font-size: 16px;
                color: #333;
            }
            .lab-info p {
                margin: 0.2rem 0;
                font-size: 14px;
                color: #555;
            }
            .lab-table {
                width: 100%;
                border-collapse: collapse;
                font-size: 14px;
            }
            .lab-table th, .lab-table td {
                padding: 0.5rem 0.75rem;
                border-bottom: 1px solid #ddd;
                text-align: left;
            }
            .lab-table th {
                background-color: #f4f6f9;
                font-weight: 600;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="lab-section">', unsafe_allow_html=True)

    critical = [r for r in lab_results if r.get("is_abnormal")]
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-header"><div class="card-title">Critical Lab Notifications</div></div>', unsafe_allow_html=True)

    if critical:
        for result in critical:
            st.markdown(f"""
                <div class="lab-notification">
                    <div class="lab-icon">!</div>
                    <div class="lab-info">
                        <h4>{result['test_name']}: {result['result_value']} {result['unit_of_measure']}</h4>
                        <p>Range: {result['reference_range']}</p>
                        <p>Reported: {result['result_date']}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("<p>No critical lab results.</p>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # --- Full Lab Panel ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-header"><div class="card-title">Full Lab Panel</div></div>', unsafe_allow_html=True)

    if lab_results:
        table_html = """
            <table class="lab-table">
                <thead>
                    <tr>
                        <th>Test</th>
                        <th>Value</th>
                        <th>Units</th>
                        <th>Reference Range</th>
                        <th>Date</th>
                    </tr>
                </thead>
                <tbody>
        """
        for r in lab_results:
            table_html += f"""
                <tr>
                    <td>{r['test_name']}</td>
                    <td>{r['result_value']}</td>
                    <td>{r['unit_of_measure']}</td>
                    <td>{r['reference_range']}</td>
                    <td>{r['result_date']}</td>
                </tr>
            """
        table_html += "</tbody></table>"
        st.markdown(table_html, unsafe_allow_html=True)
    else:
        st.markdown("<p>No lab results available.</p>", unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

