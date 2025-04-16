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
# Get all permissions from the system [Brennan-1]
@admins.route("/permissions", methods=["GET"])
def get_permissions():
    try:
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
    except Exception as e:
        current_app.logger.error(f"Route GET /permissions (admin) failed: {str(e)}")
        return make_response(jsonify({"error": "Failed to retrieve permissions"}), 500)


# ------------------------------------------------------------
# Get permissions for a specific user [Brennan-1]
@admins.route("/permissions/<user_id>", methods=["GET"])
def get_user_permissions(user_id):
    try:
        current_app.logger.info(f"GET /permissions/{user_id} route")
        cursor = db.get_db().cursor()
        cursor.execute(
            f"""SELECT permission_id, permission_name, 
                      description, user_id, is_active 
                      FROM PERMISSIONS
                      WHERE user_id = {user_id}"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /permissions/{user_id} (admin) failed: {str(e)}"
        )
        return make_response(
            jsonify({"error": "Failed to retrieve user permissions"}), 500
        )


# ------------------------------------------------------------
# Get all system users [Brennan-2]
@admins.route("/system-users", methods=["GET"])
def get_system_users():
    try:
        current_app.logger.info("GET /system-users route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT user_id, user_name, email, role, 
                      is_active, first_name, last_name, 
                      last_login, created_at, updated_at
                      FROM SYSTEM_USERS"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(f"Route GET /system-users (admin) failed: {str(e)}")
        return make_response(jsonify({"error": "Failed to retrieve system users"}), 500)


# ------------------------------------------------------------
# Get all audit logs [Brennan-3]
@admins.route("/audit-logs", methods=["GET"])
def get_audit_logs():
    try:
        current_app.logger.info("GET /audit-logs route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT log_id, user_id, action_type, 
                      table_affected, record_id, details, 
                      ip_address, action_timestamp
                      FROM AUDIT_LOGS"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(f"Route GET /audit-logs (admin) failed: {str(e)}")
        return make_response(jsonify({"error": "Failed to retrieve audit logs"}), 500)


# ------------------------------------------------------------
# Get user system records [Brennan-4]
@admins.route("/user-system-records", methods=["GET"])
def get_user_system_records():
    try:
        current_app.logger.info("GET /user-system-records route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT usr.user_id, su.user_name, su.first_name, su.last_name,
                      usr.log_id, al.action_type, al.table_affected, 
                      al.record_id, usr.access_reason, al.action_timestamp
                      FROM user_system_record usr
                      JOIN SYSTEM_USERS su ON usr.user_id = su.user_id
                      JOIN AUDIT_LOGS al ON usr.log_id = al.log_id
                      ORDER BY al.action_timestamp DESC"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /user-system-records (admin) failed: {str(e)}"
        )
        return make_response(
            jsonify({"error": "Failed to retrieve user system records"}), 500
        )


# ------------------------------------------------------------
# Get all patients [Brennan-5]
@admins.route("/patients", methods=["GET"])
def get_patients():
    try:
        current_app.logger.info("GET /patients route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT patient_id, first_name, last_name, DOB, gender,
                      contact_number, email, address, insurance_provider,
                      insurance_id, emergency_contact_name, emergency_contact_number,
                      managing_user_id, created_at, updated_at
                      FROM PATIENT"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(f"Route GET /patients (admin) failed: {str(e)}")
        return make_response(jsonify({"error": "Failed to retrieve patients"}), 500)


# ------------------------------------------------------------
# Get detailed audit logs [Brennan-6]
@admins.route("/audit-logs/details", methods=["GET"])
def get_audit_logs_details():
    try:
        current_app.logger.info("GET /audit-logs/details route")
        cursor = db.get_db().cursor()
        cursor.execute(
            """SELECT al.log_id, al.user_id, su.user_name, su.first_name, su.last_name,
                      al.action_type, al.table_affected, al.record_id, al.details,
                      al.ip_address, al.action_timestamp
                      FROM AUDIT_LOGS al
                      JOIN SYSTEM_USERS su ON al.user_id = su.user_id
                      ORDER BY al.action_timestamp DESC"""
        )

        theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(
            f"Route GET /audit-logs/details (admin) failed: {str(e)}"
        )
        return make_response(
            jsonify({"error": "Failed to retrieve detailed audit logs"}), 500
        )


# ------------------------------------------------------------
# Create new permission [Brennan-1]
@admins.route("/permissions", methods=["POST"])
def create_permission():
    try:
        current_app.logger.info("POST /permissions route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        permission_name = data.get("permission_name")
        description = data.get("description")
        user_id = data.get("user_id")
        is_active = data.get("is_active", True)

        # Validate required fields
        if not permission_name:
            return make_response(
                jsonify(
                    {"error": "Missing required field: permission_name is required"}
                ),
                400,
            )

        insert_sql_query = """
            INSERT INTO PERMISSIONS (
                permission_name, 
                description,
                user_id, 
                is_active
            ) VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            insert_sql_query,
            (permission_name, description, user_id, is_active),
        )

        db.get_db().commit()

        # Get the ID of the newly created permission
        cursor.execute("SELECT LAST_INSERT_ID()")
        new_permission_id = cursor.fetchone()["LAST_INSERT_ID()"]

        the_response = make_response(
            jsonify(
                {
                    "message": "New permission successfully created",
                    "permission_id": new_permission_id,
                }
            ),
            201,
        )
        return the_response

    except Exception as e:
        current_app.logger.error(f"Route POST /permissions (admin) failed: {str(e)}")
        db.get_db().rollback()
        return make_response(jsonify({"error": "Failed to create new permission"}), 500)


# ------------------------------------------------------------
# Assign permission to user [Brennan-1]
@admins.route("/permissions/<user_id>", methods=["POST"])
def assign_permission_to_user(user_id):
    try:
        current_app.logger.info(f"POST /permissions/{user_id} route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        permission_id = data.get("permission_id")

        # Validate required fields
        if not permission_id:
            return make_response(
                jsonify({"error": "Missing required field: permission_id is required"}),
                400,
            )

        # Check if user exists
        cursor.execute(f"SELECT user_id FROM SYSTEM_USERS WHERE user_id = {user_id}")
        if not cursor.fetchone():
            return make_response(jsonify({"error": "User not found"}), 404)

        # Check if permission exists
        cursor.execute(
            f"SELECT permission_id FROM PERMISSIONS WHERE permission_id = {permission_id}"
        )
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Permission not found"}), 404)

        # Update permission to assign to user
        update_query = """
            UPDATE PERMISSIONS
            SET user_id = %s
            WHERE permission_id = %s
        """

        cursor.execute(update_query, (user_id, permission_id))
        db.get_db().commit()

        the_response = make_response(
            jsonify(
                {
                    "message": f"Permission {permission_id} successfully assigned to user {user_id}"
                }
            ),
            200,
        )
        return the_response

    except Exception as e:
        current_app.logger.error(
            f"Route POST /permissions/{user_id} (admin) failed: {str(e)}"
        )
        db.get_db().rollback()
        return make_response(
            jsonify({"error": "Failed to assign permission to user"}), 500
        )


# ------------------------------------------------------------
# Create new system user [Brennan-2]
@admins.route("/system-users", methods=["POST"])
def create_system_user():
    try:
        current_app.logger.info("POST /system-users route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        user_name = data.get("user_name")
        password = data.get("password")
        email = data.get("email")
        role = data.get("role")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        is_active = data.get("is_active", True)

        # Validate required fields
        if not all([user_name, password, email, role, first_name, last_name]):
            return make_response(
                jsonify(
                    {
                        "error": "Missing required fields: user_name, password, email, role, first_name, and last_name are required"
                    }
                ),
                400,
            )

        # Check if username already exists
        cursor.execute(
            f"SELECT user_id FROM SYSTEM_USERS WHERE user_name = '{user_name}'"
        )
        if cursor.fetchone():
            return make_response(jsonify({"error": "Username already exists"}), 409)

        # Check if email already exists
        cursor.execute(f"SELECT user_id FROM SYSTEM_USERS WHERE email = '{email}'")
        if cursor.fetchone():
            return make_response(jsonify({"error": "Email already exists"}), 409)

        insert_sql_query = """
            INSERT INTO SYSTEM_USERS (
                user_name,
                password,
                email,
                role,
                first_name,
                last_name,
                is_active
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            insert_sql_query,
            (user_name, password, email, role, first_name, last_name, is_active),
        )

        db.get_db().commit()

        # Get the ID of the newly created user
        cursor.execute("SELECT LAST_INSERT_ID()")
        new_user_id = cursor.fetchone()["LAST_INSERT_ID()"]

        the_response = make_response(
            jsonify(
                {
                    "message": "New system user successfully created",
                    "user_id": new_user_id,
                }
            ),
            201,
        )
        return the_response

    except Exception as e:
        current_app.logger.error(f"Route POST /system-users (admin) failed: {str(e)}")
        db.get_db().rollback()
        return make_response(
            jsonify({"error": "Failed to create new system user"}), 500
        )


# ------------------------------------------------------------
# Create new audit log entry [Brennan-3]
@admins.route("/audit-logs", methods=["POST"])
def create_audit_log():
    try:
        current_app.logger.info("POST /audit-logs route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        user_id = data.get("user_id")
        action_type = data.get("action_type")
        table_affected = data.get("table_affected")
        record_id = data.get("record_id")
        details = data.get("details")
        ip_address = data.get("ip_address")

        # Validate required fields
        if not all([action_type, table_affected, record_id, ip_address]):
            return make_response(
                jsonify(
                    {
                        "error": "Missing required fields: action_type, table_affected, record_id, and ip_address are required"
                    }
                ),
                400,
            )

        # Check if user exists if provided
        if user_id:
            cursor.execute(
                f"SELECT user_id FROM SYSTEM_USERS WHERE user_id = {user_id}"
            )
            if not cursor.fetchone():
                return make_response(jsonify({"error": "User not found"}), 404)

        insert_sql_query = """
            INSERT INTO AUDIT_LOGS (
                user_id,
                action_type,
                table_affected,
                record_id,
                details,
                ip_address
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            insert_sql_query,
            (user_id, action_type, table_affected, record_id, details, ip_address),
        )

        db.get_db().commit()

        # Get the ID of the newly created audit log
        cursor.execute("SELECT LAST_INSERT_ID()")
        new_log_id = cursor.fetchone()["LAST_INSERT_ID()"]

        the_response = make_response(
            jsonify(
                {
                    "message": "New audit log entry successfully created",
                    "log_id": new_log_id,
                }
            ),
            201,
        )
        return the_response

    except Exception as e:
        current_app.logger.error(f"Route POST /audit-logs (admin) failed: {str(e)}")
        db.get_db().rollback()
        return make_response(
            jsonify({"error": "Failed to create new audit log entry"}), 500
        )


# ------------------------------------------------------------
# Create access record [Brennan-4]
@admins.route("/user-system-records", methods=["POST"])
def create_access_record():
    try:
        current_app.logger.info("POST /user-system-records route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        user_id = data.get("user_id")
        log_id = data.get("log_id")
        access_reason = data.get("access_reason")

        # Validate required fields
        if not all([user_id, log_id]):
            return make_response(
                jsonify(
                    {
                        "error": "Missing required fields: user_id and log_id are required"
                    }
                ),
                400,
            )

        # Check if user exists
        cursor.execute(f"SELECT user_id FROM SYSTEM_USERS WHERE user_id = {user_id}")
        if not cursor.fetchone():
            return make_response(jsonify({"error": "User not found"}), 404)

        # Check if log exists
        cursor.execute(f"SELECT log_id FROM AUDIT_LOGS WHERE log_id = {log_id}")
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Audit log not found"}), 404)

        # Check if record already exists
        cursor.execute(
            f"SELECT user_id FROM user_system_record WHERE user_id = {user_id} AND log_id = {log_id}"
        )
        if cursor.fetchone():
            return make_response(
                jsonify({"error": "Access record already exists"}), 409
            )

        insert_sql_query = """
            INSERT INTO user_system_record (
                user_id,
                log_id,
                access_reason
            ) VALUES (%s, %s, %s)
        """

        cursor.execute(
            insert_sql_query,
            (user_id, log_id, access_reason),
        )

        db.get_db().commit()

        the_response = make_response(
            jsonify({"message": "Access record successfully created"}), 201
        )
        return the_response

    except Exception as e:
        current_app.logger.error(
            f"Route POST /user-system-records (admin) failed: {str(e)}"
        )
        db.get_db().rollback()
        return make_response(jsonify({"error": "Failed to create access record"}), 500)


# ------------------------------------------------------------
# Update permission status [Brennan-1]
@admins.route("/permissions/<user_id>", methods=["PUT"])
def update_permission_status(user_id):
    try:
        current_app.logger.info(f"PUT /permissions/{user_id} route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        permission_id = data.get("permission_id")
        is_active = data.get("is_active")

        # Validate required fields
        if not permission_id or is_active is None:
            return make_response(
                jsonify(
                    {
                        "error": "Missing required fields: permission_id and is_active are required"
                    }
                ),
                400,
            )

        # Check if user exists
        cursor.execute(f"SELECT user_id FROM SYSTEM_USERS WHERE user_id = {user_id}")
        if not cursor.fetchone():
            return make_response(jsonify({"error": "User not found"}), 404)

        # Check if permission exists
        cursor.execute(
            f"""SELECT permission_id FROM PERMISSIONS 
                WHERE permission_id = {permission_id} AND user_id = {user_id}"""
        )
        if not cursor.fetchone():
            return make_response(
                jsonify({"error": "Permission not found for this user"}), 404
            )

        # Update permission status
        update_query = """
            UPDATE PERMISSIONS
            SET is_active = %s,
                updated_at = CURRENT_TIMESTAMP
            WHERE permission_id = %s AND user_id = %s
        """

        cursor.execute(update_query, (is_active, permission_id, user_id))
        db.get_db().commit()

        # Check if any rows were affected
        if cursor.rowcount == 0:
            return make_response(
                jsonify({"error": "No changes made to permission status"}), 400
            )

        the_response = make_response(
            jsonify({"message": "Permission status successfully updated"}), 200
        )
        return the_response

    except Exception as e:
        current_app.logger.error(
            f"Route PUT /permissions/{user_id} (admin) failed: {str(e)}"
        )
        db.get_db().rollback()
        return make_response(
            jsonify({"error": "Failed to update permission status"}), 500
        )


# ------------------------------------------------------------
# Update user status [Brennan-2]
@admins.route("/system-users", methods=["PUT"])
def update_user_status():
    try:
        current_app.logger.info("PUT /system-users route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        user_id = data.get("user_id")
        is_active = data.get("is_active")
        role = data.get("role")
        email = data.get("email")

        # Validate required fields
        if not user_id:
            return make_response(
                jsonify({"error": "Missing required field: user_id is required"}),
                400,
            )

        # At least one field to update must be provided
        if is_active is None and not role and not email:
            return make_response(
                jsonify({"error": "At least one field to update must be provided"}),
                400,
            )

        # Check if user exists
        cursor.execute(f"SELECT user_id FROM SYSTEM_USERS WHERE user_id = {user_id}")
        if not cursor.fetchone():
            return make_response(jsonify({"error": "User not found"}), 404)

        # Build the update query based on provided fields
        update_fields = []
        params = []

        if is_active is not None:
            update_fields.append("is_active = %s")
            params.append(is_active)

        if role:
            update_fields.append("role = %s")
            params.append(role)

        if email:
            # Check if email already exists for another user
            cursor.execute(
                f"SELECT user_id FROM SYSTEM_USERS WHERE email = '{email}' AND user_id != {user_id}"
            )
            if cursor.fetchone():
                return make_response(
                    jsonify({"error": "Email already in use by another user"}), 409
                )

            update_fields.append("email = %s")
            params.append(email)

        # Add updated_at timestamp
        update_fields.append("updated_at = CURRENT_TIMESTAMP")

        # Add user_id to params
        params.append(user_id)

        # Execute update query
        update_query = f"""
            UPDATE SYSTEM_USERS 
            SET {', '.join(update_fields)} 
            WHERE user_id = %s
        """
        cursor.execute(update_query, params)

        db.get_db().commit()

        # Check if any rows were affected
        if cursor.rowcount == 0:
            return make_response(
                jsonify({"error": "No changes made to user status"}), 400
            )

        the_response = make_response(
            jsonify({"message": "User status successfully updated"}), 200
        )
        return the_response

    except Exception as e:
        current_app.logger.error(f"Route PUT /system-users (admin) failed: {str(e)}")
        db.get_db().rollback()
        return make_response(jsonify({"error": "Failed to update user status"}), 500)


# ------------------------------------------------------------
# Archive inactive patient record [Brennan-5]
@admins.route("/patients", methods=["PUT"])
def archive_patient_record():
    try:
        current_app.logger.info("PUT /patients route")
        cursor = db.get_db().cursor()

        data = request.get_json()
        patient_id = data.get("patient_id")
        archive_status = data.get("archive_status", True)  # Default to archiving
        archive_reason = data.get("archive_reason")

        # Validate required fields
        if not patient_id:
            return make_response(
                jsonify({"error": "Missing required field: patient_id is required"}),
                400,
            )

        # Check if patient exists
        cursor.execute(
            f"SELECT patient_id FROM PATIENT WHERE patient_id = {patient_id}"
        )
        if not cursor.fetchone():
            return make_response(jsonify({"error": "Patient not found"}), 404)

        # Create an archive flag or field in patient record
        # Since there's no specific archive field shown in the schema,
        # we'll assume a field called 'is_archived' exists or needs to be added
        # In a real implementation, this might involve creating an archive table

        # For this example, we'll use an audit log to mark the patient as archived
        if archive_status:
            # Create audit log entry for archiving
            audit_query = """
                INSERT INTO AUDIT_LOGS (
                    user_id,
                    action_type,
                    table_affected,
                    record_id,
                    details,
                    ip_address
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """

            user_id = request.headers.get(
                "User-ID", None
            )  # Assuming user ID passed in header
            action_type = "ARCHIVE"
            table_affected = "PATIENT"
            details = f"Patient record archived. Reason: {archive_reason}"
            ip_address = request.remote_addr

            cursor.execute(
                audit_query,
                (user_id, action_type, table_affected, patient_id, details, ip_address),
            )

            db.get_db().commit()

            the_response = make_response(
                jsonify({"message": "Patient record successfully archived"}), 200
            )
        else:
            # Create audit log entry for unarchiving
            audit_query = """
                INSERT INTO AUDIT_LOGS (
                    user_id,
                    action_type,
                    table_affected,
                    record_id,
                    details,
                    ip_address
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """

            user_id = request.headers.get(
                "User-ID", None
            )  # Assuming user ID passed in header
            action_type = "UNARCHIVE"
            table_affected = "PATIENT"
            details = "Patient record unarchived"
            ip_address = request.remote_addr

            cursor.execute(
                audit_query,
                (user_id, action_type, table_affected, patient_id, details, ip_address),
            )

            db.get_db().commit()

            the_response = make_response(
                jsonify({"message": "Patient record successfully unarchived"}), 200
            )

        return the_response

    except Exception as e:
        current_app.logger.error(f"Route PUT /patients (admin) failed: {str(e)}")
        db.get_db().rollback()
        return make_response(
            jsonify({"error": "Failed to archive/unarchive patient record"}), 500
        )


# ------------------------------------------------------------
# Remove permission [Brennan-1]
@admins.route("/permissions/<user_id>", methods=["DELETE"])
def remove_permission(user_id):
    try:
        current_app.logger.info(f"DELETE /permissions/{user_id} route")
        cursor = db.get_db().cursor()

        # Get permission_id from query parameters
        permission_id = request.args.get("permission_id")

        # Validate required parameters
        if not permission_id:
            return make_response(
                jsonify(
                    {"error": "Missing required parameter: permission_id is required"}
                ),
                400,
            )

        # Check if user exists
        cursor.execute(f"SELECT user_id FROM SYSTEM_USERS WHERE user_id = {user_id}")
        if not cursor.fetchone():
            return make_response(jsonify({"error": "User not found"}), 404)

        # Check if permission exists for this user
        cursor.execute(
            f"""SELECT permission_id FROM PERMISSIONS 
                WHERE permission_id = {permission_id} AND user_id = {user_id}"""
        )
        if not cursor.fetchone():
            return make_response(
                jsonify({"error": "Permission not found for this user"}), 404
            )

        # Delete the permission (or set user_id to NULL to unassign)
        # Option 1: Completely delete the permission
        # delete_query = "DELETE FROM PERMISSIONS WHERE permission_id = %s AND user_id = %s"

        # Option 2: Unassign from user by setting user_id to NULL (preferred for audit trail)
        delete_query = """
            UPDATE PERMISSIONS
            SET user_id = NULL,
                updated_at = CURRENT_TIMESTAMP
            WHERE permission_id = %s AND user_id = %s
        """

        cursor.execute(delete_query, (permission_id, user_id))
        db.get_db().commit()

        # Check if any rows were affected
        if cursor.rowcount == 0:
            return make_response(
                jsonify({"error": "Failed to remove permission from user"}), 500
            )

        the_response = make_response(
            jsonify({"message": "Permission successfully removed from user"}), 200
        )
        return the_response

    except Exception as e:
        current_app.logger.error(
            f"Route DELETE /permissions/{user_id} (admin) failed: {str(e)}"
        )
        db.get_db().rollback()
        return make_response(
            jsonify({"error": "Failed to remove permission from user"}), 500
        )


# ------------------------------------------------------------
# Delete test records [Brennan-4]
@admins.route("/user-system-records", methods=["DELETE"])
def delete_test_records():
    try:
        current_app.logger.info("DELETE /user-system-records route")
        cursor = db.get_db().cursor()

        # Get parameters from query parameters
        user_id = request.args.get("user_id")
        log_id = request.args.get("log_id")
        is_test = (
            request.args.get("is_test", "true").lower() == "true"
        )  # Default to true for safety

        # Validate parameters - at least one filter is required
        if not (user_id or log_id):
            return make_response(
                jsonify(
                    {
                        "error": "At least one filter parameter (user_id or log_id) is required"
                    }
                ),
                400,
            )

        # For safety, we'll only delete records marked as test records
        # In a real system, we'd have a field indicating test vs. production data
        if not is_test:
            return make_response(
                jsonify({"error": "Only test records can be deleted"}),
                403,
            )

        # Build the delete query based on provided parameters
        delete_conditions = []
        params = []

        if user_id:
            delete_conditions.append("user_id = %s")
            params.append(user_id)

        if log_id:
            delete_conditions.append("log_id = %s")
            params.append(log_id)

        # Execute delete query
        delete_query = f"""
            DELETE FROM user_system_record 
            WHERE {' AND '.join(delete_conditions)}
        """
        cursor.execute(delete_query, params)

        db.get_db().commit()

        # Get number of deleted records
        deleted_count = cursor.rowcount

        if deleted_count == 0:
            return make_response(
                jsonify({"message": "No matching test records found to delete"}), 404
            )

        the_response = make_response(
            jsonify(
                {
                    "message": f"Successfully deleted {deleted_count} test record(s)",
                    "count": deleted_count,
                }
            ),
            200,
        )
        return the_response

    except Exception as e:
        current_app.logger.error(
            f"Route DELETE /user-system-records (admin) failed: {str(e)}"
        )
        db.get_db().rollback()
        return make_response(jsonify({"error": "Failed to delete test records"}), 500)
