import streamlit as st
import requests

API_BASE = "http://localhost:4000"

def run():
    st.title("🔬 Lab Results Viewer")

    patient_id = st.text_input("Enter Patient ID to View Lab Results")
    if st.button("Fetch Lab Results") and patient_id:
        res = requests.get(f"{API_BASE}/lab-results", params={"patient_id": patient_id})
        if res.ok:
            lab_data = res.json()
            st.dataframe(lab_data)
        else:
            st.error(res.json().get("error", "Unknown error"))

    st.subheader("✅ Mark Lab Result Reviewed")
    with st.form("review_result"):
        result_id = st.text_input("Result ID")
        reviewed = st.checkbox("Mark as Reviewed", value=True)
        submit_review = st.form_submit_button("Update Status")
        if submit_review:
            res = requests.put(f"{API_BASE}/lab-results", json={
                "result_id": result_id,
                "is_reviewed": reviewed
            })
            st.success(res.json()["message"])
