```yaml
parameters:
  # Optional
  API_ModuleSuffix: Service
  # Optional. Dumper will be used for json.dumps(data, cls=<API_Dumper>) to dumps the result. Could ignore if there is nothing especially in the data.
  API_Dumper: my_package.utils.MyJSONEncoder
  # Optional. Session support. Ignore if you don't want API to return cookie
  API_SecretKey: 'my-secret-key'
  # Optional. Handlers: the service which callable, will receive `app` object and do somethings. Optional
  API_AppHandler:
    - FlaskLogin

  API_Config:
    services:
      User:
        path: user
        methods:
          list: {}
      Product:
        path: product
        methods:
          login: {}
          logout: {}
services:
  UserService: ...
  ProductService: ...
  FlaskLogin: ...
```
