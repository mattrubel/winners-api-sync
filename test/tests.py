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
            "baseurl?apiKey=apikeyparameterstring",
            utils._build_url_with_api_key(
                "baseurl",
                "parameterstring",
                "apikey"))

    def test_get_s3_key(self):
        self.assertEqual(
            "raw-data/sports/2023/02/04/"
            "1948-4a412f0e-a9dc-4baa-8616-cb76c4829806.json",
            utils.get_s3_key(
                "sports",
                "2023-02-04-19-48",
                "4a412f0e-a9dc-4baa-8616-cb76c4829806"
            )
        )
