'''
输入: s = "abcdefg", k = 2
输出: "cdefgab"
'''
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = s[k:] + s[:k]
        return s


if __name__ == '__main__':
    s= "abcdefg"
    k=2
    re = Solution()
    s= re.reverseLeftWords(s,k)

    print(s)



