# Polymorphism
# multiple classes with the same method name.

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")     

for x in (car1, boat1, plane1):
  x.move()

class ram:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def age():
     print('45')

class raj:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def age():
    print('55')

class ravi:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def age():
    print('65')

for x in (ram,raj,ravi):
  x.age()