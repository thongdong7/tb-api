# tb-api
> Simple Flask API

NOTE: This library just in development mode. Not ready for production.

# Install

```
pip install tb-api
```

# Usage

Assume you have class `HelloService` at `my_package/service/Hello.py`

```python
class HelloService(object):
  def world(self, name):
    return {
      'ok': True,
      'message': 'Hello World, %s' % name
    }
```

You could start your API by following command

```
api my_package.service --module-suffix Service --project . --debug
```

or programmatically

```python
start(base_name, module_suffix, project_dir, debug)
```

API will be available at http://localhost:5000/api/Hello/world?name=Peter and the result will be

```json
{
  "ok": true,
  "message": "Hello World, Peter"
}
```

## Command

```
api [--project /path/to/project] [--debug] [--port my_port] <loader> [loader arguments]
```

`loader` could be `simple` or `ioc`

Run `api loader --help` for more info

# Main Features

* No API configuration
* Cross domain support
* Support python 2.7, 2.4, 3.5, pypy

# TODO

* Add example
* Add unit test for example
* Support load service via service loader (IOC or custom service loader)
* Support REST. Follow standard at https://github.com/refinery29/api-standards
* Support version
