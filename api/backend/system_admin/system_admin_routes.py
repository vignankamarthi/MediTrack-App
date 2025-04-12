########################################################
# Routing Connection Matrices for USER PERSONA: SYSTEM ADMIN
# 
# Purpose: Allow the physican role to easily analyze data 
# and record new findings.
########################################################

# Required Imports to Establish a Connection
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------

# Create a new Blueprint object for the System Admin User Persona
# Allows for a variable to store a collection of routes.
system_admin = Blueprint('system_admin', __name__)

#--------------------[ System Administrator User Persona ]----------------------