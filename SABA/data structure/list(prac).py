'''a=[1,2,3,4,5,6]
b=['a','b','c','d']

for x in b:
    if 'e' in b:
        a.append(x)

print(a)
#insert
b.insert(2,'a')
print(b)

b.pop()
print(b)'''
'''
a=str(input("enter the input: "))
b=['a','e','i','o','u']

c=''
for x in a:
    if x not in b:
        c=c+x

print(c)
    

a=[1,3,4,6,8,9,64,2]
a.sort()
print(a[1],',',a[-2])'''

b=[1,'a',1.3,'c',12+0j,[1,2,3,4,],(4,56,7,9),{1,3,5,6,7}]

for x in b:
    if type(x)== int:
        print(x,'=','int')
    elif type(x)== str:
        print(x,'=','str')
    elif type(x)== float:
        print(x,'=','float')
    elif type(x)== complex:
        print(x,'=','complex')
    elif type(x)== list:
        print(x,'=','list')
    elif type(x)== set:
        print(x,'=','set')
    elif type(x)== tuple:
        print(x,'=','tuple')

c=['hello','apple','iron','owl','mani']

'''for x in c:
    if x.startswith('a'):
        print(x.upper())
    elif x.startswith('e'):
        print(x.upper())
    elif x.startswith('i'):
        print(x.upper())
    elif x.startswith('o'):
        print(x.upper())
    elif x.startswith('u'):
        print(x.upper())
    else:
        print(x)'''
res=[]
for x in c:
    if x.startswith('a') or x.startswith('e') or x.startswith('i') or x.startswith('o') or x.startswith('u'):
        res.append(x.upper())
    else:
        res.append(x)
   
print(res)




