from flask import Flask
from app import database_setup
from app.views import bp

global app

def create_app(secret_key, data, database):
    user = data.get('user')
    password = data.get('password')

    db = database_setup.setup_connection(user=user, password=password, database="teste")
    database_setup.run_schema(db)

    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key
    app.register_blueprint(bp)
    app.db = db

    return app