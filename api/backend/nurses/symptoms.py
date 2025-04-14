import streamlit as st
import requests

st.title("Submit Patient Symptom")

# Input fields
patient_id = st.text_input("Patient ID")
description = st.text_area("Symptom Description")
timestamp = st.text_input("Observed Time (YYYY-MM-DD HH:MM:SS)")

if st.button("Submit Symptom"):
    if not patient_id or not description or not timestamp:
        st.error("Please fill in all fields.")
    else:
        data = {
            "patient_id": patient_id,
            "description": description,
            "timestamp": timestamp
        }

        try:
            # External access: make sure the Flask API is running on the host (port 3111)
            response = requests.post("http://localhost:3111/patient-symptoms", json=data)

            if response.status_code == 201:
                st.success("Symptom submitted successfully!")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")

        except Exception as e:
            st.error(f"Connection error: {e}")
