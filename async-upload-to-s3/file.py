import io
import boto3
import base64
from flask import Flask
from typing import Callable
from datetime import datetime
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from models import File


def renaming_file(filename: str):
    uploaded_date = datetime.utcnow()

    if filename is None:
        raise ValueError("Filename is required")

    splitted = filename.rsplit(".", 1)
    if len(splitted) < 2:
        raise ValueError("Filename must have an extension")

    updated_filename = splitted[0]
    file_extension = splitted[1]
    updated_filename = secure_filename(updated_filename.lower())
    updated_filename = f"{uploaded_date.strftime('%Y%m%d%H%M%S')}--{updated_filename}"
    updated_filename = f"{updated_filename}.{file_extension}"

    return updated_filename


def process_file_to_stream(file: FileStorage) -> dict:
    result = {
        "stream": base64.b64encode(file.stream.read()),
        "name": file.name,
        "filename": renaming_file(file.filename),
        "content_type": file.content_type,
        "content_length": file.content_length,
        "headers": {header[0]: header[1] for header in file.headers},
    }

    return result


def create_upload_file(app: Flask) -> Callable:
    s3 = boto3.client(
        "s3",
        aws_access_key_id=app.config["AWS_ACCESS_KEY"],
        aws_secret_access_key=app.config["AWS_ACCESS_SECRET"],
    )

    def upload_file(data: dict) -> str:
        data["stream"] = base64.b64decode(data["stream"])
        data["stream"] = io.BytesIO(data["stream"])
        file = FileStorage(**data)

        print("upload_file File", File)
        # s3.upload_fileobj(
        #     file,
        #     app.config["S3_BUCKET_NAME"],
        #     data["filename"],
        #     ExtraArgs={
        #         "ContentType": data["content_type"],
        #     },
        # )
        return f"{app.config['S3_BUCKET_BASE_URL']}/{data['filename']}"

    return upload_file
