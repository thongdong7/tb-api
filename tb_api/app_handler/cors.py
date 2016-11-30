from flask_cors import CORS


class FlaskCORS(object):
    def __init__(self, resources):
        self.resources = resources

    def __call__(self, app):
        CORS(app, resources=self.resources)
