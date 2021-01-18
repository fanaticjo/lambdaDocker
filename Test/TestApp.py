import unittest
from unittest import mock

import botocore
from botocore.errorfactory import ClientError
from ETL.app import handler


class S3Test(unittest.TestCase):
    def setUp(self):
        """set up"""
        self.patcher=mock.patch("ETL.app.get_s3_file",return_value=["b.txt"])
        self.patcher.start()

    @property
    def file_s3_gen(self):
        yield ["a.txt"]

    def test_check(self):
        """Using context manager to start mock"""
        with mock.patch("ETL.app.get_s3_file", side_effect=self.file_s3_gen):
            data = handler(1, 2)
            print(data)
            assert data["abc"][0] == "a.txt"

    @mock.patch("ETL.app.get_s3_file",return_value=["c.txt"])
    def test_decorator_check(self,mock_patch):
        """use decorator start mock"""
        data=handler(1,2)
        print(data)
        assert data["abc"][0] == "c.txt"

    def test_check_class_mocker(self):
        """Use class pathcer"""
        data = handler(1, 2)
        print(data)
        assert data["abc"][0] == "b.txt"

    def tearDown(self):
        """tear down"""
        self.patcher.stop()