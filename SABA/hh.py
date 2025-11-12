'''#adding two list
a=[1,2,3]
b=[4,5,6]
for  x in range(len(a)):
    print(a[x]+b[x])

#nested list
a=[[1,2],[2,4]]
b=[[3,5],[6,7]]
for i in range(len(a)):
    for j in range(len(a[i])):
        result=a[i][j]+b[i][j]
        print(result)'''
#multiplication
a=[2,4]
b=[6,8]
for x in range(len(a)):
    for y in range(len(b)-1):
        print(a[x]*b[y]+a[x]*b[y+1])
a=[2,4]
b=[6,8]
for x in range(len(a)):
    print(a[x]*b[0]+a[x]*b[1])


#leap year
a=int(input("ente the year"))
if (a%4==0):
    if(a%100!=0):
        print("leap year")
    else:
        if(a%400==0):
            print("leap year")
        else:
            print("not leap")
else:
    print("not leap year")



    
