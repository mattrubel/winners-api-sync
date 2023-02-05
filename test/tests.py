import os
import sys
import unittest

import util.utils as utils

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ''))
)


class TestUtils(unittest.TestCase):
    def test_build_url_with_api_key(self):
        self.assertEqual(
            utils._build_url_with_api_key(
                "baseurl",
                "parameterstring",
                "apikey"),
            "baseurl?apiKey=apikeyparameterstring")

    def test_get_s3_key(self):
        self.assertEqual(utils.get_s3_key("sports", "2023-02-04-19-48"),
                         "raw-data/sports/2023/02/04/1948/sports.json")
