'''
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
'''

list_a =[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
# a = list(zip(*list_a))[::-1] #[(3, 6, 9), (2, 5, 8), (1, 4, 7)]
# a = list(zip(*list_a[::-1])) #[(7, 4, 1), (8, 5, 2), (9, 6, 3)]
l = []
while len(list_a)>0:
    l.append(list_a[0])
    list_a.remove(list_a[0])
    list_a=list(map(list,zip(*list_a)))[::-1]

from itertools import chain
print(list(chain(*l)))


[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

[
    [1,2,3]
    ,[4,5,6]
    ,[7,8,9]
]
