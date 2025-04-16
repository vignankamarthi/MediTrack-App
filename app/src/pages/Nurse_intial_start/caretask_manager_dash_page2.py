import streamlit as st
import requests

API_BASE = "http://localhost:4000"

def run():
    st.title("📝 Care Task Manager")

    if st.button("Load All Care Tasks"):
        res = requests.get(f"{API_BASE}/care-tasks")
        if res.ok:
            st.table(res.json())

    st.subheader("➕ Create New Care Task")
    with st.form("create_task"):
        task_name = st.text_input("Task Name")
        description = st.text_area("Description")
        priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        duration = st.number_input("Estimated Duration (min)", min_value=1)
        submitted = st.form_submit_button("Submit")
        if submitted:
            payload = {
                "task_name": task_name,
                "description": description,
                "priority": priority,
                "estimated_duration": duration,
            }
            r = requests.post(f"{API_BASE}/care-tasks/", json=payload)
            st.success(r.json()["message"])
