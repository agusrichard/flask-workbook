# Python Flask: Asynchronous Upload to S3

### Table of Contents:

- [Description](#description)
- [Installation/Development](#installationdevelopment)

## Description

This project serves as coding material for this article, so readers can easily look at the entire code if they face some problem. The article and this project will show us how to upload files to AWS S3 from Flask application using several methods, they're normal upload, upload using threading (async upload), and upload using celery (async upload).

## Installation/Development

- Make sure you have Docker engine installed on your machine before running this project. Especially, when running upload using celery.
- Clone/Download this repository and change directory to this project.
- Create .env file and put these variables. Certainly you need to provide values to these variables:
  ```text
  SQLALCHEMY_DATABASE_URI=
  SQLALCHEMY_TRACK_MODIFICATIONS=
  AWS_ACCESS_KEY=
  S3_BUCKET_NAME=
  S3_BUCKET_BASE_URL=
  CELERY_BROKER_URL=
  CELERY_RESULT_BACKEND=
  ```
- Run `docker-compose up` to run and build project's container and related containers.
- Go to http://0.0.0.0:5000 (default url)
- Here are endpoints you can check and play with. You can test it by providing form data with key of `file` and value of your own file that you want to upload:
  - http://0.0.0.0:5000 => Basic dummy endpoint
  - http://0.0.0.0:5000/normal_upload => Synchronous upload
  - http://0.0.0.0:5000/async_upload => Asynchronous upload using threading
  - http://0.0.0.0:5000/celery_upload => Asynchronous upload using celery
