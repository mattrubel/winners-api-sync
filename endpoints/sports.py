"""
This module contains the object that interfaces with the sports endpoint
"""
import datetime

import util.utils as utils
from interface.endpoint import Endpoint


class Sports(Endpoint):
    """
    This class will contain the functionality to call the sports endpoint
    """
    def __init__(self, api_key: str, base_url: str, s3_bucket: str, aws_access_key: str, aws_secret_access_key: str):
        super().__init__()
        self.api_key = api_key
        self.base_url = base_url
        self.s3_bucket = s3_bucket
        self.call_type = "sports"
        self.datetime_string = datetime.datetime.now(tz=pytz.UTC).strftime("%Y-%m-%d-%H-%M")
        # self.s3_key = utils.get_s3_key("sports")
        self.aws_access_key = aws_access_key
        self.aws_secret_access_key = aws_secret_access_key

    def call_endpoint(self, **kwargs) -> str:
        """
        Call endpoint to retrieve sports data
        :param kwargs: not used.
        :return: string of payload
        """
        return utils.call_get_endpoint(self.base_url, "", "sports", self.api_key)

    def export_to_s3(self, payload: str):
        """
        convert string to byte array and export to s3
        :param payload: payload string
        :return:
        """
        s3_key = utils.get_s3_key(self.call_type, self.datetime_string)
        byte_stream = bytearray(payload, "UTF-8")
        utils.export_to_s3(byte_stream, self.s3_bucket, s3_key, self.aws_access_key, self.aws_secret_access_key)
