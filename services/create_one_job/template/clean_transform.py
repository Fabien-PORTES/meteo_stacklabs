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

columns = "{columns_list}"

SqlQuery0 = \'\'\'
select
{{}},
to_timestamp({timestamp_record_column}) as record_timestamp
from stationData
{where_statement}

\'\'\'.format(columns)

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "meteo_s3", table_name = "{city}_{station}", transformation_ctx = "DataSource0"]
## @return: DataSource0
## @inputs: []
DataSource0 = glueContext.create_dynamic_frame.from_catalog(database = "meteo_s3", table_name = "{city}_{station}", transformation_ctx = "DataSource0")
## @type: SqlCode
## @args: [sqlAliases = {{"stationData": DataSource0}}, sqlName = SqlQuery0, transformation_ctx = "Transform0"]
## @return: Transform0
## @inputs: [dfc = DataSource0]
Transform0 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {{"stationData": DataSource0}}, transformation_ctx = "Transform0")
## @type: DataSink
## @args: [connection_type = "s3", catalog_database_name = "meteo_s3", format = "glueparquet", connection_options = {{"path": "s3://meteostacklabsglued/{city}_{station}/", "compression": "snappy", "partitionKeys": [], "enableUpdateCatalog":true, "updateBehavior":"UPDATE_IN_DATABASE"}}, catalog_table_name = "toulouse_34_cleaned", transformation_ctx = "DataSink0"]
## @return: DataSink0
## @inputs: [frame = Transform0]
DataSink0 = glueContext.getSink(path = "s3://meteostacklabsglued/{city}_{station}/", connection_type = "s3", updateBehavior = "UPDATE_IN_DATABASE", partitionKeys = [], compression = "snappy", enableUpdateCatalog = True, transformation_ctx = "DataSink0")
DataSink0.setCatalogInfo(catalogDatabase = "meteo_s3",catalogTableName = "{city}_{station}_cleaned")
DataSink0.setFormat("glueparquet")
DataSink0.writeFrame(Transform0)

job.commit()'''