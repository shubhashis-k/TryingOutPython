__author__ = 'shubhashis'

import motor
import jsonpickle
import tornado.gen
from tornado.ioloop import IOLoop

@tornado.gen.coroutine
def my_callback():
    cursor = db.policies.find({"isActive" : "1"}, {"isActive":0, "_id":0, "LastUpdateTime":0}).sort("policyNumber",1)

    document = []

    while (yield cursor.fetch_next):
         document.append(cursor.next_object())

    ToJSON = jsonpickle.encode(document, unpicklable=False)

    print ToJSON

client = motor.MotorClient('mongodb://localhost:27017')
db = client.test

IOLoop.current().run_sync(my_callback)