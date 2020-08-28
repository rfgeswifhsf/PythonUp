'''
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。
'''
nums = [3,2,2,3]
val =3

flag =True
while flag:
    if val in nums:
        nums.remove(val)
    else:
        flag=False
print(nums)
