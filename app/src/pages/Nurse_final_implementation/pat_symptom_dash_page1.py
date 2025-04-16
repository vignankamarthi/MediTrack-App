import streamlit as st
import requests
from layout_template import render_header

API_URL = "http://localhost:5000"

def run():
    render_header()

    st.markdown("## 🩺 Patient Symptom Dashboard")

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
            st.write(f"🩺 **{record['symptom_name']}** — Severity: {record['severity']}, Patient: {record['first_name']} {record['last_name']}")
    else:
        st.info("No symptom records found.")
