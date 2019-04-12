## WSGI

WSGI 是 Python Web 服务器和 Python Web 框架之间的协议约定。

满足下面接口规范的 web app 就可运行在任一 Python Web 服务器之上

```python
def app(environ, start_response):
    '''
    environ 为 web 框架的环境参数
    start_response 为回调函数，接收响应状态和响应头两个参数
    返回响应消息主体
    一般框架都是满足可调用性（__call__）的 class，但是都必须满足 WSGI 接口规范
    '''
    status = '200 OK'
    headers = [
        ('Content-Type': 'text/html; charset=utf8'),
        ('Connection': 'keep-alive')
    ]
    start_response(status, headers)
    
    response_body = '<h1>Hello, Python!</h1>'
    return response_body
```

将框架运行在 web 服务器上，以 uWSGI 为例

```python
from wsgiref.simple_server import make_server

httpd = make_server(IP, PORT, app)
httpd.serve_forever()
```

