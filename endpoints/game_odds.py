"""
This module contains the object that interfaces with the odds endpoint
"""
import datetime
import uuid

import pytz

import util.s3 as s3
import util.utils as utils
from interface.endpoint import Endpoint


class GameOdds(Endpoint):

    def __init__(
            self,
            api_key: str,
            base_url: str,
            logging_table_name: str,
            s3_bucket: str,
            games_table_name: str,
            odds_table_name: str,
            sport: str
    ):
        super().__init__()
        self.run_key = str(uuid.uuid4())
        self.api_key = api_key
        self.base_url = base_url + sport + "/odds/"
        self.logging_table_name = logging_table_name
        self.s3_bucket = s3_bucket
        self.call_type = "game-odds"
        self.datetime_string = datetime.datetime.now(tz=pytz.UTC)\
            .strftime("%Y-%m-%d-%H-%M")
        self.games_table_name = games_table_name
        self.odds_table_name = odds_table_name
        self.sport = sport

    def call_endpoint(self, **kwargs) -> str:
        """
        Call endpoint to retrieve sports data
        :param kwargs: not used.
        :param sport: sport_key
        :return: string of payload
        """
        return utils.call_get_endpoint(
            self.base_url,
            "&regions=us&markets=h2h,spreads,totals",
            "game-odds",
            self.api_key,
            self.logging_table_name,
            self.run_key
        )

    def export_to_s3(self, payload: str):
        """
        convert string to byte array and export to s3
        :param payload: payload string
        :return:
        """
        s3_key = utils.get_s3_key(
            self.call_type + "/" + self.sport,
            self.datetime_string,
            self.run_key
        )
        byte_stream = bytearray(payload, "UTF-8")
        s3.export_to_s3(
            byte_stream,
            self.s3_bucket,
            s3_key
        )

    def write_to_dynamo(self, payload):
        """
        Write odds endpoint data to relevant dynamodb tables
        :param payload: string representation of dict returned from API call
        :return:
        """
        pass
