import json

# import requests


def lambda_handler(event, context):
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "headers": {
            'Content-Type': 'text/json', 
        }
        "body": json.dumps({'Hello', 'World'}),
    }
