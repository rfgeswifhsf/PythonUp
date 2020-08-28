'''
最长公共前缀
输入: ["flower","flow","flight"]
输出: "fl"


输入: ["dog","racecar","car"]
输出: ""

'''

char = ["flower", "flow", "flightqq"]
lens = [len(_) for _ in char]
chars = [[c for c in _] for _ in char]
print(chars)
min_len = min(lens)
import pandas as pd

df = pd.DataFrame(chars)
str =''
for i in range(min_len):
   if len(set(df[i]))==1:
       str+=list(set(df[i]))[0]
   else:
       break
print(str)

