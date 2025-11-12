#for loop
for x in range(5):
    print(x)

for x in range(1,5):
    print(x)

for x in range(2,12,3):
    print(x)

a=["hari","bala","varun"]
for x in a:
    print(x)

b="rajapandian"
for y in b:
    print(y)

data=[[2,4,6],[8,10,12]]
for x in data:
    for y in x:
        if(y==10):
            break
        print(y)
