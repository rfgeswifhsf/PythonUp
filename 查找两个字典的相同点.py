'''
怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）？
'''

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# 寻找相同key
print(a.keys()&b.keys())
# 寻找独有key
print(a.keys()-b.keys())
# 寻找完全值一致的k-v
print(a.items()&b.items())
# 过滤字典元素
c={key:a[key] for key in a.keys()-{'z','w'}}
print(c)
