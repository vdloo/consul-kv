### 0.7.2

Breaks compatiblity with previous versions.

The default endpoint is now
```
DEFAULT_ENDPOINT = 'http://localhost:8500/v1/'
```

instead of
```
DEFAULT_KV_ENDPOINT = 'http://localhost:8500/v1/kv/'
```

This makes it more sensible to use conn.get_meta. otherwise you'd have
to manually specify the kv-less default endpoint and pass 'kv/' to all
kv items you'd want to interact with. See [#20](https://github.com/vdloo/consul-kv/pull/20)

The transaction default endpoint is now `http://localhost:8500/v1/txn`. 
Note that there is no trailing slash for this endpoint.

### 0.5

Adds [CAS functionality](https://github.com/vdloo/consul-kv/pull/14). Thanks [jakobdalsgaard](https://github.com/jakobdalsgaard)!

### 0.4

Allow to [recurse nested levels](https://github.com/vdloo/consul-kv/pull/10). Thanks [nadirollo](https://github.com/nadirollo)!

