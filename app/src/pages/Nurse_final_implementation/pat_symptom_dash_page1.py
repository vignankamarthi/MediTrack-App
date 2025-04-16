import streamlit as st
import requests
from layout_template import render_header

API_URL = "http://web-api:4000"

def run():
    render_header()

    st.markdown("## 🩺 Patient Symptom Dashboard")

    # ---------------- Add Symptom Form ----------------
    if "show_symptom_form" not in st.session_state:
        st.session_state["show_symptom_form"] = False

    if st.button("➕ Add Symptom Record"):
        st.session_state["show_symptom_form"] = not st.session_state["show_symptom_form"]

    if st.session_state["show_symptom_form"]:
        with st.form("add_symptom_form"):
            st.subheader("Add Patient Symptom")
            patient_id = st.text_input("Patient ID")
            symptom_id = st.text_input("Symptom ID")
            severity = st.selectbox("Severity", ["low", "medium", "high"])
            submitted = st.form_submit_button("Submit")

            if submitted:
                payload = {
                    "patient_id": patient_id,
                    "symptom_id": symptom_id,
                    "severity_id": severity
                }
                try:
                    res = requests.post(f"{API_URL}/patient-symptom-records", json=payload)
                    if res.status_code == 201:
                        st.success("✅ Symptom record added.")
                        st.session_state["show_symptom_form"] = False
                        st.experimental_rerun()
                    else:
                        st.error(f"❌ Failed to add record: {res.status_code}")
                except Exception as e:
                    st.error(f"❌ Error: {e}")

    # ---------------- Fetch Symptom Records ----------------
    try:
        response = requests.get(f"{API_URL}/patient-symptom-records")
        response.raise_for_status()
        records = response.json()
    except Exception as e:
        st.error(f"Error fetching symptom data: {e}")
        records = []

    if records:
        for record in records:
            with st.container():
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.markdown(f"""
                        <div style='width: 12px; height: 12px; border-radius: 50%; background-color: {'#dc3545' if record['severity'] == 'high' else ('#ffc107' if record['severity'] == 'medium' else '#28a745')}; margin-top: 10px;'>
                        </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown(f"""
                        <div style='background-color:#f8f9fa; padding:1rem; border-radius:10px; margin-bottom:1rem;'>
                            <strong>Symptom:</strong> {record['symptom_name']}<br>
                            <strong>Severity:</strong> {record['severity']}<br>
                            <strong>Patient:</strong> {record['first_name']} {record['last_name']}<br>
                            <small><em>Description: {record['symptom_description']}</em></small>
                        </div>
                    """, unsafe_allow_html=True)
    else:
        st.info("No symptom records found.")

    # Add symptom form toggle
    if "show_symptom_form" not in st.session_state:
        st.session_state["show_symptom_form"] = False

    if st.button("➕ Add Symptom Record"):
        st.session_state["show_symptom_form"] = not st.session_state["show_symptom_form"]

    if st.session_state["show_symptom_form"]:
        with st.form("add_symptom_form"):
            st.subheader("Add Patient Symptom")
            patient_id = st.text_input("Patient ID")
            symptom_id = st.text_input("Symptom ID")
            severity = st.selectbox("Severity", ["low", "medium", "high"])
            submitted = st.form_submit_button("Submit")

            if submitted:
                payload = {
                    "patient_id": patient_id,
                    "symptom_id": symptom_id,
                    "severity_id": severity
                }
                try:
                    res = requests.post(f"{API_URL}/patient-symptom-records", json=payload)
                    if res.status_code == 201:
                        st.success("✅ Symptom record added.")
                        st.session_state["show_symptom_form"] = False
                        st.experimental_rerun()
                    else:
                        st.error(f"❌ Failed to add record: {res.status_code}")
                except Exception as e:
                    st.error(f"❌ Error: {e}")

    # get symptom records
    try:
        response = requests.get(f"{API_URL}/patient-symptom-records")
        response.raise_for_status()
        records = response.json()
    except Exception as e:
        st.error(f"Error fetching symptom data: {e}")
        records = []

    if records:
        for record in records:
            with st.container():
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.markdown(f"""
                        <div style='width: 12px; height: 12px; border-radius: 50%; background-color: {'#dc3545' if record['severity'] == 'high' else ('#ffc107' if record['severity'] == 'medium' else '#28a745')}; margin-top: 10px;'>
                        </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown(f"""
                        <div style='background-color:#f8f9fa; padding:1rem; border-radius:10px; margin-bottom:1rem;'>
                            <strong>Symptom:</strong> {record['symptom_name']}<br>
                            <strong>Severity:</strong> {record['severity']}<br>
                            <strong>Patient:</strong> {record['first_name']} {record['last_name']}<br>
                            <small><em>Description: {record['symptom_description']}</em></small>
                        </div>
                    """, unsafe_allow_html=True)
    else:
        st.info("No symptom records found.")

