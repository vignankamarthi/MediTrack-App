import streamlit as st
import requests
from layout_template import render_header
from datetime import datetime

API_URL = "http://web-api:4000"

def run():
    render_header()

    st.markdown("## 🔬 Lab Results Viewer")

    patient_id = st.session_state.get("current_patient_id")
    if not patient_id:
        st.warning("No patient selected. Please select a patient first.")
        return

    try:
        response = requests.get(f"{API_URL}/lab-results", params={"patient_id": patient_id})
        response.raise_for_status()
        lab_results = response.json()
    except Exception as e:
        st.error(f"Error fetching lab results: {e}")
        return

    if lab_results:
        for lab in lab_results:
            with st.expander(f"{lab['test_name']} ({str(lab['test_date'])})"):
                st.write(f"**Result:** {lab['result_value']} {lab['unit_of_measure']}")
                st.write(f"**Reference Range:** {lab['reference_range']}")
                st.write(f"**Abnormal:** {'Yes' if lab['is_abnormal'] else 'No'}")
                st.write(f"**Notes:** {lab['lab_notes'] or 'None'}")
                st.write(f"**Result Date:** {lab['result_date']}")

                if st.button(" Mark as Reviewed", key=f"mark_reviewed_{lab['result_id']}"):
                    try:
                        resp = requests.put(f"{API_URL}/lab-results", json={
                            "result_id": lab['result_id'],
                            "is_reviewed": True
                        })
                        if resp.status_code == 200:
                            st.success("Marked as reviewed")
                            st.experimental_rerun()
                        else:
                            st.error("Failed to update review status")
                    except Exception as e:
                        st.error(f"Error: {e}")
    else:
        st.info("No lab results found.")

    st.markdown("##  Medication Administration Records")

    try:
        response = requests.get(f"{API_URL}/medication-administration")
        response.raise_for_status()
        admin_records = response.json()
    except Exception as e:
        st.error(f"Error loading medication administration records: {e}")
        return

    for i, med in enumerate(admin_records):
        with st.expander(f"{med['medication_name']} - Administered on {med['administered_date']}", expanded=False):
            st.write(f"**Dosage Form:** {med['dosage_form']}")
            st.write(f"**Strength:** {med['strength']}")
            st.write(f"**Related Lab Result ID:** {med['result_id']}")

    st.markdown("###  Add Medication Administration Record")

    with st.form("new_admin_form"):
        medication_id = st.text_input("Medication ID", key="med_id_input")
        result_id = st.text_input("Lab Result ID", key="lab_result_id_input")
        administered_date = st.date_input("Administered Date", value=datetime.today(), key="admin_date_input")

        submitted = st.form_submit_button("Submit Record", key="submit_admin_record")
        if submitted:
            data = {
                "medication_id": medication_id,
                "result_id": result_id,
                "administered_date": administered_date.strftime("%Y-%m-%d")
            }
            try:
                resp = requests.post(f"{API_URL}/medication-administration", json=data)
                if resp.status_code == 200:
                    st.success(" Administration record added!")
                    st.experimental_rerun()
                else:
                    st.error(f" Failed to add record: {resp.status_code}")
            except Exception as e:
                st.error(f"Error: {e}")
          
def social_determinant_ui():
    st.markdown("##  Social Determinants Manager")

    patient_id = st.text_input("Patient ID", value="1", key="social_patient_id")

    # Assign New Social Determinant
    with st.form("assign_determinant_form"):
        st.subheader("➕ Assign New Social Determinant")
        determinant_id = st.text_input("Determinant ID", key="assign_determinant_id")
        impact_level = st.selectbox("Impact Level", ["Low", "Medium", "High"], key="assign_impact_level")

        assign_submitted = st.form_submit_button("Assign Determinant", key="assign_determinant_button")
        if assign_submitted:
            data = {
                "patient_id": patient_id,
                "determinant_id": determinant_id,
                "impact_level": impact_level
            }
            try:
                resp = requests.post(
                    f"{API_URL}/patient-social-records/{patient_id}/determinant",
                    json=data
                )
                if resp.status_code == 201:
                    st.success("✅ Determinant assigned to patient!")
                else:
                    st.error(f"❌ Failed to assign: {resp.status_code}")
            except Exception as e:
                st.error(f"Error: {e}")

    # Update Existing Social Determinant
    with st.form("update_determinant_form"):
        st.subheader(" Update Impact Level of Assigned Determinant")
        update_determinant_id = st.text_input("Determinant ID to Update", key="update_determinant_id")
        new_impact_level = st.selectbox("New Impact Level", ["Low", "Medium", "High"], key="update_impact_level")

        update_submitted = st.form_submit_button("Update Impact Level", key="update_impact_button")
        if update_submitted:
            data = {"impact_level": new_impact_level}
            try:
                resp = requests.put(
                    f"{API_URL}/patient-social-records/{patient_id}/determinant/{update_determinant_id}",
                    json=data
                )
                if resp.status_code == 200:
                    st.success(" Impact level updated!")
                else:
                    st.error(f" Update failed: {resp.status_code}")
            except Exception as e:
                st.error(f"Error: {e}")
