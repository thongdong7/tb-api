class ClientService(object):
    def list(self):
        return []

    def create(self, name):
        return "Created client %s" % name

    def get_by_id(self, client_id):
        return {
            'id': client_id,
            'name': 'Sample client'
        }
