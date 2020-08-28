'''
输入: 2.00000, 10
输出: 1024.00000
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        result =1
        if n<0:
             x=1/x
             while n<0:
                 print(x)
                 result *= x
                 n = n+1
             return result
        elif x==0:
             return result
        else:
            while n > 0:
                result *= x
                n = n - 1
            return result

s = Solution()
a = s.myPow(2.00000,-2)
print(a)
