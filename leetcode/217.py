class Solution:
    def containsDuplicate(self, nums):
        l1 = len(num)
        l2 = len(set(num))
        if l1!=l2:
            return True
        else:
            return False


num = [1,2,3,1]
s = Solution()
a = s.containsDuplicate(num)
print(a)
