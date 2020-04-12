'''

怎样实现一个键对应多个值的字典

d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}
e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}


# 排序
s=sorted(d.items(),key=lambda x:x[1])
print(s)
'''

# 1
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

print(d)
#2
d = {} # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)
#3
# d = {}
# for key, value in pairs:
#     if key not in d:
#         d[key] = []
#     d[key].append(value)

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] =5
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
print(d)
# 排序
s=sorted(d.items(),key=lambda x:x[1])
print(s)


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

print(list(zip(prices.values(),prices.keys())))
min_price=min(zip(prices.values(),prices.keys()))
min_price1=min(zip(prices.keys(),prices.values()))
print(min_price1)
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)
