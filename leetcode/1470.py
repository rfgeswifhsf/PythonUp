'''
示例 1：
输入：nums = [2,5,1,3,4,7], n = 3
输出：[2,3,5,4,1,7]
解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]

示例 2：
输入：nums = [1,2,3,4,4,3,2,1], n = 4
输出：[1,4,2,3,3,2,4,1]

示例 3：
输入：nums = [1,1,2,2], n = 2
输出：[1,2,1,2]
'''

nums = [1,2,3,4,4,3,2,1]
n = 4
l = []
for i in range(n):
    l.append(nums[i])
    l.append(nums[i+4])
print(l)
