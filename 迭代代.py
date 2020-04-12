'''
可迭代对象(Iterable)
迭代器(Iterator)
迭代(Iteration)

任意对象，只要其提供迭代器，那么就是可迭代对象

只要定义了 这些方法 __iter__,或下表索引 __getitem__  就是可迭代对象

只要定义了这些方法 __next__ 或next 那么就是一个迭代器
'''

# def generator_function():
#     m = -1
#     for i in range(10):
#         yield m
# print(type(generator_function()))
# a=generator_function()
# print(a.__next__())  #0
# print(a.__next__())  #1
# for i in generator_function():
#     print(i,end=' ') #0 1 2 3 4 5 6 7 8 9
import time
'''
iter内置函数
'''
my_string='yaohu'
print(iter(my_string).__next__())

