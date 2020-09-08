'''
示例 1：
输入：num = 14
输出：6
解释：
步骤 1) 14 是偶数，除以 2 得到 7 。
步骤 2） 7 是奇数，减 1 得到 6 。
步骤 3） 6 是偶数，除以 2 得到 3 。
步骤 4） 3 是奇数，减 1 得到 2 。
步骤 5） 2 是偶数，除以 2 得到 1 。
步骤 6） 1 是奇数，减 1 得到 0 。

示例 2：
输入：num = 8
输出：4
解释：
步骤 1） 8 是偶数，除以 2 得到 4 。
步骤 2） 4 是偶数，除以 2 得到 2 。
步骤 3） 2 是偶数，除以 2 得到 1 。
步骤 4） 1 是奇数，减 1 得到 0 。

示例 3：
输入：num = 123
输出：12
'''

num =14
# count =0
# def numberOfSteps(num):
#     c=0
#     while num!=0:
#         print(num,c)
#         if num%2==0:
#             c+=1
#             # print('c', c)
#             num = int(num/2)
#             # c+=numberOfSteps(num)
#         if num%2==1:
#             c+=1
#             # print('c', c)
#             num = num-1
#         numberOfSteps(num)
#     if num == 0:
#         return  c
#
#
# a = numberOfSteps(num)
# print('a',a)


def numberOfSteps(num):
    num = bin(num)
    num = str(num)[2:]
    count = 0
    while len(num)>0:
        if num[-1]=='1':
            num = num[0:-1]+'0'
            count+=1
        elif num[-1]=='0':
            num = num[:-1]
            count+=1
            # print(count)
    return count-1
a = numberOfSteps(123)
# print(a)
