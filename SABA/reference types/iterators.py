# Iterators
# object that contains a countable number of values.

a='Papper'
b=iter(a)

print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
 
b="bookmark"
c='cat'
d=iter(c)

print(next(d))
print(next(d))
print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d)) 

class num:
    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        a=self.n
        self.n += 1
        return a

b=num()
it=iter(b)

print(next(it))
print(next(it))
print(next(it))
print(next(it)) 