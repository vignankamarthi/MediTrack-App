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


# ------------------------------------------------------------
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
