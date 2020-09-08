class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        if len(nums)>0:
            pre = [1 for i in range(len(nums))]
            for i in range(1,len(nums)):
                if nums[i-1]<nums[i]:
                    pre[i] = pre[i]+pre[i-1]
            return max(pre)
        else:
            return 0
        # pass

nums =  [1,1,1,1,1]
s = Solution()
a = s.findLengthOfLCIS(nums)
print(a)
