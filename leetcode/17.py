'''
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

dict = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
strs= '253'
class Solution:
    def letterCombinations(self, digits: str):
        conversion={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits)==0:
            return []
        product=['']
        for k in digits:
            product=[i+j for i in product for j in conversion[k]]
        return product

s = Solution()
a = s.letterCombinations(strs)
print(a)
