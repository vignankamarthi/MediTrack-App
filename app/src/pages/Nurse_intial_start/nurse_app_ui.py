import streamlit as st
import requests

# Dante LoPriore 
# Bare Logic & Basic Structure to Buil Webpage Using Streamlit

BASE_URL = "http://localhost:5000"  

st.title("Nurse Portal - Patient Care System")

# -----------------------[ Care Tasks ]------------------------
st.header("Care Task Management")

with st.form("create_task"):
    st.subheader("Create New Care Task")
    task_name = st.text_input("Task Name")
    description = st.text_input("Description")
    priority = st.text_input("Priority")
    estimated_duration = st.text_input("Estimated Duration")
    submitted = st.form_submit_button("Create Task")

    if submitted:
        if all([task_name, description, priority, estimated_duration]):
            payload = {
                "task_name": task_name,
                "description": description,
                "priority": priority,
                "estimated_duration": estimated_duration
            }
            response = requests.post(f"{BASE_URL}/care-tasks/", json=payload)
            if response.status_code == 201:
                st.success("Task created successfully!")
            else:
                st.error("Failed to create task. Please try again.")
        else:
            st.warning("Please fill in all fields.")

st.subheader("All Care Tasks")
response = requests.get(f"{BASE_URL}/care-tasks")
if response.status_code == 200:
    tasks = response.json()
    for task in tasks:
        with st.expander(f"{task['task_name']} (Priority: {task['priority']})"):
            st.write("**Description:**", task['description'])
            st.write("**Estimated Duration:**", task['estimated_duration'])
else:
    st.error("Failed to load care tasks.")

# ---------------------- Patient Symptoms ----------------------
st.header("Patient Symptoms")
response = requests.get(f"{BASE_URL}/patient-symptom-records")
if response.status_code == 200:
    symptoms = response.json()
    for sym in symptoms:
        with st.expander(f"{sym['first_name']} {sym['last_name']} - {sym['symptom_name']}"):
            st.write("**Severity:**", sym['severity'])
            st.write("**Description:**", sym['symptom_description'])
else:
    st.error("Failed to load patient symptoms.")

# ----------------------[ Lab Results ]----------------------
st.header("Lab Results Viewer")
lab_patient_id = st.text_input("Enter Patient ID to View Lab Results")
if lab_patient_id:
    response = requests.get(f"{BASE_URL}/lab-results", params={"patient_id": lab_patient_id})
    if response.status_code == 200:
        results = response.json()
        for res in results:
            with st.expander(f"{res['test_name']} ({res['test_date']})"):
                st.write("**Result:**", res['result_value'])
                st.write("**Unit:**", res['unit_of_measure'])
                st.write("**Reference Range:**", res['reference_range'])
                st.write("**Is Abnormal:**", res['is_abnormal'])
    else:
        st.error("Failed to load lab results.")

# ----------------------[ Care Pathways ]----------------------
st.header("Care Pathways")
response = requests.get(f"{BASE_URL}/care-pathways")
if response.status_code == 200:
    pathways = response.json()
    for path in pathways:
        with st.expander(f"{path['pathway_name']}"):
            st.write("**Description:**", path['description'])
            st.write("**Standard Duration:**", path['standard_duration'])
else:
    st.error("Failed to load care pathways.")

