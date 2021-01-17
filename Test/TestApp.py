import unittest
from unittest import mock

import botocore
from botocore.errorfactory import ClientError
from ETL.app import handler


class S3Test(unittest.TestCase):
    def test_check(self):
        with mock.patch("ETL.app.get_s3_file", side_effect=["a.txt"]):
            data = handler(1, 2)
            print(data)
            assert data["abc"] == "a.txt"


