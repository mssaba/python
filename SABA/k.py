def fact(n):#factorial
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
#n=int(input("enter the number:"))
#print(fact(n))

def fibo(n):#fibonacci
    if(n<2):
        return n
    else:
        return fibo(n-1)+fibo(n-2)
#n= int (input("enter the number"))
#print(fibo(n))

n=[6,5,4,3,2,1]
f=list(map(fact,n))
print('factorial =',f)

n=[10,3,4,5]
fi=list(map(fibo,n))
print('fibo=',fi)

