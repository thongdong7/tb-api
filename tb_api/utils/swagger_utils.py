from six.moves.urllib.parse import urlparse

from flask import request


def _build_method_paths(method_config):
    ret = {}

    for method in method_config.http_methods:
        parameters = []
        for field in method_config.fields:
            parameter = {
                'name': field.name,
                'in': 'query',
                'description': field.description,
                'required': field.required,
            }

            if field.type == 'boolean':
                parameter['type'] = 'string'
                parameter["enum"] = ["true", "false"]

            parameters.append(parameter)

        ret[method] = {
            "summary": "",
            "description": "",
            "parameters": parameters,
            # 'produces': [
            #     "text/html",
            #     "application/json",
            # ],
            'tags': method_config.tags,
            'responses': {
                200: {
                    'description': "successful operation",
                },
                400: {
                    'description': "Invalid status value"
                },
                500: {
                    'description': 'Server error'
                },
            },
        }

    return ret


def _build_paths(config):
    ret = {}

    for module_path in config.path_map:
        module_config = config.path_map[module_path]
        for method_path in module_config:
            method_config = module_config[method_path]
            ret['/%s/%s' % (module_path, method_path)] = _build_method_paths(method_config)

    return ret


def flask_build_swagger(config):
    o = urlparse(request.url_root)
    print(o)

    return build_swagger(config, o.netloc)


def build_swagger(config, host):
    paths = _build_paths(config)

    return {
        "swagger": "2.0",
        "info": {
            "description": "",
            "version": "1.0.0",
            "title": "Swagger Petstore",
            "termsOfService": "",
            "contact": {
                "email": ""
            },
            "license": {
                "name": "",
                "url": ""
            }
        },
        "host": host,
        "basePath": "/api",
        "schemes": [
            "http"
        ],
        "paths": paths
    }
