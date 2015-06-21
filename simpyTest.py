__author__ = 'softenglab'

from SimPy.Simulation import *
#from Simpy.SimPlot import *
from random import expovariate,seed

class Source(Process):
    def generate(self,number,counters):
        for i in range(number):
            nameOfCustomer = "Customer%d"%i
            c = Customer(name = nameOfCustomer)
            activate(c,c.visit(counters))
            yield hold,self,2

def NoInSystem(R):
    """ Total number of customers in the resource R"""
    return (len(R.waitQ)+len(R.activeQ))

class Customer(Process):
     def visit(self,counters):
        arrive = now()
        Qlength = [NoInSystem(counters[i]) for i in range(Nc)]
        #print "%7.4f %s: Here I am. %s"%(now(),self.name,Qlength)
        for i in range(Nc):
            if Qlength[i] == 0 or Qlength[i] == min(Qlength):
                choice = i  # the chosen queue number
                break

        yield request,self,counters[choice]
        wait = now()-arrive
        w.observe(wait)
        #print(self.name,"Waited",wait)
        yield hold,self,5
        #print(now(),"I'm Leaving")
        yield release,self,counters[choice]



Nc = 2

initialize()
s = Source()
w = Monitor()
kk = [Resource(name="Clerk0",monitored=True),Resource(name="Clerk1",monitored=True)]
activate(s,s.generate(number=10,counters=kk),at=0)
simulate(until=100)
a = kk[0].waitMon
b = kk[1].waitMon





print(a)
print(b)

def calcWait(list):
    a = list
    waitList = []
    for i in range (0,3):
        waitList.insert(i,0)

    for i in range(0,len(a) - 1,1):
        #c = a[i]
        #print(c[0], c[1])
        c1 = a[i+1]
        c0 = a[i]

        noOfWaiting = c0[1]
        waitList[noOfWaiting] += c1[0] - c0[0]

    sum = 0
    expected = 0
    for i in waitList:
        sum += i

    print(waitList)
    print(sum)

    j = 0

    for i in waitList:
        expected += j * (1.0*i)/sum
        j = j+1

    print(" %s" % expected)

print("For A")
calcWait(a)
print("For B")
calcWait(b)