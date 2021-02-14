from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db =  SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://agusrichard:agusrichard@db/rest_flask_app_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from src.todo import todo as todo_blueprint
    app.register_blueprint(todo_blueprint, url_prefix='/todo')

    with app.app_context():
        from src.todo import model
        db.create_all()  # Create database tables for our data models
        db.session.commit()

        return app