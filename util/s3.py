import logging

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

session = boto3.Session()


def export_to_s3(
        byte_stream: bytes,
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
