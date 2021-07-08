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

# update hadoop conf to avoid creation of empty folders $_folder_$
hadoop_conf = sc._jsc.hadoopConfiguration()
hadoop_conf.set("fs.s3.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")

{DATASOURCES}

Transform0 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {DATASOURCE_MAPPING}, transformation_ctx = "Transform0")

Transform0 = Transform0.toDF()
# write data with spark write method as dynamic frame context doesn't support overwrite
Transform0.write.mode('overwrite').parquet('s3://meteostacklabsglued/{S3_FOLDER}')

job.commit()'''