#tuple
#it uses paranthesis
#allow duplicate and it is unchangeable
#any other function similar to list wont work in tuple

tup1=(1,3,4,3,'a','b')
for x in tup1:
    print(type(x))

#adding two tuple

tup2=(1,23,4,5)
tup3=('a','c','e')
tup=tup2+tup3
print(tup)


tup2=(1,23,4,5)
tup3=('a','c','e')
tup=(tup2,tup3)#prints two tuple inside a tuple
print(tup)


#deleting tup
tup5=(23,45,667,898)
del tup

#assingn value
tup6=(1,23,5,6,7)
a,b,*c=tup6
print(a)
print(b)#*b collects everything in between into a list.
print(c)

#tuple comprehension
b=tuple(y for y in range(1,5))
print(b)

#adding items in tuple using list
tup7=('a','b','c')
y=list(tup7)
y[-1]='d'
tup7=tuple(y)
print(tup7)

#slicing

tup8=(1,3,4,5,6,7,8,7)
print(tup8[3:])
print(tup8[::-1])
print(tup8[3:7])
