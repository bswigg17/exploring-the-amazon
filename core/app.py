import json
import boto3
from boto3.dynamodb.conditions import Key

# import requests


# def lambda_handler(event, context):
#     dynamodb = boto3.resource('dynamodb')
#     table = dynamodb.Table('TeamDB')
#     res = table.query(
#         KeyConditionExpression=Key('team').eq('ELERA_PAY')
#     )
#     data = res['Items']
#     return {
#         "statusCode": 200,
#         "headers": {
#             'Content-Type': 'text/json', 
#         }, 
#         "body": json.dumps(item),
#     }

# def put_data_handler(event, context): 
#     dynamodb = boto3.resource('dynamodb')
#     table = dynamodb.Table('TeamDB')


def get_data_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('TeamDB')
    # Grab query params for data. 
    params = event.get('queryStringParameters')
    # Query Data 
    data = ""
    # If no params, then no data
    if params is None: 
        data = 'None'
    # If only team param, then grab all data
    elif not params.get('data', 0):
        response = table.query(
                KeyConditionExpression=Key('team').eq(params['team'])
            )
        data = response['Items']
    # If team param and data param, then get. 
    else:
        response = table.get_item(
                Key={
                    "team": params['team'],
                    "data": params['data']
                }
            )
        data = response['Item']
    return {
        'statusCode': 200, 
        'headers': {
            'Content-Type': 'text/json'
        }, 
        'body': json.dumps(data)
    }