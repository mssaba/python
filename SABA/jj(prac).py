def square(n):
    return n%2==0
num=[2,3,4,5]
sq=filter(square,num)
print(list(sq))


def rev(a):
    c=0
    while(a>0):
        b=a%10
        c=c*10+b
        a=a//10
    return c
#print(rev(a=int(input("enter number;"))))

a=[12345,23456,'abas']
reverse=filter(lambda a:type(a)==int,a)
b=map(rev,reverse)
print(list(b))

a=['hello','welcome','good','bad']
def mid(x):
    return x[len(x)//2]
#print(mid())
def middle(y):
    return y[len(y)//2]+y[len(y)//2-1]

odd=list(filter(lambda x:(len(x)%2)!=0,a))
b=list(map(mid,odd))
print(b)

even=list(filter(lambda y:(len(y)%2)==0,a))
c=list(map(middle,even))
print(c)

