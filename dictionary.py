import SimPy

__author__ = 'shubhashis'

stuff = {"name": 'Zed', 'age': 39, 'height': 6 * 12 + 2}

list = ["1", "2", "3"]

stuff["list"] = list

print(stuff["name"])
print(stuff['age'])

for i in stuff:
    print(stuff[i])
