########################################################
# Routing Connection Matrices for USER PERSONA: PHARMACIST
# 
# Purpose: Allow the physican role to easily analyze data 
# and record new findings.
########################################################

# Required Imports to Establish a Connection
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------

# Create a new Blueprint object for the Pharmacist User Persona
# Allows for a variable to store a collection of routes.
pharmacist = Blueprint('pharmacist', __name__)

#--------------------[ Pharmacist User Persona ~ Sarah Chen #1 ]----------------------
@pharmacist.route('/medication-records/<int:patient_id>', methods=['GET'])
def get_medication_history(patient_id):
    history = [
        {"medication": "Lisinopril", "dosage": "10mg", "frequency": "Daily"},
        {"medication": "Metformin", "dosage": "500mg", "frequency": "Twice a day"}
    ]
    return jsonify(history), 200


@pharmacist.route('/medication-record/<int:patient_id>', methods=['PUT'])
def update_medication_schedule(patient_id):
    data = request.get_json()
    return jsonify({
        "message": f"Updated medication schedule for patient {patient_id}",
        "updated_data": data
    }), 200
