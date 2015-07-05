__author__ = 'shubhashis'

class Thing(object):
    def __init__(self, name):
        self.address = "New york"
        self.list = [1,2]
        self.name = name
        self.age = 10

obj = Thing('Awesome')

import jsonpickle
frozen = jsonpickle.encode(obj)
print(frozen)


melted = jsonpickle.decode(frozen)
#print(melted.age) #will work

print(melted.__dict__)

print("attributes")

for i in melted.__dict__:
    print(i,melted.__dict__[i])




print("Unpicklable")
frozen = jsonpickle.encode(obj, unpicklable=False)
print(frozen)

melted1 = jsonpickle.decode(frozen)
print(melted1)

#print(melted1.age) #wont work

