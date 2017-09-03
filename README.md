[![Build Status](https://travis-ci.org/vdloo/consul-kv.svg?branch=master)](https://travis-ci.org/vdloo/consul-kv)

# consul-kv

Python 3 client for the [consul key/value store](https://www.consul.io/docs/agent/http/kv.html).

## Installation

Get it from [pypi](https://pypi.python.org/pypi/consul_kv/)
```
pip install consul_kv
```

Or install directly from GitHub
```
pip install git+https://github.com/vdloo/consul-kv.git@master#egg=consul_kv
```

Note: this library is rolling release and does not employ semantic versioning. 

Do not depend on the master or update to a new release without checking the changelog, 
there may be breaking changes. If you want to ensure nothing breaks when a new version 
is released, pin your pip requirements like for example `consul_kv==0.7.2`.

## Usage

Instantiate a client
```python
from consul_kv import Connection
conn = Connection(endpoint='http://localhost:8500/v1/')
```

PUT a key
```python
conn.put('the/key', 'the_value')
```

Atomically PUT a list of keys and values ([transaction](https://www.consul.io/docs/agent/http/kv.html#txn)).
```python
mapping = {
    'a/key': 'a_value',
    'another/k': 'another_value'
}
conn.put_mapping(mapping)
```

Atomically PUT a dictionary
```python
dictionary = {
    'a': {
        'key': 'a_value'
    },
    'another': {
        'k': 'another_value'
    }
}
conn.put_dict(dictionary)
```

Atomically PUT a dictionary if the keys don't already exist
```python
dictionary = {
    'a': {
        'key': 'a_value'
    },
    'another': {
        'k': 'another_value'
    }
}
conn.put_dict(dictionary, verb='cas')
```

GET a key
```python
conn.get('the/key')
{'the/key': 'the_value'}
```

GET all keys under a path
```python
conn.get('the', recurse=True)
{'the/key': 'the_value', 'the/other_key': 'the_other_value'}

# or
conn.get_mapping('the')
{'the/key': 'the_value', 'the/other_key': 'the_other_value'}
```

GET a dictionary based on all keys under a path
```python
conn.get_dict('the')
{'the': {'key': 'the_value', 'other_key': 'the_other_value'}}
```

DELETE a key
```python
conn.delete('the/key')
```

DELETE all keys under a path
```python
conn.delete('the', recurse=True)
```

GET information about the agent from the [Agent HTTP API](https://www.consul.io/api/agent.html)
```python
conn.get_meta('agent/self')
```


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
