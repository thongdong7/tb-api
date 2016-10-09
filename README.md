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

API will be available at http://localhost:5000/api/Hello/world?name=Peter and the result will be

```json
{
  "ok": true,
  "message": "Hello World, Peter"
}
```

# Main Features

* No API configuration
* Cross domain support
