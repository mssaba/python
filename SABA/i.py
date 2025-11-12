'''a=input("enter the input:")
b=""
for x in a:
    if(x.isupper()):
        b+= x.lower()
        
    else:
        b+= x.upper()
print(b)'''



a=input("enter input")
b=["a","e","i","o","u"]
c=0
for x in a:
    if x in b:
        c=c+1
print(c)
