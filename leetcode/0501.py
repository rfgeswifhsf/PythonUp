'''
插入。给定两个32位的整数N与M，以及表示比特位置的i与j。
编写一种方法，将M插入N，使得M从N的第j位开始，到第i位结束。
假定从j位到i位足以容纳M，也即若M = 10 011，那么j和i之间至少可容纳5个位。
例如，不可能出现j = 3和i = 2的情况，因为第3位和第2位之间放不下M。

示例1:
 输入：N = 1024(10000000000), M = 19(10011), i = 2, j = 6
 输出：N = 1100(10001001100)

示例2:
 输入： N = 0, M = 31(11111), i = 0, j = 4
 输出：N = 31(11111)
'''

class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        N = bin(N)
        M = bin(M)

        pass

s = Solution()
a = s.insertBits()
print(a)
