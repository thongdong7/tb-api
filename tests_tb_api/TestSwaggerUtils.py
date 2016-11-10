import unittest

from tb_api.model import APIConfig
from tb_api.utils.swagger_utils import build_swagger


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
                }
            }
        }

        config = APIConfig(data)
        ret = build_swagger(config, 'localhost')
        method_path_config = ret['paths']['/user/login']

        self.assertIn('post', method_path_config)
        self.assertNotIn('get', method_path_config)


if __name__ == '__main__':
    unittest.main()
