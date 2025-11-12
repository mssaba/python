'''def name():
    print("saba")
name()

def name():
    return "saba"
print(name())

#x=int(input("x="))
def square(x):
    return x**2
print(square(int(input("x="))))'''

'''def square(x):
    a=x**2
    return a
square(int(input("x=")))

y=square(2)+2

print(y)'''

'''def myFun(x, y=10): # Default Arguments
    print("x: ", x)
    print("y: ", y)

myFun(10)'''
def student(fname, lname):
    print(fname, lname)

student(fname='Python', lname='Practice') # Keyword Arguments
student(lname='Practice', fname='Geeks')

def nameAge(name, age): # Positional Arguments
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)
