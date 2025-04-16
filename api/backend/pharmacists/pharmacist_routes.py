########################################################
# Pharmacist routes blueprint file
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
pharmacists = Blueprint("pharmacists", __name__)


# ------------------------------------------------------------
# Get medication history for a specific patient [Sarah-1]
@pharmacists.route("/medication-records/<patient_id>", methods=["GET"])
def get_medication_records(patient_id):
    try:
        current_app.logger.info(f"GET /medication-records/{patient_id} route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT mr.patient_id, m.medication_name, 
                      mr.dosage, mr.frequency 
                      FROM medication_record mr
                      JOIN MEDICATIONS m ON mr.medication_id = m.medication_id
                      WHERE mr.patient_id = {0}""".format(
                patient_id
            )
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /medication-records/{patient_id} (pharmacist) failed: {str(e)}"
        )
        return make_response(
            jsonify({"error": "Failed to retrieve medication records"}), 500
        )


# ------------------------------------------------------------
# Get all medications from the database [Sarah-1]
@pharmacists.route("/medications", methods=["GET"])
def get_medications():
    try:
        current_app.logger.info("GET /medications route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT medication_id, medication_name, generic_name,
                      medication_class, dosage_form, strength,
                      manufacturer, ndc_code, is_controlled, control_class
                      FROM MEDICATIONS"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /medications (pharmacist) failed: {str(e)}"
        )
        return make_response(
            jsonify({"error": "Failed to retrieve medications database"}), 500
        )


# ------------------------------------------------------------
# Get prescription outcomes [Sarah-2]
@pharmacists.route("/prescription-outcome-records", methods=["GET"])
def get_prescription_outcomes():
    try:
        current_app.logger.info("GET /prescription-outcome-records route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT por.outcome_id, por.prescription_id, 
                      p.prescription_date, p.duration, p.refills,
                      to1.outcome_name, por.effectiveness
                      FROM prescription_outcome_record por
                      JOIN PRESCRIPTIONS p ON por.prescription_id = p.prescription_id
                      JOIN TREATMENT_OUTCOMES to1 ON por.outcome_id = to1.outcome_id
                      ORDER BY p.prescription_date DESC"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /prescription-outcome-records (pharmacist) failed: {str(e)}"
        )
        return make_response(
            jsonify({"error": "Failed to retrieve prescription outcomes"}), 500
        )


# ------------------------------------------------------------
# Get patient education records [Sarah-4]
@pharmacists.route("/patient-education", methods=["GET"])
def get_patient_education():
    try:
        current_app.logger.info("GET /patient-education route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT pe.record_id, pe.provider_id, hp.first_name, hp.last_name,
                      pe.comprehension_level, pe.notes
                      FROM PATIENT_EDUCATION pe
                      JOIN HEALTHCARE_PROVIDER hp ON pe.provider_id = hp.provider_id
                      ORDER BY pe.record_id"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /patient-education (pharmacist) failed: {str(e)}"
        )
        return make_response(
            jsonify({"error": "Failed to retrieve education records"}), 500
        )


# ------------------------------------------------------------
# View education-patient relationships [Sarah-4]
@pharmacists.route("/patient-education-records", methods=["GET"])
def get_patient_education_records():
    try:
        current_app.logger.info("GET /patient-education-records route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT per.patient_id, p.first_name, p.last_name, 
                      per.education_id, pe.comprehension_level,
                      pe.notes, per.education_date, hp.first_name as provider_first_name,
                      hp.last_name as provider_last_name
                      FROM patient_education_record per
                      JOIN PATIENT p ON per.patient_id = p.patient_id
                      JOIN PATIENT_EDUCATION pe ON per.education_id = pe.record_id
                      JOIN HEALTHCARE_PROVIDER hp ON pe.provider_id = hp.provider_id
                      ORDER BY per.education_date DESC, p.last_name, p.first_name"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /patient-education-records (pharmacist) failed: {str(e)}"
        )
        return make_response(
            jsonify({"error": "Failed to retrieve education-patient relationships"}),
            500,
        )


# ------------------------------------------------------------
# Return patient medication schedule [Sarah-5]
@pharmacists.route("/medication-record/<patient_id>", methods=["GET"])
def get_medication_schedule(patient_id):
    try:
        current_app.logger.info(f"GET /medication-record/{patient_id} route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT mr.patient_id, p.first_name, p.last_name, 
                      mr.medication_id, m.medication_name, m.generic_name,
                      m.dosage_form, m.strength, mr.dosage, mr.frequency
                      FROM medication_record mr
                      JOIN PATIENT p ON mr.patient_id = p.patient_id
                      JOIN MEDICATIONS m ON mr.medication_id = m.medication_id
                      WHERE mr.patient_id = {0}
                      ORDER BY m.medication_name""".format(
                patient_id
            )
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /medication-record/{patient_id} (pharmacist) failed: {str(e)}"
        )
        return make_response(
            jsonify({"error": "Failed to retrieve patient medication schedule"}), 500
        )


# ------------------------------------------------------------
# Generate medication reconciliation data [Sarah-6]
@pharmacists.route("/prescription-patient-records/<patient_id>", methods=["GET"])
def get_medication_reconciliation(patient_id):
    try:
        current_app.logger.info(f"GET /prescription-patient-records/{patient_id} route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT ppr.patient_id, p.first_name, p.last_name, 
                      ppr.prescription_id, pr.prescription_date,
                      pr.duration, pr.refills, pr.instructions,
                      hp.first_name as prescriber_first_name, hp.last_name as prescriber_last_name,
                      m.medication_name, m.generic_name, m.dosage_form, 
                      m.strength, mpr.dosage, mpr.route
                      FROM prescription_patient_record ppr
                      JOIN PATIENT p ON ppr.patient_id = p.patient_id
                      JOIN PRESCRIPTIONS pr ON ppr.prescription_id = pr.prescription_id
                      JOIN HEALTHCARE_PROVIDER hp ON pr.prescriber_id = hp.provider_id
                      JOIN medication_prescription_record mpr ON pr.prescription_id = mpr.prescription_id
                      JOIN MEDICATIONS m ON mpr.medication_id = m.medication_id
                      WHERE ppr.patient_id = {0}
                      ORDER BY pr.prescription_date DESC""".format(
                patient_id
            )
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /prescription-patient-records/{patient_id} (pharmacist) failed: {str(e)}"
        )
        return make_response(
            jsonify({"error": "Failed to generate medication reconciliation data"}), 500
        )


# ------------------------------------------------------------
# Add new medication to patient record [Sarah-1]
@pharmacists.route("/medication-records/<patient_id>", methods=["POST"])
def add_medication_to_patient(patient_id):
    try:
        current_app.logger.info(f"POST /medication-records/{patient_id} route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        medication_id = data.get("medication_id")
        dosage = data.get("dosage")
        frequency = data.get("frequency")

        # Validate required fields
        if not medication_id:
            return make_response(
                jsonify({"error": "Missing required field: medication_id is required"}),
                400,
            )

        # Check if patient exists
        cursor.execute(
            f"SELECT patient_id FROM PATIENT WHERE patient_id = {patient_id}"
        )
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Patient not found"}), 404)

        # Check if medication exists
        cursor.execute(
            f"SELECT medication_id FROM MEDICATIONS WHERE medication_id = {medication_id}"
        )
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Medication not found"}), 404)

        # Check if medication record already exists
        cursor.execute(
            f"""SELECT patient_id 
                FROM medication_record 
                WHERE patient_id = {patient_id} AND medication_id = {medication_id}"""
        )
        if cursor.fetchone():
            return make_response(
                jsonify(
                    {"error": "This medication is already in the patient's record"}
                ),
                409,
            )

        insert_sql_query = """
            INSERT INTO medication_record (
                patient_id, 
                medication_id,
                dosage,
                frequency
            ) VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            insert_sql_query,
            (patient_id, medication_id, dosage, frequency),
        )

        db.get_db().commit()

        the_response = make_response(
            jsonify({"message": "Medication successfully added to patient record"}), 201
        )
        return the_response

    except Exception as e:
        current_app.logger.error(
            f"Route POST /medication-records/{patient_id} (pharmacist) failed: {str(e)}"
        )
        db.get_db().rollback()
        return make_response(
            jsonify({"error": "Failed to add medication to patient record"}), 500
        )


# ------------------------------------------------------------
# Create new patient education record [Sarah-4]
@pharmacists.route("/patient-education", methods=["POST"])
def create_patient_education():
    try:
        current_app.logger.info("POST /patient-education route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        provider_id = data.get("provider_id")
        comprehension_level = data.get("comprehension_level")
        notes = data.get("notes")

        # Validate required fields
        if not provider_id:
            return make_response(
                jsonify({"error": "Missing required field: provider_id is required"}),
                400,
            )

        # Check if provider exists
        cursor.execute(
            f"SELECT provider_id FROM HEALTHCARE_PROVIDER WHERE provider_id = {provider_id}"
        )
        if not cursor.fetchone():
            return make_response(
                jsonify({"error": "Healthcare provider not found"}), 404
            )

        insert_sql_query = """
            INSERT INTO PATIENT_EDUCATION (
                provider_id, 
                comprehension_level,
                notes
            ) VALUES (%s, %s, %s)
        """

        cursor.execute(
            insert_sql_query,
            (provider_id, comprehension_level, notes),
        )

        db.get_db().commit()

        # Get the ID of the newly created education record
        cursor.execute("SELECT LAST_INSERT_ID()")
        new_education_id = cursor.fetchone()["LAST_INSERT_ID()"]

        the_response = make_response(
            jsonify(
                {
                    "message": "New patient education record successfully created",
                    "education_id": new_education_id,
                }
            ),
            201,
        )
        return the_response

    except Exception as e:
        current_app.logger.error(
            f"Route POST /patient-education (pharmacist) failed: {str(e)}"
        )
        db.get_db().rollback()
        return make_response(
            jsonify({"error": "Failed to create new patient education record"}), 500
        )


# ------------------------------------------------------------
# Create patient-education relationship [Sarah-4]
@pharmacists.route("/patient-education-records", methods=["POST"])
def create_patient_education_relationship():
    try:
        current_app.logger.info("POST /patient-education-records route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        patient_id = data.get("patient_id")
        education_id = data.get("education_id")
        education_date = data.get("education_date")

        # Validate required fields
        if not all([patient_id, education_id]):
            return make_response(
                jsonify(
                    {
                        "error": "Missing required fields: patient_id and education_id are required"
                    }
                ),
                400,
            )

        # Check if patient exists
        cursor.execute(
            f"SELECT patient_id FROM PATIENT WHERE patient_id = {patient_id}"
        )
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Patient not found"}), 404)

        # Check if education record exists
        cursor.execute(
            f"SELECT record_id FROM PATIENT_EDUCATION WHERE record_id = {education_id}"
        )
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Education record not found"}), 404)

        # Check if relationship already exists
        cursor.execute(
            f"""SELECT patient_id 
                FROM patient_education_record 
                WHERE patient_id = {patient_id} AND education_id = {education_id}"""
        )
        if cursor.fetchone():
            return make_response(
                jsonify(
                    {"error": "This patient-education relationship already exists"}
                ),
                409,
            )

        insert_sql_query = """
            INSERT INTO patient_education_record (
                patient_id, 
                education_id,
                education_date
            ) VALUES (%s, %s, %s)
        """

        cursor.execute(
            insert_sql_query,
            (patient_id, education_id, education_date),
        )

        db.get_db().commit()

        the_response = make_response(
            jsonify({"message": "Patient-education relationship successfully created"}),
            201,
        )
        return the_response

    except Exception as e:
        current_app.logger.error(
            f"Route POST /patient-education-records (pharmacist) failed: {str(e)}"
        )
        db.get_db().rollback()
        return make_response(
            jsonify({"error": "Failed to create patient-education relationship"}), 500
        )


# ------------------------------------------------------------
# Update prescription effectiveness [Sarah-2]
@pharmacists.route("/prescription-outcome-records", methods=["PUT"])
def update_prescription_effectiveness():
    try:
        current_app.logger.info("PUT /prescription-outcome-records route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        outcome_id = data.get("outcome_id")
        prescription_id = data.get("prescription_id")
        effectiveness = data.get("effectiveness")

        # Validate required fields
        if not all([outcome_id, prescription_id, effectiveness]):
            return make_response(
                jsonify(
                    {
                        "error": "Missing required fields: outcome_id, prescription_id, and effectiveness are required"
                    }
                ),
                400,
            )

        # Check if record exists
        cursor.execute(
            f"""SELECT outcome_id 
                FROM prescription_outcome_record 
                WHERE outcome_id = {outcome_id} AND prescription_id = {prescription_id}"""
        )
        if not cursor.fetchone():
            return make_response(
                jsonify({"error": "Prescription outcome record not found"}), 404
            )

        # Execute update query
        update_query = """
            UPDATE prescription_outcome_record 
            SET effectiveness = %s 
            WHERE outcome_id = %s AND prescription_id = %s
        """
        cursor.execute(update_query, (effectiveness, outcome_id, prescription_id))

        db.get_db().commit()

        the_response = make_response(
            jsonify({"message": "Prescription effectiveness successfully updated"}), 200
        )
        return the_response

    except Exception as e:
        current_app.logger.error(
            f"Route PUT /prescription-outcome-records (pharmacist) failed: {str(e)}"
        )
        db.get_db().rollback()
        return make_response(
            jsonify({"error": "Failed to update prescription effectiveness"}), 500
        )


# ------------------------------------------------------------
# Update dosage and frequency [Sarah-5]
@pharmacists.route("/medication-record/<patient_id>", methods=["PUT"])
def update_medication_dosage_frequency(patient_id):
    try:
        current_app.logger.info(f"PUT /medication-record/{patient_id} route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        medication_id = data.get("medication_id")
        dosage = data.get("dosage")
        frequency = data.get("frequency")

        # Validate required fields
        if not medication_id:
            return make_response(
                jsonify({"error": "Missing required field: medication_id is required"}),
                400,
            )

        # At least one of these fields must be present
        if not any([dosage, frequency]):
            return make_response(
                jsonify(
                    {"error": "At least one of dosage or frequency must be provided"}
                ),
                400,
            )

        # Check if record exists
        cursor.execute(
            f"""SELECT patient_id 
                FROM medication_record 
                WHERE patient_id = {patient_id} AND medication_id = {medication_id}"""
        )
        if not cursor.fetchone():
            return make_response(
                jsonify({"error": "Medication record not found for this patient"}), 404
            )

        # Build the update query based on provided fields
        update_fields = []
        params = []

        if dosage is not None:
            update_fields.append("dosage = %s")
            params.append(dosage)

        if frequency is not None:
            update_fields.append("frequency = %s")
            params.append(frequency)

        # Add patient_id and medication_id to params
        params.append(patient_id)
        params.append(medication_id)

        # Execute update query
        update_query = f"""
            UPDATE medication_record 
            SET {', '.join(update_fields)} 
            WHERE patient_id = %s AND medication_id = %s
        """
        cursor.execute(update_query, params)

        db.get_db().commit()

        # Check if any rows were affected
        if cursor.rowcount == 0:
            return make_response(
                jsonify({"error": "No changes made to medication record"}), 400
            )

        the_response = make_response(
            jsonify(
                {"message": "Medication dosage and/or frequency successfully updated"}
            ),
            200,
        )
        return the_response

    except Exception as e:
        current_app.logger.error(
            f"Route PUT /medication-record/{patient_id} (pharmacist) failed: {str(e)}"
        )
        db.get_db().rollback()
        return make_response(
            jsonify({"error": "Failed to update medication dosage and frequency"}), 500
        )
