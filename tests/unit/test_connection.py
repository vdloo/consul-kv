from consul_kv import Connection
from consul_kv.api import DEFAULT_ENDPOINT
from tests.testcase import TestCase


class TestConnection(TestCase):
    def setUp(self):
        self.put_kv = self.set_up_patch('consul_kv.put_kv')
        self.get_kv = self.set_up_patch('consul_kv.get_kv')
        self.delete_kv = self.set_up_patch('consul_kv.delete_kv')
        self.endpoint = 'http://some_host:8500/v1/kv/'
        self.conn = Connection(endpoint=self.endpoint)

    def test_connection_has_correct_endpoint(self):
        self.assertEqual(self.conn.endpoint, self.endpoint)

    def test_connection_uses_default_endpoint_if_none_specified(self):
        conn = Connection()

        self.assertEqual(conn.endpoint, DEFAULT_ENDPOINT)

    def test_connection_put_calls_put_kv_with_endpoint(self):
        self.conn.put('key1', 'value1')

        self.put_kv.assert_called_once_with(
            'key1', 'value1', endpoint=self.endpoint
        )

    def test_connection_get_calls_get_kv_with_endpoint(self):
        self.conn.get('key1')

        self.get_kv.assert_called_once_with(
            k='key1', recurse=False, endpoint=self.endpoint
        )

    def test_connection_get_recurses_if_specified(self):
        self.conn.get('key2', recurse=True)

        self.get_kv.assert_called_once_with(
            k='key2', recurse=True, endpoint=self.endpoint
        )

    def test_connection_delete_calls_delete_kv_with_endpoint(self):
        self.conn.delete('key1')

        self.delete_kv.assert_called_once_with(
            k='key1', recurse=False, endpoint=self.endpoint
        )

    def test_connection_delete_recurses_if_specified(self):
        self.conn.delete('key2', recurse=True)

        self.delete_kv.assert_called_once_with(
            k='key2', recurse=True, endpoint=self.endpoint
        )
