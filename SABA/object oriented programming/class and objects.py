#class and object
#format of class
'''class class_name:
    statement'''
#example
class sample:
    x=1
a=sample()#object(instance of class is object)
print(a)
print(a.x)
   
class person:
    def __init__(self,age,name):
        self.name=name
        self.age=age
c=person(12,'ram')
print(c.name)
print(c.age)

class per:
    def __init__(self,age,name):
        self.name=name
        self.age=age

    def __str__(self):
        return f'{self.name},{self.age}'
c=per(12,'ram')
print(c)

# classmethod(instance_method)

class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1
   def showcount(self):
      print (self.empCount)
      
   counter = classmethod(showcount)#KEY WORD FOR CLASS METHOD

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)

e1.showcount()
Employee.counter() 
#IT SHOWS 3 AS IT RUNS 3 TIMES 