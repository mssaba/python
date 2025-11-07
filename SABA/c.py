'''a=str(input("write a sentance:"))
print(a[:7].title()+a[7:14]+a[-1].capitalize())'''
'''
a=str(input("enter the input:"))
print(a[0].upper()+a[1:len(a)//2]+a[len(a)//2].upper()+a[(len(a)//2+1):-1]+a[-1].upper())


a=str(input("enter the input:"))
c=a[0].upper()
d=a[1:(len(a)//2)]
e=a[len(a)//2].upper()
f=a[(len(a)//2+1):-1]
g=a[-1].upper()
print(c+d+e+f+g)'''

'''a=str(input("Enter the input :"))
b=(a[0:len(a)//2])
c=(a[(len(a)//2):])
print(c+b)'''


'''s = "Hello "
print(s * 3)


s = "My name is {} and I am {} years old.".format("Alice", 22)
print(s)

s = "Hell\bo "
print(s)

txt = "Hello \bWorld!"
print(txt) 

print("Hello\rWorld")'''

'''a='hi'
print(a.center(7))


s= " welcome to mayiladuthurai"
a= " today is a good day"
print('a'.join(s))'''

'''words = ['Hello', 'World!']
print(" ".join(words))'''
'''
a=hi note
gysgxd
husq
print(a.splitlines())'''

#a=str(input("Enter the input:"))
#a=a.capitalize()
#a=a[len(a)//2].capitalize()
#print(a)

a="hello"
print(a.replace(a[-1],"i"))

a=str(input("Enter the input:"))
a=a.capitalize()
a=a.replace(a[-1],a[-1].upper())
a=a.replace(a[len(a)//2],a[len(a)//2].upper())
print(a)        



