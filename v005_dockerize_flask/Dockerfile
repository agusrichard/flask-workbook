FROM ubuntu:20.04

LABEL agusrichard "agus.richard21@gmail.com"

RUN apt-get update -y && apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD ["python3", "./app.py"]