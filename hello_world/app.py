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
            'Content-Type': 'text/html', 
        }
        "body": "<html><h1>Hello, world<h1><html>",
    }
