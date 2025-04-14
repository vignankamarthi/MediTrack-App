from flask import Flask

from backend.db_connection import db

# Added imports for MediTrack blueprints
from backend.nurses.nurse_routes import nurses
from backend.pharmacists.pharmacist_routes import pharmacists
from backend.physicians.physician_routes import physicians
from backend.system_admins.admin_routes import admins
import os
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    # Load environment variables
    # This function reads all the values from inside
    # the .env file (in the parent folder) so they
    # are available in this file.  See the MySQL setup
    # commands below to see how they're being used.
    load_dotenv()

    # secret key that will be used for securely signing the session
    # cookie and can be used for any other security related needs by
    # extensions or your application
    # app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    # # these are for the DB object to be able to connect to MySQL.
    # app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config["MYSQL_DATABASE_USER"] = os.getenv("DB_USER").strip()
    app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("MYSQL_ROOT_PASSWORD").strip()
    app.config["MYSQL_DATABASE_HOST"] = os.getenv("DB_HOST").strip()
    app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("DB_PORT").strip())
    app.config["MYSQL_DATABASE_DB"] = os.getenv(
        "DB_NAME"
    ).strip()  # Change this to your DB name

    # Initialize the database object with the settings above.
    app.logger.info("current_app(): starting the database connection")
    db.init_app(app)

    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    # Register MediTrack blueprints
    app.register_blueprint(nurses, url_prefix="/n")
    app.register_blueprint(pharmacists, url_prefix="/ph")
    app.register_blueprint(physicians, url_prefix="/dr")
    app.register_blueprint(admins, url_prefix="/admin")

    # Don't forget to return the app object
    return app
