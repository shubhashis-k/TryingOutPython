__author__ = 'shubhashis'

import motor
import json
import jsonpickle
import tornado.gen
from tornado.ioloop import IOLoop

@tornado.gen.coroutine
def my_callback():
    cursor = db.policies.find({"is_active" : "1"}, {"is_active":0, "_id":0, "last_updatetime":0}).sort("number",1)

    document = []

    while (yield cursor.fetch_next):
         document.append(cursor.next_object())

    ToJSON = jsonpickle.encode(document, unpicklable=False)

    a = json.loads(ToJSON)

    for i in a:
        print(i)

client = motor.MotorClient('mongodb://localhost:27017')
db = client.test

IOLoop.current().run_sync(my_callback)


#json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
#a = json.loads(json_string)
#print(a,a['first_name'])

from datetime import datetime
dt = datetime.now()
print(dt.isoformat("T"))
