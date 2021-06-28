import boto3
import os
import json
import urllib
from datetime import datetime
from template.glue_conf import cleaning_job_conf
from template.clean_transform import script as job_script
from transform_conf import CONF

SCRIPT_JOB_S3 = os.environ['S3_JOB_SCRIPT_BUCKET']

def main(event, context):
    glue_client = boto3.client('glue')
    s3_client = boto3.client('s3')


    object_path = event['Records'][0]['s3']['object']['key']
    city, station = object_path.split('/')[0].split('-')

    city_station_conf = [c for c in CONF if (c['city'].lower() == city) and c['station'].lower() == station][0]
    city_station_conf['columns_list'] = ', '.join(city_station_conf['columns_list'])


    # create pyspark transform script to clean city-station data
    script_name = '{}_{}_cleaned.py'.format(city, station)
    script = job_script.format(**city_station_conf)
    s3_client.put_object(
        Body=script,
        Bucket=SCRIPT_JOB_S3,
        Key='scripts/{}'.format(script_name)
        )

    # create glue job ro clean city-station data
    job_name = '{}_{}_cleaned'.format(city, station)
    cleaning_job_conf['Name'] = job_name
    cleaning_job_conf['Command']['ScriptLocation'] = 's3://' + SCRIPT_JOB_S3 + '/scripts/' + script_name

    try:
        glue_client.create_job(**cleaning_job_conf)
    except glue_client.exceptions.IdempotentParameterMismatchException:
        del cleaning_job_conf['Name']
        del cleaning_job_conf['Tags']
        glue_client.update_job(
            JobName=job_name,
            JobUpdate=cleaning_job_conf)
    
    glue_client.start_job_run(JobName=job_name)
    
    response = {
        "statusCode": 200,
        "body": json.dumps('success')
    }

    return response
