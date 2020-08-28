'''
方法一

'''

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zigzag = ['' for i in range(numRows)]  # 初始化zigzag为['','','']
        row = 0                                # 当前的行数
        step = 1                               # 步数：控制数据的输入
        for c in s:
            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1
            zigzag[row] += c
            row += step
        print(zigzag)
        return '-'.join(zigzag)


s = "A"  #LCIRETOESIIGEDHN"
# [0,1,2,3,4,5,0,1,2,3,4,5,0,1]
# [A,B,C,D,E,F,G,H,I,J,K,L,M,N]
numRows = 1
sss = Solution()
ass = sss.convert(s,numRows)
print(ass)

'''
方法二
'''
nums = numRows-1+numRows-1
ls=''

print('nums',nums)
if numRows==1:
    print(s)
else:
    for j in range(0,numRows):
        for i in range(len(s)):
            if i%(nums)==j or i%(nums)==nums-j:
                # print(strs[i],end='-')
                ls = ls+s[i]
print(ls)
