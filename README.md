# METEO

This project aims to create vizualization on top of data related to Toulouse weather. These data can be found on the gouvernement open data [website](https://www.data.gouv.fr/fr/datasets/?q=toulouse&tag=environnement)

## Getting started

This project needs following software:
- [serverless](https://www.serverless.com/) application framework
- [python 3.*](https://www.python.org/downloads/)

It also needs some infrastructure:
- S3 bucket: meteostacklabs: store raw level of project data
- S3 bucket: meteostacklabsglued: store data transformed by glue jobs
- S3 bucket: aws-glue-assets-530505212955-eu-west-1: store Glue assets like transform scripts

An AWS IAM user with Admin rights is also needed to deploy the application with the appropriate credentials for CLI. You can follow this [documentation](https://docs.aws.amazon.com/fr_fr/IAM/latest/UserGuide/id_users_create.html) to setup your account.

The above steps don you can configure your AWS credentials in serverless by running

> serverless config credentials --provider aws --key {KEY}] --secret {secret}

Deployment of a service is done thanks to:

> serverless deploy -c .\serverless.yml

## Architecture

The current architecture is showned in the image below.

[Current Architecture](current_architecture.svg)
<img src="./current_architecture.svg">

The AWS services that are used are:
- S3: store ingested and transformed data, assets and configurations
- lambda: backing serverless application
- glue: to orchestrate data jobs and workflows
- quick sight: serving layer with dashboards
- athena: query development

There are 4 services in the serverless application:
 - create_update_job: create a glue job and associated the transformation logic given a configuration
 - create_update_jobs: create all jobs given a configuration
 - import_data: import data for a given url to an S3 bucket
 - import_all_data: import project data given a configurations


## TODO

1. Replace lambda function logic creation with lambda step functions for handling of more complex workflow
2. Move currently isolated configuration to a more flexible and/or versionable configuration store
3. Handle Glue workflow creation and update throuhg Glue blueprints to automate workflow update
4. Subscribe to enterprise quicksight edition to leverage dashboard exposition through a serverless website
5. Better parametrization of serverless application infrastructure for a deeper devops approach
6. Better error handling and logging for observability purpose
7. Better table storage to avoid multiple small files
8. Create a cloud formation template for project infrastructure