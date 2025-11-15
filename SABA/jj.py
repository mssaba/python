#position arg
def add(a,b):
    return a+b
print(add(2,3))
#here 2 goes to a and 3 goes to b coz of their position

#default word agr
def nam(name="hi"):
    print('hello',name)
nam()#this prints hello hi
nam('ram')#this prints helo ram


#key word arg
def clg(name,age):
    print("name:",name,"age:",age)
clg(name='ss',age='23')
#here key wrods helps to assin value to parameters

#arbitary arg
#1.(*) position
def addition(*a):
    b=0
    for num in a:
        b +=num
    print(b)
addition(1,2,3)
#*a reads positon of arguments

#2.(**)keyword
def print_i(**k):
    for key,value in k.items():
        print(key,value)
print_i(name='ss',age=25)
#reads through all dictonary items and key words and
#print the key with value

#lambda
a=lambda a,b:a**b
print(a(2,2))

b=lambda x:x*2
print(b(56))

# Mapping (with lambda)
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
#map()>> it apply fun to every item in list
def s(x): # with basic function
    return x**2
num=[1,2,3,4,5]
sq=map(s,num)
print(list(sq))

# filter() is very similar to if else condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

def fil(x):
    return x%2==0
num=12,13,15,14,16
f=filter(fil,num)
print(list(f))
