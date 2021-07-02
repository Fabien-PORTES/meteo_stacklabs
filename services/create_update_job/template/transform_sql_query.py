script = '''import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)

SqlQuery0 = \'\'\'{QUERY}\'\'\'

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

{DATASOURCES}

Transform0 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {DATASOURCE_MAPPING}, transformation_ctx = "Transform0")

DataSink0 = glueContext.getSink(path = "s3://meteostacklabsglued/{S3_FOLDER}/", connection_type = "s3", updateBehavior = "UPDATE_IN_DATABASE", partitionKeys = [], compression = "snappy", enableUpdateCatalog = True, transformation_ctx = "DataSink0")
DataSink0.setCatalogInfo(catalogDatabase = "meteo_s3", catalogTableName = "{TABLE_NAME}")
DataSink0.setFormat("glueparquet")
DataSink0.writeFrame(Transform0)


job.commit()'''