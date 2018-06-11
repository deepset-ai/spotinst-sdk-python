import unittest

from spotinst_sdk import SpotinstClient
from spotinst_sdk.aws_elastigroup import *


class SpotinstClientTestCase(unittest.TestCase):

    def setUp(self):
        self.client = SpotinstClient(auth_token='dummy-token', account_id='act-1234567')


# region Internal Methods
class SpotinstClientExcludeMissingTest(SpotinstClientTestCase):
    def runTest(self):
        dummy_obj = {"valid_key": "valid_value", "null_key": None, "ignored_key": none}
        expected_obj = {"valid_key": "valid_value", "null_key": None}
        actual_obj = self.client.exclude_missing(dummy_obj)
        self.assertDictEqual(actual_obj, expected_obj)
# endregion
