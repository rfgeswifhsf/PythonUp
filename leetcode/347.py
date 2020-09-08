class Solution:
    def topKFrequent(self, nums, k: int) :
        dict_ = dict()
        for i in nums:
            if i in dict_:
                dict_[i]+=1
            else:
                dict_[i]=1
        print(dict_)
        d = sorted(dict_.items(),key=lambda x:x[1],reverse=True)
        keys =[_[0] for _ in  d[:k]]
        return keys


nums = [1,1,1,2,2,3]
k = 2
s = Solution()
a=s.topKFrequent(nums,k)
