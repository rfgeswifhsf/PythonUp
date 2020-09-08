'''
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例：
输入：nums = [5,2,6,1]
输出：[2,1,1,0]
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素
'''

class Solution:
    def countSmaller(self, nums):
        pre_list = [0]*len(nums)
        j=0
        while j<len(nums):
            for i in range(j,len(nums)):
                if nums[j]>nums[i]:
                    pre_list[j]+=1
            j+=1
        return pre_list

nums = [5,2,6,1]
s = Solution()
a = s.countSmaller(nums)
print(a)
