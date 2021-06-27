import boto3
import os
import json
import urllib
from datetime import datetime
from job_conf.job_template import cleaning_job_conf
from script_template.toulouse import script as job_script


SCRIPT_JOB_S3 = os.environ['S3_JOB_SCRIPT_BUCKET']

def main(event, context):
    glue_client = boto3.client('glue')
    s3_client = boto3.client('s3')

    columns = event['columns']
    city = event['city'].lower()
    station = event['station']

    script_name = '{}_{}_cleaned.py'.format(city, station)
    script = job_script.format(COLUMNS=', '.join(columns), city=city, station_num=station)
    s3_client.put_object(
        Body=script,
        Bucket=SCRIPT_JOB_S3,
        Key='scripts/{}'.format(script_name)
        )

    job_name = '{}_{}_cleaned'.format(city, station)
    cleaning_job_conf['Name'] = job_name
    cleaning_job_conf['Command']['ScriptLocation'] = 's3://' + SCRIPT_JOB_S3 + '/scripts/' + script_name
    glue_client.create_job(**cleaning_job_conf)
    
    response = {
        "statusCode": 200,
        "body": json.dumps('success')
    }

    return response
