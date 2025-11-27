#list
#>in a order
#>can be changed
#>can use duplicates
#>items can be of any data type

list1=["a",'b',1,3,4]
print(list1)


#len of list
print(len(list1))

#index of list
print(list1[0])
print(list1.index('a'))#finding index

#converting to list
list2=list(('a','b','c',1))
print(list2)

#access using index

print(list2[1])
print(list2[2:3])
print(list2[:4])
print(list2[2:])
print(list2[-1])

#item change in list

list2[2]='e'
print(list2)

list2[1:3]='f'
print(list2)

#insert item in list(it insert using index)
list2.insert(1,'r')
print(list2)

#add items in list(always add at last)
list2.append("orange")
print(list2)

#adding (two list )or (list and tuple )
tuple1=('d','g')
list2.extend(tuple1)
print(list2)

#removing particular item in list
list2.remove('a')
print(list2)

list2.pop(1)
print(list2)

#pop()empty removes the last item in the list 

#del() deletes the particular item
#this func can also delete the entire list 
del list2[0]
print(list2)

#clear() this func clears the data in the list
list2.clear()
print(list2 )

#sort() this func arrange the data in oder
#this can also reverse the order of the list
list3=[5,3,2,6,8,1]
list3.sort()
print(list3)

list3.sort(reverse=True)
print(list3)

#reverse () this reverse the order of the cuurent list

list3.reverse()
print(list3)

#addding two list
list4=['a','d','r']
list5=['u','k','m']
list6=list4+list5
print(list6)
#using append
for x in list5:
    list4.append(x)
print(list4)
#using extend adds list at last of the list
list5.extend(list4)
print(list5)
#example
n=['apple','cake','run','sun']
b=[]
for x in n:
    if "c" in x:
        b.append(x)
print(b)

#copy()
a=[1,2,3,4,5]
b=a.copy()
print(b)

#finding min max
c=[1,7,9,8,5,3]
print(min(c))
print(max(c))

#zip()
q=[20,30,40]
x=['ram','rajesh','ravi']
o=list(zip(x,q))
print(o)
