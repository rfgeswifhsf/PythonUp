'''
输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

递增子数列。
'''

nums =[4,6,7,7]





# l_set={('1',)}
# print(type(l_set)) #<class 'set'>
# l_set.update({('11',)+('1',)}) #{('1',), ('11', '1')}
# print(l_set)


pres = {(nums[0], )}
for i in nums[1:]:
    pres.update({j+(i, ) for j in pres if j[-1] <= i})
    pres.add((i, ))
print([list(i) for i in pres if len(i) > 1])

print(pres)
