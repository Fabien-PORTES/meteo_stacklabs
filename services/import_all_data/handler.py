import boto3
import os
import json
import urllib
from datetime import datetime
from station_list import CONF

ONE_STATION_LAMBDA = os.environ['IMPORT_ONE_STATION']

def main(event, context):
    lambda_client = boto3.client('lambda')
    for c in CONF:
        lambda_client.invoke(FunctionName=ONE_STATION_LAMBDA, 
                            InvocationType='Event',
                            Payload=json.dumps(c))

    response = {
        "statusCode": 200,
        "body": json.dumps('success')
    }

    return response

