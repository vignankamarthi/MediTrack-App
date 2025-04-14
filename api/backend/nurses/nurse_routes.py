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
