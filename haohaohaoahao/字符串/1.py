'''
输入: haystack = "hello", needle = "ll"
输出: 2
'''

haystack = "hello"
needle = "ll"

if needle in haystack:
    print(haystack.index(needle))
else:
    print(-1)

'''
回文
输入: "A man, a plan, a canal: Panama"
输出: true

输入: "race a car"
输出: false
'''

s = "A man, a plan, a canal: Panama"
s = s.lower().replace(', ', "")
print(s)
s1=s[::-1]
if s==s1:
    print(True)
else:
    print(False)



'''
旋转字符串
'''
'''
输入: A = 'abcde', B = 'cdeab'
输出: true
'''
print('--------------')
A = 'abcdce'
B = 'cdceab'

list_index = [i for i,x in enumerate(A) if x == B[0]]
print(list_index)
for i in list_index:
    if B==A[i:]+A[0:i]:
        print(True)
        print(i)
        break



'''
最长子串
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3
'''
print('---------')
s= "abcabcbb"
# lenth = len(set(s))
# print(lenth)
windows_lenth = len(set(s))
flag = False
for i in range(windows_lenth,0,-1):
    for j in range(len(s)):
        if len(set(s[j:j+i]))==i:
            print('i',i)
            flag=True
            break
    if flag ==True:
        break
