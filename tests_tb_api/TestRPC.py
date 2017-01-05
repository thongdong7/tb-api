# encoding=utf-8
import logging
import unittest
import os
import flaskr
import unittest
import tempfile

__author__ = 'hiepsimu'

logging.basicConfig(level=logging.DEBUG)


class RPCTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        with flaskr.app.app_context():
            flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def test_01(self):
        pass


if __name__ == '__main__':
    unittest.main()
