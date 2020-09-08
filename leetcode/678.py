class Solution(object):
    def checkValidString(self, strs):
        num = 0
        for s in strs:
            if s == ')':
                num -= 1
            else:
                num += 1
            if num < 0:
                return False

        num = 0
        for s in strs[::-1]:
            if s == '(':
                num -= 1
            else:
                num += 1
            if num < 0:
                return False

        return True


ss = '***)))((('  # *是万能的
s =Solution()
a =s.checkValidString(ss)
print(a)
