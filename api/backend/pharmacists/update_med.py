import streamlit as st
import requests

st.title("Update Medication Record")

record_id = st.text_input("Medication Record ID")
new_dosage = st.text_input("New Dosage")
new_frequency = st.text_input("New Frequency")

if st.button("Update Record"):
    if not record_id or not new_dosage or not new_frequency:
        st.error("Please fill in all fields.")
    else:
        try:
            response = requests.put(
                f"http://localhost:3111/medication-records/{record_id}",
                json={"dosage": new_dosage, "frequency": new_frequency}
            )

            if response.status_code == 200:
                st.success("Medication record updated successfully.")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Connection error: {e}")
