'''
 输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
 输出：2
'''

a = 0b11101
b = 0b01111
print(a^b)
print(str(bin(a^b)).count('1'))
