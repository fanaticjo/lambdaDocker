import unittest
from unittest import mock

from ETL.app import handler


class S3Test(unittest.TestCase):
    def test_check(self):
        with mock.patch("ETL.app.get_s3_file",return_value="a.txt"):
            data = handler(1, 2)
            print(data)
            assert data["abc"] == "a.txt"
