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



#--------------------[System Admin User Persona ~ Brennan #1 ]----------------------



# Get all permissions from the system
@admins.route("/permissions", methods=["GET"])
def get_permissions():
    current_app.logger.info("GET /permissions route")
    cursor = db.get_db().cursor()
    cursor.execute(
        '''SELECT permission_id, permission_name, 
                      description, user_id, is_active 
                      FROM PERMISSIONS'''
    )

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Create new permission
@admins.route('/permissions', methods=['POST'])
def create_new_permission():
    cursor = db.get_db().cursor()
    current_app.logger.info(f"POST /permissions route")

    data = request.get_json()

    permission_name = data.get('permission_name')
    description = data.get('description')
    user_id = data.get('user_id')

    if not (permission_name and description and user_id): 
        return make_response(jsonify({"error": "Missing Inputs and Change is required and no new input"}), 400)
    

    mysql_sql_query = '''
        INSERT INTO PERMISSIONS (permission_name, description, user_id
        ) VALUES (%s, %s, %s)
    '''

    cursor.execute(mysql_sql_query, (permission_name, description, user_id))
    
    db.get_db().commit()

    the_response = make_response(jsonify({"message": "Permission was Sucessfully Created"}), 201)

    if data:
        return the_response
    else:
        return make_response(jsonify({"error": "Permission Not Found"}), 404)
    
# Get permissions for a specific user from the system
@admins.route("/permissions/<user_id>", methods=["GET"])
def get_permissions_for_user(user_id):
    current_app.logger.info("GET /permissions/{user_id} route")
    cursor = db.get_db().cursor()
    cursor.execute(
        '''SELECT permission_id, permission_name, 
                      description, user_id, is_active 
                      FROM PERMISSIONS
                      WHERE user_id = {0}'''.format(user_id)
    )

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Assign permission for user
@admins.route('/permissions/<user_id>', methods=['POST'])
def create_new_permission_for_user(user_id):
    cursor = db.get_db().cursor()
    current_app.logger.info(f"POST //permissions/{user_id} route")

    data = request.get_json()

    permission_name = data.get('permission_name')
    description = data.get('description')


    if not (permission_name and user_id): 
        return make_response(jsonify({"error": "Missing Inputs and Change is required and no new input"}), 400)
    

    mysql_sql_query = '''
        INSERT INTO PERMISSIONS (permission_name, description, user_id
        ) VALUES (%s, %s, %s)
    '''

    cursor.execute(mysql_sql_query, (permission_name, description, user_id))
    
    db.get_db().commit()

    the_response = make_response(jsonify({"message": "Permission was Sucessfully Created"}), 201)

    if data:
        return the_response
    else:
        return make_response(jsonify({"error": "Permission Not Found"}), 404)

# update a patient's social determinant impact level
@admins.route('/permissions/<user_id>', methods=['PUT'])
def update_permission_status(user_id):
    cursor = db.get_db().cursor()
    current_app.logger.info(f"PUT /permissions/{user_id} route")

    data = request.get_json()
    permission_id = data.get('permission_id')
    is_active = data.get('is_active')


    if not (permission_id and is_active):
        return make_response(jsonify({"error": "There is no valid permission to add to this user"}), 400)
    

    mysql_query = '''
        UPDATE PERMISSIONS
        SET is_active = %s, updated_at = CURRENT_TIMESTAMP
        WHERE permission_id = %s AND user_id = %s
    '''
    cursor.execute(mysql_query, (is_active, permission_id, user_id))
    
    db.get_db().commit()
    
    the_response = make_response(jsonify({"message": "Permission Status was Sucessfully Updated"}))
    the_response.status_code = 200
    return the_response

# remove a permission from a user
@admins.route('/permissions/<user_id>', methods=['DELETE'])
def remove_user_permissions(user_id):
    cursor = db.get_db().cursor()
    current_app.logger.info(f"DELETE /permissions/{user_id} route")

    data = request.get_json()
    permission_id = data.get('permission_id')

    if not (permission_id):
        return make_response(jsonify({"error": "There is no valid determinant assigned to the patient"}), 400)
    

    mysql_query = '''
        DELETE FROM PERMISSIONS
        WHERE permission_id = %s AND user_id = %s
    '''
    cursor.execute(mysql_query, (permission_id, user_id))
    
    db.get_db().commit()
    
    the_response = make_response(jsonify({"message": "User Permissions was Sucessfully Removed"}))
    the_response.status_code = 200
    return the_response



    #--------------------[System Admin User Persona ~ Brennan #2 ]----------------------
    


# Return all system users
@admins.route("/system-users", methods=["GET"])
def get_all_system_users():
    current_app.logger.info("GET /system-users route")
    cursor = db.get_db().cursor()
    cursor.execute(
        '''SELECT user_id, user_name, email, role, is_active, first_name, last_name, last_login, created_at, updated_at
                      FROM SYSTEM_USER'''
    )

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Create new system user
@admins.route('/system-users', methods=['POST'])
def create_new_system_user():
    cursor = db.get_db().cursor()
    current_app.logger.info(f"POST /system-users route")

    data = request.get_json()

    user_id = data.get('user_id')
    user_name = data.get('user_name')
    password = data.get('password')
    email = data.get('email')
    role = data.get('role')
    is_active = data.get('is_active')
    first_name = data.get('first_name')
    last_name = data.get('last_name')


    if not (user_id and user_name and email): 
        return make_response(jsonify({"error": "Missing Inputs and Change is required and no new input"}), 400)
    

    mysql_sql_query = '''
        INSERT INTO SYSTEM_USERS (user_id, user_name, password, email, role, is_active, first_name, last_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''

    cursor.execute(mysql_sql_query, (user_id, user_name, password, email, role, is_active, first_name, last_name))
    
    db.get_db().commit()

    the_response = make_response(jsonify({"message": "System User Created Sucessfully"}), 201)

    
    return the_response


# update a user's activity status
@admins.route('/system-users', methods=['PUT'])
def update_user_permission_status(user_id):
    cursor = db.get_db().cursor()
    current_app.logger.info(f"PUT /system-users route")

    data = request.get_json()
    user_id = data.get('user_id')
    is_active = data.get('is_active')


    if not (user_id and is_active):
        return make_response(jsonify({"error": "Invalid Input and unable to change user's activity status"}), 400)
    

    mysql_query = '''
        UPDATE SYSTEM_USERS
        SET is_active = %s, updated_at = CURRENT_TIMESTAMP
        WHERE user_id = %s
    '''
    cursor.execute(mysql_query, (is_active, user_id))
    
    db.get_db().commit()
    
    the_response = make_response(jsonify({"message": "User's activity status was created sucessfully"}))
    the_response.status_code = 200
    return the_response



#--------------------[System Admin User Persona ~ Brennan #3 ]----------------------



# Return comprehensive audit logs
@admins.route("/audit-logs", methods=["GET"])
def get_all_audit_logs():
    current_app.logger.info("GET /audit-logs route")
    cursor = db.get_db().cursor()
    cursor.execute(''' SELECT al.log_id, al.user_id, sysU.user_name, sysU.role, al.action_type, al.table_affected, al.record_id, al.details, al.ip_address, al.action_timestamp
                      FROM AUDIT_LOGS al
                      JOIN SYSTEM_USERS sysU ON al.user_id = sysU.user_id
                      ORDER BY al.action_timestamp DESC'''
                      
    )

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#Create new audit log entry 
@admins.route('/audit-logs', methods=['POST'])
def create_new_audit_log():
    cursor = db.get_db().cursor()
    current_app.logger.info(f"POST /audit-logs route")

    data = request.get_json()

    user_id = data.get('user_id')
    action_type = data.get('action_type')
    table_affected = data.get('table_affected')
    record_id = data.get('record_id')
    ip_address = data.get('ip_address')



    if not (user_id and record_id and ip_address): 
        return make_response(jsonify({"error": "Missing Inputs and Change is required and no new input"}), 400)
    

    mysql_sql_query = '''
        INSERT INTO AUDIT_LOGS (user_id, action_type, table_affected, record_id, ip_address) VALUES (%s, %s, %s, %s, %s)
    '''

    cursor.execute(mysql_sql_query, (user_id, action_type, table_affected, record_id, ip_address))
    
    db.get_db().commit()

    the_response = make_response(jsonify({"message": "Audit Log Was Created Sucessfully"}), 201)

    
    return the_response



#--------------------[System Admin User Persona ~ Brennan #4 ]----------------------



# Return user system access records
@admins.route('/user-system-records', methods=['GET'])
def get_user_system_records():
    current_app.logger.info("GET /user-system-records route")
    cursor = db.get_db().cursor()
    cursor.execute(
        '''SELECT al.log_id, al.user_id, sysU.user_name, su.role, al.action_type, al.table_affected, al.record_id, al.details, al.ip_address, al.action_timestamp
                      FROM user_system_record usr
                      JOIN SYSTEM_USERS sysU ON usr.user_id = sysU.user_id
                      JOIN AUDIT_LOGS al ON usr.log_id = al.log_id 
                      ORDER BY al.action_timestamp DESC'''
                      
    )

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Create access record
@admins.route('/user-system-records', methods=['POST'])
def create_new_user_system_record():
    cursor = db.get_db().cursor()
    current_app.logger.info(f"POST /user-system-records route")

    data = request.get_json()

    user_id = data.get('user_id')
    log_id = data.get('log_id')
    access_reason = data.get('access_reason')

    if not (user_id and log_id and access_reason): 
        return make_response(jsonify({"error": "Missing Inputs and Change is required and no new input"}), 400)
    

    mysql_sql_query = '''
        INSERT INTO user_system_record (user_id, log_id, access_reason) VALUES (%s, %s, %s)
    '''

    cursor.execute(mysql_sql_query, (user_id, log_id, access_reason))
    
    db.get_db().commit()

    the_response = make_response(jsonify({"message": "Access Record Was Created Sucessfully"}), 201)

    return the_response

# Delete test records 
@admins.route('/user-system-records', methods=['DELETE'])
def delete_user_system_records():
    cursor = db.get_db().cursor()
    current_app.logger.info(f"DELETE /user-system-records route")

    data = request.get_json()
    access_reason = data.get('access_reason')
    user_id = data.get('user_id')

    if not (access_reason):
        return make_response(jsonify({"error": "There is no valid access reason to be able to delete the user"}), 400)
    

    mysql_query = '''
        DELETE FROM user_system_record
        WHERE user_id = %s AND access_reason = %s
    '''
    cursor.execute(mysql_query, (user_id, access_reason))
    
    db.get_db().commit()
    
    the_response = make_response(jsonify({"message": "User System Record was Sucessfully Removed"}))
    the_response.status_code = 200
    return the_response


#--------------------[System Admin User Persona #5 ]----------------------
#need to complete
#--------------------[System Admin User Persona #6 ]----------------------
#need to complete