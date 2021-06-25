import boto3
import json
import urllib
from datetime import datetime

S3_BUCKET = "meteostacklabs"

def main(event, context):
    url = event['url']
    city = event['city']
    station = event['station']

    res = urllib.request.urlopen(urllib.request.Request(
        url=url,
        headers={'Accept': 'application/json'},
        method='GET'),
    timeout=100
    )
    
    s3_file_path = '{}-{}/{}'.format(city, station, '{}-{}'.format(city, station))
    s3 = boto3.client('s3')
    
    s3.upload_fileobj(res, S3_BUCKET, s3_file_path)


    response = {
        "statusCode": 200,
        "body": json.dumps('success')
    }

    return response

