import json


def lambda_handler(event, context):
    request_body = json.loads(event["body"])
    response = f"Hello {request_body['name']}! Your age is {request_body['age']}"
    return {"statusCode": 200, "body": json.dumps(response)}
