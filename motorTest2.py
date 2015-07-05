__author__ = 'shubhashis'

import motor

import tornado.gen
from tornado.ioloop import IOLoop

@tornado.gen.coroutine
def my_callback():
    cursor = db.blog.find({"isActive" : "1"}, {"isActive":0})

    while (yield cursor.fetch_next):
         document = cursor.next_object()
         print document

client = motor.MotorClient('mongodb://localhost:27017')
db = client.test

IOLoop.current().run_sync(my_callback)