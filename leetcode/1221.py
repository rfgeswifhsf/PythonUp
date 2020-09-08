'''
示例 1：
输入：s = "RLRRLLRLRL"
输出：4
解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。

示例 2：
输入：s = "RLLLLRRRLR"
输出：3
解释：s 可以分割为 "RL", "LLLRRR", "LR", 每个子字符串中都包含相同数量的 'L' 和 'R'。

示例 3：
输入：s = "LLLLRRRR"
输出：1
解释：s 只能保持原样 "LLLLRRRR".
'''

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num = 0
        l=[]
        for i in range(len(s)):
            if s[i]=='L':
                num+=-1

            if s[i]=='R':
                num+= 1

            if num ==0:
                l.append(i)
        return len(l)



s = "RLLLLRRRLR"
ss= Solution()
a =ss.balancedStringSplit(s)
print(a)
