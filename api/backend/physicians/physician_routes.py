########################################################
# Physician routes blueprint file
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

# ------------------------------------------------------------
# Create a new Blueprint object, which is a collection of
# routes.
physicians = Blueprint("physicians", __name__)


# Get treatment outcomes with effectiveness ratings [James-1]
@physicians.route("/treatment-outcomes", methods=["GET"])
def get_treatment_outcomes():
    try:
        current_app.logger.info("GET /treatment-outcomes route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT to1.outcome_id, t.treatment_name, 
                      to1.outcome_name, to1.description, to1.is_positive
                      FROM TREATMENT_OUTCOMES to1
                      JOIN TREATMENT t ON to1.treatment_id = t.treatment_id"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /treatment-outcomes (physician) failed: {str(e)}"
        )
        return make_response(
            jsonify({"error": "Failed to retrieve treatment outcomes"}), 500
        )


# Return all medical conditions [James-1]
@physicians.route("/medical-conditions", methods=["GET"])
def get_list_medical_conditions():
    try:
        current_app.logger.info("GET /medical-conditions route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT condition_id, condition_name, description, icd_code, is_chronic
               FROM MEDICAL_CONDITION"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /medical-conditions (physician) failed: {str(e)}"
        )
        return make_response(
            jsonify({"error": "Failed to retrieve medical conditions"}), 500
        )


# Return specific condition details with related treatments [James-1]
@physicians.route("/condition-treatment-protocol/<condition_id>", methods=["GET"])
def get_known_side_effects_from_treatment(condition_id):
    try:
        current_app.logger.info(
            f"GET /condition-treatment-protocol/{condition_id} route"
        )
        cursor = db.get_db().cursor()
        cursor.execute(
            f"""SELECT mc.condition_name, mc.description AS condition_description, 
                 t.treatment_name, t.description AS treatment_description, 
                 to1.outcome_name AS possible_outcome, to1.description AS outcome_description, to1.is_positive
                 FROM condition_treatment_protocol ctp
                 JOIN MEDICAL_CONDITION mc ON ctp.condition_id = mc.condition_id
                 JOIN TREATMENT t ON ctp.treatment_id = t.treatment_id
                 LEFT JOIN TREATMENT_OUTCOMES to1 ON t.treatment_id = to1.treatment_id
                 WHERE ctp.condition_id = {condition_id}
            """
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /condition-treatment-protocol/{condition_id} (physician) failed: {str(e)}"
        )
        return make_response(
            jsonify(
                {
                    "error": "Failed to retrieve treatment protocols for specified condition"
                }
            ),
            500,
        )


# Return patient medication records for adherence analysis [James-2]
@physicians.route("/medication-records/<patient_id>", methods=["GET"])
def get_medication_records(patient_id):
    try:
        current_app.logger.info(f"GET /medication-records/{patient_id} route")
        cursor = db.get_db().cursor()
        cursor.execute(
            f"""SELECT med.medication_name, med.generic_name, med.dosage_form, med.strength, 
                 mr.dosage, mr.frequency, al.log_id, al.action_type, al.table_affected, 
                 al.details, al.ip_address, al.action_timestamp
                 FROM medication_record mr
                 JOIN MEDICATIONS med ON mr.medication_id = med.medication_id
                 LEFT JOIN audit_patient_record apr ON mr.patient_id = apr.patient_id
                 LEFT JOIN AUDIT_LOGS al ON al.log_id = apr.log_id
                 WHERE mr.patient_id = {patient_id}
            """
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /medication-records/{patient_id} (physician) failed: {str(e)}"
        )
        return make_response(
            jsonify(
                {
                    "error": "Failed to retrieve medication records for the specified patient"
                }
            ),
            500,
        )


# Return provider performance metrics [James-4]
@physicians.route("/healthcare-providers", methods=["GET"])
def get_healthcare_provider_performance_metrics():
    try:
        current_app.logger.info("GET /healthcare-providers route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT hp.provider_id, hp.first_name, hp.last_name, hp.specialization, hp.department, 
               COUNT(DISTINCT ptr.treatment_id) AS treatments_managed, 
               COUNT(DISTINCT ppr.patient_id) AS patients_served, 
               COUNT(DISTINCT pe.record_id) AS amount_education_sessions, 
               COUNT(DISTINCT pr.prescription_id) AS amount_prescriptions_written, 
               COUNT(DISTINCT ppr2.protocol_id) AS amount_protocols
               FROM HEALTHCARE_PROVIDER hp
               LEFT JOIN provider_treatment_record ptr ON hp.provider_id = ptr.provider_id
               LEFT JOIN patient_provider_record ppr ON hp.provider_id = ppr.provider_id
               LEFT JOIN PATIENT_EDUCATION pe ON pe.provider_id = hp.provider_id
               LEFT JOIN PRESCRIPTIONS pr ON hp.provider_id = pr.prescriber_id
               LEFT JOIN provider_protocol_record ppr2 ON hp.provider_id = ppr2.provider_id
               GROUP BY hp.provider_id
               ORDER BY hp.first_name, hp.last_name
            """
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /healthcare-providers (physician) failed: {str(e)}"
        )
        return make_response(
            jsonify(
                {"error": "Failed to retrieve healthcare provider performance metrics"}
            ),
            500,
        )


# Return all clinical protocols [James-5]
@physicians.route("/clinical-protocols", methods=["GET"])
def get_all_clinical_protocols():
    try:
        current_app.logger.info("GET /clinical-protocols route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT protocol_id, protocol_name, description, version, effective_date,
               expiration_date, is_active, created_at, updated_at
               FROM CLINICAL_PROTOCOL
            """
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /clinical-protocols (physician) failed: {str(e)}"
        )
        return make_response(
            jsonify({"error": "Failed to retrieve clinical protocols"}), 500
        )


# Return specific protocol details [James-5]
@physicians.route("/clinical-protocols/<protocol_id>", methods=["GET"])
def get_protocol_details(protocol_id):
    try:
        current_app.logger.info(f"GET /clinical-protocols/{protocol_id} route")
        cursor = db.get_db().cursor()
        cursor.execute(
            f"""SELECT protocol_id, protocol_name, description, version, effective_date, expiration_date,
               is_active, created_at, updated_at
               FROM CLINICAL_PROTOCOL
               WHERE protocol_id = {protocol_id}
            """
        )

        theData = cursor.fetchall()

        if not theData:
            return make_response(jsonify({"error": "Protocol not found"}), 404)

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /clinical-protocols/{protocol_id} (physician) failed: {str(e)}"
        )
        return make_response(
            jsonify({"error": "Failed to retrieve protocol details"}), 500
        )


# Return treatment records for readmission analysis [James-6]
@physicians.route("/patient-treatment-records", methods=["GET"])
def get_treatment_records():
    try:
        current_app.logger.info("GET /patient-treatment-records route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT ptr.patient_id, p.first_name, p.last_name, t.treatment_name, 
               ptr.start_date, ptr.end_date, ptr.status
               FROM patient_treatment_record ptr
               JOIN PATIENT p ON ptr.patient_id = p.patient_id
               JOIN TREATMENT t ON ptr.treatment_id = t.treatment_id
               ORDER BY ptr.start_date DESC, ptr.patient_id
            """
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /patient-treatment-records (physician) failed: {str(e)}"
        )
        return make_response(
            jsonify({"error": "Failed to retrieve patient treatment records"}), 500
        )


# Create new clinical protocol [James-5]
@physicians.route("/clinical-protocols", methods=["POST"])
def create_new_clinical_protocol():
    try:
        current_app.logger.info("POST /clinical-protocols route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        protocol_name = data.get("protocol_name")
        description = data.get("description")
        version = data.get("version")
        effective_date = data.get("effective_date")
        expiration_date = data.get("expiration_date")
        is_active = data.get("is_active", True)

        # Validate required fields
        if not all([protocol_name, version, effective_date]):
            return make_response(
                jsonify(
                    {
                        "error": "Missing required fields: protocol_name, version, and effective_date are required"
                    }
                ),
                400,
            )

        insert_sql_query = """
            INSERT INTO CLINICAL_PROTOCOL (
                protocol_name, 
                description,
                version, 
                effective_date,
                expiration_date, 
                is_active
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            insert_sql_query,
            (
                protocol_name,
                description,
                version,
                effective_date,
                expiration_date,
                is_active,
            ),
        )

        db.get_db().commit()

        the_response = make_response(
            jsonify({"message": "New Clinical Protocol was Successfully Created"}), 201
        )
        return the_response

    except Exception as e:
        current_app.logger.error(
            f"Route POST /clinical-protocols (physician) failed: {str(e)}"
        )
        db.get_db().rollback() 
        return make_response(
            jsonify({"error": "Failed to create new clinical protocol"}), 500
        )


# Update protocol status (active/inactive) [James-5]
@physicians.route("/clinical-protocols/<protocol_id>", methods=["PUT"])
def update_protocol_status(protocol_id):
    try:
        current_app.logger.info(f"PUT /clinical-protocols/{protocol_id} route")

        data = request.get_json()
        # Allow full update of protocol details
        protocol_name = data.get("protocol_name")
        description = data.get("description")
        version = data.get("version")
        effective_date = data.get("effective_date")
        expiration_date = data.get("expiration_date")
        is_active = data.get("is_active")

        # Validate that at least some data was provided
        if not any(
            [
                protocol_name,
                description,
                version,
                effective_date,
                expiration_date,
                is_active is not None,
            ]
        ):
            return make_response(jsonify({"error": "No update data provided"}), 400)

        # Check if protocol exists
        cursor = db.get_db().cursor()
        cursor.execute(
            "SELECT protocol_id FROM CLINICAL_PROTOCOL WHERE protocol_id = %s",
            (protocol_id,),
        )
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Protocol not found"}), 404)

        # Build the update query based on provided fields
        update_fields = []
        params = []

        if protocol_name:
            update_fields.append("protocol_name = %s")
            params.append(protocol_name)

        if description:
            update_fields.append("description = %s")
            params.append(description)

        if version:
            update_fields.append("version = %s")
            params.append(version)

        if effective_date:
            update_fields.append("effective_date = %s")
            params.append(effective_date)

        if expiration_date:
            update_fields.append("expiration_date = %s")
            params.append(expiration_date)

        if is_active is not None:
            update_fields.append("is_active = %s")
            params.append(is_active)

        # Add the updated_at field
        update_fields.append("updated_at = CURRENT_TIMESTAMP")

        # Add protocol_id to params
        params.append(protocol_id)

        # Execute update query
        update_query = f"UPDATE CLINICAL_PROTOCOL SET {', '.join(update_fields)} WHERE protocol_id = %s"
        cursor.execute(update_query, params)

        db.get_db().commit()

        # Check if any rows were affected
        if cursor.rowcount == 0:
            return make_response(jsonify({"error": "No changes made to protocol"}), 400)

        the_response = make_response(
            jsonify({"message": "Successfully updated clinical protocol"}), 200
        )
        return the_response

    except Exception as e:
        current_app.logger.error(
            f"Route PUT /clinical-protocols/{protocol_id} (physician) failed: {str(e)}"
        )
        db.get_db().rollback() 
        return make_response(
            jsonify({"error": "Failed to update protocol status"}), 500
        )
