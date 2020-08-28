'''
s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
'''
s = "loveleetcode"
k=0
while k<len(s)-1:
    if s[k] in s[k+1:]:
        k+=1
    else:
        print(k)
        break
