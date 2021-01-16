import json
import boto3
import logging

logger = logging.getLogger("test")


def get_s3_file(bucket=None, Key=None):
    s3 = boto3.client('s3')
    return s3.list_objects(
        Bucket=bucket,
        Prefix=Key,
        Delimiter="/"
    )['Contents']


def handler(event, context):
    logger.info("starting the task")
    data=get_s3_file("Test","Key")
    return {"abc": data}
