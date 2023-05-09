import decimal
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

        final_dict = convert_float_to_decimal_in_structures(write_content)

        table.put_item(Item=final_dict)
    except Exception as e:
        logger.error(f"Error writing content to dynamodb table: {table_name}")
        logger.error(e)
        raise e

    logger.info(f"Successfully wrote content to dynamodb table: {table_name}")


def convert_float_to_decimal_in_structures(structure: [iter, dict]):
    """
    Convert float values in markets structure to Decimal so they can be written
    to ddb
    :param structure: nested list or dict
    :return: same structure with float values converted to decimals
    """
    if isinstance(structure, dict):
        for key, value in structure.items():
            if isinstance(value, dict) or isinstance(value, list):
                convert_float_to_decimal_in_structures(value)
            elif isinstance(value, float):
                structure[key] = decimal.Decimal(str(value))
    elif isinstance(structure, list):
        for idx, value in enumerate(structure):
            if isinstance(value, dict) or isinstance(value, list):
                convert_float_to_decimal_in_structures(value)
            elif isinstance(value, float):
                structure[idx] = decimal.Decimal(str(value))

    return structure
