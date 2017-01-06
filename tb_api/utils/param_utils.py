from flask import request


def parse_request_param(method_config, field, value):
    field_config = method_config.get_field(field)
    if not field_config:
        return value

    return field_config.parse_value(value)


def parse_request_params(method_config, params):
    for field in params:
        params[field] = parse_request_param(method_config, field, value=params[field])


def load_request_params(ignore_fields):
    params = {}

    # Get parameters from url
    for k in request.args.keys():
        if k in ignore_fields:
            continue
        # print(k)
        params[k] = request.args.get(k)

    # Get parameters from body
    request_json = None
    try:
        request_json = request.get_json()
    except:
        # Invalid json in body
        pass

    if request_json:
        for field in request_json:
            params[field] = request_json[field]

    # Load file
    if request.files:
        for field in request.files:
            params[field] = request.files[field]

    # Load form
    if request.form:
        for field in request.form:
            params[field] = request.form[field]

    return params
