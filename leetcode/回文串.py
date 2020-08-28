'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：

输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：

输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        dp1 = [[0]*length for i in range(length)]
        # 初始化
        for i in range(length):
            dp1[i][i] = 1
            pass
        for i in range(length-1):
            j = i + 1
            if s[i] == s[j]:
                dp1[i][j] = 1
                pass
            pass
        # 对其他的赋值
        for k in range(2, length):
            for i in range(length - k):
                j = i + k
                if s[i] == s[j]:
                    dp1[i][j] = dp1[i+1][j-1]
                    pass
                pass
            pass
        # 返回
        d = [sum(dp1[i][:]) for i in range(length)]
        return sum(d)
        pass
    pass

a= 'aaaaa'
s = Solution()
b = s.countSubstrings(a)
print(b)
