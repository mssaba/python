name=input("enter the name :")
age=input("enter the age")
e=input("enter your qualification :")
a="engineering"
b="arts and science"
if(e==a):
    f=input("enter ur field in engineering:")
    s=input("enter ur spl skill")
    p="python"
    m="full stack"
    d="app development"
    if(s==p):
        vaccancy='''available vaccancy are
                  1.software developer
                  2.sysytem maintenance
                  3.data analyst'''
        print(vaccancy)
    elif(s==m):
        vaccancy='''available vaccancy are
                  1.developer
                  2.sn.developer
                  3.jn.developer'''
        print(vaccancy)
    elif(s==d):
        vaccancy='''available vaccancy are
                  1.app developer
                  2.app maintenanace
                  3.jn.developer'''
        print(vaccancy)
elif(e==b):
    f=input("enter ur field :")
    s=input("enter ur spl skill")
    p="human resource"
    m="business development"
    d="administration"
    if(s==p):
        vaccancy='''available vaccancy are
                  1.hr role
                  2.sn.hr role in buisness
                  3.jn.hr role'''
        print(vaccancy)
    elif(s==m):
        vaccancy='''available vaccancy are
                  1.general maneger
                  2.assitan executive
                  3.junior administrator'''
        print(vaccancy)
    elif(s==d):
        vaccancy='''available vaccancy are
                  1.supervisor
                  2.deputy ceo
                  3.managing director'''
    


