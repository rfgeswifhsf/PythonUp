'''
示例 1:

输入: [1,7,5,3,6,0,4,2,3,1]
输出: ？

只允许一次买入和一次卖出，求最大收益

'''

s = [1,7,5,3,6,0,4,2,3,1]

def bp(s):
    bp_=0
    if len(s)>1:
        min_, max_ = min(s), max(s)
        min_index = s.index(min_)
        bp_ = max(s[min_index:])-min_
        s = s[:min_index]

    else:
        return bp_
    getscore = max(bp(s),bp_)
    return getscore

a= bp(s)
print(a)
