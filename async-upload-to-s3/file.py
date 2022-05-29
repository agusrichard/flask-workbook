import io
import boto3
import base64
from flask import Flask
from datetime import datetime
from typing import Callable, Dict
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from app import app

s3 = boto3.client(
    "s3",
    aws_access_key_id=app.config["AWS_ACCESS_KEY"],
    aws_secret_access_key=app.config["AWS_ACCESS_SECRET"],
)


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

def process_files_to_streams(files: Dict[str, FileStorage]) -> dict:
    """
    Process a file to a base64 string
    """
    result = {}

    for key, file in files.items():
        if file is None or file.filename == "":
            continue  # skip not required fields/files

        result[key] = {
            "stream": base64.b64encode(file.stream.read()),
            "name": file.name,
            "filename": renaming_file(file.filename),
            "content_type": file.content_type,
            "content_length": file.content_length,
            "headers": {header[0]: header[1] for header in file.headers},
        }

    return result

def upload_file(data: dict) -> str:
    data["stream"] = base64.b64decode(data["stream"])
    data["stream"] = io.BytesIO(data["stream"])
    file = FileStorage(**data)

    s3.upload_fileobj(
        file,
        app.config["S3_BUCKET_NAME"],
        data["filename"],
        ExtraArgs={
            "ContentType": data["content_type"],
        },
    )
    return f"{app.config['S3_BUCKET_BASE_URL']}/{data['filename']}"