import logging
import os

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


def export_to_s3(
        byte_stream: bytearray,
        s3_bucket: str,
        s3_key: str
):
    """

    :param byte_stream:
    :param s3_bucket:
    :param s3_key:
    :return:
    """
    logger.info(f"Writing byte_stream to s3://{s3_bucket}/{s3_key}")
    try:
        s3_client = session.client("s3")
        s3_client.put_object(
            Body=byte_stream,
            Bucket=s3_bucket,
            Key=s3_key
        )
    except Exception as e:
        logger.error(f"Error writing byte stream to s3 {e}")
        raise e
