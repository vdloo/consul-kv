from base64 import b64decode
from json import loads
from os.path import join
from urllib import request
from logging import getLogger

log = getLogger(__name__)

DEFAULT_ENDPOINT = 'http://localhost:8500/v1/kv/'


def put_kv(k, v, endpoint=DEFAULT_ENDPOINT):
    """
    Put a key and value to the distributed key value store at the location path
    :param str k: the key to put
    :param str v: the value to put
    :param str endpoint: api path to PUT to
    :return None:
    """
    encoded = str.encode(str(v))
    url = join(endpoint, k)
    req = request.Request(
        url=url, data=encoded, method='PUT'
    )
    with request.urlopen(req) as f:
        log.debug("PUT k v pair ({}, {}) to {}: {}, {}".format(
            k, v, url, f.status, f.reason
        ))


def get_kv(k, recurse=False, endpoint=DEFAULT_ENDPOINT):
    """
    Get the key value mapping from the distributed key value store
    :param str k: key to get
    :param bool recurse: whether or not to recurse over the path and
    retrieve all nested values
    :param str endpoint: path to get the value from
    :return dict mapping: key value mapping
    """
    url = join(endpoint, k)
    req = request.Request(
        url=join(url, '?recurse') if recurse else url,
        method='GET'
    )
    with request.urlopen(req) as r:
        result = loads(r.read().decode('utf-8'))
    mapping = {
        # values are stored base64 encoded in consul, they
        # are decoded before returned by this function.
        r['Key']: b64decode(r['Value']).decode('utf-8') for r in result
    }
    return mapping


def delete_kv(k, recurse=False, endpoint=DEFAULT_ENDPOINT):
    """
    Delete a key from the distributed key value store
    :param str k: the key to delete
    :param bool recurse: recurse the path and delete all entries
    :param str endpoint: api path to DELETE
    :return:
    """
    url = join(endpoint, k)
    req = request.Request(
        url=join(url, '?recurse') if recurse else url,
        method='DELETE'
    )
    with request.urlopen(req) as f:
        log.debug("DELETEd key {}{}: {} {}".format(
            url,
            ' recursively' if recurse else '',
            f.status,
            f.reason
        ))
