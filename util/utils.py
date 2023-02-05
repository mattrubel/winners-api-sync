import logging

import requests

import util.dynamodb as dynamodb

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def _build_url_with_api_key(
        base_url: str,
        parameter_string: str,
        api_key: str
) -> str:
    """

    :param base_url:
    :param parameter_string:
    :return: string of built url
    """
    api_string = f"?apiKey={api_key}"
    return base_url + api_string + parameter_string


def _write_response_log(dynamodb_table_name: str, **kwargs):
    """
    log response information storage
    :param dynamodb_table_name: table name to write log to
    :param kwargs:
    :return:
    """
    log_dict = kwargs
    dynamodb.write_to_dynamodb(
        log_dict,
        dynamodb_table_name,
    )


def call_get_endpoint(
        base_url: str,
        parameter_string: str,
        call_type: str,
        api_key: str,
        logging_table_name: str,
        run_key: str
) -> str:
    """
    Given a base_url and parameter_string, return json string
    :param base_url: base url for requests
    :param parameter_string: string of parameters
            needed to be appended to the base_url
    :param call_type: type of call sport, event, odds, etc.
    :param api_key: api_key
    :param logging_table_name
    :param run_key: randomly generated id for run
    :return: return string containing response content
    """
    url = _build_url_with_api_key(base_url, parameter_string, api_key)
    response = requests.get(url)

    headers = dict(response.headers)

    status_code = response.status_code

    try:
        _write_response_log(
            logging_table_name,
            log_key=run_key,
            call_type=call_type,
            date=headers.get('Date'),
            status_code=status_code,
            base_url=base_url,
            parameter_string=parameter_string,
            requests_used=headers.get('X-Requests-Used'),
            requests_remaining=headers.get('X-Requests-Remaining')
        )
    except Exception as e:
        logger.warning(f"Unable to successfully write response log {e}")

    if status_code == 200:
        content = response.content.decode("UTF-8")
        return content
    else:
        raise RuntimeError(f"Failure on {call_type} call.")


def get_s3_key(call_type: str, datetime_string: str, run_key: str) -> str:
    """
    Given call_type, get s3 key path with date type incorporated
    :param call_type: type of call
    :param datetime_string: datetime string
    :param run_key: unique run key
    :return: string with s3 key
    """
    datetime_split = datetime_string.split("-")
    date_structure = '/'.join(datetime_split[0:3])
    file_name = ''.join(datetime_split[3:]) + "-" + run_key
    return f"raw-data/{call_type}/{date_structure}/{file_name}.json"
