import datetime
import logging

import boto3
import pytz
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def _build_url_with_api_key(base_url: str, parameter_string: str, api_key: str) -> str:
    """
    Get API key from environment variable
    :param base_url:
    :param parameter_string:
    :return:
    """
    # api_key = os.environ.get("API_KEY")
    # assert api_key is not None, "Missing API_KEY environment variable"

    api_string = f"?apiKey={api_key}"

    return base_url + api_string + parameter_string


def _write_response_log(**kwargs):
    """
    log response information storage
    :param kwargs:
    :return:
    """
    log_dict = kwargs
    print(log_dict)
    # TODO write log_dict


def call_get_endpoint(base_url: str, parameter_string: str, call_type: str, api_key: str) -> str:
    """
    Given a base_url and parameter_string, return json string
    :param base_url: base url for requests
    :param parameter_string: string of parameters needed to be appended to the base_url
    :param call_type: type of call sport, event, odds, etc.
    :param api_key: api_key
    :return: return string containing response content
    """
    url = _build_url_with_api_key(base_url, parameter_string, api_key)
    response = requests.get(url)

    headers = dict(response.headers)

    status_code = response.status_code

    try:
        _write_response_log(
            call_type=call_type,
            date=headers.get('Date'),
            status_code=status_code,
            base_url=base_url,
            parameter_string=parameter_string,
            requests_used=headers.get('X-Requests-Used'),
            requests_remaining=headers.get('X-Requests-Remaining')
        )
    except Exception:
        logger.warning("Unable to successfully write response log")

    if status_code == 200:
        content = response.content.decode("UTF-8")
        return content
    else:
        raise RuntimeError(f"Failure on {call_type} call.")


def export_to_s3(byte_stream, s3_bucket, s3_key, aws_access_key, aws_secret_access_key):
    """

    :param byte_stream:
    :param s3_bucket:
    :param s3_key:
    :param aws_access_key:
    :param aws_secret_access_key
    :return:
    """
    logger.info(f"Writing byte_stream to s3://{s3_bucket}/{s3_key}")
    try:
        session = boto3.Session(
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_access_key,
        )
        s3_client = session.client("s3")
        s3_client.put_object(
            Body=byte_stream,
            Bucket=s3_bucket,
            Key=s3_key
        )
    except Exception as e:
        logger.error(f"Error writing byte stream to s3 {e}")
        raise e


def get_s3_key(call_type: str) -> str:
    """
    Given call_type, get s3 key path with date type incorporated
    :param call_type:
    :return: string with s3 key
    """
    date_split = datetime.datetime.now(tz=pytz.UTC).strftime("%Y-%m-%d-%H-%M").split("-")
    date_structure = '/'.join(date_split[0:3]) + '/' + ''.join(date_split[3:])
    return f"raw-data/{call_type}/{date_structure}/{call_type}.json"
