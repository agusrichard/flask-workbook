from flask import request
from typing import Callable

from models import File
from file import process_file_to_stream


class Routes:
    def __init__(self, upload_file: Callable) -> None:
        self.upload_file = upload_file

    def index(self):
        print("Routes File", File)
        return "Hello World!"

    def normal_upload(self):
        file = request.files["file"]
        data = process_file_to_stream(file)
        self.upload_file(data)
        return "Normal upload"

    def async_upload(self):
        return "Async upload"

    def celery_upload(self):
        return "Celery upload"
