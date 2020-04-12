'''
四舍五入
'''
print(round(1.23456,1))
print(round(1.23456,3))

'''
精确浮点运算
'''

a=4.2
b=2.1
print(a+b)  #6.300000000000001
print((a+b)==6.3)  #False
'''
原因：
由底层CPU和IEEE 754标准通过自己的浮点单位去执行算术时的特征。
由于Python的浮点数据类型使用底层表示存储数据，因此你没办法去避免这样的误差

解决：decimal 有一定的性能损耗

允许你控制计算的每一方面，包括数字位数和四舍五入运算
'''
from decimal import Decimal
a1=Decimal('4.2')
b1=Decimal('2.1')
print(a1+b1)  #6.3
print((a1+b1)==Decimal('6.3')) #True
#****************
import math
nums=[1.23e+18, 1, -1.23e+18]
print(sum(nums)) # 0.0
print(math.fsum(nums)) # 1.0

'''
数字格式化输出
'''
x=1234.56789
print(format(x,'0.2f'))     #   1234.57
print(format(x,'>10.1f'))   #       1234.6
print(format(x,'<10.1f'))   #   1234.6
print(format(x,'^10.1f'))   #  1234.6
print(format(x,','))        #   1,234.56789
print(format(x, 'e'))       #   1.234568e+03
