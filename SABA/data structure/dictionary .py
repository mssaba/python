#dictionary
#it has a key and value (eg: 'name'[key]:'saba'[value])
#ordered,changable,no duplicates

dict1={
    'age': 23 ,
    'name':'ram'
}
print(dict1)
#len of dictionary
print(len(dict1))

#accessing elements in dictonary
a=dict(name='raj',age=30,country='india')
#get()
print(a.get('age'))
#can also print values ,key, items seperately
print(dict1.keys())
print(dict1.values())
print(dict1.items())

#adding items to dictionary
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car["color"] = "white"
print(car)
#can be done also using update
car.update({'horsepower':35})
print(car)

#deleting
#deleting particular item in the list 
car.pop('horsepower')
print(car)
#the below remove the last item in the dictionary
car.popitem()
print(car)
#del only particular
del car['year']
print(car)
#for loop in dictionary
thisdict = dict(name = "John", age = 36, country = "Norway")
for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)

for x, y in thisdict.items():
  print(x, y)
#copy function in dictionary
mydict = thisdict.copy()
print(mydict)
#conerting into dictionary
mydict = dict(thisdict)
print(mydict)
#nested dictionary
# Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
