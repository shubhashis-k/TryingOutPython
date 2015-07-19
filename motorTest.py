__author__ = 'shubhashis'

import motor
from datetime import datetime
import tornado.gen
from tornado.ioloop import IOLoop

def run(method):
    return tornado.ioloop.IOLoop.instance().run_sync(lambda: method)

def my_callback():
        db_name = 'test'
        connection_string = 'mongodb://localhost:27017'
        client = motor.MotorClient(connection_string)

        run(client[db_name].policies.insert(
        {
            "number" 	: 5,
            "text"      : "This is a random policy",
            "is_active"	: "1",
            "last_updatetime": "some time"
        }
        ))


my_callback()
