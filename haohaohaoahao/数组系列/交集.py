'''
输入: nums1 = [1,2,2,1], nums2 = [2,2]

输出: [2,2]
'''

nums1 = [1,2,3,4,4,13]
nums2 =  [1,2,3,9,10]


i,j=0,0
lis_sub=[]
nums1 =sorted(nums1)
nums2=sorted(nums2)

while i<len(nums1) and j <len(nums2):
        if nums1[i]==nums2[j]:
            lis_sub.append(nums1[i])
            i+=1
            j+=1
        else:
            i+=1
print(lis_sub)
