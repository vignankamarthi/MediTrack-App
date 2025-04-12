########################################################
# Routing Connection Matrices for USER PERSONA: PHARMACIST
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

# Create a new Blueprint object for the Pharmacist User Persona
# Allows for a variable to store a collection of routes.
pharmacist = Blueprint('pharmacist', __name__)

#--------------------[ Pharmacist User Persona ~ Sarah Chen #1 ]----------------------