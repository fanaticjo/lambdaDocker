import json
import re
from pprint import pprint

import boto3
import logging
from botocore.errorfactory import ClientError

logger = logging.getLogger("test")

s3 = boto3.client('s3')


def get_s3_file(bucket=None, Key=None):
    try:
        paginator = s3.get_paginator('list_objects_v2')
        response_iterator = paginator.paginate(
            Bucket=bucket,
            Delimiter='/',
            Prefix=Key
        )
        for x in response_iterator:
            for y in x['Contents']:
                if y['Key'].endswith('.json'):
                    yield y['Key']
    except ClientError as e:
        error=e.response.get('Error',None)
        if error is None:
            logger.warning('Non identifiable botocore error raising the exception')
            raise e
        elif error.get('Code').lower()=='nosuchbucket':
            logger.error("Bucket does not exist")
            return None
        else:
            logger.error("Error not identified",e.response)
            raise e
    except Exception as e:
        logger.error("Generic Exception occured",e)
        raise e


def handler(event, context):
    Bucket = "iap-ec2-demo1"
    Key = "Weather/Currently/"
    logger.info("starting the task")
    data = get_s3_file(Bucket, Key)
    for x in data:
        logger.info(x)
    logger.info(data)
    return {"abc": data}


if __name__ == "__main__":
    handler(1, 2)
