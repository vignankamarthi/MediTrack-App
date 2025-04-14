########################################################
# Pharmacist routes blueprint file
#########################################################
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
