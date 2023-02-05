import logging
import os

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)


AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


def write_to_dynamodb(
        write_content: dict,
        table_name: str
):
    """
    write a single line to dynamodb table
    :param write_content:
    :param table_name:
    :return:
    """
    logger.info(f"Writing content to dynamodb table: {table_name}")
    try:
        ddb_resource = session.resource("dynamodb")
        table = ddb_resource.Table(table_name)
        table.put_item(Item=write_content)
    except Exception as e:
        logger.error(f"Error writing content to dynamodb table: {table_name}")
        logger.error(e)
        raise e

    logger.info(f"Successfully wrote content to dynamodb table: {table_name}")
