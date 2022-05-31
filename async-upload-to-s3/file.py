import io
import boto3
import base64
from datetime import datetime
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


def process_file_to_stream(file: FileStorage, to_utf8: bool = False) -> dict:
    stream = base64.b64encode(file.stream.read())
    result = {
        "stream": stream if not to_utf8 else stream.decode("utf-8"),
        "name": file.name,
        "filename": renaming_file(file.filename),
        "content_type": file.content_type,
        "content_length": file.content_length,
        "headers": {header[0]: header[1] for header in file.headers},
    }

    return result


def upload_file(file: FileStorage) -> str:
    s3.upload_fileobj(
        file,
        app.config["S3_BUCKET_NAME"],
        file.filename,
        ExtraArgs={
            "ContentType": file.content_type,
        },
    )
    return f"{app.config['S3_BUCKET_BASE_URL']}/{file.filename}"


def upload_file_from_stream(data: dict) -> str:
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
