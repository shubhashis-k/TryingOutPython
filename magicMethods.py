__author__ = 'shubhashis'

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def changeName(self, name):
       self.__dict__['name'] = name

   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary


   def __str__(self):
       return self.name + " " + `self.salary`

e = Employee("S", 10000)
e.changeName("Feint")
print e
