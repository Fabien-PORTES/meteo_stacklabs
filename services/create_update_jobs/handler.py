import boto3
import os
from transform_conf import CONF
import json

ONE_JOB_LAMBDA = os.environ['ONE_JOB_LAMBDA']

def main(event, context):
    lambda_client = boto3.client('lambda')
    for c in CONF:
        lambda_client.invoke(FunctionName=ONE_JOB_LAMBDA, 
                            InvocationType='Event',
                            Payload=json.dumps(c))

    response = {
        "statusCode": 200,
        "body": json.dumps('success')
    }

    return response
