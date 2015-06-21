__author__ = 'shubhashis'

def function2():
    for i in range(1,100,1):
        print("I am being held")

    return 1

def function1():
    result = yield function2()
    print(result)
    print("blockade released")



a = function1()
print(a)

