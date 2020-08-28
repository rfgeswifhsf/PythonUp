def calculates(number, n, result):
    if n == 1:
        if number[0] == result:
            print (number[0],end='')
            return True

    else:
        if calculates(number, n-1, result - number[n-1]):
            print  (' + ', number[n-1],end='')
            return True
        if calculates(number, n-1, result + number[n-1]):
            print (' - ', number[n-1],end="")
            return True
        if calculates(number, n-1, result / number[n-1]):
            print  (' * ', number[n-1],end='' )
            return True
    return False



number = [8, 6, 3, 4] #这里填四张牌的数字
a = calculates(number, 2, 24)
print(a)
