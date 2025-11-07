'''a=str(input("enter a number 1 :"))
b=str(input("enter a number 2 :"))
if(a==b):
    print("a=b")
elif(a>b):
    print("a>b")
elif(a<b):
    print("a<b")
else:
    print("invalid")#if else elif'''


#nested if

m=int(input("mark: "))
if(m>=80):
    print('gread A')
    if(m>90):
        print("with distintion")
    else:
        print("a")
else:
    print("c")
