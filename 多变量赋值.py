# record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# name, *email, phone_numbers = record
# print(phone_numbers)

# item=[1,2,3,4,5,6]
# def sum(items):
#     head,*tail=items
#     print(tail)
#     return  head+sum(tail) if tail else head
#
# print(sum(item))

from collections import deque

q = deque(maxlen=3)  #新建一个固定大小的队列,, 最老的元素会自动被移除掉。
print(q)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(q)
q.appendleft(5)
print(q)
q.pop()
print(q)
q.popleft()
print(q)


import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
