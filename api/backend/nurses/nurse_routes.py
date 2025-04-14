########################################################
# Nurse routes blueprint file
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from db_connection import db

# ------------------------------------------------------------
# Create a new Blueprint object, which is a collection of
# routes.
nurses = Blueprint("nurses", __name__)


#--------------------[Nurse User Persona ~ Maria #1 ]----------------------


# Get all care tasks from the system
@nurses.route("/care-tasks", methods=["GET"])
def get_care_tasks():
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


# create a new care task
@nurses.route('/care-tasks/', methods=['POST'])
def create_new_caretask():
    data = request.get_json()
    query = ''' INSERT INTO CARE_TASKS (
    task_name,
    description,
    priority, 
    estimated_duration
    ) VALUES (%s, %s, %s, %s)
    
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (data.get('task_name'),
                           data.get('description'),
                           data.get('priority'),
                           data.get('estimated_duration')))
    
    
    db.get_db().commit()
    return make_response(jsonify({"message": "New Care Task was Sucessfully Created"}), 201)

# return the details about a specific care task
@nurses.route('/care-tasks/<task_id>', methods=['GET'])
def get_specific_caretask(task_id):
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT task_id, task_name, description, priority, estimated_duration, 
                   created_at, updated_at
                   FROM CARE_TASKS
                   WHERE task_id = %s''', (task_id,))
    
    theData = cursor.fetchone()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200


    if theData:
        return the_response
    else:
        return make_response(jsonify({"error": "Care Task Not Found"}), 404)
        

# update a specific care task description
@nurses.route('/care-tasks/<task_id>/description', methods=['PUT'])
def update_known_caretask(task_id):

    data = request.get_json()
    new_description = data.get('description')

    if not new_description: 
        return make_response(jsonify({"error": "Change is required and no new input"}), 400)
    
    mysql_query = ''' UPDATE CARE_TASKS
    SET description = %s, updated_at = CURRENT_TIMESTAMP
    WHERE task_id = %s 
    '''

    cursor = db.get_db().cursor()
    cursor.execute(mysql_query, (new_description, task_id))
    

    the_response = make_response(jsonify({"message": "Care Task Description was Updated"}))
    the_response.status_code = 200
    return the_response


#--------------------[Nurse User Persona ~ Maria #2 ]----------------------



# return patient symptoms 
@nurses.route('/patient-symptom-records', methods=['GET'])
def get_patient_symptoms():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT patSR.patient_id,
                   p.first_name, p.last_name,
                   s.symptom_name, s.description AS symptom_description, 
                   patSR.severity, s.severity_code, s.created_at, s.updated_at
                   FROM patient_symptom_record patSR
                   JOIN PATIENT p ON patSR.patient_id = p.patient_id
                   JOIN SYMPTOMS s ON patSR.symptom_id = s.symptom_id
                   ORDER BY p.last_name, p.first_name         
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# add new patient symptom record
@nurses.route('/patient-symptom-records', methods=['POST'])
def create_patient_symptom():
    data = request.get_json()
    cursor = db.get_db().cursor()
    mysql_query = '''INSERT INTO patient_symptom_record (
                   patient_id,
                   symptom_id,
                   severity
                   ) VALUES (%s, %s, %s)
    '''
    
    cursor.execute(mysql_query, (data.get('patient_id'), data.get('symptom_id'), data.get('severity_id')))

    db.get_db().commit()
    the_response = make_response(jsonify({"message": "Patient symptom recorded added"}))
    the_response.status_code = 201
    return the_response

# update symptom severity
@nurses.route('/patient-symptom-records', methods=['PUT'])
def update_symptom_severity():
    cursor = db.get_db().cursor()
    data = request.get_json()
    patient_id = data.get('patient_id')
    symptom_id = data.get('symptom_id')
    severity = data.get('severity_id')

    if not (patient_id and symptom_id and severity):
        return  make_response(jsonify({"error": "All needed inputs are required"}), 400)
    
    mysql_query = ''' UPDATE patient_symptom_record
    SET severity = %s 
    WHERE patient_id = %s AND symptom_id = %s
    '''

    cursor.execute(mysql_query, (severity, patient_id, symptom_id))
    
    db.get_db().commit()
    
    the_response = make_response(jsonify({"message": "Symptom severity wa Sucessfully Updated"}))
    the_response.status_code = 200
    return the_response




#--------------------[Nurse User Persona ~ Maria #3 ]----------------------



# get lab results for a patient
@nurses.route('/lab-results', methods=['GET'])
def get_lab_results():
    cursor = db.get_db().cursor()
    patient_id = request.args.get('patient_id')

    if not patient_id:
        return make_response(jsonify({"error": "A patient id is wrong and required"}), 400)
    cursor.execute('''SELECT lab.result_id, lab.test_name, lab.test_date, lab.result_date, lab.result_value, 
                   lab.reference_range, lab.unit_of_measure, lab.is_abnormal, lab.lab_notes
                   FROM LAB_RESULTS
                   WHERE lab.patient_id = {0}
                   ORDER BY lab.result_date
    ''').format(patient_id)
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# mark lab result review status 
@nurses.route('/lab-results', methods=['PUT'])
def mark_reviewed_lab_results():
    cursor = db.get_db().cursor()
    data = request.get_json()
    result_id = data.get('result_id')
    is_reviewed = data.get('is_reviewed', True)

    if not result_id:
        return make_response(jsonify({"error": "There is no result id present"}), 400)
    

    mysql_query = '''
        UPDATE LAB_RESULTS
        SET is_reviewed = %s, updated_at = CURRENT_TIMESTAMP
        WHERE result_id = %s
    '''
    cursor.execute(mysql_query, (is_reviewed, result_id))
    
    db.get_db().commit()
    
    the_response = make_response(jsonify({"message": "Lab Review Status was Changed"}))
    the_response.status_code = 200
    return the_response



#--------------------[Nurse User Persona ~ Maria #4 ]----------------------



# output medication administration records
@nurses.route('/medication-administration', methods=['GET'])
def get_medication_admin_records():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT medAdm.medication_id, med.medication_name, 
                   med.dosage_form, med.strength, medAdm.result_id, medAdm.administered_date
                   FROM medication_administration medAdm
                   JOIN MEDICATIONS med ON med.medication_id = medAdm.medication_id
                   ORDER BY medAdm.administered_date
    ''')
    
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# create a new administration record
@nurses.route('/medication-administration', methods=['POST'])
def create_new_admin_record():

    cursor = db.get_db().cursor()
    data = request.get_json()

    medication_id = data.get('medication_id')
    result_id = data.get('result_id')
    administered_date = data.get('administered_date')

    if not (result_id and medication_id and administered_date):
        return make_response(jsonify({"error": "There input is not invalid due to all variables needed"}), 400)
    

    mysql_query = '''
        INSERT INTO medication_administration (
            medication_id, 
            result_id,
            administered_date
        ) VALUES (%s, %s, %s)
    '''
    cursor.execute(mysql_query, (medication_id, result_id, administered_date))
    
    db.get_db().commit()
    
    the_response = make_response(jsonify({"message": "A Medication Admin Record was Succesfully Inputed"}))
    the_response.status_code = 200
    return the_response



#--------------------[Nurse User Persona ~ Maria #5 ]----------------------



# produce all care pathways
@nurses.route('/care-pathways', methods=['GET'])
def get_all_care_pathways():
    cursor = db.get_db().cursor()
    cursor.execute('''Select pathway_id, pathway_name, description, standard_duration, is_active, created_at, updated_at
                   FROM CARE_PATHWAY
                   ORDER BY pathway_name
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# create new care pathways
@nurses.route('/care-pathways', methods=['POST'])
def create_new_care_pathways():
    cursor = db.get_db().cursor()
    data = request.get_json()

    patient_id = data.get('patient_id')
    pathway_id = data.get('pathway_id')

    if not (pathway_id and patient_id):
        return make_response(jsonify({"error": "There input is not invalid and all variables are required"}), 400)
    
    mysql_query = '''
        INSERT INTO patient_pathway_record (
            patient_id, 
            pathway_id
        ) VALUES (%s, %s)
    '''
    cursor.execute(mysql_query, (patient_id, pathway_id))
    
    db.get_db().commit()
    
    the_response = make_response(jsonify({"message": "Care pathway was assigned to patient"}))
    the_response.status_code = 201
    return the_response


# produce patient care pathway assignments 
@nurses.route('/patient-pathway-records', methods=['GET'])
def get_patient_care_pathway():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT patPR.patient_id, 
                   p.first_name, p.last_name, 
                   carePath.pathway_id, 
                   carePath.pathway_name, 
                   carePath.description,
                   carePath.standard_duration,
                   carePath.is_active
                   FROM patient_pathway patPR
                   JOIN PATIENT p ON p.patient_id = patPR.patient_id
                   JOIN CARE_PATHWAY carePath ON patPR.pathway_id = carePath.pathway_id
                   ORDER BY patPR.patient_id
                   ''')

    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# assign care pathway to patient
@nurses.route('/patient-pathway-records', methods=['POST'])
def assign_care_pathway_to_patient():
    cursor = db.get_db().cursor()
    data = request.get_json()

    patient_id = data.get('patient_id')
    pathway_id = data.get('pathway_id')

    if not (pathway_id and patient_id):
        return make_response(jsonify({"error": "There input is not invalid and all variables are required"}), 400)
    
    mysql_query = '''
        INSERT INTO patient_pathway_record (
            patient_id, 
            pathway_id
        ) VALUES (%s, %s)
    '''
    cursor.execute(mysql_query, (patient_id, pathway_id))
    
    db.get_db().commit()
    
    the_response = make_response(jsonify({"message": "Care pathway was assigned to patient"}))
    the_response.status_code = 201
    return the_response



#--------------------[Nurse User Persona ~ Maria #6 ]----------------------



# get the patient social determinant records
@nurses.route('/patient-social-records/<patient_id>/determinant', methods=['GET'])
def get_patient_social_determinant_records(patient_id):
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT sd.determinant_id, sd.determinant_name, sd.category, psr.impact_level
                  FROM patient_social_record psr 
                  JOIN SOCIAL_DETERMINANTS sd ON sd.determinant_id = psr.determinant_id
                  WHERE psr.patient_id = %s''', (patient_id,))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# add social determinant to the patient's record
@nurses.route('/patient-social-records/<patient_id>/determinant', methods=['POST'])
def assign_social_determinant_to_patient(patient_id):
    cursor = db.get_db().cursor()
    data = request.get_json()

    patient_id = data.get('patient_id')
    determinant_id = data.get('determinant_id')
    impact_level = data.get('impact_level')

    if not (impact_level and determinant_id):
        return make_response(jsonify({"error": "There input is not invalid and all variables are required"}), 400)
    
    mysql_query = '''
        INSERT INTO patient_social_record (
            patient_id,
            determinant_id, 
            impact_level
        ) VALUES (%s, %s, %s)
    '''
    cursor.execute(mysql_query, (patient_id, determinant_id, impact_level))
    
    db.get_db().commit()
    
    the_response = make_response(jsonify({"message": "Social Determinant was Created & Assigned to Patient's Record"}))
    the_response.status_code = 201
    return the_response

# update a patient's social determinant impact level
@nurses.route('/patient-social-records/<patient_id>/determinant/<determinant_id>', methods=['PUT'])
def update_pat_social_determ_impact_level(patient_id, determinant_id):
    cursor = db.get_db().cursor()
    data = request.get_json()
    impact_level = data.get('impact_level')

    if not determinant_id:
        return make_response(jsonify({"error": "There is no valid determinant assigned to the patient"}), 400)
    

    mysql_query = '''
        UPDATE patient_social_record
        SET impact_level = %s
        WHERE patient_id = %s AND determinant_id=%s
    '''
    cursor.execute(mysql_query, (impact_level, patient_id, determinant_id))
    
    db.get_db().commit()
    
    the_response = make_response(jsonify({"message": "Update to the Social Determinant Impact Level was Updated"}))
    the_response.status_code = 200
    return the_response
