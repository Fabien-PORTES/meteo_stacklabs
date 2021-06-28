cleaning_job_conf = {
    'Name':'',
    'Description':'',
    'Role':'meteo_aws_glue_role',
    'ExecutionProperty':{
        'MaxConcurrentRuns': 20
    },
    'Command':{
        'Name': 'glueetl',
        'ScriptLocation': None,
        'PythonVersion': '3'
    },
    'DefaultArguments':{
        'enable-spark-ui': 'true',
        'spark-event-logs-path': 's3://aws-glue-assets-530505212955-eu-west-1/sparkHistoryLogs/',
        'enable-glue-datacatalog': 'true'
    },
    'NonOverridableArguments':{},
    'MaxRetries':0,
    'Timeout':2880,
    'Tags':{
        'project': 'meteo'
    },
    'GlueVersion':'2.0',
    'NumberOfWorkers':2,
    'WorkerType':'G.1X'
}
