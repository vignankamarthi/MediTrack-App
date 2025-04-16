########################################################
# Nurse routes blueprint file
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
nurses = Blueprint("nurses", __name__)


# ------------------------------------------------------------
# Get all care tasks from the system [Maria-1]
@nurses.route("/care-tasks", methods=["GET"])
def get_care_tasks():
    try:
        current_app.logger.info("GET /care-tasks route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT task_id, task_name, description, 
                    priority, estimated_duration FROM CARE_TASKS"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(f"Route GET /care-tasks (nurse) failed: {str(e)}")
        return make_response(jsonify({"error": "Failed to retrieve care tasks"}), 500)


# ------------------------------------------------------------
# Get specific task details [Maria-1]
@nurses.route("/care-tasks/<task_id>", methods=["GET"])
def get_task_details(task_id):
    try:
        current_app.logger.info(f"GET /care-tasks/{task_id} route")
        cursor = db.get_db().cursor()
        cursor.execute(
            f"""SELECT task_id, task_name, description, priority, estimated_duration 
               FROM CARE_TASKS 
               WHERE task_id = {task_id}"""
        )

        theData = cursor.fetchall()

        if not theData:
            return make_response(jsonify({"error": "Task not found"}), 404)

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(f"Route GET /care-tasks/{task_id} (nurse) failed: {str(e)}")
        return make_response(jsonify({"error": "Failed to retrieve task details"}), 500)


# ------------------------------------------------------------
# Get patient symptom records [Maria-2]
@nurses.route("/patient-symptom-records", methods=["GET"])
def get_patient_symptom_records():
    try:
        current_app.logger.info("GET /patient-symptom-records route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT psr.patient_id, p.first_name, p.last_name, 
                  s.symptom_name, s.description, psr.severity 
               FROM patient_symptom_record psr
               JOIN PATIENT p ON psr.patient_id = p.patient_id
               JOIN SYMPTOMS s ON psr.symptom_id = s.symptom_id
               ORDER BY p.last_name, p.first_name, s.symptom_name"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(f"Route GET /patient-symptom-records (nurse) failed: {str(e)}")
        return make_response(jsonify({"error": "Failed to retrieve patient symptom records"}), 500)


# ------------------------------------------------------------
# Get lab results [Maria-3]
@nurses.route("/lab-results", methods=["GET"])
def get_lab_results():
    try:
        current_app.logger.info("GET /lab-results route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT lr.result_id, lr.patient_id, p.first_name, p.last_name, 
                  lr.test_name, lr.test_date, lr.result_date, 
                  lr.result_value, lr.reference_range, lr.unit_of_measure, 
                  lr.is_abnormal, lr.lab_notes 
               FROM LAB_RESULTS lr
               JOIN PATIENT p ON lr.patient_id = p.patient_id
               ORDER BY lr.result_date DESC, p.last_name, p.first_name"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(f"Route GET /lab-results (nurse) failed: {str(e)}")
        return make_response(jsonify({"error": "Failed to retrieve lab results"}), 500)


# ------------------------------------------------------------
# Get medication administration records [Maria-4]
@nurses.route("/medication-administration", methods=["GET"])
def get_medication_administration():
    try:
        current_app.logger.info("GET /medication-administration route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT ma.medication_id, m.medication_name, m.dosage_form, m.strength,
                  ma.result_id, lr.patient_id, p.first_name, p.last_name,
                  ma.administered_date, lr.test_name, lr.result_value, lr.unit_of_measure
               FROM medication_administration ma
               JOIN MEDICATIONS m ON ma.medication_id = m.medication_id
               JOIN LAB_RESULTS lr ON ma.result_id = lr.result_id
               JOIN PATIENT p ON lr.patient_id = p.patient_id
               ORDER BY ma.administered_date DESC, p.last_name, p.first_name"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(f"Route GET /medication-administration (nurse) failed: {str(e)}")
        return make_response(jsonify({"error": "Failed to retrieve medication administration records"}), 500)


# ------------------------------------------------------------
# Get all care pathways [Maria-5]
@nurses.route("/care-pathways", methods=["GET"])
def get_care_pathways():
    try:
        current_app.logger.info("GET /care-pathways route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT pathway_id, pathway_name, description, standard_duration, is_active
               FROM CARE_PATHWAY
               ORDER BY pathway_name"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(f"Route GET /care-pathways (nurse) failed: {str(e)}")
        return make_response(jsonify({"error": "Failed to retrieve care pathways"}), 500)


# ------------------------------------------------------------
# Get patient care pathway assignments [Maria-5]
@nurses.route("/patient-pathway-records", methods=["GET"])
def get_patient_pathway_records():
    try:
        current_app.logger.info("GET /patient-pathway-records route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT ppr.patient_id, p.first_name, p.last_name, 
                  ppr.pathway_id, cp.pathway_name, cp.description, cp.standard_duration
               FROM patient_pathway_record ppr
               JOIN PATIENT p ON ppr.patient_id = p.patient_id
               JOIN CARE_PATHWAY cp ON ppr.pathway_id = cp.pathway_id
               ORDER BY p.last_name, p.first_name, cp.pathway_name"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(f"Route GET /patient-pathway-records (nurse) failed: {str(e)}")
        return make_response(jsonify({"error": "Failed to retrieve patient pathway records"}), 500)


# ------------------------------------------------------------
# Return patient social determinant records [Maria-6]
@nurses.route("/patient-social-records", methods=["GET"])
def get_patient_social_records():
    try:
        current_app.logger.info("GET /patient-social-records route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT psr.patient_id, p.first_name, p.last_name, 
                  psr.determinant_id, sd.determinant_name, sd.category, sd.description, 
                  psr.impact_level
               FROM patient_social_record psr
               JOIN PATIENT p ON psr.patient_id = p.patient_id
               JOIN SOCIAL_DETERMINANTS sd ON psr.determinant_id = sd.determinant_id
               ORDER BY p.last_name, p.first_name, sd.determinant_name"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(f"Route GET /patient-social-records (nurse) failed: {str(e)}")
        return make_response(jsonify({"error": "Failed to retrieve patient social determinant records"}), 500)


# ------------------------------------------------------------
# Create new care task [Maria-1]
@nurses.route("/care-tasks", methods=["POST"])
def create_care_task():
    try:
        current_app.logger.info("POST /care-tasks route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        task_name = data.get("task_name")
        description = data.get("description")
        priority = data.get("priority")
        estimated_duration = data.get("estimated_duration")

        # Validate required fields
        if not all([task_name, priority]):
            return make_response(
                jsonify({"error": "Missing required fields: task_name and priority are required"}),
                400,
            )

        insert_sql_query = """
            INSERT INTO CARE_TASKS (
                task_name, 
                description,
                priority, 
                estimated_duration
            ) VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            insert_sql_query,
            (task_name, description, priority, estimated_duration),
        )

        db.get_db().commit()

        # Get the ID of the newly created task
        cursor.execute("SELECT LAST_INSERT_ID()")
        new_task_id = cursor.fetchone()["LAST_INSERT_ID()"]

        the_response = make_response(
            jsonify({
                "message": "New Care Task was Successfully Created",
                "task_id": new_task_id
            }), 
            201
        )
        return the_response

    except Exception as e:
        current_app.logger.error(f"Route POST /care-tasks (nurse) failed: {str(e)}")
        db.get_db().rollback()
        return make_response(jsonify({"error": "Failed to create new care task"}), 500)


# ------------------------------------------------------------
# Add new patient symptom record [Maria-2]
@nurses.route("/patient-symptom-records", methods=["POST"])
def create_patient_symptom_record():
    try:
        current_app.logger.info("POST /patient-symptom-records route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        patient_id = data.get("patient_id")
        symptom_id = data.get("symptom_id")
        severity = data.get("severity")

        # Validate required fields
        if not all([patient_id, symptom_id]):
            return make_response(
                jsonify({"error": "Missing required fields: patient_id and symptom_id are required"}),
                400,
            )

        # Check if patient exists
        cursor.execute(f"SELECT patient_id FROM PATIENT WHERE patient_id = {patient_id}")
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Patient not found"}), 404)

        # Check if symptom exists
        cursor.execute(f"SELECT symptom_id FROM SYMPTOMS WHERE symptom_id = {symptom_id}")
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Symptom not found"}), 404)

        # Check if record already exists
        cursor.execute(
            f"SELECT patient_id FROM patient_symptom_record WHERE patient_id = {patient_id} AND symptom_id = {symptom_id}"
        )
        if cursor.fetchone():
            return make_response(jsonify({"error": "Patient symptom record already exists"}), 409)

        insert_sql_query = """
            INSERT INTO patient_symptom_record (
                patient_id, 
                symptom_id,
                severity
            ) VALUES (%s, %s, %s)
        """

        cursor.execute(
            insert_sql_query,
            (patient_id, symptom_id, severity),
        )

        db.get_db().commit()

        the_response = make_response(
            jsonify({"message": "New Patient Symptom Record was Successfully Created"}), 
            201
        )
        return the_response

    except Exception as e:
        current_app.logger.error(f"Route POST /patient-symptom-records (nurse) failed: {str(e)}")
        db.get_db().rollback()
        return make_response(jsonify({"error": "Failed to create new patient symptom record"}), 500)


# ------------------------------------------------------------
# Create new medication administration record [Maria-4]
@nurses.route("/medication-administration", methods=["POST"])
def create_medication_administration():
    try:
        current_app.logger.info("POST /medication-administration route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        medication_id = data.get("medication_id")
        result_id = data.get("result_id")
        administered_date = data.get("administered_date")

        # Validate required fields
        if not all([medication_id, result_id]):
            return make_response(
                jsonify({"error": "Missing required fields: medication_id and result_id are required"}),
                400,
            )

        # Check if medication exists
        cursor.execute(f"SELECT medication_id FROM MEDICATIONS WHERE medication_id = {medication_id}")
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Medication not found"}), 404)

        # Check if lab result exists
        cursor.execute(f"SELECT result_id FROM LAB_RESULTS WHERE result_id = {result_id}")
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Lab result not found"}), 404)

        # Check if record already exists
        cursor.execute(
            f"SELECT medication_id FROM medication_administration WHERE medication_id = {medication_id} AND result_id = {result_id}"
        )
        if cursor.fetchone():
            return make_response(jsonify({"error": "Medication administration record already exists"}), 409)

        insert_sql_query = """
            INSERT INTO medication_administration (
                medication_id, 
                result_id,
                administered_date
            ) VALUES (%s, %s, %s)
        """

        cursor.execute(
            insert_sql_query,
            (medication_id, result_id, administered_date),
        )

        db.get_db().commit()

        the_response = make_response(
            jsonify({"message": "New Medication Administration Record was Successfully Created"}), 
            201
        )
        return the_response

    except Exception as e:
        current_app.logger.error(f"Route POST /medication-administration (nurse) failed: {str(e)}")
        db.get_db().rollback()
        return make_response(jsonify({"error": "Failed to create new medication administration record"}), 500)


# ------------------------------------------------------------
# Create new care pathway [Maria-5]
@nurses.route("/care-pathways", methods=["POST"])
def create_care_pathway():
    try:
        current_app.logger.info("POST /care-pathways route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        pathway_name = data.get("pathway_name")
        description = data.get("description")
        standard_duration = data.get("standard_duration")
        is_active = data.get("is_active", True)

        # Validate required fields
        if not pathway_name:
            return make_response(
                jsonify({"error": "Missing required field: pathway_name is required"}),
                400,
            )

        insert_sql_query = """
            INSERT INTO CARE_PATHWAY (
                pathway_name, 
                description,
                standard_duration, 
                is_active
            ) VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            insert_sql_query,
            (pathway_name, description, standard_duration, is_active),
        )

        db.get_db().commit()

        # Get the ID of the newly created pathway
        cursor.execute("SELECT LAST_INSERT_ID()")
        new_pathway_id = cursor.fetchone()["LAST_INSERT_ID()"]

        the_response = make_response(
            jsonify({
                "message": "New Care Pathway was Successfully Created",
                "pathway_id": new_pathway_id
            }), 
            201
        )
        return the_response

    except Exception as e:
        current_app.logger.error(f"Route POST /care-pathways (nurse) failed: {str(e)}")
        db.get_db().rollback()
        return make_response(jsonify({"error": "Failed to create new care pathway"}), 500)


# ------------------------------------------------------------
# Assign care pathway to patient [Maria-5]
@nurses.route("/patient-pathway-records", methods=["POST"])
def assign_pathway_to_patient():
    try:
        current_app.logger.info("POST /patient-pathway-records route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        patient_id = data.get("patient_id")
        pathway_id = data.get("pathway_id")

        # Validate required fields
        if not all([patient_id, pathway_id]):
            return make_response(
                jsonify({"error": "Missing required fields: patient_id and pathway_id are required"}),
                400,
            )

        # Check if patient exists
        cursor.execute(f"SELECT patient_id FROM PATIENT WHERE patient_id = {patient_id}")
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Patient not found"}), 404)

        # Check if pathway exists
        cursor.execute(f"SELECT pathway_id FROM CARE_PATHWAY WHERE pathway_id = {pathway_id}")
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Care pathway not found"}), 404)

        # Check if assignment already exists
        cursor.execute(
            f"SELECT patient_id FROM patient_pathway_record WHERE patient_id = {patient_id} AND pathway_id = {pathway_id}"
        )
        if cursor.fetchone():
            return make_response(jsonify({"error": "Patient is already assigned to this care pathway"}), 409)

        insert_sql_query = """
            INSERT INTO patient_pathway_record (
                patient_id, 
                pathway_id
            ) VALUES (%s, %s)
        """

        cursor.execute(
            insert_sql_query,
            (patient_id, pathway_id),
        )

        db.get_db().commit()

        the_response = make_response(
            jsonify({"message": "Care Pathway Successfully Assigned to Patient"}), 
            201
        )
        return the_response

    except Exception as e:
        current_app.logger.error(f"Route POST /patient-pathway-records (nurse) failed: {str(e)}")
        db.get_db().rollback()
        return make_response(jsonify({"error": "Failed to assign care pathway to patient"}), 500)


# ------------------------------------------------------------
# Add social determinant to patient [Maria-6]
@nurses.route("/patient-social-records", methods=["POST"])
def add_social_determinant_to_patient():
    try:
        current_app.logger.info("POST /patient-social-records route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        patient_id = data.get("patient_id")
        determinant_id = data.get("determinant_id")
        impact_level = data.get("impact_level")

        # Validate required fields
        if not all([patient_id, determinant_id]):
            return make_response(
                jsonify({"error": "Missing required fields: patient_id and determinant_id are required"}),
                400,
            )

        # Check if patient exists
        cursor.execute(f"SELECT patient_id FROM PATIENT WHERE patient_id = {patient_id}")
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Patient not found"}), 404)

        # Check if social determinant exists
        cursor.execute(f"SELECT determinant_id FROM SOCIAL_DETERMINANTS WHERE determinant_id = {determinant_id}")
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Social determinant not found"}), 404)

        # Check if record already exists
        cursor.execute(
            f"SELECT patient_id FROM patient_social_record WHERE patient_id = {patient_id} AND determinant_id = {determinant_id}"
        )
        if cursor.fetchone():
            return make_response(jsonify({"error": "This social determinant is already assigned to this patient"}), 409)

        insert_sql_query = """
            INSERT INTO patient_social_record (
                patient_id, 
                determinant_id,
                impact_level
            ) VALUES (%s, %s, %s)
        """

        cursor.execute(
            insert_sql_query,
            (patient_id, determinant_id, impact_level),
        )

        db.get_db().commit()

        the_response = make_response(
            jsonify({"message": "Social Determinant Successfully Added to Patient"}), 
            201
        )
        return the_response

    except Exception as e:
        current_app.logger.error(f"Route POST /patient-social-records (nurse) failed: {str(e)}")
        db.get_db().rollback()
        return make_response(jsonify({"error": "Failed to add social determinant to patient"}), 500)


# ------------------------------------------------------------
# Update task priority/description [Maria-1]
@nurses.route("/care-tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    try:
        current_app.logger.info(f"PUT /care-tasks/{task_id} route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        description = data.get("description")
        priority = data.get("priority")
        estimated_duration = data.get("estimated_duration")

        # Validate that at least one field to update is provided
        if not any([description, priority, estimated_duration]):
            return make_response(
                jsonify({"error": "No update data provided. Provide at least one field to update."}),
                400,
            )

        # Check if task exists
        cursor.execute(f"SELECT task_id FROM CARE_TASKS WHERE task_id = {task_id}")
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Task not found"}), 404)

        # Build the update query based on provided fields
        update_fields = []
        params = []

        if description is not None:
            update_fields.append("description = %s")
            params.append(description)

        if priority is not None:
            update_fields.append("priority = %s")
            params.append(priority)

        if estimated_duration is not None:
            update_fields.append("estimated_duration = %s")
            params.append(estimated_duration)

        # Add the updated_at field
        update_fields.append("updated_at = CURRENT_TIMESTAMP")

        # Add task_id to params
        params.append(task_id)

        # Execute update query
        update_query = f"UPDATE CARE_TASKS SET {', '.join(update_fields)} WHERE task_id = %s"
        cursor.execute(update_query, params)

        db.get_db().commit()

        # Check if any rows were affected
        if cursor.rowcount == 0:
            return make_response(jsonify({"error": "No changes made to task"}), 400)

        the_response = make_response(
            jsonify({"message": "Task Successfully Updated"}),
            200
        )
        return the_response

    except Exception as e:
        current_app.logger.error(f"Route PUT /care-tasks/{task_id} (nurse) failed: {str(e)}")
        db.get_db().rollback()
        return make_response(jsonify({"error": "Failed to update task"}), 500)


# ------------------------------------------------------------
# Update symptom severity [Maria-2]
@nurses.route("/patient-symptom-records", methods=["PUT"])
def update_symptom_severity():
    try:
        current_app.logger.info("PUT /patient-symptom-records route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        patient_id = data.get("patient_id")
        symptom_id = data.get("symptom_id")
        severity = data.get("severity")

        # Validate required fields
        if not all([patient_id, symptom_id, severity]):
            return make_response(
                jsonify({"error": "Missing required fields: patient_id, symptom_id, and severity are required"}),
                400,
            )

        # Check if record exists
        cursor.execute(
            f"""SELECT patient_id 
                FROM patient_symptom_record 
                WHERE patient_id = {patient_id} AND symptom_id = {symptom_id}"""
        )
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Patient symptom record not found"}), 404)

        # Execute update query
        update_query = """
            UPDATE patient_symptom_record 
            SET severity = %s 
            WHERE patient_id = %s AND symptom_id = %s
        """
        cursor.execute(update_query, (severity, patient_id, symptom_id))

        db.get_db().commit()

        the_response = make_response(
            jsonify({"message": "Symptom Severity Successfully Updated"}),
            200
        )
        return the_response

    except Exception as e:
        current_app.logger.error(f"Route PUT /patient-symptom-records (nurse) failed: {str(e)}")
        db.get_db().rollback()
        return make_response(jsonify({"error": "Failed to update symptom severity"}), 500)


# ------------------------------------------------------------
# Mark lab result review status [Maria-3]
@nurses.route("/lab-results", methods=["PUT"])
def update_lab_result_review_status():
    try:
        current_app.logger.info("PUT /lab-results route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        result_id = data.get("result_id")
        is_reviewed = data.get("is_reviewed")
        review_notes = data.get("review_notes")

        # Validate required fields
        if not all([result_id, is_reviewed is not None]):
            return make_response(
                jsonify({"error": "Missing required fields: result_id and is_reviewed are required"}),
                400,
            )

        # Check if lab result exists
        cursor.execute(f"SELECT result_id FROM LAB_RESULTS WHERE result_id = {result_id}")
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Lab result not found"}), 404)

        # Build update query
        update_fields = ["is_reviewed = %s"]
        params = [is_reviewed]

        if review_notes is not None:
            update_fields.append("lab_notes = %s")
            params.append(review_notes)

        # Add the updated_at field
        update_fields.append("updated_at = CURRENT_TIMESTAMP")

        # Add result_id to params
        params.append(result_id)

        # Execute update query
        update_query = f"UPDATE LAB_RESULTS SET {', '.join(update_fields)} WHERE result_id = %s"
        cursor.execute(update_query, params)

        db.get_db().commit()

        the_response = make_response(
            jsonify({"message": "Lab Result Review Status Successfully Updated"}),
            200
        )
        return the_response

    except Exception as e:
        current_app.logger.error(f"Route PUT /lab-results (nurse) failed: {str(e)}")
        db.get_db().rollback()
        return make_response(jsonify({"error": "Failed to update lab result review status"}), 500)


# ------------------------------------------------------------
# Update impact level [Maria-6]
@nurses.route("/patient-social-records", methods=["PUT"])
def update_impact_level():
    try:
        current_app.logger.info("PUT /patient-social-records route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        patient_id = data.get("patient_id")
        determinant_id = data.get("determinant_id")
        impact_level = data.get("impact_level")

        # Validate required fields
        if not all([patient_id, determinant_id, impact_level]):
            return make_response(
                jsonify({"error": "Missing required fields: patient_id, determinant_id, and impact_level are required"}),
                400,
            )

        # Check if record exists
        cursor.execute(
            f"""SELECT patient_id 
                FROM patient_social_record 
                WHERE patient_id = {patient_id} AND determinant_id = {determinant_id}"""
        )
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Patient social determinant record not found"}), 404)

        # Execute update query
        update_query = """
            UPDATE patient_social_record 
            SET impact_level = %s 
            WHERE patient_id = %s AND determinant_id = %s
        """
        cursor.execute(update_query, (impact_level, patient_id, determinant_id))

        db.get_db().commit()

        the_response = make_response(
            jsonify({"message": "Social Determinant Impact Level Successfully Updated"}),
            200
        )
        return the_response

    except Exception as e:
        current_app.logger.error(f"Route PUT /patient-social-records (nurse) failed: {str(e)}")
        db.get_db().rollback()
        return make_response(jsonify({"error": "Failed to update social determinant impact level"}), 500)
