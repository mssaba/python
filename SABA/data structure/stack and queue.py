#stack
#is basically called last in first out
s=[1,2,3,4,5]
s.append(6)
print(s)
s.pop()#this removes the last item added so last in first out
print(s)

#queue
#is basically called first ib first out
from collections import deque
q=deque([1,2,3,4,5])
q.append(6)
print(q)
q.popleft
print(q)
