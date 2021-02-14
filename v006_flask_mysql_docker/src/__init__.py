from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db =  SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://agusrichard:agusrichard@0.0.0.0:3308/rest_flask_app_db'
    
    db.init_app(app)
    
    return app