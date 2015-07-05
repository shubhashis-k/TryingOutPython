__author__ = 'shubhashis'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.gen import Return
from tornado.httpclient import AsyncHTTPClient


def fun2():
    yield "Hello"


from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        response = yield self.do_test()
        self.write(response)

    @tornado.gen.coroutine
    def do_test(self):
        raise Return('test')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()