FROM ubuntu:20.04

MAINTAINER Agus Richard "agus.richard21@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r /app/requirements.txt

COPY . /app

RUN export FLASK_APP=app.py && export FLASK_ENV=development

ENTRYPOINT ["flask", "run"]