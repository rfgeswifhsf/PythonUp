'''
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
连续子数组 [4,-1,2,1] 的和最大，为 6。

nums  -2,1,-2,4,-1,2,1,-5,4
dp    -2,1,-1,4,3, 5,6, 1,5
'''

nums =[-2,1,-2,4,-1,2,1,-5,4]

i=0
dp = nums[0]
l=[dp]
while i<len(nums)-1:

    dp = max(nums[i+1],dp+nums[i+1])
    i+=1
    l.append(dp)
print(l)
print(max(l))
