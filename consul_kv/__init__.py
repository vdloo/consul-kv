from consul_kv.api import DEFAULT_KV_ENDPOINT, put_kv, get_kv, delete_kv, put_kv_txn


class Connection(object):
    """
    Client for the consul key value store API
    """
    kv_endpoint = DEFAULT_KV_ENDPOINT

    @staticmethod
    def _kv_endpoint_to_txn_endpoint(kv_endpoint):
        """
        Rewrite a key/value endpoint to a txn endpoint for atomic updates
        :param str kv_endpoint: endpoint to replace the kv path for with txn
        :return str txn_endpoint: the url with the kv path replaced with txn
        """
        return kv_endpoint.replace('/v1/kv', '/v1/txn')

    def __init__(self, endpoint=None):
        self.kv_endpoint = endpoint or self.kv_endpoint
        self.txn_endpoint = self._kv_endpoint_to_txn_endpoint(
            self.kv_endpoint
        )

    def put(self, k, v):
        """
        Put a key value pair at the configured endpoint
        :param str k: key to put
        :param str v: value to put
        :return None:
        """
        return put_kv(k, v, endpoint=self.kv_endpoint)

    def put_mapping(self, mapping):
        """
        Atomically (Txn) put a key/value mapping at the configured endpoint
        :param dict mapping: dict of key/values put
        :returnNone:
        """
        return put_kv_txn(mapping, endpoint=self.txn_endpoint)

    def get(self, k=None, recurse=False):
        """
        Get a value for a key or all values under that key if recursive is specified
        :param str k: key to get
        :param bool recurse: return nested entries
        :return dict mapping: retrieved key/value mapping
        """
        return get_kv(k=k, recurse=recurse, endpoint=self.kv_endpoint)

    def delete(self, k=None, recurse=False):
        """
        Delete the specified key or all values under that key if recursive is specified
        :param str k: key to delete
        :param bool recurse: delete nested entries
        :return None:
        """
        return delete_kv(k=k, recurse=recurse, endpoint=self.kv_endpoint)
