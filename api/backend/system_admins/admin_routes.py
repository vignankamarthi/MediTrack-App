########################################################
# Admin routes blueprint file
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
admins = Blueprint("admins", __name__)


# ------------------------------------------------------------
# Get all permissions from the system
@admins.route("/permissions", methods=["GET"])
def get_permissions():
    current_app.logger.info("GET /permissions route")
    cursor = db.get_db().cursor()
    cursor.execute(
        """SELECT permission_id, permission_name, 
                      description, user_id, is_active 
                      FROM PERMISSIONS"""
    )

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response
