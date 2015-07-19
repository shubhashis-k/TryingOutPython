__author__ = 'shubhashis'

__author__ = 'shubhashis'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.gen import Return
import jsonpickle
import motor
from datetime import datetime


from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

@tornado.gen.coroutine
def generate_policy():
    dt = datetime.now()
    policy = {"number" : 1,"text" : "This is a random policy","is_active"	: "1","last_updatetime": dt.isoformat("T") }
    raise Return(policy)


@tornado.gen.coroutine
def insert_policy(policy):
        client = motor.MotorClient('mongodb://localhost:27017')
        db = client.test
        yield db.policies.insert(policy)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        policy = yield generate_policy()
        yield insert_policy(policy)
        self.write("data inserted")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])

    client = motor.MotorClient('mongodb://localhost:27017')
    db = client.test
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
