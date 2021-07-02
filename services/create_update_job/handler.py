import boto3
import os
import json
from template.glue_conf import job_conf
from transform_generation import get_script

SCRIPT_JOB_S3 = os.environ['S3_JOB_SCRIPT_BUCKET']

def main(event, context):
    glue_client = boto3.client('glue')
    s3_client = boto3.client('s3')

    # create pyspark transform script to clean city-station data
    script_name = '{}.py'.format(event['table_name'])
    script = get_script(**event)
    s3_client.put_object(
        Body=script,
        Bucket=SCRIPT_JOB_S3,
        Key='scripts/{}'.format(script_name)
        )

    # create glue job according to passed configuration
    job_name = event['table_name']
    job_conf['Name'] = job_name
    job_conf['Command']['ScriptLocation'] = 's3://' + SCRIPT_JOB_S3 + '/scripts/' + script_name

    try:
        glue_client.create_job(**job_conf)
    except glue_client.exceptions.IdempotentParameterMismatchException:
        del job_conf['Name']
        if 'Tags' in job_conf:
            del job_conf['Tags']
        glue_client.update_job(
            JobName=job_name,
            JobUpdate=job_conf)
    
    response = {
        "statusCode": 200,
        "body": json.dumps('success')
    }

    return response
