from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db =  SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://agusrichard:agusrichard@0.0.0.0:3308/rest_flask_app_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    
    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes

        db.create_all()  # Create database tables for our data models

        return app

    return app