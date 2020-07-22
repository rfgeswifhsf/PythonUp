'''
给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''


nums = [-2,0,1,1,2]
nums.sort()
print(nums)
list =[]
for i in range(0,len(nums)-2):
   left = i+1
   right = len(nums)-1

   while left< right:

       if nums[i]+nums[left]+nums[right] == 0:
           if [nums[i],nums[left],nums[right]] not in list:
                list.append([nums[i],nums[left],nums[right]])
           while left<right and nums[left]==nums[left+1]:
                left =left+1
           while left < right and nums[right] == nums[right-1] :
               right = right - 1
       elif nums[i]+nums[left]+nums[right]<0:
           left=left+1
       elif nums[i]+nums[left]+nums[right]>0:
           right = right-1

print(list)

