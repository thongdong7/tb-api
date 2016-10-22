# encoding=utf-8

from flask import Flask
from flask import Response
from flask import json
from flask import request

from tb_api.exception import APIError, format_html
from tb_api.crossdomain import crossdomain
from tb_api.module_manager import ModuleManager

format_field = '_format'
ignore_fields = set([format_field])


def load_app(base_name, module_suffix='Service', static_folder='static', static_index_file=None):
    app = Flask(__name__, static_folder=static_folder)

    module_manager = ModuleManager(base_name, module_suffix=module_suffix)

    @app.route("/")
    def index():
        if static_index_file:
            return open(static_index_file).read()

        return "Hello World!"

    @app.route("/api/<module_name>/<method_name>")
    @crossdomain(origin='*')
    def api_call(module_name, method_name):
        # print(request.args)

        try:
            method = module_manager.get_method(module_name, method_name)
            # print(method)

            params = {}
            for k in request.args.keys():
                if k in ignore_fields:
                    continue
                # print(k)
                params[k] = request.args.get(k)

        # print(params)

            data = method(**params)
            try:
                content = json.dumps(data)
            except:
                raise
            return Response(content,
                            mimetype="application/json")
        except APIError as e:
            error_message = str(e)
            mimetype = None

            # return request.args.get(format_field)
            if request.args.get(format_field) == 'html':
                content = format_html(error_message)
                mimetype = 'text/html'
            else:
                content = json.dumps({
                    'ok': False,
                    'message': error_message
                })
                mimetype = 'application/json'

            return Response(content, status=404,
                            mimetype=mimetype)

    return app
