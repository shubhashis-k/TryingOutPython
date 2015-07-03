__author__ = 'shubhashis'

import motor

import tornado.gen
from tornado.ioloop import IOLoop

@tornado.gen.coroutine
def my_callback():
    someValue = yield db.blog.find_one()
    print(someValue['somekey'])

client = motor.MotorClient('mongodb://localhost:27017')
db = client.test

IOLoop.current().run_sync(my_callback)