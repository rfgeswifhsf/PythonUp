'''
枚举(enumerate)是Python内置函数

允许我们遍历数据并自动计数
'''
my_list=['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list,1):
    print(c,value,'||',end='  ')

print('\n')

#***************************
c=list(enumerate(my_list,1))
print(c)

print(dir(my_list))
