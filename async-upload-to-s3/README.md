# Python Flask: Asynchronous Upload to S3

### Table of Contents:

- [Description](#description)
- [Installation/Development](#installationdevelopment)

## Description

This project serves as coding material for this article, so readers can easily look at the entire code if they face some problem

## Installation/Development

- Make sure you have Docker engine installed on your machine before running this project. Especially, when running upload using celery.
- Clone/Download this repository and change directory to this project.
- Run `docker-compose up` to run and build project's container and related containers.
- Go to http://0.0.0.0:5000 (default url)
- Here are endpoints you can check and play with. You can test it by providing form data with key of `file` and value of your own file that you want to upload:
  - http://0.0.0.0:5000 => Basic dummy endpoint
  - http://0.0.0.0:5000/normal_upload => Synchronous upload
  - http://0.0.0.0:5000/async_upload => Asynchronous upload using threading
  - http://0.0.0.0:5000/celery_upload => Asynchronous upload using celery
