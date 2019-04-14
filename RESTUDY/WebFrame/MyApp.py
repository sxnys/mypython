from wsgiref.simple_server import make_server
from pprint import pprint

def myapp(environ, start_response):
    pprint(environ)
    print(environ['QUERY_STRING'])

    status = '200 OK'
    headers = [
        ('Content-Type', 'text/html; charset=utf8')
    ]
    start_response(status, headers)

    return [b'<h1>Hello Python!</h1>']


if __name__ == '__main__':

    httpd = make_server('127.0.0.1', 8888, myapp)
    httpd.serve_forever()

        