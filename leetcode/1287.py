class Solution:
    def findSpecialInteger(self, arr):
        l = [-1,]
        j = []
        max_num = 0
        max_index=0
        for i in range(0,len(arr)-1):
            if arr[i]<arr[i+1]:
                c= 1
            else:
                c+=1
            max_num = max(c,max_num)
        print(max_num)


arr = [1,2,2,6,6,6,6,7,10]
s = Solution()
a = s.findSpecialInteger(arr)


