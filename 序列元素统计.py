'''

怎样找出一个序列中出现次数最多的元素呢？

'''

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts=Counter(words)  #统计 Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1})
top_three=word_counts.most_common(3)  #最多 3 个 [('eyes', 8), ('the', 5), ('look', 4)]
print(word_counts)
print(top_three)
print(word_counts['not'])  #统计 某个词 出现次数

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
word_counts.update(morewords) # 添加词
a=Counter(words)
b=Counter(morewords)
print('a',a)
print('b',b)
print('a+b',a+b)
print('a-b',a-b)
