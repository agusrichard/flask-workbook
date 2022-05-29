from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from models import File

with app.app_context():
    db.create_all()

from file import create_upload_file

upload_file = create_upload_file(app)

from routes import Routes

routes = Routes(upload_file)

app.add_url_rule("/", "index", routes.index, methods=["GET"])
app.add_url_rule(
    "/normal_upload", "normal_upload", routes.normal_upload, methods=["POST"]
)
app.add_url_rule("/async_upload", "async_upload", routes.async_upload, methods=["POST"])
app.add_url_rule(
    "/celery_upload", "celery_upload", routes.celery_upload, methods=["POST"]
)


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "File": File}
