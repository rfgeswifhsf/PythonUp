'''
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
'''

# nums = [2,5,1,9,3,2]
# # nums = [1,2,3,4,5,6,7,8]
# class Solution:
#     def lengthOfLIS(self, nums):
#         if not nums:
#             return 0
#         dp = [1 for _ in range(len(nums))]
#         for i in range(1, len(nums)):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j]+1)
#         print(dp)
#         return max(dp)
#
# s =Solution()
# a = s.lengthOfLIS(nums)
# print(a)


s =  [10,9,2,5,3,7,101,18]

one_list =[1 for i in range(len(s))]

for i in range(len(s)):
    for j in range(i):
        if s[i]>s[j]:
            one_list[i]=max(one_list[i],one_list[j]+1)
            print(i,j,one_list[i],one_list[j]+1)

print(max(one_list))

