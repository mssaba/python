#set
#it uses curly braces{}
#it has unordered ,unchangable,unindexed colloection

set={"a","b",1,2}
print(set)

thisset = {"apple", "banana", "cherry", False, True, 0, 1, 2} # 1==True, 0==False
print(thisset)

#true false
set1={"hi",'bye','welcome','good'}
print('hi' in set1)
print('bye' not in set1)

#adding collection to set
#add
set2={'c','e','f','g'}#since un ordered it can be added anywhere
set2.add('i')
print(set2)
#update
set3={'ram','jaanu','jessy'}
set3.update({'malathy'})
print(set3)

#removing items form set
#remove
set4={'raj','ram','ravi','mani'}
set4.remove('raj')
print(set4)
#discard
set4.discard('raj')
print(set4)
#pop
y=set4.pop()
print(y)
print(set4)#prints the other items in the list

#clear only clear the items in the set
set4.clear()
print(set4)

#operatin in set

#union
set5={1,2,3,4,5}
set6={1,3,5,7,8}
set7=set5.union(set6) #also be noted by |
print(set7)

#intersection
set7=set5.intersection(set6) #also be noted by &
print(set7)

#symmeteric difference
set7=set5.difference(set6) #it can also be noted by ^
print(set7)
