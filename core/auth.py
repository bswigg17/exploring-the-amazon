import json

def auth_handler(event, context):
    return {
        'statusCode': '200',
        'headers': {
            'Content-Type': 'text/json'
        },
        'body': json.dumps(['Success'])
    }