import enum
from sqlalchemy import Enum

from app import db

class UploadStatus(enum.Enum):
    PENDING = 1
    PROCESSING = 2
    COMPLETE = 3
    ERROR = 4

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    url = db.Column(db.String(255), unique=True, nullable=False)
    upload_status = db.Column(Enum(UploadStatus), nullable=False)

    def __repr__(self):
        return f'<File {self.name}>'