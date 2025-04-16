import streamlit as st
import requests

API_BASE = "http://localhost:4000"

def run():
    st.title("🩺 Patient Symptoms Dashboard")

    if st.button("Load All Patient Symptoms"):
        res = requests.get(f"{API_BASE}/patient-symptom-records")
        if res.ok:
            st.dataframe(res.json())

    st.subheader("➕ Add Symptom Record")
    with st.form("add_symptom"):
        patient_id = st.text_input("Patient ID")
        symptom_id = st.text_input("Symptom ID")
        severity = st.selectbox("Severity", ["Low", "Moderate", "High"])
        submitted = st.form_submit_button("Submit")
        if submitted:
            data = {
                "patient_id": patient_id,
                "symptom_id": symptom_id,
                "severity_id": severity
            }
            r = requests.post(f"{API_BASE}/patient-symptom-records", json=data)
            st.success(r.json()["message"])
