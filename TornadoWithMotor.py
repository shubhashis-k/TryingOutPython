__author__ = 'shubhashis'

__author__ = 'shubhashis'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.gen import Return
import jsonpickle
import motor

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        response = yield self.fetch_policies()
        self.write(response)

    @tornado.gen.coroutine
    def fetch_policies(self):
        cursor = db.policies.find({"isActive" : "1"}, {"isActive":0, "_id":0, "LastUpdateTime":0}).sort("policyNumber",1)
        policies = []
        while (yield cursor.fetch_next):
             policies.append(cursor.next_object())

        PolicyToJSON = jsonpickle.encode(policies, unpicklable=False)

        raise Return(PolicyToJSON)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])

    client = motor.MotorClient('mongodb://localhost:27017')
    db = client.test
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
