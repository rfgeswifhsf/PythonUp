'''
输入："(()())(())"
输出："()()()"

输入："(()())(())(()(()))"
输出："()()()()(())"

'''

# S = "(()())(())(()(()))"
S = "((()())(()()))"

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        S = S.replace('()','a')
        S = S.replace('a','()').replace('-','')
        print('S',S)
        count = 0
        l = []
        for i in range(len(S)-1,-1,-1):
            if S[i]==')':
                c = -1
            elif S[i]=='(':
                c = 1
            else:
                c = 0
            count +=c
            print(count)
            if count == 0:
                l.append(i)


        st = ''
        i=0
        l.reverse()
        print('l',l)

        while i<len(l)-1 and len(l)>1:
            st += S[l[i]:l[i+1]][1:-1]
            i+=1
        st+=S[l[-1]:][1:-1]
        return st

s = Solution()
a = s.removeOuterParentheses(S)
print(a)
