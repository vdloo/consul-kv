from consul_kv.api import DEFAULT_ENDPOINT, put_kv, get_kv, delete_kv


class Connection(object):
    """
    Client for the consul key value store API
    """
    endpoint = DEFAULT_ENDPOINT

    def __init__(self, endpoint=None):
        self.endpoint = endpoint or self.endpoint

    def put(self, k, v):
        return put_kv(k, v, endpoint=self.endpoint)

    def get(self, k, recurse=False):
        return get_kv(k, recurse=recurse, endpoint=self.endpoint)

    def delete(self, k, recurse=False):
        return delete_kv(k, recurse=recurse, endpoint=self.endpoint)
