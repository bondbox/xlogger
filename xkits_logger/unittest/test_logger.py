# coding:utf-8

import unittest
from unittest import mock

from xkits_logger import logger


class TestOnceFilter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @mock.patch.object(logger, "time")
    def test_timeout(self, mock_time):
        mock_time.side_effect = [1.0, 60.0, 61.0, 62.0]
        filter = logger.OnceFilter()
        self.assertEqual(filter.max_interval_seconds, 60)
        self.assertFalse(filter.timeout)
        self.assertFalse(filter.timeout)
        self.assertTrue(filter.timeout)


class TestLogger(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.logger = logger.Logger()

    def tearDown(self):
        pass

    def test_initiate_logger(self):
        self.logger.initiate_logger(self.logger.get_logger(), "debug")
        self.logger.initiate_logger(self.logger.get_logger(), "info")
        self.logger.get_logger().info("test")
        self.logger.get_logger().info("test")

    @mock.patch.object(logger.os, "makedirs", mock.MagicMock())
    @mock.patch.object(logger.os.path, "isdir", mock.MagicMock(side_effect=[True]))  # noqa:E501
    @mock.patch.object(logger.os.path, "exists", mock.MagicMock(side_effect=[False]))  # noqa:E501
    @mock.patch.object(logger.os.path, "dirname", mock.MagicMock())
    @mock.patch.object(logger.logging, "FileHandler", mock.MagicMock())
    def test_new_file_handler(self):
        logger.Logger.new_file_handler("unittest.log")

    def test_stdout(self):
        logger.Logger.stdout_yellow("warning")
        logger.Logger.stdout_green("ok")
        logger.Logger.stdout_red("fail")

    def test_stderr(self):
        logger.Logger.stderr_yellow("warning")
        logger.Logger.stderr_green("ok")
        logger.Logger.stderr_red("fail")


if __name__ == "__main__":
    unittest.main()
