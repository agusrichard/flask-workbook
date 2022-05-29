FROM python:3.8-alpine

LABEL agusrichard "agus.richard21@gmail.com"

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

RUN FLASK_APP=app.py && FLASK_ENV=development

CMD ["python", "/app/app.py"]