__author__ = 'shubhashis'

class Thing(object):
    def __init__(self, name):
        self.name = name
        self.age = 10

obj = Thing('Awesome')

import jsonpickle
frozen = jsonpickle.encode(obj)
print(frozen)


melted = jsonpickle.decode(frozen)
print(melted.__dict__)

print("attributes")

for i in melted.__dict__:
    print(i,melted.__dict__[i])


