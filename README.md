# consul-kv

Python 3 client for the [consul key/value store](https://www.consul.io/docs/agent/http/kv.html).

## Development

Create a virtualenv
```
mkvirtualenv -a $(pwd) -p /usr/bin/python3 consul_kv
echo "PYTHONPATH=`pwd`" >> $VIRTUAL_ENV/bin/postactivate
pip3 install pip --upgrade
pip3 install -r requirements/development.txt
```

Run the tests
```
./runtests.sh -1
```
