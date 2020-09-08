class Solution:
    def majorityElement(self, nums):
        dicts = dict()
        for i in nums:
            if i not in dicts:
                dicts[i]=1
            else:
                dicts[i]+=1

        dicts = list(sorted(dicts.items(),key=lambda x:x[1],reverse=True))
        if dicts[0][1]>int(len(nums)/2):
            return dicts[0][0]



nums = [5, 2, 3, 2, 2, 2, 5, 4, 2]
s = Solution()
a = s.majorityElement(nums)
