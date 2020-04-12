from fractions import Fraction

a1=Fraction(5,4) # 四分之五
print(a1)
print(a1.numerator)  # 分子
print(a1.denominator) # 分母

c1=float(0.5)
print(Fraction(*c1.as_integer_ratio())) # 小数转分数
