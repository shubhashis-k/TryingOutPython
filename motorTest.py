__author__ = 'shubhashis'

import motor

import tornado.gen
from tornado.ioloop import IOLoop

@tornado.gen.coroutine
def my_callback():
    document = {'somekey': 'some value'}
    yield db.blog.insert(
        {
            "policyNumber" 	: 1,
            "policy"	: "policy 1",
            "isActive"	: "1",
            "currdate"	: "new Date()"
        }
    )
    print("Successfully inserted Value")



client = motor.MotorClient('mongodb://localhost:27017')
db = client.test

IOLoop.current().run_sync(my_callback)



