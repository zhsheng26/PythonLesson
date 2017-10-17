# environ：一个包含所有HTTP请求信息的dict对象；
# start_response：一个发送HTTP响应的函数。

# start_response()函数接收两个参数，一个发送HTTP响应的函数是HTTP响应码，
# 一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示。


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    path_info_ = environ['PATH_INFO']
    body = '<h1>Hello, %s!</h1>' % (path_info_[1:] or 'web')
    return [body.encode('utf-8')]
