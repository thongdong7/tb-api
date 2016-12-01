import unittest
from pprint import pprint

from tb_api.model.config import APIConfig
from tb_api.utils.swagger_utils import build_swagger


def gen_swagger(data):
    config = APIConfig(data)
    return build_swagger(config, 'localhost')


class SwaggerUtilsTestCase(unittest.TestCase):
    def test_01(self):
        data = {
            "services": {
                "User": {
                    "path": "user",
                    "tags": ["User", "User1"],
                    "methods": {
                        "login": {
                            "method": ['post'],
                            "fields": [
                                {
                                    "name": "username",
                                },
                                {
                                    "name": "password",
                                },
                                {
                                    "name": "remember_me",
                                    "type": "boolean"
                                },
                            ]
                        }
                    }
                },
                "Client": {
                    "path": "clients",
                    "methods": {

                    }
                }
            }
        }

        ret = gen_swagger(data)
        method_path_config = ret['paths']['/user/login']

        self.assertIn('post', method_path_config)
        self.assertNotIn('get', method_path_config)

    def test_restful(self):
        data = {
            "paths": {
                "clients": {
                    "tags": ['Client'],
                    "get": {
                        "method": "$ClientService.list",
                        "summary": "List clients"
                    },
                    "post": {
                        "method": "$ClientService.create",
                        "summary": "Create client",
                        "fields": [{
                            "name": "body",
                            "in": "body",
                            "schema": "Client"
                        }]
                    }
                }
            },
            "definitions": {
                "Client": {
                    "type": "object"
                }
            }
        }

        ret = gen_swagger(data)
        paths = ret['paths']

        # pprint(paths)

        self.assertIn('/clients', paths)
        paths_clients = paths['/clients']

        self.assertIn('get', paths_clients)
        self.assertIn('post', paths_clients)

        # Validate tags
        paths_clients_get = paths_clients['get']
        self.assertEqual(['Client'], paths_clients_get['tags'])

        # Validate schema
        paths_clients_post = paths_clients['post']
        self.assertEqual({"$ref": "#/definitions/Client"}, paths_clients_post['parameters'][0]['schema'])

        # Validate definitions
        self.assertIn('definitions', ret)
        self.assertIn('Client', ret['definitions'])
        # pprint(ret)

if __name__ == '__main__':
    unittest.main()
