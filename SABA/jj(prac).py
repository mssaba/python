def info(name,age):
    if(age>18):
        return "elligible"
    else:
        return "not elligible"
name=input("enter name:")
age=int(input("enter age:"))
print(info(name,age))


def grp(a):
    if(a==1):
        u=int(input("enter ur chemistry mark:"))
        m=int(input("enter ur math mark:"))
        p=int(input("enter ur physics mark:"))
        c=int(input("enter ur computer mark:"))
        if(u>30 and m>30 and p>30 and c>30):
            r=(u+m+p+c)/4
            print("average=",r)
    elif(a==2):
        t=int(input("enter ur chemistry mark:"))
        q=int(input("enter ur biology mark:"))
        x=int(input("enter ur physics mark:"))
        y=int(input("enter ur maths mark:"))
        if(t>30 and q>30 and x>30 and y>30):
            w=(t+q+x+y)/4
            print("average",w)

a='''available grp
     1.computer science
     2.biology'''
print(a)
a=int(input('select the grp'))
print(grp(a))

def choice(w):
     if(90<w<100):
            choice='''elligilbe for all course
                  1.MBBS
                  2.BDS
                  3.BPT
                  4.PSYCHOLOGY'''
            print(choice)
    


