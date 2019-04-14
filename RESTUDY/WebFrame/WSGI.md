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



----



### 大致流程及相关源码

#### 1、初始化服务器对象 `httpd = make_server(IP, PORT, app)`

调用的是 `simply_server` 模块中的 `make_server` 方法

```python
def make_server(
    host, port, app, server_class=WSGIServer, handler_class=WSGIRequestHandler
):
    """Create a new WSGI server listening on `host` and `port` for `app`"""
    server = server_class((host, port), handler_class)
    server.set_app(app)
    return server
```

改方法会初始化一个 `WSGIServer` 服务器对象（继承关系 `WSGIServer -> HTTPServer -> socketserver.TCPServer -> BaseServer` ），设置该服务器对象的 `application` 为传入的自定义 `app`，请求管理类 `RequestHandlerClass` 为默认的`WSGIRequestHandler`:

```python
# simple_server.py
# in WSGIServer class
def get_app(self):
    return self.application

def set_app(self,application):
    self.application = application
```

```python
# socketserver.py
# in BaseServer class
def __init__(self, server_address, RequestHandlerClass):
    """Constructor.  May be extended, do not override."""
    self.server_address = server_address
    self.RequestHandlerClass = RequestHandlerClass
    self.__is_shut_down = threading.Event()
    self.__shutdown_request = False
```

#### 2、服务启动 `httpd.serve_forever()`

`serve_forever()` 方法是调用的基类 `BaseServer` 的方法，方法中有一个处理请求的方法 `self._handle_request_noblock()`，该方法中 `self.process_request(request, client_address)`，该方法中有 `self.finish_request(request, client_address)`：

```python
# socketserver.py
# in BaseServer class
def finish_request(self, request, client_address):
    """Finish one request by instantiating RequestHandlerClass."""
    self.RequestHandlerClass(request, client_address, self)
```

其中 `RequestHandlerClass` 是初始化为了 `WSGIRequestHandler`

#### 3、处理 HTTP 请求

```python
# simple_server.py
# in WSGIRequestHandler class
def handle(self):
    ...
   	handler = ServerHandler(
        self.rfile, self.wfile, self.get_stderr(), self.get_environ()
    )
    handler.request_handler = self      # backpointer for logging
    handler.run(self.server.get_app())
```

`run()` 方法是调用的基类 `BaseHandler` 的`run()` 方法：

`self.result = application(self.environ, self.start_response)`

`start_response` 方法：

```python
# handlers.py
# in BaseHandler class
def start_response(self, status, headers,exc_info=None):
    """'start_response()' callable as specified by PEP 3333"""

    if exc_info:
        try:
            if self.headers_sent:
                # Re-raise original exception if headers sent
                raise exc_info[0](exc_info[1]).with_traceback(exc_info[2])
        finally:
            exc_info = None        # avoid dangling circular ref
    elif self.headers is not None:
        raise AssertionError("Headers already set!")

    self.status = status
    self.headers = self.headers_class(headers)
    status = self._convert_string_type(status, "Status")
    assert len(status)>=4,"Status must be at least 4 characters"
    assert status[:3].isdigit(), "Status message must begin w/3-digit code"
    assert status[3]==" ", "Status message must have a space after code"

    if __debug__:
        for name, val in headers:
            name = self._convert_string_type(name, "Header name")
            val = self._convert_string_type(val, "Header value")
            assert not is_hop_by_hop(name),"Hop-by-hop headers not allowed"

    return self.write
```

