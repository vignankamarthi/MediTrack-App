import streamlit as st
import requests
import pandas as pd

API_BASE = "http://localhost:3006/nurse"  # Adjust this to match your actual Flask URL
st.set_page_config(layout="wide")
st.title("👩‍⚕️ Nurse Dashboard")

# ------------------ Care Tasks ------------------
st.header("📋 Care Tasks")

with st.expander("➕ Create New Task"):
    with st.form("create_task"):
        task_name = st.text_input("Task Name")
        description = st.text_area("Description")
        priority = st.selectbox("Priority", [1, 2, 3])
        estimated_duration = st.number_input("Estimated Duration (mins)", min_value=0)
        if st.form_submit_button("Submit"):
            res = requests.post(f"{API_BASE}/care-tasks/", json={
                "task_name": task_name,
                "description": description,
                "priority": priority,
                "esimated_duration": estimated_duration
            })
            st.success("Task created" if res.ok else res.text)

care_tasks = requests.get(f"{API_BASE}/care-tasks").json()
st.dataframe(pd.DataFrame(care_tasks))

# ------------------ Patient Symptom Records ------------------
st.header("🩺 Patient Symptom Records")
symptoms = requests.get(f"{API_BASE}/patient-symptom-records").json()
st.dataframe(pd.DataFrame(symptoms))

with st.expander("➕ Add New Symptom Record"):
    with st.form("add_symptom"):
        patient_id = st.text_input("Patient ID")
        symptom_id = st.text_input("Symptom ID")
        severity_id = st.text_input("Severity ID")
        if st.form_submit_button("Submit"):
            res = requests.post(f"{API_BASE}/patient-symptom-records", json={
                "patient_id": patient_id,
                "symptom_id": symptom_id,
                "severity_id": severity_id
            })
            st.success("Symptom recorded" if res.ok else res.text)

# ------------------ Lab Results ------------------
st.header("🧪 Lab Results")
lab_patient_id = st.text_input("Enter patient ID to fetch lab results")
if lab_patient_id:
    res = requests.get(f"{API_BASE}/lab-results", params={"patient_id": lab_patient_id})
    if res.ok:
        st.dataframe(pd.DataFrame(res.json()))
    else:
        st.error(res.text)

# ------------------ Medication Administration ------------------
st.header("💊 Medication Administration Records")
meds = requests.get(f"{API_BASE}/medication-administration").json()
st.dataframe(pd.DataFrame(meds))

with st.expander("➕ Add Medication Admin Record"):
    with st.form("add_admin"):
        med_id = st.text_input("Medication ID")
        result_id = st.text_input("Result ID")
        administered_date = st.date_input("Administered Date")
        if st.form_submit_button("Submit"):
            res = requests.post(f"{API_BASE}/medication-administration", json={
                "medication_id": med_id,
                "result_id": result_id,
                "administered_date": str(administered_date)
            })
            st.success("Admin record added" if res.ok else res.text)

# ------------------ Care Pathways ------------------
st.header("🧭 Care Pathways")
paths = requests.get(f"{API_BASE}/care-pathways").json()
st.dataframe(pd.DataFrame(paths))

# ------------------ Social Determinants ------------------
st.header("🌍 Social Determinants")
with st.form("view_social"):
    patient_social_id = st.text_input("Patient ID for Social Determinants")
    if st.form_submit_button("Fetch"):
        res = requests.get(f"{API_BASE}/patient-social-records/{patient_social_id}/determinant")
        if res.ok:
            st.dataframe(pd.DataFrame(res.json()))
        else:
            st.error(res.text)

with st.expander("➕ Assign Social Determinant"):
    with st.form("assign_social"):
        patient_id = st.text_input("Patient ID")
        determinant_id = st.text_input("Determinant ID")
        impact_level = st.text_input("Impact Level")
        if st.form_submit_button("Submit"):
            res = requests.post(f"{API_BASE}/patient-social-records/{patient_id}/determinant", json={
                "determinant_id": determinant_id,
                "impact_level": impact_level
            })
            st.success("Social determinant assigned" if res.ok else res.text)