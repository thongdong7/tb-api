# encoding=utf-8
import json
import logging
import unittest
import os
import unittest
import tempfile

from os.path import abspath, dirname, join

from tb_api.loader.ioc import LoaderIOC
from tb_api.model.config import Config
from tb_api.script import get_app

__author__ = 'hiepsimu'

logging.basicConfig(level=logging.DEBUG)


test_dir = abspath(dirname(__file__))
test_data_dir = join(test_dir, 'data')


class RPCTestCase(unittest.TestCase):
    def setUp(self):
        project_dir = join(test_data_dir, 't1')
        debug = True
        port = 32999
        config = Config(project_dir, debug, port)
        final_config_files = [join(project_dir, 'services.yml')]
        module_suffix = ''
        config.loader = LoaderIOC(final_config_files, module_suffix)

        app = get_app(config)
        app.config['TESTING'] = True
        self.app = app.test_client()

    # def tearDown(self):
    #     os.close(self.db_fd)
    #     os.unlink(flaskr.app.config['DATABASE'])

    def responseOk(self, response):
        self.assertEqual(200, response.status_code)

    def responseNotFound(self, response):
        self.assertEqual(404, response.status_code)

    def test_could_load_swagger(self):
        ret = self.app.get('/api/v1/swagger.json')
        self.responseOk(ret)

    def test_could_call_rpc(self):
        ret = self.app.get('/rpc/v1/TextService/upper?text=hello')
        # print(ret.data)
        self.responseOk(ret)
        assert b'HELLO' in ret.data

    def test_exception_when_call_invalid_rpc_params(self):
        response = self.app.get('/rpc/v1/TextService/upper?text1=hello')
        self.responseNotFound(response)

        ret = json.loads(response.data.decode('utf-8'))
        self.assertFalse(ret['ok'])
        self.assertEqual("upper() got an unexpected keyword argument 'text1'", ret['message'])

    def test_exception_when_call_invalid_rpc_method(self):
        response = self.app.get('/rpc/v1/TextService/invalid_method?text=hello')
        self.responseNotFound(response)

        ret = json.loads(response.data.decode('utf-8'))
        self.assertFalse(ret['ok'])
        self.assertIn("API 'TextService' does not have method 'invalid_method'", ret['message'])

    def test_exception_when_call_invalid_rpc_service(self):
        response = self.app.get('/rpc/v1/InvalidService/invalid_method?text=hello')
        self.responseNotFound(response)

        ret = json.loads(response.data.decode('utf-8'))
        self.assertFalse(ret['ok'])
        self.assertIn("Invalid API 'InvalidService'", ret['message'])

    def test_exception_inside_rpc_method(self):
        response = self.app.get('/rpc/v1/TextService/method_exception')
        # print(response.data)
        self.responseNotFound(response)

        ret = json.loads(response.data.decode('utf-8'))
        self.assertFalse(ret['ok'])
        self.assertIn("Error inside method: Exception in-side method", ret['message'])


if __name__ == '__main__':
    unittest.main()
