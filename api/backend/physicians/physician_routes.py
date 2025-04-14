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


#--------------------[Physican User Persona ~ James #1 ]----------------------



# Get treatment outcomes with effectiveness ratings
@physicians.route("/treatment-outcomes", methods=["GET"])
def get_treatment_outcomes():
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


# Output all known medical conditions
@physicians.route('/medical-conditions', methods=['GET'])
def get_list_medical_conditions():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT mc.condition_id, mc.condition_name, mc.description, mc.icd_code, mc.ischronic
                   FROM MEDICAL_CONDITION mc
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


# Return specific side effects and condition details that pertain to a certain treatment beiing used
@physicians.route('/condition-treatment-protocol/<condition_id>', methods=['GET'])
def get_known_side_effects_from_treatment(condition_id):
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT mc.condition_name, mc.description AS condition_description, t.treatment_name, t.description AS treatment_description, 
                   to.outcome_name AS possible_outcome, to.description, outcome_description, to.is_positive
                   FROM condition_treatment_protocol condTreatProto
                   JOIN MEDICAL_CONDITION mc ON condTreatProto.condition_id = mc.condition_id
                   JOIN TREATMENT t ON condTreatProto.treatment_id = t.treatment_id
                   LEFT JOIN TREATMENT_OUTCOME to ON t.treatment_id = to.treatment_id
                   WHERE condTreatProto.condition_id = {0}
    ''').format(condition_id)
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response



#--------------------[Physican User Persona ~ James #2 ]----------------------



# return all medication records and log for a specfic patient 
@physicians.route('/medication-records/<patient_id>', methods=['GET'])
def get_medication_records(patient_id):
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT med.medication_name, med.generic_name, med.dosage_form, med.strength, 
                   medRecord.dosage, medRecord.frequency, audLog.log_id, audLog.action_type, audLog.table_affected, audLog.details, audLog.ip_address, audLog_action_timestamp, 
                   FROM medication_record AS medRecord
                   JOIN MEDICATIONS med ON medRecord.medication_id = med.medication_id
                   LEFT JOIN audit_patient_record patRec ON medRecord.patient_id = patRec.patient_id
                   LEFT JOIN AUDIT_LOGS audLog ON audLog.log_id = patRec.log_id
                   WHERE patRec.patient_id = {0}
    ''').format(patient_id)
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response



#--------------------[Physican User Persona ~ James #4 ]----------------------



# to produce all the known preformance metrics for each healthcare provider
@physicians.route('/healthcare-providers', methods=['GET'])
def get_healthcare_provider_performance_metrics():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT hp.provider_id, hp.first_name, hp.last_name, hp.specialization, hp.department, 
                   COUNT(DISTINCT ptr.treatment_id) AS treatments_managed, 
                   COUNT(DISTINCT prescript.patient_id) AS patients_served, 
                   COUNT(DISTINCT patEdu.record_id) AS amount_education_sessions, 
                   COUNT(DISTINCT pr.prescription_id) AS amount_prescriptions_written, 
                   COUNT(DISTINCT ppr.protocol_id) AS amount_protocols
                   FROM HEALTHCARE_PROVIDER hp
                   LEFT JOIN provider_treatment_record ptr ON hp.provider_id = ptr.provider_id
                   LEFT JOIN patient_provider_record pp ON hp.provider_id = pp.provider_id
                   LEFT JOIN PATIENT_EDUCATION patEdu ON patEdu.provider_id = hp.provider_id
                   LEFT JOIN PRESCRIPTIONS prescript ON hp.provider_id = prescript.provider_id
                   LEFT JOIN provider_protocol_record ppr ON hp.provider_id = ppr.provider_id
                   GROUP BY hp.provider_id
                   ORDER BY hp.first_name, hp.last_name
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response



#--------------------[Physican User Persona ~ James #5 ]----------------------



# produce a list of all the clinical protocols from the system
@physicians.route('/clinical-protocols', methods=['GET'])
def get_all_clinical_protocols():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT protocol_id, protocol_name, description, version, effective_date
                   expiration_date, is_active, created_at, updated_at
                   FROM CLINICAL_PROTOCOL
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


# create a new clinical protocol into the system
@physicians.route('/clinical-protocols', methods=['POST'])
def update_known_clinical_protocol():
    cursor = db.get_db().cursor()

    data = request.get_json()
    protocol_name = data.get('protocol_name')
    description = data.get('description')
    version = data.get('version')
    effective_date = data.get('effective_date')
    expiration_date = data.get('expiration_date')
    is_active = data.get('is_active', True)

    insert_sql_query = '''
        INSERT INTO CLINICAL_PROTOCOL (
            protocol_name, 
            description,
            version, 
            effective_date,
            expiration_date, 
            is_active
        ) VALUES (%s, %s, %s, %s, %s, %s)
    '''

    cursor.execute(insert_sql_query, (protocol_name, description, version, effective_date, expiration_date, is_active))
    
    db.get_db().commit()

    the_response = make_response(jsonify({"message": "New Clinical Protocol was Sucessfully Created"}), 201)

    if data:
        return the_response
    else:
        return make_response(jsonify({"error": "Clincial Protocol Not Found"}), 404)

# return specific protocol details
@physicians.route('/clinical-protocols/<protocol_id>', methods=['GET'])
def get_protocol_details(protocol_id):
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT protocol_id, protocol_name, description, version, effective_date, expiration_date,
                   is_active, created_at, updated_at
                   FROM CLINCIAL_PROTOCOL
                   WHERE protocol_id {0}
    ''').format(protocol_id)
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# update specific protocol details and status (active/inactive)
@physicians.route('/clinical-protocols/<protocol_id>', methods=['UPDATE'])
def update_protocol_details():
    data = request.get_json()
    cursor = db.get_db().cursor()
    mysql_query = '''Update CLINICAL_PROTOCOL
                   SET
                   protocol_name = %s, 
                   description = %s, 
                   version = %s, 
                   effective_date = %s,
                   expiration_date = %s,
                   is_active = %s,
                   updated_at = CURRENT_TIMESTAMP
                   WHERE protocol_id = %s 
        '''

    cursor.execute(mysql_query, (
         data.get('protocol_name'), 
         data.get('description'), 
         data.get('version'), 
         data.get('effective_date'), 
         data.get('expiration_date'), 
         data.get('is_active', True), 
         data.get('protocol_id')))

    db.get_db().commit()
    the_response = make_response(jsonify({"message": "Sucessfully Updated Clinical Protocol"}), 200)
    return the_response



#--------------------[Physican User Persona ~ James #6 ]----------------------



# produce all treatment records for re-admission analysis
@physicians.route('/patient-treatment-records/', methods=['GET'])
def update_treatment_records():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT ptr.patient_id, p.first_name, p.last_name, t.treatment_name, ptr.startdate, ptr.enddate, ptr.status
                   FROM patient_treatment_record ptr,
                   JOIN PATIENT p ON ptr.patient_id = p.patient_id
                   JOIN TREATMENT T ON ptr.treament_id = t.treatment_id
                   ORDER BY ptr.start_date, ptr.patient_id DESC
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response
