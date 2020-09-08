'''
给你一个整数数组 arr ，以及 a、b 、c 三个整数。请你统计其中好三元组的数量。
如果三元组 (arr[i], arr[j], arr[k]) 满足下列全部条件，则认为它是一个 好三元组 。

    0 <= i < j < k < arr.length
    |arr[i] - arr[j]| <= a
    |arr[j] - arr[k]| <= b
    |arr[i] - arr[k]| <= c

其中 |x| 表示 x 的绝对值。
返回 好三元组的数量 。

示例 1：
输入：arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
输出：4
解释：一共有 4 个好三元组：[(3,0,1), (3,0,1), (3,1,1), (0,1,1)] 。

示例 2：
输入：arr = [1,1,2,2,3], a = 0, b = 0, c = 1
输出：0
解释：不存在满足所有条件的三元组。
'''

arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
class Solution:
    def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:

        # print(arr)
        arr_ = range(0,len(arr))
        a_set={(arr_[0],)}

        for i in arr_[1:]:
            a_set.update({j + (i,) for j in a_set if len(j)<3 })
            a_set.add((i,))
        count = 0
        a_set = [_ for _ in a_set if len(_)==3]

        l=[]
        for i in a_set:
            i=list(i)
            if len(i)==3:
                if abs(arr[i[0]]-arr[i[1]])<=a:
                    if abs(arr[i[1]]-arr[i[2]])<=b:
                        if abs(arr[i[0]]-arr[i[2]])<=c:
                            l.append([arr[i[0]],arr[i[1]],arr[i[2]]])
                            count+=1
        return count
s = Solution()
a = s.countGoodTriplets(arr,a,b,c)
print(a)
