from template.transform_sql_query import script


def get_datasource(tables_name, database='meteo_s3'):
    datasources = '''DataSource{i} = glueContext.create_dynamic_frame.from_catalog(database = "{database}", table_name = "{table_name}", transformation_ctx = "DataSource{i}")'''
    return '\n\n'.join([datasources.format(table_name=t, database=database, i=i) for i, t in enumerate(tables_name)])

def get_script(query, datasources, s3_folder, table_name):
    datasource_mapping = '{{{}}}'.format(', '.join(['"{}": DataSource{}'.format(a, i) for i, a in enumerate(datasources)]))
    query = query.format(**dict(('datasource_{}'.format(i), d ) for i,d in enumerate(datasources)))
    return script.format(
        QUERY=query,
        DATASOURCES=get_datasource(datasources),
        DATASOURCE_MAPPING=datasource_mapping,
        S3_FOLDER=s3_folder,
        TABLE_NAME=table_name
    )
