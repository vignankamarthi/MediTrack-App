import streamlit as st
from datetime import datetime
import requests

API_URL = "http://web-api:4000"

def render_header(patient_data=None):
    nurse_name = "Nurse Maria Rodriguez"
    nurse_initials = "MR"

    # Default fallback if no patient data is provided
    patient = patient_data or {
        "id": "1",
        "full_name": "John Doe",
        "initials": "JD",
        "age": 56,
        "gender": "Male",
        "admit_date": "2025-03-20",
        "doctor": "Dr. James Wilson"
    }
    
    admit_str = datetime.strptime(patient["admit_date"], "%Y-%m-%d").strftime("%b %d, %Y")

    st.markdown(f"""
        <style>
            .header, .patient-header {{ font-family: 'Segoe UI', sans-serif; }}
            .header {{ display: flex; justify-content: space-between; align-items: center; background-color: #f8f9fa; padding: 1rem; border-bottom: 1px solid #dee2e6; }}
            .logo {{ font-size: 1.8rem; font-weight: bold; color: #005a87; }}
            .user-info {{ display: flex; align-items: center; gap: 1rem; }}
            .user-avatar {{ background-color: #005a87; color: white; border-radius: 50%; width: 36px; height: 36px; display: flex; justify-content: center; align-items: center; font-weight: bold; }}
            .patient-header {{ display: flex; justify-content: space-between; align-items: center; padding: 1rem; border-bottom: 1px solid #ddd; }}
            .patient-info {{ display: flex; gap: 1rem; align-items: center; }}
            .patient-avatar {{ background-color: #17a2b8; color: white; font-weight: bold; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; }}
            .action-buttons {{ display: flex; gap: 0.5rem; }}
            .btn {{ padding: 0.5rem 1rem; border-radius: 6px; cursor: pointer; font-size: 0.9rem; }}
            .btn-outline {{ border: 1px solid #007bff; background-color: white; color: #007bff; }}
            .btn-primary {{ background-color: #007bff; color: white; border: none; }}
        </style>

        <div class="header">
            <div class="logo">MediTrack</div>
            <div class="user-info">
                <span>{nurse_name}</span>
                <div class="user-avatar">{nurse_initials}</div>
            </div>
        </div>

        <div class="patient-header">
            <div class="patient-info">
                <div class="patient-avatar">{patient["initials"]}</div>
                <div class="patient-details">
                    <h2>{patient["full_name"]}</h2>
                    <p>ID: {patient["id"]} • {patient["age"]} years • {patient["gender"]}</p>
                    <p>Admitted: {admit_str} • Primary: {patient["doctor"]}</p>
                </div>
            </div>
            <div class="action-buttons">
                <button class="btn btn-outline">Patient History</button>
                <button class="btn btn-primary">Add Note</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

def get_patient_details(patient_id):
    try:
        response = requests.get(f"{API_URL}/patient-profile", params={"patient_id": patient_id})
        if response.status_code == 200:
            return response.json()
    except:
        return None
    return None
