class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        i,j=0,len(nums)-1

        while(i<j):
            if(nums[i]+nums[j]==target):
                res.append([nums[i],nums[j]])
                i+=1
                j-=1
            elif (nums[i]+nums[j])<target:
                i+=1
            else:j-=1
        return res



nums = [5,6,5,6]
target = 11

s= Solution()
a =s.pairSums(nums,target)


