'''
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Solution:
    def combine(self, n: int, k: int) :
        pre = [_ for _ in range(1,n+1)]
        l = {(pre[0],)}
        for i in pre[1:]:
            l.update({j+(i,) for j in l if len(j)<k})
            l.add((i,))
            print(l)
        l = [list(_) for _ in l if len(_)==k]
        return l



n=3
k=3
s = Solution()
a = s.combine(n,k)
print(a)
