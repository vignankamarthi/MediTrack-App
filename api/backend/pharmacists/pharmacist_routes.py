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



#--------------------[Pharmacists User Persona ~ Sarah #1 ]----------------------

# Get medication history for a specific patient
@pharmacists.route("/medication-records/<patient_id>", methods=["GET"])
def get_medication_records(patient_id):
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

# create and add new medication to patient record in the system
@pharmacists.route('/medication-records/<patient_id>', methods=['POST'])
def add_new_medications_patient_record(patient_id):
    cursor = db.get_db().cursor()
    current_app.logger.info(f"POST /medication-records/{patient_id} route")

    data = request.get_json()
    medication_id = data.get('medication_id')
    dosage = data.get('dosage')
    frequency = data.get('frequency')

    mysql_sql_query = '''
        INSERT INTO medication_record (patient_id, medication_id, dosage, frequency
        ) VALUES (%s, %s, %s, %s)
    '''

    if not all([medication_id, dosage, frequency]):
        return make_response(jsonify({"error": "All fields (medication_id, dosage, frequency) are required"}), 400)

    cursor.execute(mysql_sql_query, (patient_id, medication_id, dosage, frequency))
    
    db.get_db().commit()

    the_response = make_response(jsonify({"message": "Medication was Sucessfully Added to Patient Record"}), 201)

    if data:
        return the_response
    else:
        return make_response(jsonify({"error": "Medication Not Found"}), 404)
    

# return medication database 
@pharmacists.route("/medications", methods=["GET"])
def get_medications():
    current_app.logger.info(f"GET /medication route")
    cursor = db.get_db().cursor()
    cursor.execute(
        """SELECT medication_id, medication_name, generic_name, medication_class, dosage_form, strength, manufacturer, ndc_code, is_controlled, control_class
                      FROM MEDICATIONS
        """
    )

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response



#--------------------[Pharmacists User Persona ~ Sarah #2 ]----------------------



# return produce prescription outcomes 
@pharmacists.route("/prescription-outcome-records", methods=["GET"])
def get_prescription_outcomes():
    current_app.logger.info(f"GET /prescription-outcome-records route")
    cursor = db.get_db().cursor()
    cursor.execute(
        """SELECT preOR.outcome_id, preOR.prescription_id, preOR.effectiveness, to.outcome_name, p.prescription_date
        FROM prescription_outcome_record preOR
        JOIN TREATMENT_OUTCOMES to ON to.outcome_id = preOR.outcome_id
        JOIN PRESCRIPTIONS p ON preOR.prescription_id = p.prescription_id
        """
    )

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Update prescription effectivenes
@pharmacists.route('/prescription-outcome-records', methods=['PUT'])
def update_prescription_effectivenes():
    current_app.logger.info(f"PUT /prescription-outcome-records route")
    data = request.get_json()
    outcome_id = data.get('outcome_id')
    prescription_id = data.get('prescription_id')
    new_effectiveness = data.get('new_effectiveness')

    if not (outcome_id and prescription_id and new_effectiveness): 
        return make_response(jsonify({"error": "Missing Inputs and Change is required and no new input"}), 400)
    
    mysql_query = ''' UPDATE prescription_outcome_record
    SET effectiveness = %s
    WHERE outcome_id = %s AND prescription_id = %s 
    '''

    cursor = db.get_db().cursor()
    cursor.execute(mysql_query, (new_effectiveness, outcome_id, prescription_id))
    
    db.get_db().commit()
    the_response = make_response(jsonify({"message": "Effectivenes of Prescription was Updated"}))
    the_response.status_code = 200
    return the_response


#--------------------[Pharmacists User Persona ~ Sarah #4 ]----------------------

# Return education records 
@pharmacists.route("/patient-education", methods=["GET"])
def get_patient_education():
    current_app.logger.info(f"GET /patient-education route")
    cursor = db.get_db().cursor()
    cursor.execute(
        """SELECT pEdu.record_id, pEdu.provider_id, hp.first_name, hp.last_name, pEdu.comprehension_level, pEdu.notes, pEdu.created_at
        FROM PATIENT_EDUCATION pEdu
        JOIN HEALTHCARE_PROVIDER hp ON pEdu.provider_id = hp.provider_id
        ORDER BY pEdu.created_at DESC
        """
    )

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Create new patient education record in the system
@pharmacists.route('/patient-education', methods=['POST'])
def create_new_patient_education_record():
    cursor = db.get_db().cursor()
    current_app.logger.info(f"POST /patient-education route")

    data = request.get_json()

    provider_id = data.get('provider_id')
    comprehension_level = data.get('comprehension_level')
    notes = data.get('notes')

    if not (provider_id and comprehension_level and notes): 
        return make_response(jsonify({"error": "Missing Inputs and Change is required and no new input"}), 400)
    

    mysql_sql_query = '''
        INSERT INTO PATIENT_EDUCATION (provider_id, comprehension_level, notes
        ) VALUES (%s, %s, %s)
    '''

    cursor.execute(mysql_sql_query, (provider_id, comprehension_level, notes))
    
    db.get_db().commit()

    the_response = make_response(jsonify({"message": "Patient Education Record was Sucessfully Created"}), 201)

    if data:
        return the_response
    else:
        return make_response(jsonify({"error": "Medication Not Found"}), 404)
    
# View education-patient relationships
@pharmacists.route("/patient-education-records", methods=["GET"])
def get_education_patient_relationships():
    current_app.logger.info(f"GET /patient-education-records route")
    cursor = db.get_db().cursor()
    cursor.execute(
        """SELECT pEduRec.patient_id, p.first_name, p.last_name, pEduRec.education_id, pe.comprehension_level, pe.notes, pEduRec.education_date
        FROM patient_education_record pEduRec
        JOIN PATIENT p ON pEduRec.patient_id = p.patient_id
        JOIN PATIENT_EDUCATION pe ON pEduRec.education_id = pe.education_id
        ORDER BY pEduRec.education_date DESC
        """
    )

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response
    
# Create patient-education relationship  in the system
@pharmacists.route('/patient-education-records', methods=['POST'])
def create_new_patient_education_record_v2():
    cursor = db.get_db().cursor()
    current_app.logger.info(f"POST /patient-education-records route")

    data = request.get_json()

    patient_id = data.get('patient_id')
    education_id = data.get('education_id')
    education_date = data.get('education_date')

    if not (patient_id and education_id and education_date): 
        return make_response(jsonify({"error": "Missing Inputs and Change is required and no new input"}), 400)
    

    mysql_sql_query = '''
        INSERT INTO patient_education_record (patient_id, education_id, education_date
        ) VALUES (%s, %s, %s)
    '''

    cursor.execute(mysql_sql_query, (patient_id, education_id, education_date))
    
    db.get_db().commit()

    the_response = make_response(jsonify({"message": "Patient Education Record was Sucessfully Created"}), 201)

    if data:
        return the_response
    else:
        return make_response(jsonify({"error": "Medication Not Found"}), 404)
    


#--------------------[Pharmacists User Persona ~ Sarah #5 ]----------------------



# Return patient medication schedule
@pharmacists.route("/medication-record/<patient_id>", methods=["GET"])
def get_patient_medication_schedule(patient_id):
    current_app.logger.info(f"GET /medication-record/{patient_id} route ")
    cursor = db.get_db().cursor()
    cursor.execute(
        """SELECT mr.patient_id, p.first_name, p.last_name, mr.medication_id, m.medication_name, m.dosage_form, m.strength, mr.dosage, mr.frequency
        FROM medication_record mr
        JOIN PATIENT p ON mr.patient_id = p.patient_id
        JOIN MEDICATIONS m ON m.medication_id = mr.medication_id
        WHERE mr.patient_id = {0}
        """.format(patient_id)
    )

    theData = cursor.fetchall()
    if theData:
        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    else:
        return make_response(jsonify({"error": "No medication plan or scedule for this selected patient"}), 404)

# Update medication dosage/frequency for a given record
@pharmacists.route("/medication-record/<patient_id>", methods=["PUT"])
def update_medications_dos_freq(patient_id):
    current_app.logger.info(f"PUT /medication-records/{patient_id} route")

    data = request.get_json()
    new_dosage = data.get("dosage")
    new_frequency = data.get("frequency")
    medication_id = data.get("medication_id")

    cursor = db.get_db().cursor()

    if not(new_dosage and new_frequency and medication_id):
        return make_response(jsonify({"error": "Missing Inputs and Change is required and no new input"}), 400)
    
    query = """
        UPDATE medication_record
        SET dosage = %s,
            frequency = %s
        WHERE patient_id = %s AND medication_id = %s
    """
    cursor.execute(query, (new_dosage, new_frequency, patient_id, medication_id))
    db.get_db().commit()

    the_response = make_response(jsonify({"message": "Sucessfully Updated medication dosage/frequency"}))
    the_response.status_code = 200
    return the_response



#--------------------[Pharmacists User Persona ~ Sarah #6 ]----------------------



# Return patient medication schedule
@pharmacists.route("/prescription-patient-records/<patient_id>", methods=["GET"])
def get_medication_reconcilation(patient_id):
    current_app.logger.info(f"GET /prescription-patient-records/{patient_id} route ")
    cursor = db.get_db().cursor()
    cursor.execute(
        """SELECT p.patient_id, p.first_name, p.last_name, pr.prescription_id, m.medication_name, 
        m.dosage_form, m.strength, pre.instructions, pre.prescription_date, pre.refills
        FROM prescription_patient_record pr
        JOIN PATIENT p ON pr.patient_id = p.patient_id
        JOIN PRESCRIPTIONS pre ON pr.prescription_id = pre.prescription_id
        JOIN medication_prescription_record mpr ON pre.prescription_id = mpr.prescription_id
        JOIN MEDICATIONS m ON mpr.medication_id = m.medication_id
        WHERE p.patient_id = {0}
        ORDER BY pre.prescription_date DESC
        """.format(patient_id)
    )

    theData = cursor.fetchall()
    if theData:
        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    else:
        return make_response(jsonify({"error": "No reconcilation data found for the patient"}), 404)